import hashlib,multiprocessing as mp
import time as timer

def bruteThread(number,chars,jump,sha,done):
    start = timer.time()
    b = [number]
    a = len(chars)
    b_len = 1
    c = 0
    while True:
        c+=1
        for i in range(b_len-1, -1, -1):
            if b[i] >= a:
                b[i] = b[i] - a
                if i == 0:
                    b.insert(0, 0)
                    b_len+=1
                    if number == 0:
                        print(f"Brutforcing at: {b_len} characters")
                else:
                    b [i-1] += 1
        x = ""
        for i in b:
            x += chars [i]

        if hashlib.sha256(x.encode()).hexdigest() == sha:
            pw = hashlib.sha256(x.encode()).hexdigest()
            print(f"|Password: {x}")
            print(f"|SHA256: {pw}")
            time = timer.time()-start
            print(f"|Time: {time}")
            print(f"|Hashes: {c}") #fix
            print(f"|Speed: {int(c/time)}H/s")
            done.set()
            return

        b [b_len - 1] += jump


if __name__ == "__main__":
    while True:
        sha = input("SHA256 hash: ")
        mode = input("Mode: ")
        if mode == "number" or mode == "1" or mode == "num":
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
            continue
        threadcount = mp.cpu_count()
        done = mp.Event()
        jobs = []

        for x in range(threadcount):
            p = mp.Process(target=bruteThread, args=(x,chars,threadcount,sha,done,))
            jobs.append(p)
            p.start()
        done.wait()
        for x in jobs:
            x.kill()
