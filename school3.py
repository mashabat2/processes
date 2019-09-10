import threading, random
from threading import Thread
import time


class ReadText:
    def __init__(self, text):
        self.text = text


    def read_text(self):
        names = []
        with open(self.text) as file:
            for name in file:
                name = name.strip()
                names.append(name)
        return names



class SplitChild:
    def __init__(self, names):
        self._mutex = threading.RLock()
        self.names = names


    def f(self):
        self._mutex.acquire()
        random_class = []

        for name in self.names:
            self.names.remove(name)
            if len(random_class) < 10:
                random_class.append(name)
            else:
                break
        print('В ' + str(random.randint(1,11)) + ' классе учатся:', random_class, '\n')
        self._mutex.release()


def main():
    t0 = time.time()

    text = ReadText('a.txt').read_text()

    childs = SplitChild(text)
    p = Thread(target=childs.f)
    p2 = Thread(target=childs.f)

    p.start()
    p.join()

    p2.start()
    p2.join()

    print('time:', time.time() - t0)

if __name__ == '__main__':
    main()
