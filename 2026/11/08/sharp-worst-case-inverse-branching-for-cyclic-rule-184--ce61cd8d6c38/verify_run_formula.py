#!/usr/bin/env python3
"""Independent run decomposition and integer transfer-matrix checks."""
from random import Random


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]


def run_formula(y):
    n=len(y)
    if y=='0'*n or y=='1'*n:return 1
    start=next(i for i in range(n) if y[i]=='0' and y[(i-1)%n]=='1')
    word=''.join(y[(start+j)%n] for j in range(n))
    runs=[]
    i=0
    while i<n:
        val=word[i]
        j=i+1
        while j<n and word[j]==val:j+=1
        runs.append((val,j-i))
        i=j
    assert len(runs)%2==0 and runs[0][0]=='0' and runs[-1][0]=='1'
    a=[runs[j][1] for j in range(0,len(runs),2)]
    b=[runs[j][1] for j in range(1,len(runs),2)]
    t=len(a)
    P=[[1,0],[0,1]]
    for j in range(t):
        M=[[int((b[j]==1 and u==1) or (a[(j+1)%t]==1 and v==1)) for v in (0,1)] for u in (0,1)]
        P=matmul(P,M)
    return P[0][0]+P[1][1]


def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


def luc(n):
    a,b=2,1
    for _ in range(n):a,b=b,a+b
    return a

for n in range(1,201):
    if n%2==0:
        y='01'*(n//2)
        assert run_formula(y)==luc(n//2)
    else:
        y='00'+('10'*((n-1)//2)) if n>=3 else '0'
        # fix length n: 00 + 10*(k-1) + 1, e.g. 00101
        if n>=3:
            k=(n-1)//2
            y='00'+'10'*(k-1)+'1'
        assert len(y)==n and run_formula(y)==fib((n+1)//2)
R=Random(11449)
for n in [4,5,7,8,11,16,20,33,48,71,100,199]:
    for _ in range(100):
        y=''.join(str(R.randrange(2)) for _ in range(n))
        assert run_formula(y)==run_formula(y[1:]+y[:1])
        if n>=4:
            cap=luc(n//2) if n%2==0 else fib((n+1)//2)
            assert run_formula(y)<=cap
print('RUN_FORMULA_VERIFY_OK 200')
