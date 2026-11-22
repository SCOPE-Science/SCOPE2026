"""Exact small-state checks for a fixed-length exclusion ring, its sectors and current."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque
from math import comb, gcd

def compositions(total, n):
    if n==1:
        yield (total,)
    else:
        for a in range(total+1):
            for b in compositions(total-a,n-1):
                yield (a,)+b

def transitions(state,L,N,I):
    x,h=state
    for j in range(N):
        for direction in (1,-1):
            donor=j if direction==1 else (j-1)%N
            receiver=(j-1)%N if direction==1 else j
            if h[donor]<I:continue
            z=list(h); z[donor]-=I;z[receiver]+=I
            xx=(x+direction*I*(j==0))%L
            yield (xx,tuple(z)), donor, direction

def sector_key(s,L,I):
    x,h=s
    K=sum(a//I for a in h)
    if K:return (tuple(a%I for a in h),x%gcd(L,I))
    return (tuple(a%I for a in h),x)

def sectors(L,N,I):
    states=[(x,h) for h in compositions(L-N,N) for x in range(L)]
    unvisited=set(states)
    classes=[]
    while unvisited:
        s=next(iter(unvisited)); Q=deque([s]);unvisited.remove(s); cl=[]
        while Q:
            v=Q.popleft();cl.append(v)
            for vv,_,_ in transitions(v,L,N,I):
                if vv in unvisited:
                    unvisited.remove(vv);Q.append(vv)
        classes.append(cl)
    keys={}
    for c in classes:
        k={sector_key(s,L,I) for s in c}
        assert len(k)==1,(L,N,I,k)
        q=next(iter(k)); assert q not in keys,(L,N,I,q)
        keys[q]=c
    return keys

def w(g):
    return F(2) if g==3 else F(1)

def equilibrium_sector(cl,L,N,I):
    # Full state mass is the product of headway weights; all sites in phase equally weighted.
    weights={s:__import__('math').prod((w(1+h) for h in s[1]),start=F(1)) for s in cl}
    Z=sum(weights.values(),F(0))
    for s in cl:
        ins=F(0); outs=F(0)
        for t in cl:
            for dest,donor,direction in transitions(t,L,N,I):
                rate=(F(2) if direction==1 else F(1))*w(1+t[1][donor]-I)/w(1+t[1][donor])
                if t==s:outs+=weights[s]*rate
                if dest==s:ins+=weights[t]*rate
        assert ins==outs,(L,N,I,cl[0],s,ins,outs)
    k=sum(h//I for h in cl[0][1]);
    if not k:return
    residues=tuple(h%I for h in cl[0][1])
    def zpart(kk):
        return sum((__import__('math').prod((w(1+residues[i]+I*v[i]) for i in range(N)),start=F(1)) for v in compositions(kk,N)),F(0))
    expected=F(I*N,L)*zpart(k-1)/zpart(k)
    measured=sum(weights[s] * F(I,L) * sum((F(2)-F(1))*w(1+h-I)/w(1+h) for h in s[1] if h>=I) for s in cl)/Z
    assert expected==measured,(expected,measured)

for L in range(4,12):
 for N in range(2,min(5,L)):
  for I in range(2,min(5,L)):
   cls=sectors(L,N,I)
   for c in cls.values():
    if len(c)>120:continue
    equilibrium_sector(c,L,N,I)
   Fcount=sum(1 for cc in combinations(range(L),N)
           if all(((cc[(i+1)%N]-cc[i])%L -1)<I for i in range(N)))
   exact=(L*sum(1 for a in product(range(I),repeat=N) if sum(a)==L-N))//N
   assert Fcount==exact,(L,N,I,Fcount,exact)
print('PASS: exhaustive communicating classes, exact Gibbs global balance, sector current, frozen counts on finite rings.')
for L,N,I in ((12,8,2),(12,6,2),(15,10,2)):
 V=L-N
 count=L*sum(1 for a in product(range(I),repeat=N) if sum(a)==V)//N
 print(f'L={L}, N={N}, I={I}: {count} frozen out of {comb(L,N)}')
