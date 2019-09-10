from multiprocessing import Process
import random
import time


class A:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def f(text):
        a = []
        b = []
        with open(text) as f1:
            for name in f1:
                name = name.strip()
                if len(a)<=10 or len(b)<=10:
                    rand = random.randint(1,2)
                    if rand == 1:
                        a.append(name)
                    else:
                        b.append(name)
                else:
                    break
        print('В классе А:',a,'\n','В классе Б:',b)

def main():
    t0 = time.time()

    p = Process(target=A.f, args=('a.txt',))
    p.start()
    p.join()

    print('time:', time.time() - t0)


if __name__ == '__main__':
    main()
