# lauda
# Copyright 2015 Andrea Stagi
# See LICENSE for details.

"""
Lauda - A very simple python module for measuring time
"""

from .stopwatch import StopWatch, StopWatchException
from .decorators import stopwatch
from .contextmanager import stopwatch as stopwatchcm

__version__ = '1.1.0'
__author__ = 'Andrea Stagi'
__license__ = 'MIT'

__all__ = ['StopWatch', 'StopWatchException', 'stopwatch', 'stopwatchcm']
