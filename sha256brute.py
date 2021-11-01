import hashlib, multiprocessing as mp
import time as timer


def bruteThread(number, chars, jump, sha, done,_list):
    start = timer.time()
    b = [number]
    a = len(chars)
    b_len = 1
    c = 0
    while True:
        c += 1
        for i in range(b_len - 1, -1, -1):
            if b[i] >= a:
                b[i] = b[i] % a
                if i == 0:
                    b.insert(0, int(b[i]/a))
                    b_len += 1
                    if number == 0:
                        print(f"Brutforcing at: {b_len} characters")
                else:
                    b[i - 1] += 1
        x = ""

        for i in b:
            try: x += chars[i]
            except Exception:
                print(b,i,number)
                return


        if hashlib.sha256(x.encode()).hexdigest() == sha:
            pw = hashlib.sha256(x.encode()).hexdigest()
            _list.append(x)
            _list.append(c)
            _list.append(number)
            done.set()
            return

        b[b_len - 1] += jump


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
        mp_list = mp.Manager().list()
        done = mp.Event()
        jobs = []
        start = timer.time()
        print(f'Starting with {threadcount} {"subprocess" if threadcount == 1 else "subprocesses"}..')
        for x in range(threadcount):
            p = mp.Process(target=bruteThread, args=(x, chars, threadcount, sha, done,mp_list))
            jobs.append(p)
            p.start()
        print('All subprocesses successfully started!')
        done.wait()
        time = timer.time() - start
        for x in jobs:
            x.kill()
        print()
        print(f"|Password: {mp_list[0]}")
        print(f"|SHA256: {sha}")
        print(f"|Time: {round(time,2)}s")
        print(f"|Hashes~: {mp_list[1]*threadcount}")  # fix
        speed_s = int((mp_list[1]*threadcount) / time)
        print(f"|Speed~: {speed_s}H/s -> ~{round(speed_s/1000)}kH/s -> ~{round(speed_s/1000000)}MH/s")
        print(f"|Subprocess: {mp_list[2]}")
