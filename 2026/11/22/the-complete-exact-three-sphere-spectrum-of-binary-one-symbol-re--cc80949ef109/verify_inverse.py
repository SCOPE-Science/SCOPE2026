"""Reverse reduction membership check, independent of forward generation."""
from itertools import product
from functools import lru_cache

def initial_run(w):
    i = 1
    while i < len(w) and w[i] == w[0]:i += 1
    return i

def expected(n,r):
    return n*(n+1)*(n+2)//6 + r*(n+2)-r*(r-1)//2

@lru_cache(None)
def inverse_step(w):
    return frozenset(w[:i]+w[i+1:] for i in range(1,len(w)) if w[i]!=w[i-1])

@lru_cache(None)
def inverse_three(y):
    d={y}
    for step in range(3):
        d={v for w in d for v in inverse_step(w)}
    return frozenset(d)

def run():
    for n in range(1,9):
        hist={x:0 for x in map(''.join,product('01',repeat=n))}
        for ytuple in product('01', repeat=n+3):
            y=''.join(ytuple)
            for parent in inverse_three(y):
                if parent in hist:hist[parent]+=1
        for x,count in hist.items():
            assert count==expected(n,initial_run(x)),(x,count)
        print('PASS inverse n=',n,'sources=',len(hist))

if __name__=='__main__':run()
