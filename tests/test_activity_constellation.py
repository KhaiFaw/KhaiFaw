import importlib.util
from datetime import date, timedelta
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location(
    'constellation', Path(__file__).resolve().parents[1] / 'scripts/render_activity_constellation.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
NS = {'s': 'http://www.w3.org/2000/svg'}


class ActivityTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 9, 19)
        self.activity = {self.today - timedelta(days=2): (1, 1),
                         self.today - timedelta(days=1): (5, 2), self.today: (20, 4)}
        self.root = ET.fromstring(module.render('KhaiFaw', self.today, self.activity))
        self.cells = self.root.findall('.//s:rect[@data-date]', NS)

    def test_only_real_contribution_days_animate(self):
        self.assertEqual(len(self.cells), 371)
        for cell in self.cells:
            self.assertEqual(cell.find('s:animate', NS) is not None, int(cell.attrib['data-count']) > 0)

    def test_same_week_days_light_separately_in_date_order(self):
        arrivals = []
        for cell in self.cells:
            animation = cell.find('s:animate', NS)
            if animation is not None:
                times = [float(v) for v in animation.attrib['keyTimes'].split(';')]
                self.assertEqual(times, sorted(times))
                arrivals.append(times[1])
        self.assertEqual(len(arrivals), 3)
        self.assertTrue(all(a < b for a, b in zip(arrivals, arrivals[1:])))

    def test_count_controls_brightness_and_halo_monotonically(self):
        values = [module.contribution_light(n, 40) for n in range(41)]
        luminances = [sum(int(color[i:i+2], 16) * weight for i, weight in
                          zip((1, 3, 5), (.2126, .7152, .0722))) for color, _ in values]
        self.assertTrue(all(a < b for a, b in zip(luminances, luminances[1:])))
        self.assertTrue(all(a[1] < b[1] for a, b in zip(values, values[1:])))

    def test_star_arrivals_match_cell_reveal_times(self):
        motion = self.root.find('.//s:g[@id="travelling-star"]/s:animateMotion', NS)
        arrivals = [float(t) for t in motion.attrib['keyTimes'].split(';')]
        self.assertEqual(motion.attrib['calcMode'], 'spline')
        self.assertIn(' C', motion.attrib['path'])
        for cell in self.cells:
            animation = cell.find('s:animate', NS)
            if animation is not None:
                reveal = float(animation.attrib['keyTimes'].split(';')[1])
                self.assertLess(min(abs(t - reveal) for t in arrivals), 0.000001)
                colors = animation.attrib['values'].split(';')
                self.assertEqual(colors[0], colors[-1])
                self.assertEqual(colors[2], colors[3])  # Remains lit until global fade.

    def test_empty_calendar_stays_dark(self):
        root = ET.fromstring(module.render('Empty', self.today, {}))
        self.assertEqual(len(root.findall('.//s:rect[@data-date]/s:animate', NS)), 0)
        self.assertIn('0 contributions', root.find('s:desc', NS).text)

    def test_dense_year_does_not_rush_and_holds_completed_grid(self):
        days = [(self.today - timedelta(days=370-i), 1, 1) for i in range(371)]
        journey = module.star_journey(days)
        arrivals = list(journey['arrivals'].values())
        self.assertTrue(all(b - a > 1.1 for a, b in zip(arrivals, arrivals[1:])))
        self.assertGreater(journey['fade_start'] - arrivals[-1], 2.4)

    def test_future_days_are_not_lit(self):
        future = self.today + timedelta(days=1)
        root = ET.fromstring(module.render('Test', self.today, {future: (99, 4)}))
        self.assertEqual(len(root.findall('.//s:rect[@data-date]/s:animate', NS)), 0)
        self.assertIsNone(root.find('.//s:g[@id="travelling-star"]', NS))

    def test_animation_is_inline_and_has_no_static_switch_or_cell_hopping(self):
        style = self.root.find('.//s:style', NS).text
        self.assertNotIn('prefers-reduced-motion', style)
        self.assertNotIn('display:none', style)
        self.assertIsNone(self.root.find('.//s:rect[@id="day-cursor"]', NS))
        self.assertNotIn('calcMode="discrete"', ET.tostring(self.root, encoding='unicode'))

    def test_star_visits_only_active_dates_in_order(self):
        days = [(self.today - timedelta(days=6-i), i if i % 2 else 0, 1) for i in range(7)]
        journey = module.star_journey(days)
        self.assertEqual(list(journey['arrivals']), [day for day, count, _ in days if count])
        self.assertEqual(journey['points'][0], 0)
        self.assertEqual(journey['points'][-1], 1)
        self.assertEqual(journey['points'], sorted(journey['points']))
        self.assertEqual(journey['times'], sorted(journey['times']))
        self.assertEqual(journey['path'].count(' C'), 3)

    def test_single_day_path_is_valid(self):
        journey = module.star_journey([(self.today, 3, 1)])
        self.assertEqual(len(journey['arrivals']), 1)
        self.assertGreater(journey['duration'], 4)
        self.assertEqual(len(journey['points']), len(journey['times']))


if __name__ == '__main__':
    unittest.main()
