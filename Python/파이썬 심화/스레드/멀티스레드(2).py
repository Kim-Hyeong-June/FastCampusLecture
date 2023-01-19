import threading
import time


def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 오!!! 지금이 매수 타이밍인가")
        time.sleep(1)
        print("[매수] 풀매수 가즈아!! ...")
        time.sleep(1)

def saler():
    for i in range(5):
        print("[매도] 데이터 요청 중...")
        time.sleep(1)
        print("[매도] 데이터 분석 중...")
        time.sleep(1)
        print("[매도] 오!!! 지금이 매수 타이밍인가")
        time.sleep(1)
        print("[매도] 풀매수 가즈아!! ...")
        time.sleep(1)

print("[메인] start")
buyer = threading.Thread(target = buyer)
saler = threading.Thread(target = saler)
buyer.start()
saler.start()

buyer.join()
saler.join()

print("#메인장이 종료 되었습니다.")