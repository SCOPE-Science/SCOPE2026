#!/usr/bin/env python3
"""Independent exhaustive enumeration of weight <= n labels on L(K_n).
Uses direct closed neighborhoods, not the classification theorem.
"""
from itertools import combinations
from math import factorial

def exhaustive(n):
    E=list(combinations(range(n),2)); m=len(E)
    adj=[[j for j,(u,v) in enumerate(E) if u in e or v in e] for e in E]
    f=[0]*m
    counts={}
    tests=0
    def emit(weight):
        nonlocal tests
        tests+=1
        for neighborhood,lab in zip(adj,f):
            if lab<=1:
                s=sum(f[j] for j in neighborhood)
                if s<3 or s>4: return
        counts[weight]=counts.get(weight,0)+1
    def rec(i,weight):
        if i==m:
            emit(weight)
            return
        for lab in range(min(3,n-weight)+1):
            f[i]=lab
            rec(i+1,weight+lab)
        f[i]=0
    rec(0,0)
    return tests,counts

if __name__=='__main__':
    for n,expected in [(5,22),(6,130),(7,822)]:
        tests,counts=exhaustive(n)
        assert counts=={n:expected},(n,counts)
        print(f'n={n}: tested {tests} labelings of weight <= {n}; exactly {expected} feasible, all weight {n}')
    print('DIRECT_EXHAUSTIVE_PASS')
