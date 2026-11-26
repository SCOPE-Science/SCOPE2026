#!/usr/bin/env python3
"""Exact finite-polynomial certificate for the characteristic-17 quintic a-number strata.

Uses only Python's standard library.  Every polynomial is a tuple of
coefficients in F_17 in increasing degree; no symbolic algebra package is needed.
"""
from math import comb
P=17

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]%P==0:a.pop()
    return tuple(v%P for v in a)
def add(a,b):
    return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%P for i in range(max(len(a),len(b)))])
def neg(a): return trim([-v for v in a])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]=(c[i+j]+ai*bj)%P
    return trim(c)
def pw(a,n):
    res=(1,)
    while n:
        if n&1:res=mul(res,a)
        a=mul(a,a);n//=2
    return res
def scl(k,a):return trim([k*v for v in a])
Z=(0,);ONE=(1,);L=(0,1)

def coeff_fpower(N,t):
    # f(X)^N = X^N (X^2-1)^N (X^2-L)^N
    if (t-N)%2 or t<N or t>5*N: return Z
    s=(t-N)//2
    ans=Z
    for u in range(N+1):
        v=s-u
        if 0<=v<=N:
            factor=comb(N,u)*comb(N,v)*(-1)**(N-u+N-v)
            ans=add(ans,scl(factor,pw(L,N-v)))
    return ans

def block(i):
    N=4*i
    return [[coeff_fpower(N,17*(b+1)-1-a) for a in range(i)] for b in range(i)]
B1=block(1);B2=block(2);B3=block(3)
q=add(sub(pw(L,2),scl(3,L)),ONE)
h=mul(mul(sub(L,(2,)),add(L,(8,))),q)
assert B1==[[scl(6,q)]]
assert B2==[[scl(2,mul(pw(L,4),h)),Z],[Z,scl(2,h)]]
assert B3[0][1]==Z and B3[1][0]==Z and B3[1][2]==Z and B3[2][1]==Z
assert B3[1][1]==scl(-2,mul(mul(pw(L,2),pw(sub(L,ONE),8)),q))
minor=sub(mul(B3[0][0],B3[2][2]),mul(B3[0][2],B3[2][0]))
assert minor==scl(5,mul(pw(L,10),pw(sub(L,ONE),8)))
# The full determinant factors as (nonzero scalar)*L^16*(L-1)^16*(L-2)^2*(L+8)^2*q^4.
D=scl(1, mul(mul(B1[0][0],mul(B2[0][0],B2[1][1])),mul(B3[1][1],minor)))
expected=scl(-2,mul(mul(pw(L,16),pw(sub(L,ONE),16)),mul(mul(pw(sub(L,(2,)),2),pw(add(L,(8,)),2)),pw(q,4))))
assert D==expected
# For each admissible L, the 2x2 even block is invertible. The remaining
# four dimensions are 1+1+1+1 singleton blocks (one i=1, two i=2, one i=3).
# Thus their zero/nonzero status gives both rank of Cartier and its stable rank.
def poly_eval(poly,v):
    z=0
    for c in reversed(poly):z=(z*v+c)%P
    return z
for t in range(17):
    if t in (0,1):continue
    diag=[B1[0][0], B2[0][0], B2[1][1], B3[1][1]]
    expected_zeros = 2 if t in (2,9) else 0
    assert sum(poly_eval(f,t)==0 for f in diag)==expected_zeros,(t,diag)
# q=L^2-3L+1 has discriminant 5, a nonsquare in F17.
assert 5 not in {x*x%17 for x in range(17)}
# In K=F17[sqrt(5)] its roots are (3 +/- sqrt(5))/2.
# Both are nonzero and not 1, have product 1, and are distinct from 2,9.
assert poly_eval(q,0)!=0 and poly_eval(q,1)!=0
assert poly_eval(q,2)!=0 and poly_eval(q,9)!=0
# For q=0, the three singleton sources and the i=3 middle vanish;
# the i=3 even minor is still invertible, so rank=p-rank=2.
# For L=2,9, just the two i=2 singleton sources vanish, so rank=4.
# All remaining parameters are ordinary.
print('CERTIFICATE_OK: characteristic 17, two exceptional inversion orbits; (p-rank,a)=(4,2),(2,4)')
