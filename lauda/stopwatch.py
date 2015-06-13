import time


class StopWatchException(Exception):
    pass


class StopWatch():

    _stop = 0
    _start = 0
    _started = False

    def start(self):
        self._start = time.time()
        self._started = True
        return self._start

    def stop(self):
        if not self.started:
            raise StopWatchException('StopWatch not started!')
        self._stop = time.time()
        self._started = False
        return self.elapsed_time

    @property
    def started(self):
        return self._started

    @property
    def start_time(self):
        return self._start

    @property
    def stop_time(self):
        return self._stop

    @property
    def elapsed_time(self):
        return (self._stop - self._start)
