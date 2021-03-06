from lauda import StopWatch, stopwatch, stopwatchcm

def stopwatch_sum_cb(watch, function):
    print ('Time spent inside {0} is {1} sec.'.format(function, watch.elapsed_time))

def stopwatch_sum_cb_w_cm(watch):
    print ('Time spent is {0} sec.'.format(watch.elapsed_time))

@stopwatch(callback=stopwatch_sum_cb)
def awesome_sum(a, b):
    return a + b

@stopwatch
def awesome_mul(a, b):
    return a * b

@stopwatch
def awesome_print():
    print 'Hello Niki!'

print awesome_sum(5, 10)
print awesome_mul(5, 10)
awesome_print()

watch = StopWatch()
watch.start()
for i in range(100000):
    pass
print ('Time is running out.. {0} sec.'.format(watch.elapsed_time))
for i in range(10000000):
    pass
watch.stop()
print ('Time spent in range: {0} sec.'.format(watch.elapsed_time))

with stopwatchcm(callback=stopwatch_sum_cb_w_cm):
    c = 5 * 10

watch = StopWatch()
watch.start()
for i in range(10000000):
    pass
print ('Time spent in first range: {0} sec.'.format(watch.checkpoint()))
for i in range(10000000):
    pass
print ('Time spent in second range: {0} sec.'.format(watch.checkpoint()))
for i in range(10000000):
    pass
print ('Time spent in third range: {0} sec.'.format(watch.checkpoint()))
watch.stop()
print ('Time spent in range total: {0} sec.'.format(watch.elapsed_time))
