#!/usr/bin/env python3
"""Independent exact coefficient extraction from the excursion sign grammar."""
from collections import defaultdict
from math import comb
N=78
# E: positive (or negative) primitive first-return excursion.
E=[0]*(N+1)
for j in range(1,N//2+1):
    E[2*j]=comb(2*j-2,j-1)//j
M=[0]*(N+1);M[0]=1
for n in range(1,N+1): M[n]=2*comb(n-1,(n-1)//2)
# Sign-sequence grammar: state -1 empty, 0 starting with negative, 1 currently positive, 2 currently negative after initial positive.
S=[defaultdict(int) for _ in range(N//2+1)]
S[0][(-1,0)]=1
for ell in range(1,N//2+1):
    for (state,k),num in S[ell-1].items():
        if state==-1:
            S[ell][(0,0)]+=num # first negative: permanently terminal
            S[ell][(1,0)]+=num # first positive
        elif state==0:
            S[ell][(0,0)]+=2*num
        elif state==1:
            S[ell][(1,k)]+=num
            S[ell][(2,k+1)]+=num
        else:
            S[ell][(2,k)]+=num
            S[ell][(1,k)]+=num
# Powers of E; E^ell is the weight for ell excursions.
powers=[[0]*(N+1) for _ in range(N//2+1)]
powers[0][0]=1
for ell in range(1,N//2+1):
    for n in range(2*ell,N+1):
        powers[ell][n]=sum(E[j]*powers[ell-1][n-j] for j in range(2,n+1,2))
# All length-n walks: complete excursion sequence plus terminal zero-free meander.
counts=[[0]*(N//4+2) for _ in range(N+1)]
for ell in range(N//2+1):
    krow=defaultdict(int)
    for (state,k),v in S[ell].items():krow[k]+=v
    for n in range(2*ell,N+1):
        weight=sum(powers[ell][j]*M[n-j] for j in range(2*ell,n+1))
        if not weight:continue
        for k,v in krow.items(): counts[n][k]+=weight*v
for n in range(N+1):
    assert sum(counts[n])==2**n,(n,sum(counts[n]))
    assert max(k for k,v in enumerate(counts[n]) if v)>=(n//4) if n>=4 else True
    assert sum((k>n//4)*v for k,v in enumerate(counts[n]))==0
    if n%2==0 and n+1<=N:assert all(counts[n+1][k]==2*counts[n][k] for k in range(len(counts[n])))
# Completely independent dynamic program: track walk altitude, first sign of current excursion,
# first completed excursion sign, last completed sign, and negative-run count.
dp={(0,None,None,None,0):1}
for n in range(1,51):
    nxt=defaultdict(int)
    for (h,current,first,last,k),number in dp.items():
        for step in ('a','b'):
            curr=current if h!=0 else step
            h2=h+(1 if step=='a' else -1)
            if h2==0:
                if first is None:
                    new_first=curr
                    new_last=curr
                    new_k=0
                else:
                    new_first=first
                    new_k=k+(first=='a' and curr=='b' and last=='a')
                    new_last=curr
                nxt[(0,None,new_first,new_last,new_k)]+=number
            else:
                nxt[(h2,curr,first,last,k)]+=number
    dp=nxt
    row=defaultdict(int)
    for (h,curr,first,last,k),v in dp.items():row[k]+=v
    for k,v in row.items():assert counts[n][k]==v,(n,k,counts[n][k],v)
    assert sum(row.values())==2**n
for n in (4,6,8,10,12,14,30,50,78):
    print(f'n={n:2} loss={counts[n][0]} nonzero={sum(counts[n][1:])} max={max(k for k,v in enumerate(counts[n]) if v)}')
print('PASS: 79 coefficient rows normalized; independent path-state DP checked through length 50')
