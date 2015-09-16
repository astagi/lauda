from contextlib import contextmanager
from .stopwatch import StopWatch


@contextmanager
def stopwatch(callback=None):
    watch = StopWatch()
    watch.start()
    yield
    elapsed = watch.stop()
    if callback:
        callback(watch)
    else:
        print('Executed in {0} seconds'.format(elapsed))
