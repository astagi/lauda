import time


class StopWatch():

    _stop = 0
    _start = 0

    def start(self):
        self._start = time.time()
        return self._start

    def stop(self):
        self._stop = time.time()
        return self.elapsed_time

    @property
    def start_time(self):
        return self._start

    @property
    def stop_time(self):
        return self._stop

    @property
    def elapsed_time(self):
        return (self._stop - self._start)
