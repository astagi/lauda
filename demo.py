from lauda import StopWatch, stopwatch

def stopwatch_sum_cb(watch, function):
    print ('Time spent {0}'.format(watch.elapsed_time))

@stopwatch(callback=stopwatch_sum_cb)
def awesome_sum(a, b):
    return a + b

@stopwatch()
def awesome_mul(a, b):
    return a * b

print awesome_sum(5, 10)
print awesome_mul(5, 10)

watch = StopWatch()
watch.start()
for i in range(10000000):
    pass
watch.stop()
print ('Time spent in range {0}'.format(watch.elapsed_time))
