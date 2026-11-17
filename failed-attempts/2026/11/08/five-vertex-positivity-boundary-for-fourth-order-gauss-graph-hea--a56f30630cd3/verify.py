#!/usr/bin/env python3
"""Exact arithmetic checks for positivity of a two-stage Gauss step on cycle graphs.
Run: python verify.py. Python 3 standard library only.
"""
from fractions import Fraction as Q
from itertools import product


def matmul(a,b):
    n=len(a); return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def inverse(a):
    n=len(a); m=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        p=next(i for i in range(k,n) if m[i][k]);m[k],m[p]=m[p],m[k]
        t=m[k][k];m[k]=[z/t for z in m[k]]
        for i in range(n):
            if i!=k:
                t=m[i][k]
                if t: m[i]=[m[i][j]-t*m[k][j] for j in range(2*n)]
    return [row[n:] for row in m]

def step(n,h):
    L=[[Q(2*int(i==j)-int((i-j)%n in (1,n-1))) for j in range(n)] for i in range(n)]
    L2=matmul(L,L)
    D=[[h*h*L2[i][j]+6*h*L[i][j]+12*int(i==j) for j in range(n)] for i in range(n)]
    LI=matmul(L,inverse(D))
    return [[Q(int(i==j))-12*h*LI[i][j] for j in range(n)] for i in range(n)]

def claimed(n,d,h):
    if n==3:
        den=3*h*h+6*h+4
        return ((3*h*h-2*h+4) if d==0 else 4*h)/den
    if n==4:
        den=(h*h+3*h+3)*(4*h*h+6*h+3)
        vals=[4*h**4+3*h**3+6*h*h+9*h+9,3*h*(h*h+3*h+3),9*h*h*(h+1)]
        return vals[d]/den
    if n==5:
        den=25*h**4+150*h**3+360*h*h+360*h+144
        vals=[25*h**4+30*h**3+72*h*h+72*h+144,72*h*(h+2),12*h*h*(5*h+6)]
        return vals[d]/den
    raise ValueError(n)

# Rational-function identity: every entry of the update can be written
# with determinant denominator degree <= 2n and numerator <= 2n;
# the claimed formula denominator degree <= 2n. Clearing denominators
# gives a polynomial of degree <= 4n. Therefore 4n+1 exact samples prove
# identity for all real nonnegative h, with no singularities on h>=0.
checks=0
for n in (3,4,5):
    for k in range(4*n+1):
        h=Q(k,2)
        T=step(n,h)
        for j in range(n):
            d=min(j,n-j)
            assert T[0][j]==claimed(n,d,h),(n,h,j,T[0][j],claimed(n,d,h))
            checks+=1
        assert all(sum(row)==1 for row in T)

# Exact C6 failure witness at a common universal timestep.
assert step(6,Q(8))[0][1]==Q(-6584,580537)

# Certified rational enclosures for sqrt(921), sqrt(3), u and v.
Rlo,Rhi=Q('30.34798'),Q('30.34799')
assert Rlo**2<921<Rhi**2
assert Q('1.73205')**2<3<Q('1.73206')**2
assert Q('10.5686')**2<51+2*Rlo
assert Q('10.5687')**2>51+2*Rhi
assert Q('3.1138')**2<2*Rlo-51
assert Q('3.1139')**2>2*Rhi-51
# Complex resolvent coefficients at h=8: delta=u+i v,
# rho=|(19+i*sqrt(3)-delta)/16|, |A/delta|=1/sqrt(4sqrt(921)).
assert 4*Rlo>Q(1)/Q('.091')**2
rhosq=((19-Q('10.5686'))**2+(Q('3.1139')-Q('1.73205'))**2)/256
assert rhosq<Q('.54')**2
Qup=Q('121.3920')
assert 4*Rhi<Qup
Nlo=22*Q('10.5686')-Qup-18*Q('1.73206')*Q('3.1139')
assert Q(3,4)*Nlo/Qup>Q('0.086')
tail=24*Q('.091')*(Q('.54')**6+Q('.54')**8)/(1-Q('.54')**7)
assert tail<Q('.071')<Q('.086')

# The cycle pseudoinverse Green function g(d) has zero sum and
# L g = e_0 - 1/n. This is an algebraic identity for all integer n>=3;
# these checks are independent sampled sanity tests.
for n in range(3,31):
    g=[Q(n*n-1,12*n)-Q(d*(n-d),2*n) for d in range(n)]
    assert sum(g)==0
    for d in range(n):
        assert 2*g[d]-g[(d-1)%n]-g[(d+1)%n] == Q(int(d==0))-Q(1,n)
    assert g[1]==Q((n-1)*(n-5),12*n)
print('VERIFY_OK',checks,'exact small-cycle identities; exact C6 witness; rational Fourier bounds; Green-function tests')
