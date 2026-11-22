#!/usr/bin/env python3
"""Exact standalone verification for a characteristic-11 Ciani quartic slice.
No optional packages, network access, or external files are required.
"""
from collections import Counter
from itertools import product
from math import factorial
P = 11

def fadd(x, y): return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)
def fneg(x): return ((-x[0])%P,(-x[1])%P)
def fsub(x,y): return fadd(x,fneg(y))
def fmul(x,y): return ((x[0]*y[0]-x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def fpow(x,n):
    ans=(1,0)
    while n:
        if n&1: ans=fmul(ans,x)
        x=fmul(x,x); n//=2
    return ans
def finv(x):
    assert x!=(0,0)
    return fpow(x,119)
def fq(n):return (n%P,0)
def fdiv(x,y):return fmul(x,finv(y))
def fsum(*xs):
    ans=(0,0)
    for x in xs:ans=fadd(ans,x)
    return ans
ZERO=(0,0);ONE=(1,0);W=(0,1)
FIELD=[(a,b) for a in range(P) for b in range(P)]
SQUARE_ROOTS={}
for v in FIELD:SQUARE_ROOTS.setdefault(fmul(v,v),[]).append(v)

# Calculate Hasse--Witt entries as exact coefficient polynomials of F^10.
# In each monomial, the first three entries are (degree in X,Y,Z),
# and the last two are (degree in r,s). The x^4,y^4,z^4 terms
# have coefficient 1; x^2 y^2 has coefficient r; the other two s.
TERMS=[(4,0,0,0,0),(0,4,0,0,0),(0,0,4,0,0),
       (2,2,0,1,0),(2,0,2,0,1),(0,2,2,0,1)]
def compositions(n,k):
    if k==1:
        yield (n,)
        return
    for m in range(n+1):
        for rest in compositions(n-m,k-1):yield (m,)+rest

def coeff_polynomial(target):
    out=Counter()
    for ks in compositions(10,6):
        exp=tuple(sum(ks[i]*TERMS[i][j] for i in range(6)) for j in range(3))
        if exp!=target:continue
        exr=sum(ks[i]*TERMS[i][3] for i in range(6))
        exs=sum(ks[i]*TERMS[i][4] for i in range(6))
        c=factorial(10)
        for k in ks:c//=factorial(k)  # successive divisions are exact
        out[(exr,exs)]+=c
    return {k:v%P for k,v in out.items() if v%P}

def padd(f,g):
    h=Counter(f)
    for k,v in g.items():h[k]+=v
    return {k:v%P for k,v in h.items() if v%P}
def pmul(f,g):
    out=Counter()
    for (a,b),u in f.items():
        for (c,d),v in g.items():out[(a+c,b+d)]+=u*v
    return {k:v%P for k,v in out.items() if v%P}
def pscale(f,k):return {p:(v*k)%P for p,v in f.items() if (v*k)%P}
def ppow(f,n):
    h={(0,0):1}
    for _ in range(n):h=pmul(h,f)
    return h

r={(1,0):1}; s={(0,1):1}; one={(0,0):1}
D=padd(ppow(r,2),pscale(one,-4))
E=pscale(pmul(s,padd(r,pscale(one,-2))),2)
F=padd(ppow(s,2),pscale(one,-4))
U=F
V=pscale(padd(ppow(s,2),pscale(r,-2)),2)
A=pmul(E,pmul(padd(ppow(E,2),pmul(D,F)),
              padd(ppow(E,2),pscale(pmul(D,F),8))))
B=pmul(V,pmul(padd(ppow(V,2),ppow(U,2)),
              padd(ppow(V,2),pscale(ppow(U,2),8))))
assert A == coeff_polynomial((20,10,10))
assert B == coeff_polynomial((10,10,20))
# The two duplicated diagonal coefficients are A; the remaining one is B.
# Factors of A on the smooth locus (r-2 is invertible).
t=ppow(s,2)
L1=padd(pscale(pmul(t,padd(r,one)),5),pscale(padd(r,pscale(one,2)),-4))
L2=padd(pmul(t,padd(r,pscale(one,8))),padd(r,pscale(one,2)))
assert A==pmul(pscale(pmul(s,ppow(padd(r,pscale(one,-2)),3)),2),pmul(L1,L2))

def value(poly,R,S):
    acc=ZERO
    for (i,j),k in poly.items():
        acc=fadd(acc,fmul(fq(k),fmul(fpow(R,i),fpow(S,j))))
    return acc

def smooth(R,S):
    return (R!=fq(2) and R!=fq(-2) and S!=fq(2) and S!=fq(-2)
            and fmul(S,S)!=fadd(R,fq(2)))

def rank(R,S):
    av=value(A,R,S);bv=value(B,R,S)
    return 2*(av!=ZERO)+(bv!=ZERO)

# Direct geometric computation of the intersections of A=0 and B=0.
# In t=s^2, the five B components are 2(t-2r)=c(t-4),
# c=0, +5, -5, +w, -w, w^2=-1. The three A components are
# s=0, 5t(r+1)=4(r+2), and t(r+8)=-(r+2).
CS=[ZERO,fq(5),fq(-5),W,fneg(W)]
geometric=set()
for c in CS:
    assert c!=fq(2) and c!=fq(-2)
    geometric.add((c,ZERO))
    t1=fdiv(fmul(fq(-4),fadd(c,fq(2))),fmul(fq(5),fsub(fq(2),c)))
    t2=fdiv(fadd(c,fq(2)),fsub(fq(2),c))
    r1=fdiv(fsub(fmul(fq(4),c),fq(2)),fq(5))
    r2=fdiv(fadd(fmul(fq(5),c),fq(2)),fq(4))
    assert t1!=t2 and t1!=fq(4) and t2!=fq(4)
    for rr,tt in ((r1,t1),(r2,t2)):
        # Every quadratic root is already in F_121, including both s roots.
        roots=SQUARE_ROOTS.get(tt,[])
        assert len(roots)==2
        for ss in roots:
            assert smooth(rr,ss)
            assert value(A,rr,ss)==ZERO and value(B,rr,ss)==ZERO
            geometric.add((rr,ss))
assert len(geometric)==25
# Along each B line the L1 and L2 equations are quadratics in t,
# with roots precisely {4,t1} and {4,t2}. The root 4 yields (r,t)=(2,4),
# which is excluded from the smooth base. Since t1,t2!=4, the surviving
# intersections are transverse. Distinct B lines meet only at (2,4).
# The remaining A component s=0 meets each B line transversely at (c,0).

for qfield,name in [(FIELD,'F121'),([(a,0) for a in range(P)],'F11')]:
    census=Counter();a0=b0=total=0;found=set()
    for R,S in product(qfield,repeat=2):
        if not smooth(R,S):continue
        total+=1
        a=value(A,R,S);b=value(B,R,S)
        a0+=(a==ZERO);b0+=(b==ZERO)
        k=rank(R,S);census[k]+=1
        if k==0:found.add((R,S))
    if name=='F121':
        assert total==14043 and [census[k] for k in range(4)]==[25,326,560,13132]
        assert a0==351 and b0==585 and found==geometric
    else:
        assert total==73 and [census[k] for k in range(4)]==[9,14,18,32]
        assert a0==23 and b0==27
    print(name,'smooth=',total,'p_ranks=',*[census[k] for k in range(4)],'A_zero=',a0,'B_zero=',b0)
print('CIANI_F11_25_REDUCED_SUPERSPECIAL_POINTS_VERIFIED')
