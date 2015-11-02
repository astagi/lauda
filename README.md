# Lauda
[![Build Status][travis-image]][travis-url] [![Codecov.io Status][codecovio-image]][codecovio-url]
[![Latest Version](https://img.shields.io/pypi/v/lauda.svg)](https://pypi.python.org/pypi/lauda/)
[![Supported Python versions](https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.3%2C%203.4-blue.svg)](https://pypi.python.org/pypi/lauda/)
[![License](https://img.shields.io/github/license/astagi/lauda.svg)](https://pypi.python.org/pypi/lauda/)
[![Downloads](https://img.shields.io/pypi/dm/lauda.svg)](https://pypi.python.org/pypi/lauda/)

A very simple python module for measuring time.

## Install

    pip install lauda

## Usage
You can use lauda `StopWatch` to measure a portion of code

```python
from lauda import StopWatch

watch = StopWatch()
watch.start()
for i in range(10000000):
    pass
watch.stop()
print ('Time spent in range {0}'.format(watch.elapsed_time))
```
You can also get the `elapsed_time` when the stopwatch is running

If you want to measure an entire function execution, you can decorate it using the `stopwatch` decorator

```python
from lauda import stopwatch

@stopwatch
def awesome_mul(a, b):
    return a * b
```

By default `stopwatch` decorator will print the time spent inside the decorated function, if you want more control you can pass to your decorator a callback that will receive a `StopWatch` instance and the decorated function.

```python
from lauda import stopwatch

def stopwatch_sum_cb(watch, function):
    print ('Time spent {0}'.format(watch.elapsed_time))

@stopwatch(callback=stopwatch_sum_cb)
def awesome_sum(a, b):
    return a + b
```

If you want to measure a block of code, you can use the `stopwatchcm` context manager

```python
from lauda import stopwatchcm

with stopwatchcm():
    c = a * b
```

By default `stopwatchcm` context manager will print the time spent inside the context manager body, if you want more control you can pass to your context manager a callback that will receive a `StopWatch` instance.

```python
from lauda import stopwatchcm

def stopwatch_sum_cb(watch):
    print ('Time spent {0}'.format(watch.elapsed_time))

with stopwatchcm(callback=stopwatch_sum_cb):
    c = a + b
```

[travis-url]: https://travis-ci.org/astagi/lauda
[travis-image]: http://img.shields.io/travis/astagi/lauda.svg?branch=master

[codecovio-url]: http://codecov.io/github/astagi/lauda?branch=master
[codecovio-image]: https://img.shields.io/codecov/c/github/astagi/lauda.svg
