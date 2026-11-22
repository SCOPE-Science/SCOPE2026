#!/usr/bin/env python3
"""Supplementary finite tests for a four-point Fourier cancellation theorem.

This is a finite floating-point diagnostic, not a proof of the theorem.
Run: python CHECK.py
"""
from itertools import combinations
from math import comb, cos, pi
import cmath


def predicted(N):
    if N % 2 == 0:
        return 0.0
    return 2*(cos(pi/N)-cos(2*pi/N))


def gaps(points, N):
    p = sorted(points)
    return [p[1]-p[0],p[2]-p[1],p[3]-p[2],N+p[0]-p[3]]


def expected_odd(points,N):
    m=(N-3)//2
    target=[1,m,2,m]
    g=gaps(points,N)
    return any(g == target[i:]+target[:i] for i in range(4)) or any(g[::-1] == target[i:]+target[:i] for i in range(4))


def expected_even(points,N):
    s=set(points)
    return all((a+N//2)%N in s for a in s)


def run():
    total=0
    for N in range(4,27):
        z=[cmath.exp(2j*pi*j/N) for j in range(N)]
        minimum=predicted(N)
        equal=0
        for A in combinations(range(N),4):
            total+=1
            observed=abs(sum(z[a] for a in A))
            tolerance=2e-9
            assert observed >= minimum-tolerance, (N,A,observed,minimum)
            exact=expected_even(A,N) if N%2==0 else expected_odd(A,N)
            found=abs(observed-minimum)<tolerance
            assert found==exact, (N,A,observed,minimum,found,exact)
            equal+=found
        wanted=comb(N//2,2) if N%2==0 else N
        assert equal==wanted, (N,equal,wanted)
        print(f'N={N}: minimum={minimum:.12g}; minimizers={equal}; PASS')
    print(f'PASS: {total} four-subsets checked; formula and equality orbits for every N=4,...,26.')

if __name__=='__main__':
    run()
