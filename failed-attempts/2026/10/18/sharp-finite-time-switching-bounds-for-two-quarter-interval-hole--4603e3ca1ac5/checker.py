#!/usr/bin/env python3
"""Independent integer tests for finite-horizon switching of two Markov holes."""
from itertools import product

def matrix_count(schedule):
    zero, one = 1, 1
    for kind in schedule:
        if kind == 0:
            zero, one = one, zero + one
        else:
            zero, one = zero + one, zero
    return zero + one

def direct_count(schedule):
    n=len(schedule)
    return sum(all(not(bits[t]==bits[t+1]==schedule[t]) for t in range(n))
               for bits in product((0,1), repeat=n+1))

def fib(k):
    a,b=0,1
    for _ in range(k): a,b=b,a+b
    return a

def check():
    independent_cases=0
    for n in range(0,9):
        vals=[]
        for w in product((0,1),repeat=n):
            c=matrix_count(w)
            assert c==direct_count(w),(n,w,c,direct_count(w))
            vals.append((c,w));independent_cases+=1
        lo=min(c for c,_ in vals); hi=max(c for c,_ in vals)
        assert lo==n+2 and hi==fib(n+3), (n,lo,hi)
        if n>=2:
            assert {w for c,w in vals if c==lo}=={tuple(i%2 for i in range(n)),tuple((i+1)%2 for i in range(n))}
            assert {w for c,w in vals if c==hi}=={(0,)*n,(1,)*n}
    for n in range(9,16):
        vals=[(matrix_count(w),w) for w in product((0,1),repeat=n)]
        assert min(c for c,_ in vals)==n+2
        assert max(c for c,_ in vals)==fib(n+3)
        assert {w for c,w in vals if c==n+2}=={tuple(i%2 for i in range(n)),tuple((i+1)%2 for i in range(n))}
        assert {w for c,w in vals if c==fib(n+3)}=={(0,)*n,(1,)*n}
    # Two-step operator for the 0,1 schedule is B A, with transitions 1 to 0.
    A=((0,1),(1,1)); B=((1,1),(1,0))
    C=tuple(tuple(sum(B[i][j]*A[j][k] for j in range(2)) for k in range(2)) for i in range(2))
    assert C==((1,2),(0,1))
    for n in range(0,101):
        alt=tuple(i%2 for i in range(n)); static=(0,)*n
        assert matrix_count(alt)==n+2
        assert matrix_count(static)==fib(n+3)
    print('PASS: %d independent direct-bit versus matrix comparisons, n<=8'%independent_cases)
    print('PASS: all schedule extrema and uniqueness for n<=15')
    print('PASS: closed formulas up to n=100, and 2-step adjacency identity')

if __name__=='__main__':
    check()
