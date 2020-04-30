import time

start_time = time.time()

while True:
    print(time.time() - start_time)
    if time.time() - start_time >= 10:
        break
