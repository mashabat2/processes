from queue import Queue
from threading import Thread  # (2 класса "AB" учеников)
import time


class SearchName:
    def __init__(self, text):
        super().__init__()
        self.text = text

    def search(self, q):
        with open(self.text) as text1:
            for i in text1:
                q.put(i)
            q.put(None)
            q.put(None)

    @staticmethod
    def splitting(q, clas):
        while True:
            item = q.get()
            if item is None:
                break
            print(clas, item)

def main():
    t0 = time.time()

    q = Queue(2)
    A = Thread(target=SearchName.splitting, args=(q, "A class:"))
    B = Thread(target=SearchName.splitting, args=(q, "B class:"))

    A.start()
    B.start()

    SearchName('a.txt').search(q)

    A.join()
    B.join()

    print('time:', time.time() - t0)

if __name__ == '__main__':
    main()




