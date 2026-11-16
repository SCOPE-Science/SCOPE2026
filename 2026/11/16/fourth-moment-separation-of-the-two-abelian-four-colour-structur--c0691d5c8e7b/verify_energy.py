"""Exact 64-state energy certificate for proper four-colourings of K_{2,n}.
Python 3, standard library only. Run: python verify_energy.py
"""
from itertools import product
from collections import Counter
from pathlib import Path
import csv

EXPECTED = {
    'C4': {2: 2, 4: 12, 6: 30, 8: 1, 10: 18, 21: 1},
    'V4': {4: 18, 6: 24, 8: 3, 10: 18, 21: 1},
}

def plus(group, a, b):
    return (a+b)%4 if group=='C4' else a^b

def minus(group, a, b):
    return (a-b)%4 if group=='C4' else a^b

def states(group):
    for d0,d1,d2 in product(range(4), repeat=3):
        d3=minus(group, plus(group,d0,d1),d2)
        ds=(d0,d1,d2,d3)
        allowed=[tuple(x for x in range(4) if x not in (0,d)) for d in ds]
        score=0
        for a,b,c in product(*allowed[:3]):
            d=minus(group, plus(group,a,b), c)
            score+=(d in allowed[3])
        yield ds,score

def energy(group,n):
    return 64*sum(t**n for t, mult in EXPECTED[group].items() for _ in range(mult))

def main():
    with Path(__file__).with_name('T_TABLE.csv').open(encoding='utf8',newline='') as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==64
    for g in ('C4','V4'):
        data=list(states(g))
        assert [(int(row['d1']),int(row['d2']),int(row['d3'])) for row in rows]==[d[:3] for d,t in data]
        assert [int(row['T_'+g]) for row in rows]==[t for d,t in data]
        hist=dict(sorted(Counter(t for _,t in data).items()))
        assert len(data)==64 and hist==EXPECTED[g],(g,hist)
        print(g, 'T-histogram',hist)
        for n in range(1,8):
            assert energy(g,n)==64*sum(t**n for _,t in data)
    for n in range(1,11):
        diff=energy('V4',n)-energy('C4',n)
        surjections=sum((-1)**j*__import__('math').comb(3,j)*(4-j)**n for j in range(4))
        assert diff==128*2**n*surjections
        assert (diff==0)==(n<=2)
    print('PASS: complete 64-state census and all-length identities')
if __name__=='__main__':main()
