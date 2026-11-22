#!/usr/bin/env python3
"""Exact-rational checks for a finite-mode Fourier sign-set theorem.

Standard library only. Every assertion concerns the displayed finite certificate;
the Fourier eigenfunction identity and the half-line tail arguments are proved in
RESULT.md rather than inferred from sampled values.
"""
from fractions import Fraction as F
from math import comb, isqrt


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def add(p, q):
    return [((p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0)))
            for i in range(max(len(p), len(q)))]


def scale(p, c):
    return [c*x for x in p]


def mulz(p):
    return [F(0)] + p


def laguerre(alpha, n):
    if n == 0:
        return [F(1)]
    a = [F(1)]
    b = [1+alpha, F(-1)]
    for k in range(1,n):
        d = add(add(scale(b, 2*k+1+alpha),scale(mulz(b), F(-1))),
                scale(a,-(k+alpha)))
        a,b=b,scale(d,F(1,k+1))
    return b

L1=laguerre(F(-1,2),1)
L3=laguerre(F(-1,2),3)
L5=laguerre(F(-1,2),5)
A=add(L3,scale(L1,-L3[0]/L1[0]))
B=add(L5,scale(L1,-L5[0]/L1[0]))
require(A == [F(0),F(-15,12),F(15,12),F(-2,12)], 'A Laguerre identity')
require(B == [F(0),F(-945,480),F(1575,480),F(-630,480),F(90,480),F(-4,480)],
        'B Laguerre identity')


def Q(t):
    return [F(945)-600*t,F(-1575)+600*t,F(630)-80*t,F(-90),F(4)]


def bernstein(t,l,r):
    # Q_t(l+(r-l)s) in power basis, then degree-four Bernstein basis.
    c=Q(t)
    p=[sum(c[j]*comb(j,i)*l**(j-i)*(r-l)**i for j in range(i,5))
       for i in range(5)]
    return [sum(p[i]*F(comb(k,i),comb(4,i)) for i in range(k+1))
            for k in range(5)]

# Each row: closed t range, and closed rational z subintervals where Q_t<0.
STRIPS=[
(F(-1),F(-1,2),[(F(1),F(3)),(F(3),F(5)),(F(5),F(7)),(F(7),F(173,20))]),
(F(-1,2),F(0),[(F(95,100),F(406,100)),(F(566,100),F(1063,100))]),
(F(0),F(1,2),[(F(87,100),F(291,100)),(F(596,100),F(1191,100))]),
(F(1,2),F(1),[(F(73,100),F(220,100)),(F(606,100),F(1291,100))]),
(F(1),F(3,2),[(F(47,100),F(180,100)),(F(612,100),F(1376,100))]),
(F(3,2),F(2),[(F(8,100),F(158,100)),(F(616,100),F(1451,100))])
]

# For q>=0, floor(sqrt(q)*10^4); exact integer arithmetic.
def sqrt_lower(q):
    require(q >= 0,'sqrt domain')
    return isqrt(q.numerator*10**8 // q.denominator)

def sqrt_upper(q):
    return sqrt_lower(q)+1

require(len(STRIPS)==6,'six parameter strips')
for lo,hi,regions in STRIPS:
    require(lo < hi,'strip endpoints')
    for a,b in regions:
        require(F(0)<=a<b,'region endpoints')
        for t in (lo,hi):
            vals=bernstein(t,a,b)
            require(all(v<0 for v in vals),f'Bernstein signs: {lo},{hi}; {a},{b}')
    k=sum(sqrt_lower(b)-sqrt_upper(a) for a,b in regions)
    require(k>17000,f'root-length bound strip {lo},{hi}: {k}')
    print(f'[{lo},{hi}]: certified sqrt-z length > {k}/10000 > 17/10')

# For t>=2, (z-r_-)(z-r_+)>0 on [0,1] and [7,12], so Q_t<=Q_2.
TAIL_REGIONS=[(F(0),F(1)),(F(7),F(12))]
for a,b in TAIL_REGIONS:
    require(all(v<0 for v in bernstein(F(2),a,b)), 'positive t-tail signs')
k=sum(sqrt_lower(b)-sqrt_upper(a) for a,b in TAIL_REGIONS)
require(k>17000,'positive t-tail sqrt length')
print('positive parameter tail: certified sqrt-z length >',k,'/10000')

# For t<=-1, Q_t <= Q_-1 on [r_-,r_+].  Its exact Bernstein
# coefficients on that algebraic interval are
# (-180, -(24135+1575 sqrt(105))/32, -1945/4,
#          -(24135-1575 sqrt(105))/32, -180).
# All negative because 10<sqrt(105)<11 and 24135>1575*11.
require(10*10<105<11*11,'sqrt(105) enclosure')
require(24135 > 1575*11,'algebraic Bernstein signs')

# Recompute the algebraic Bernstein coefficients, not merely their sign.
# An ordered pair (a,b) means a+b*sqrt(105), with rational a,b.
def qadd(u,v): return (u[0]+v[0],u[1]+v[1])
def qmul(u,v): return (u[0]*v[0]+105*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def qscale(u,c): return (u[0]*c,u[1]*c)
def qpow(u,n):
    out=(F(1),F(0))
    for _ in range(n):out=qmul(out,u)
    return out
ra=(F(15,4),F(-1,4)); delta=(F(0),F(1,2))
c=Q(F(-1))
power=[]
for i in range(5):
    v=(F(0),F(0))
    for j in range(i,5):
        v=qadd(v,qscale(qmul(qpow(ra,j-i),qpow(delta,i)),c[j]*comb(j,i)))
    power.append(v)
ber=[]
for k in range(5):
    v=(F(0),F(0))
    for i in range(k+1):
        v=qadd(v,qscale(power[i],F(comb(k,i),comb(4,i))))
    ber.append(v)
expected=[(F(-180),F(0)),(F(-24135,32),F(-1575,32)),
          (F(-1945,4),F(0)),(F(-24135,32),F(1575,32)),
          (F(-180),F(0))]
require(ber==expected,'algebraic Bernstein coefficient identities')

# Verify fixed sign at the two roots of D= z^2-15z/2+15/2:
# Q_t mod D is -180, for every t (remainder independent of t).
# Fractions: z^2=(15z-15)/2; implement modulo for all terms.
def reduce_D(p):
    arr=p[:]
    for n in range(len(arr)-1,1,-1):
        v=arr[n]
        arr[n]=F(0)
        arr[n-1] += F(15,2)*v
        arr[n-2] -= F(15,2)*v
    return arr[:2]
for t in (F(-123),F(-1),F(0),F(2),F(341,7)):
    require(reduce_D(Q(t)) == [F(-180),F(0)],'Q modulo D')

# The target delta=sqrt(r_+)-sqrt(r_-) is <sqrt(7)-1<17/10:
# 1<r_-<r_+<7 follows from 10<sqrt(105)<11, and sqrt(7)<27/10.
require(F(7)<F(27,10)**2,'comparison threshold')
print('PASS: Fourier-mode polynomial identities and all rational sign/length certificates.')
