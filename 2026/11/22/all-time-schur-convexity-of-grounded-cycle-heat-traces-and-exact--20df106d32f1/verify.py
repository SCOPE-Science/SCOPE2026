#!/usr/bin/env python3
"""Reproducible finite checks for the discrete cyclic grounded heat-trace theorem.
The mathematical proof is analytic and does not depend on these finite tests.
"""
from itertools import combinations
from math import comb, exp, cos, pi, factorial
import numpy as np

def h(length, time):
    if length == 0:
        return 0.0
    return sum(exp(-time*(2-2*cos(pi*j/(length+1)))) for j in range(1,length+1))

def gaps(n, selected):
    ss=sorted(selected)
    return [(ss[(i+1)%len(ss)]-ss[i])%n or n for i in range(len(ss))]

def energy(n,selected,t):
    lap=np.zeros((n,n))
    for i in range(n):
        lap[i,i]=2
        lap[i,(i+1)%n]=-1
        lap[i,(i-1)%n]=-1
    keep=[i for i in range(n) if i not in selected]
    eig=np.linalg.eigvalsh(lap[np.ix_(keep,keep)]) if keep else []
    return sum(exp(-t*v) for v in eig)

def main():
    checks=0
    for length in range(1,7):
        for t in (.7,1.1,2.,3.):
            convex=h(length+1,t)-2*h(length,t)+h(length-1,t)
            assert convex>0, (length,t,convex)
            lower=2*exp(-2*t)*t**(2*length)/factorial(2*length)
            assert convex+1e-13>=lower
            checks+=2
    for n in range(3,11):
        for k in range(1,n+1):
            q,r=divmod(n,k)
            assert n*comb(k,r)%k==0
            optimum=n*comb(k,r)//k
            for t in (.7,1.3,2.0):
                count=0
                for ss in combinations(range(n),k):
                    gs=gaps(n,ss)
                    formula=sum(h(x-1,t) for x in gs)
                    actual=energy(n,ss,t)
                    assert abs(formula-actual)<2e-10,(n,k,ss,t,formula,actual)
                    target=(k-r)*h(q-1,t)+r*h(q,t)
                    assert formula+2e-10>=target,(n,k,ss,t)
                    balanced=(max(gs)-min(gs)<=1)
                    if balanced:
                        assert abs(formula-target)<2e-10
                        count+=1
                    else:
                        assert formula>target+1e-13,(n,k,ss,t,formula,target)
                    checks+=3
                assert count==optimum,(n,k,t,count,optimum)
                checks+=1
    # Integer walk counting gives an independent exact check of the key convexity mechanism.
    for size in range(1,13):
        for power in range(0,26):
            def closed(length):
                m=np.zeros((length,length),dtype=object)
                for i in range(length-1):m[i,i+1]=m[i+1,i]=1
                # repeated squaring via Python-integer matrices
                mat=np.eye(length,dtype=object)
                for _ in range(power):mat=mat@m
                return sum(mat[i,i] for i in range(length))
            d=closed(size+1)-2*closed(size)+ (closed(size-1) if size>1 else 0)
            assert d>=0,(size,power,d)
            if power==2*size:
                assert d>=2,(size,power,d)
            checks+=1
    print(f'PASS: {checks} independent finite checks; all tested balanced sets are exactly optimal.')

if __name__=='__main__':main()
