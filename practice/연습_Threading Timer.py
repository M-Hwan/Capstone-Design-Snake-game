import time
import threading

end = False
score = 100000

def score_decrease(second):
    global end, score

    if end:
        return
    score -= 10
    print(score)
    threading.Timer(second, score_decrease, [second]).start()

score_decrease(2)