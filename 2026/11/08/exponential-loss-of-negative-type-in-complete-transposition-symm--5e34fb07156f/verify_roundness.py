#!/usr/bin/env python3
"""Exact class-character checks and rational-root sign certificates for permutation Cayley distance."""
from functools import lru_cache
from math import factorial
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=65
@lru_cache(None)
def partitions(n,cap=None):
    if n==0:return ((),)
    if cap is None:cap=n
    return tuple((k,)+p for k in range(min(cap,n),0,-1) for p in partitions(n-k,k))
def rim_sign(shape,inside):
    cells={(i,j) for i,r in enumerate(shape) for j in range(inside[i] if i<len(inside) else 0,r)}
    if not cells:return 0
    seen={next(iter(cells))}; todo=list(seen)
    while todo:
        i,j=todo.pop()
        for u in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if u in cells and u not in seen: seen.add(u);todo.append(u)
    if len(seen)<len(cells):return 0
    if any((i+1,j) in cells and (i,j+1) in cells and (i+1,j+1) in cells for i,j in cells):return 0
    return (-1)**(len({i for i,j in cells})-1)
@lru_cache(None)
def character(shape,cycles):
    if not cycles:return int(not shape)
    v=0
    for rest in partitions(sum(shape)-cycles[0]):
        if len(rest)>len(shape) or any(rest[i]>shape[i] for i in range(len(rest))):continue
        sg=rim_sign(shape,rest)
        if sg:v+=sg*character(rest,cycles[1:])
    return v
def cls_size(mu):
    z=1
    for j in set(mu):z*=j**mu.count(j)*factorial(mu.count(j))
    return factorial(sum(mu))//z
def coeffs(n):
    ps=partitions(n); out={}
    for shape in ps:
        dim=character(shape,(1,)*n)
        x=[sum(cls_size(mu)*character(shape,mu) for mu in ps if n-len(mu)==r) for r in range(1,n)]
        out[shape]=(dim,x)
    for mu in ps: assert sum(character(sh,mu)**2 for sh in ps)==factorial(n)//cls_size(mu)
    return out
EXPECTED={
 3:{(2,1):(0,-2),(1,1,1):(-3,2)},
 4:{(3,1):(6,-3,-6),(2,2):(0,-2,0),(2,1,1):(-6,-3,6),(1,1,1,1):(-6,11,-6)},
 5:{(4,1):(20,20,-20,-24),(3,2):(10,-5,-10,0),(3,1,1):(0,-30,0,24),(2,2,1):(-10,-5,10,0),(2,1,1,1):(-20,20,20,-24),(1,1,1,1,1):(-10,35,-50,24)}
}
for n in (3,4,5,6):
    data=coeffs(n)
    if n<6:
        for shape, row in EXPECTED[n].items():assert tuple(data[shape][1])==row,(n,shape)
    assert len(data)==len(partitions(n))
    print('character table orthogonality and central Fourier coefficients OK',n)

# Independent polynomial consistency check for the signed hook-character content factorization.
def polymul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
for n in range(3,8):
    dim, numbers=coeffs(n)[(n-2,1,1)]
    poly=[1]
    for j in range(n-2):poly=polymul(poly,[1,j])
    poly=polymul(polymul(poly,[1,-1]),[1,-2])
    assert [dim*v for v in poly[:n]]==[dim]+numbers,(n,poly,numbers)
print('Hook content product verified as exact polynomials for n=3,...,7')

def root_bracket(base,pow_num,denom,precision=10**12):
    T=pow(base,pow_num)*pow(precision,denom)
    low=precision;high=base*precision
    while low+1<high:
        mid=(low+high)//2
        if pow(mid,denom)<=T:low=mid
        else:high=mid
    return Fraction(low,precision),Fraction(low+1,precision)

def sign_S5_bounds(p_num,p_den):
    lx,ux=root_bracket(2,p_num,p_den)
    ly,uy=root_bracket(3,p_num,p_den)
    lz,uz=root_bracket(4,p_num,p_den)
    return -10+35*lx-50*uy+24*lz,-10+35*ux-50*ly+24*uz
assert sign_S5_bounds(3,10)[1]<0
assert sign_S5_bounds(8,25)[0]>0
assert 2**8*4**25<5**25 # 2^(8/25)<5/4
# Verified monotonicity interval: log2 > .69, log3 < 1.1,
# 2^(.3)>1.23, 4^(.3)>1.51, 3^(.32)<1.422.
assert pow(2,3)*100**10>123**10
assert pow(4,3)*100**10>151**10
assert pow(3,8)*500**25<711**25
assert Fraction(69,100)*(35*Fraction(123,100)+48*Fraction(151,100))-50*Fraction(11,10)*Fraction(711,500)>0
assert Fraction(69,100)<Decimal(2).ln() and Decimal(3).ln()<Fraction(11,10)

def d_pow(a,b):return (Decimal(a).ln()*b).exp()
def root5():
    lo=Decimal(3)/10;hi=Decimal(8)/25
    def f(t):return -10+35*d_pow(2,t)-50*d_pow(3,t)+24*d_pow(4,t)
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2
beta5=root5()
assert Decimal('.31316016')<beta5<Decimal('.31316017')
for lam,(dim,nums) in coeffs(5).items():
    if lam in [(5,),(1,1,1,1,1)]:continue
    eig=sum(Decimal(c)*d_pow(j+1,beta5) for j,c in enumerate(nums))/dim
    assert eig<0,(lam,eig)
print('S5 unique sign block threshold',beta5,'others strictly negative')
# independent full distance-matrix conditional-negative-type check at beta5 using numpy only if installed
try:
    import numpy as np,itertools
    perms=list(itertools.permutations(range(5))); pos={p:i for i,p in enumerate(perms)}
    def inv(p):
        r=[0]*len(p)
        for i,v in enumerate(p):r[v]=i
        return r
    D=np.empty((120,120),dtype=float)
    for i,a in enumerate(perms):
        ai=inv(a)
        for j,b in enumerate(perms):
            c=[ai[b[k]] for k in range(5)];cycles=0;seen=set()
            for k in range(5):
                if k not in seen:
                    cycles+=1;x=k
                    while x not in seen:seen.add(x);x=c[x]
            D[i,j]=(5-cycles)**float(beta5)
    eig=np.linalg.eigvalsh(-D/2)
    # -D/2 is positive on zero-sum; two nulls (constant is not null of D, so one actual sign zero)
    assert np.sum(eig<-1e-8)==1 # trivial block negative; sign block zero
    assert np.sum(abs(eig)<1e-8)==1
    assert np.sum(eig>1e-8)==118
    print('Direct 120x120 distance-matrix spectral check OK; endpoint Euclidean rank 118')
except ImportError:
    print('numpy absent: skipped independent dense spectral check')
print('ALL_CAYLEY_ROUNDNESS_CERTIFICATES_OK')
