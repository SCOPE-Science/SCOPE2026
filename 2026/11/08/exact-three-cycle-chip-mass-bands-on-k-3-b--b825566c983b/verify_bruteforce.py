"""Independent exhaustive test of the period-three chip-mass polynomial on K_{3,b}."""
from collections import Counter
from itertools import product
from math import comb

def step(state,b):
    # The first three vertices have b neighbors; the remaining b have three.
    first_fires=sum(v>=b for v in state[:3])
    second_fires=sum(v>=3 for v in state[3:])
    return tuple(v + second_fires - b*(v>=b) for v in state[:3]) + tuple(v + first_fires - 3*(v>=3) for v in state[3:])

def predicted(b):
    result=Counter()
    for r in range(1,b-1):
        for s in range(1,b-r):
            t=b-r-s
            w=6*comb(b,r)*comb(b-r,s)
            for i in range(r):
                for j in range(s):
                    for k in range(t):
                        result[4*b+i+j+k]+=w
                        result[6*b+i+j+k]+=w
    return result

def enumerated(b):
    histogram=Counter()
    checked=0
    for small in product(range(2*b),repeat=3):
        for large in product(range(6),repeat=b):
            state=small+large
            next1=step(state,b)
            if next1!=state and step(step(next1,b),b)==state:
                histogram[sum(state)]+=1
            checked+=1
    return checked,histogram

def main():
    for b in (3,4):
        n,h=enumerated(b)
        p=predicted(b)
        assert h==p, (b,h,p)
        expected=12*b*(b-1)*(b-2)*3**(b-3)
        assert sum(h.values())==expected
        print(f'PASS b={b}; bounded states={n}; primitive-three configurations={sum(h.values())}; histogram={sorted(h.items())}')
    print('ALL BRUTE-FORCE CHECKS PASSED')

if __name__=='__main__': main()
