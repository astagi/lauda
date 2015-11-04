import unittest

from lauda import StopWatch, StopWatchException


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

    def test_stopwatch_exceptions(self):
        stopwatch = StopWatch()
        self.assertRaises(StopWatchException, stopwatch.stop)

    def test_elapsed_time(self):
        stopwatch = StopWatch()
        start_time = stopwatch.start()
        elapsed_time_ongoing = stopwatch.elapsed_time
        elapsed_time_final = stopwatch.stop()
        self.assertTrue(elapsed_time_ongoing > 0)
        self.assertTrue(elapsed_time_ongoing < elapsed_time_final)

    def test_elapsed_time_zero(self):
        stopwatch = StopWatch()
        elapsed_time_ongoing = stopwatch.elapsed_time
        self.assertEqual(elapsed_time_ongoing, 0)
