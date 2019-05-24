import sys
import random
from linkedbst import LinkedBST
import time
import copy

sys.setrecursionlimit(500000)

def search(file):

    with open(file, 'r') as f:
        done = f.readlines()
    for i in range(len(done)):
        done[i] = done[i].rstrip().lower()

    words = []
    for i in range(10000):
        words.append(random.choice(done))

    words = list(set(words))
    tree = LinkedBST(set(done))

    def first():
        start_time = time.time()
        for word in words:
            num = done.index(word)
        fin_time = time.time() - start_time
        return fin_time

    def second():
        start_time = time.time()
        for word in words:
            tree.find(word)
        fin_time = time.time() - start_time
        return fin_time

    def third():
        new_tree = copy.deepcopy(tree)
        new_tree.rebalance()
        start_time = time.time()
        for word in words:
            new_tree.find(word)
        fin_time = time.time() - start_time
        return fin_time

    print('1 : ', first())
    print('2 : ', second())
    print('3 : ', third())

if __name__ == '__main__':
    search('words.txt')
