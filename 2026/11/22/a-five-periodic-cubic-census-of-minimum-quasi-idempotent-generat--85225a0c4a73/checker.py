#!/usr/bin/env python3
"""Exact integer certificate for a five-periodic generating-set census."""
INF=10**9
S=[(l,r,a,b) for l in (0,1) for r in (0,1) for a in (0,1) for b in (0,1)]
I={s:i for i,s in enumerate(S)}
T=[[] for _ in S]
for i,(L,R,A,B) in enumerate(S):
    for l,r in ((0,1),(1,0),(1,1)):
        if (L or l) and (R or r) and (l or B):
            T[i].append((I[(l,r,R,A)],l+r))

def step(v):
    new=[(INF,0)]*16
    for i,(c,m) in enumerate(v):
        if c==INF: continue
        for j,w in T[i]:
            x,y=new[j]
            if c+w<x: new[j]=(c+w,m)
            elif c+w==x: new[j]=(x,y+m)
    return new
A=[(0,1,0,1),(0,1,1,0),(0,1,1,1),(1,0,1,0),
   (1,0,1,1),(1,1,0,1),(1,1,1,0),(1,1,1,1)]
C=(5,5,6,5,6,6,6,7)
def E(j):
    v=(2*j+1)*(2*j*j+8*j+3)
    assert v%3==0
    return v//3
def vector(j):
    nums=(2*j+1,1,2*j+1,2*j+1,E(j),(j+1)*(2*j+1),2*j+1,E(j))
    x=[(INF,0)]*16
    for s,c,m in zip(A,C,nums): x[I[s]]=(c+6*j,m)
    return x
v=[(INF,0)]*16
v[I[(0,1,0,0)]]=(1,1)
for _ in range(3):v=step(v)
assert v==vector(0), 'initial vector'
# With the constant vector C, every five-step choice of optimal arcs is
# independent of j. Its count entries are degree <=3 polynomials in j.
# Four distinct evaluations certify identity of such polynomials.
for j in range(4):
    v=vector(j)
    for _ in range(5):v=step(v)
    assert v==vector(j+1),('five-step certificate',j)
for j in range(4):
    v=vector(j)
    target=(1,(j+1)*(2*j+3),2*(j+1),2*j+3,E(j+1))
    for h,wanted in enumerate(target):
        best=min(c for s,(c,m) in zip(S,v) if s[1]==s[2]==1)
        count=sum(m for s,(c,m) in zip(S,v) if c==best and s[1]==s[2]==1)
        assert count==wanted,('terminal',j,h,count,wanted)
        v=step(v)
def formula(n):
    if n==4:return 1
    k,r=divmod(n,5)
    if r==0:return ((2*k-1)*(2*k*k+4*k-3))//3
    if r==1:return 1
    if r==2:return k*(2*k+1)
    if r==3:return 2*k
    return 2*k+1
v=[(INF,0)]*16;v[I[(0,1,0,0)]]=(1,1)
for i in range(2,59):
    v=step(v)
    n=i+2
    best=min(c for s,(c,m) in zip(S,v) if s[1]==s[2]==1)
    num=sum(m for s,(c,m) in zip(S,v) if c==best and s[1]==s[2]==1)
    assert num==formula(n),(n,num,formula(n))
    assert best+1==6*n//5-(n%5==1),(n,best)
print('QUASI_IDEMPOTENT_MINIMAL_GENERATOR_CENSUS_CERTIFICATE_PASSED')
