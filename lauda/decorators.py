from functools import wraps
from .stopwatch import StopWatch


def _start_stopwatch(wrapped, callback, args, kwargs):
    stopwatch = StopWatch()
    stopwatch.start()
    ret = wrapped(*args, **kwargs)
    elapsed = stopwatch.stop()
    if callback and wrapped is not callback:
        callback(stopwatch, wrapped)
    else:
        print('Executed {0} in {1} seconds'.format(wrapped, elapsed))
    return ret


def stopwatch(callback=None):
    def stopwatch_decorator(wrapped=None, *args, **kwargs):
        if wrapped is None:
            wrapped = callback
            return _start_stopwatch(wrapped, callback, args, kwargs)
        else:
            @wraps(wrapped)
            def wrapper(*args, **kwargs):
                return _start_stopwatch(wrapped, callback, args, kwargs)
            return wrapper
    return stopwatch_decorator
