#!/usr/bin/env python3
"""Finite independent checks for exact period-doubling shift state complexity.
Requires only Python >=3.9. No finite experiment is used as an infinite proof.
"""
from collections import deque


def valuation2(t):
    assert t >= 1
    return (t & -t).bit_length() - 1


def expected(m, c):
    t = c + 1
    steps = 0
    while t > 1:
        t = (t + 1)//2
        steps += 1
    return steps + 2*m


def dfa(m, c):
    # states are ("g",q,e) or ("C",e); minimality not assumed
    first = ("g", c + 1, 0)
    queue = deque([first]); seen = {first}
    def go(st,b):
        if st[0] == "C": return st
        _,q,e=st
        if (q+b)%2: return ("C",e)
        return ("g",(q+b)//2,(e+1)%m)
    while queue:
        s=queue.popleft()
        for b in (0,1):
            t=go(s,b)
            if t not in seen:
                seen.add(t);queue.append(t)
    states=sorted(seen)
    def out(s):
        if s[0] == "C": return s[1]
        return (valuation2(s[1])+s[2])%m
    return first,states,go,out


def minimize_nstates(m,c):
    first,states,go,out=dfa(m,c)
    cells={s:out(s) for s in states}
    while True:
        # compute exact Moore refinement, independent of the claimed formula
        signatures={s:(cells[s],cells[go(s,0)],cells[go(s,1)]) for s in states}
        ids={v:i for i,v in enumerate(sorted(set(signatures.values())))}
        refine={s:ids[signatures[s]] for s in states}
        if len(set(refine.values())) == len(set(cells.values())):
            break
        cells=refine
    return len(states),len(set(refine.values())),first,go,out


def direct(m,c,n):return valuation2(n+c+1)%m


def digits_lsd(n):
    if n==0: return [0]
    ds=[]
    while n:
        ds.append(n%2); n//=2
    return ds


def main():
    nchecks=0
    for m in range(2,10):
        for c in range(256):
            reach, minimal, initial, go, out=minimize_nstates(m,c)
            formula=expected(m,c)
            assert (reach,minimal)==(formula,formula),(m,c,reach,minimal,formula)
            for n in range(80):
                state=initial
                for digit in digits_lsd(n): state=go(state,digit)
                assert out(state)==direct(m,c,n),(m,c,n)
                # arbitrary zero padding on the most-significant side
                for _ in range(3): state=go(state,0)
                assert out(state)==direct(m,c,n),(m,c,n,"padding")
                nchecks+=1
    # Compare 8192 letters of the substitution fixed point with valuation formula
    for m in range(2,10):
        word=[0]
        while len(word)<8192:
            word=[y for x in word for y in (0,(x+1)%m)]
        assert all(word[n]==valuation2(n+1)%m for n in range(8192))
    print(f"PASS: 2048 shift/modulus automata; {nchecks} numerical input checks; 8192-symbol fixed-point checks for 8 alphabet sizes")

if __name__=='__main__':main()
