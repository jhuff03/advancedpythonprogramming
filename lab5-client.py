from lab5 import Time

t1 = Time(1, 2, 3)
t2 = Time(23, 9, 7)

print(t1.toString())

print(t1.timeInSeconds())

print(t1.whatTimeIsIt())\

print(t2.twelveHourClock())

print(t2.compareTo(t1))