import unittest
import time
from mock import Mock, patch

from lauda import StopWatch, stopwatch


class TestDecorators(unittest.TestCase):

    @patch('lauda.StopWatch.stop')
    @patch('lauda.StopWatch.start')
    def test_stopwatch(self, mock_stopwatch_start, mock_stopwatch_stop):
        @stopwatch
        def my_function():
            time.sleep(0.1)
        my_function()
        mock_stopwatch_start.assert_called_with()
        mock_stopwatch_stop.assert_called_with()

    @patch('lauda.StopWatch.stop')
    @patch('lauda.StopWatch.start')
    def test_stopwatch_callback(self, mock_stopwatch_start, mock_stopwatch_stop):
        my_callback = Mock(return_value=None)
        @stopwatch(callback=my_callback)
        def my_function(n):
            time.sleep(0.1)
        self.assertFalse(my_callback.called)
        my_function(15)
        self.assertTrue(my_callback.called)
        callback_args = my_callback.call_args
        self.assertTrue(isinstance(callback_args[0][0], StopWatch))
        self.assertTrue(isinstance(callback_args[0][1], my_function.__class__))
        mock_stopwatch_start.assert_called_with()
        mock_stopwatch_stop.assert_called_with()
