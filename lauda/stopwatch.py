import time


class StopWatchException(Exception):
    pass


class StopWatch():

    _stop = 0
    _start = 0
    _started = False
    _checkpoint = 0

    def start(self):
        self._start = time.time()
        self._started = True
        self._checkpoint = self._start
        return self._start

    def stop(self):
        if not self.started:
            raise StopWatchException('StopWatch not started!')
        self._stop = time.time()
        self._started = False
        return self.elapsed_time

    def checkpoint(self):
        if not self.started:
            raise StopWatchException('StopWatch not started!')
        now = time.time()
        self._checkpoint, diff_checkpoint = now, (now - self._checkpoint)
        return diff_checkpoint

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
        current_time = self._stop
        if not current_time and self.started:
            current_time = time.time()
        return (current_time - self._start)
