import unittest
import time
from mock import Mock, patch

from lauda import StopWatch, stopwatch, stopwatchcm


class TestContextManager(unittest.TestCase):

    @patch('lauda.StopWatch.stop')
    @patch('lauda.StopWatch.start')
    def test_stopwatch(self, mock_stopwatch_start, mock_stopwatch_stop):
        with stopwatchcm():
            time.sleep(0.1)
        mock_stopwatch_start.assert_called_with()
        mock_stopwatch_stop.assert_called_with()

    @patch('lauda.StopWatch.stop')
    @patch('lauda.StopWatch.start')
    def test_stopwatch_callback(self, mock_stopwatch_start, mock_stopwatch_stop):
        my_callback = Mock(return_value=None)

        with stopwatchcm(callback=my_callback):
            time.sleep(0.1)
            self.assertFalse(my_callback.called)

        self.assertTrue(my_callback.called)
        callback_args = my_callback.call_args
        self.assertTrue(isinstance(callback_args[0][0], StopWatch))
        self.assertTrue(len(callback_args[0]) == 1)
        mock_stopwatch_start.assert_called_with()
        mock_stopwatch_stop.assert_called_with()
