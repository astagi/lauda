# Lauda
A very simple python module for measuring time.

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
