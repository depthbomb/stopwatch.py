from datetime import timedelta
from time import perf_counter_ns
from humanize import naturaldelta
from typing import Self, Optional


class Stopwatch:
    _digits: int
    _start: float
    _end: Optional[float]

    def __init__(self, digits: int = 2) -> None:
        self._digits = digits
        self._start = self._time()
        self._end = None

    def __repr__(self) -> str:
        return naturaldelta(timedelta(milliseconds=self.duration), minimum_unit="MILLISECONDS")

    @property
    def duration(self) -> float:
        """
        Returns the current duration of the instance
        """
        return self._end - self._start if self._end is not None else self._time() - self._start

    @property
    def running(self) -> bool:
        """
        Whether the instance is currently running
        """
        return self._end is not None

    def restart(self) -> Self:
        """
        Restarts the timing of the instance
        """
        self._start = self._time()
        self._end = None
        return self

    def reset(self) -> Self:
        """
        Resets the timing of the instance
        """
        self._start = self._time()
        self._end = self._start
        return self

    def start(self) -> Self:
        """
        Starts the timing if it isn't already running
        """
        if not self.running:
            self._start = self._time() - self.duration
            self._end = None
        return self

    def stop(self) -> Self:
        """
        Stops the timing if it is running
        """
        if self.running:
            self._end = self._time()
        return self

    @staticmethod
    def _time() -> int:
        return perf_counter_ns() // 1_000_000
