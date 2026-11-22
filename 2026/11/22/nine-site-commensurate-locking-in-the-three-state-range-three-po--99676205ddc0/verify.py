#!/usr/bin/env python3
"""Exact finite checks for a three-colour, range-three antiferromagnetic Potts ring."""
from itertools import product, permutations
from collections import Counter

ALPHABET = tuple(range(3))
STATES = tuple(product(ALPHABET, repeat=3))
IDX = {s:i for i,s in enumerate(STATES)}
TRANS = [[(IDX[(b,c,d)], int(d==a)+int(d==b)+int(d==c))
          for d in ALPHABET] for a,b,c in STATES]

def brute(n):
    best=None; ways=0
    for spins in product(ALPHABET, repeat=n):
        energy=sum(spins[i]==spins[(i+d)%n] for i in range(n) for d in (1,2,3))
        if best is None or energy<best: best,ways=energy,1
        elif energy==best: ways+=1
    return best,ways

def transfer(n):
    best=None; ways=0
    for start in range(len(STATES)):
        dynamic={start:(0,1)}
        for _ in range(n):
            nxt={}
            for p,(val,num) in dynamic.items():
                for q,cost in TRANS[p]:
                    new=val+cost
                    if q not in nxt or new<nxt[q][0]: nxt[q]=(new,num)
                    elif new==nxt[q][0]: nxt[q]=(new,nxt[q][1]+num)
            dynamic=nxt
        if start in dynamic:
            val,num=dynamic[start]
            if best is None or val<best: best,ways=val,num
            elif val==best: ways+=num
    return best,ways

def prescribed(n):
    word=(0,0,1,2,2,0,1,1,2)
    assert n%9==0
    strings=set()
    for offset in range(3):
        for p in permutations(ALPHABET):
            strings.add(tuple(p[word[(i+offset)%9]] for i in range(n)))
    return strings

def main():
    checks=0
    for n in range(7,13):
        assert brute(n)==transfer(n)
        checks+=1
    for n in range(7,109):
        energy,count=transfer(n)
        assert energy*3>=n
        assert (energy*3==n)==(n%9==0)
        if n%9==0:
            assert energy==n//3 and count==18
            explicit=prescribed(n)
            assert len(explicit)==18
            for spins in explicit:
                assert sum(spins[i]==spins[(i+d)%n] for i in range(n) for d in (1,2,3))==n//3
        checks+=1
    print('RANGE_THREE_POTTS_CHECKS_PASSED',checks)

if __name__=='__main__': main()
