import multiprocessing as mp

def sub_process(name):
    print("[sub] start")
    print(name)
    print("[sub] end")

if __name__ == "__main__":
    print("[main] start")
    p = mp.Process(target = sub_process)