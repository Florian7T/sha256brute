import threading,time,hashlib,multiprocessing
from timeit import default_timer as timer


def bruteThread(number,chars,jump,sha):
    startTimer = timer()
    b = [number]
    a = len(chars)
    while True:
        for i in range(len(b)-1, -1, -1):
            if b[i] >= a:
                b[i] = b[i] % a
                if i == 0:
                    b.insert(0, 1)
                    if number == 0:
                        print(f"Brutforcing at: {len(b)} characters")
                else:
                    b [i-1] += 1
        x = ""
        for i in b:
            x += chars [i]
        b[len(b) - 1] += jump
        if hashlib.sha256(x.encode()).hexdigest() == sha:
            pw = hashlib.sha256(x.encode()).hexdigest()
            c = ""
            print(f"|Password: {x}")
            print(f"|SHA256: {pw}")
            print(f"|Time: {timer()-startTimer}")



if __name__ == "__main__":
    sha = input("SHA256 hash: ")

    mode = input("Mode: ")
    if mode == "number" or mode == "1":
        chars = "0123456789"
    elif mode == "letter" or mode == "2":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif mode == "lower" or mode == "3":
        chars = "abcdefghijklmnopqrstuvwxyz"
    elif mode == "upper" or mode == "4":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif mode == "all" or mode == "5":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else:
        print(f'Mode: {mode} doesn\'t exist. Modes:')
        print("1: number")
        print("2: letter")
        print("3: lower")
        print("4: upper")
        print("5: all")
        exit(0)

    threadcount = int(input("CPU Cores: "))
    threading = False
    jobs = []
    for x in range(threadcount):
        if threading:
            t = threading.Thread(target=bruteThread, args=(x,))
            t.start()
        else:
            p = multiprocessing.Process(target=bruteThread, args=(x,chars,threadcount,sha,))
            jobs.append(p)
            p.start()




