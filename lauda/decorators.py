from functools import wraps, partial
from .stopwatch import StopWatch


def stopwatch(method=None, callback=None):
    if method is None:
        return partial(stopwatch, callback=callback)

    @wraps(method)
    def wrapper(*args, **kwargs):
        stopwatch = StopWatch()
        stopwatch.start()
        ret = method(*args, **kwargs)
        elapsed = stopwatch.stop()
        if callback:
            callback(stopwatch, method)
        else:
            print('Executed {0} in {1} seconds'.format(method, elapsed))
        return ret
    return wrapper
