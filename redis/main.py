import redis
import datetime
import numpy as np


r = redis.Redis(host='127.0.0.1', port=6379, db=0)

print("set")
for n in [1, 10, 100, 1000, 10000, 100000]:
    print(f"started at {datetime.datetime.now()}")

    times = []
    for i in range(n):
        key = f"{i}"
        value = "some value"

        start = datetime.datetime.now()
        r.set(key, value)
        end = datetime.datetime.now()

        times.append((end - start).total_seconds())

    times = np.array(times)

    print(f"n = {n}")
    print(f"min: {np.min(times):.4f}s")
    print(f"max: {np.max(times):.4f}s")
    print(f"avg: {np.average(times):.4f}s")
    print(f"std: {np.std(times):.4f}s")
    print()
print(f"finished at {datetime.datetime.now()}")


print("get")
for n in [1, 10, 100, 1000, 10000, 100000]:
    print(f"started at {datetime.datetime.now()}")

    times = []
    for i in range(n):
        key = f"{i}"
        value = "some value"

        start = datetime.datetime.now()
        r.get(key)
        end = datetime.datetime.now()

        times.append((end - start).total_seconds())

    times = np.array(times)

    print(f"n = {n}")
    print(f"min: {np.min(times):.4f}s")
    print(f"max: {np.max(times):.4f}s")
    print(f"avg: {np.average(times):.4f}s")
    print(f"std: {np.std(times):.4f}s")
    print()
print(f"finished at {datetime.datetime.now()}")
