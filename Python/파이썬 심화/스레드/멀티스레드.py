import threading

def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>>")
    print(f"[sub] {keyword}로 검색을 시작합니다 ...")
    print("[sub] end")

print("[main] start")
worker = threading.Thread(target = work)

worker.start()

print("[main] 메인 스레드는 자기할일을 합니다. .. ")