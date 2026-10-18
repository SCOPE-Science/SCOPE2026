#!/usr/bin/env python3
from itertools import combinations, permutations
from math import gcd

# Exact arithmetic in Z[zeta_30] = Z[x]/Phi_30(x),
# Phi_30(x) = x^8+x^7-x^5-x^4-x^3+x+1.
PHI = (1,1,0,-1,-1,-1,0,1,1)
ZERO = (0,)*8
ONE = (1,)+(0,)*7
Z = (0,1)+(0,)*6

def add(a,b):
    return tuple(a[i]+b[i] for i in range(8))

def neg(a):
    return tuple(-v for v in a)

def mul(a,b):
    c=[0]*15
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                if bj:
                    c[i+j]+=ai*bj
    for d in range(14,7,-1):
        q=c[d]
        if q:
            c[d]=0
            s=d-8
            for i in range(8):
                c[s+i]-=q*PHI[i]
    return tuple(c[:8])

def power(a,n):
    r=ONE
    while n:
        if n&1:
            r=mul(r,a)
        a=mul(a,a)
        n//=2
    return r

ZP=[power(Z,k) for k in range(30)]
assert power(Z,30)==ONE and power(Z,15)!=ONE and power(Z,10)!=ONE and power(Z,6)!=ONE

# F_25 = F_5[a]/(a^2-2), represented by pairs u+v*a.
def fmul(x,y):
    return ((x[0]*y[0]+2*x[1]*y[1])%5,
            (x[0]*y[1]+x[1]*y[0])%5)

def fpow(x,n):
    r=(1,0)
    while n:
        if n&1:
            r=fmul(r,x)
        x=fmul(x,x)
        n//=2
    return r

def trace(x):
    # a^5=-a, so Tr(u+v*a)=2u.
    return (2*x[0])%5

g=(1,2)
assert fpow(g,24)==(1,0)
assert fpow(g,12)!=(1,0) and fpow(g,8)!=(1,0)

H=[fpow(g,4*t) for t in range(6)]
assert len(set(H))==6
REPS=[fpow(g,i) for i in range(4)]

def entry(r,s,j):
    # chi_j(g^(4t)) = zeta_6^(jt) = zeta_30^(5jt);
    # epsilon(x)=zeta_5^Tr(x)=zeta_30^(6Tr(x)).
    rs=fmul(r,s)
    out=ZERO
    for t,h in enumerate(H):
        out=add(out,ZP[(5*j*t+6*trace(fmul(h,rs)))%30])
    return out

def determinant(M):
    n=len(M)
    total=ZERO
    for p in permutations(range(n)):
        inv=sum(p[i]>p[k] for i in range(n) for k in range(i+1,n))
        term=ONE
        for i,j in enumerate(p):
            term=mul(term,M[i][j])
        total=add(total,neg(term) if inv&1 else term)
    return total

def census(M):
    n=len(M)
    by_size={}
    witnesses=[]
    for k in range(1,n+1):
        total=zeros=0
        for I in combinations(range(n),k):
            for J in combinations(range(n),k):
                total+=1
                D=determinant([[M[i][j] for j in J] for i in I])
                if D==ZERO:
                    zeros+=1
                    if len(witnesses)<12:
                        witnesses.append((k,I,J))
        by_size[k]=(total,zeros)
    return by_size,witnesses

expected={
  0:{1:(25,0),2:(100,0),3:(100,0),4:(25,0),5:(1,0)},
  1:{1:(16,0),2:(36,0),3:(16,0),4:(1,0)},
  2:{1:(16,0),2:(36,10),3:(16,0),4:(1,0)},
  3:{1:(16,8),2:(36,18),3:(16,8),4:(1,0)},
  4:{1:(16,0),2:(36,10),3:(16,0),4:(1,0)},
  5:{1:(16,0),2:(36,0),3:(16,0),4:(1,0)},
}

summary={}
for j in range(6):
    reps=[(0,0)]+REPS if j==0 else REPS
    M=[[entry(r,s,j) for s in reps] for r in reps]
    by_size,witnesses=census(M)
    assert by_size==expected[j], (j,by_size)
    assert determinant(M)!=ZERO
    order=1 if j==0 else 6//gcd(j,6)
    summary[j]=(order,sum(z for _,z in by_size.values()),witnesses[:1])

# Explicit failure witnesses.
assert summary[2][2][0]==(2,(0,1),(0,3))
assert summary[3][2][0]==(1,(0,),(1,))
assert summary[4][2][0]==(2,(0,1),(0,3))

# NVM exactly for character orders 1 and 6.
nvm_orders={summary[j][0] for j in range(6) if summary[j][1]==0}
assert nvm_orders=={1,6}
assert {j for j in range(6) if summary[j][1]==0}=={0,1,5}

print("VERIFY_OK")
print("j:order:zero_minors =", " ".join(f"{j}:{summary[j][0]}:{summary[j][1]}" for j in range(6)))
