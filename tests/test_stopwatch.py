import unittest

from lauda import StopWatch


class TestStopwatch(unittest.TestCase):

    def test_stopwatch(self):
        stopwatch = StopWatch()
        start_time = stopwatch.start()
        self.assertTrue(start_time > 0)
        elapsed_time = stopwatch.stop()
        self.assertTrue(elapsed_time > 0)
        self.assertEqual(elapsed_time, stopwatch.elapsed_time)
        self.assertEqual(
            elapsed_time,
            stopwatch.stop_time - stopwatch.start_time
        )
