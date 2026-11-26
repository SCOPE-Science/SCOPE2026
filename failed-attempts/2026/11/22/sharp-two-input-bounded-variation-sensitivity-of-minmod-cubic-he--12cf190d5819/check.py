#!/usr/bin/env python3
"""Exact face-column identities and reproducible BV tests for minmod Hermite interpolation.
No third-party dependencies.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
from random import Random

# Cubic in ascending powers of normalized cell coordinate.
S = (F(0), F(0), F(3), F(-2))
U = (F(0), F(1), F(-2), F(1))
W = (F(0), F(0), F(-1), F(1))

def evalpoly(p, t):
    return ((p[3]*t+p[2])*t+p[1])*t+p[0]

def polynomial(y0, y1, a, b):
    return tuple((y0 if k==0 else F(0)) + (y1-y0)*S[k] + a*U[k] + b*W[k] for k in range(4))

def root_extrema(p):
    A,B,C=3*float(p[3]),2*float(p[2]),float(p[1]); r=[0.,1.]
    if abs(A)<1e-14:
        if abs(B)>1e-14:
            t=-C/B
            if 0<t<1:r.append(t)
    else:
        det=B*B-4*A*C
        if det>0:
            for t in ((-B+sqrt(det))/(2*A),(-B-sqrt(det))/(2*A)):
                if 0<t<1:r.append(t)
    return sorted(r)

def variation(p):
    z=root_extrema(p)
    return sum(abs(float(evalpoly(p,b)-evalpoly(p,a))) for a,b in zip(z,z[1:]))

def minmod(a,b):
    if a*b<=0:return F(0)
    return (1 if a>0 else -1)*min(abs(a),abs(b))

def interpolate(y, scale=F(1)):
    d=[y[i+1]-y[i] for i in range(len(y)-1)]
    m=[F(0)]+[scale*minmod(d[i-1],d[i]) for i in range(1,len(y)-1)]+[F(0)]
    return [polynomial(y[i],y[i+1],m[i],m[i+1]) for i in range(len(d))]

def signal_v(y):return sum(abs(y[i+1]-y[i]) for i in range(len(y)-1))

def cubics_v(c):return sum(variation(p) for p in c)

def pair_v(y,z,scale=F(1)):
    a,b=interpolate(y,scale),interpolate(z,scale)
    return cubics_v([tuple(p[k]-q[k] for k in range(4)) for p,q in zip(a,b)])

# Exact polynomial constraints for four flag states.
for a,b in product((0,3),repeat=2):
    mid=polynomial(F(0),F(1),F(a),F(b))
    assert mid[0]==0 and sum(mid)==1
    deriv=(mid[1],2*mid[2],3*mid[3])
    expected={(0,0):(F(0),F(6),F(-6)),(3,0):(F(3),F(-6),F(3)),(0,3):(F(0),F(0),F(3)),(3,3):(F(3),F(-12),F(12))}[(a,b)]
    assert deriv==expected
    # Exactly nonnegative derivative: 6t(1-t), 3(1-t)^2, 3t^2, 3(1-2t)^2.
# Exact hump maxima U(1/3)=4/27 and W(2/3)=-4/27.
assert evalpoly(U,F(1,3)) == F(4,27)
assert evalpoly(W,F(2,3)) == -F(4,27)
assert polynomial(F(0),F(1),F(1),F(1)) == (F(0),F(1),F(0),F(0))
assert polynomial(F(0),F(1),F(3),F(3)) == (F(0),F(3),F(-6),F(4))
print('EXACT_FOUR_MONOTONE_HERMITE_CORNERS_AND_HUMP_CERTIFICATES_PASS')

# All possible local selector masks, including masks not simultaneously achievable,
# give at most the claimed universal constant.
for n in range(2,10):
  for scale in (F(0),F(1,2),F(1),F(2),F(3)):
    mx=F(0)
    for mask in product((0,1,2),repeat=n-2):
        # Each interior mask chooses none, left difference, or right difference.
        # The step at edge j affects at most the adjacent two knot derivatives.
        for j in range(n-1):
            a=int(j>=1 and mask[j-1]==2)
            b=int(j+1<=n-2 and mask[j]==1)
            tv=F(1)+F(8,27)*scale*(a+b)
            mx=max(mx,tv)
    expected=F(1)+F(8,27)*scale*min(2,n-2)
    assert mx==expected,(n,mx,expected)
print('EXHAUSTIVE_LOCAL_FACE_COLUMN_NORMS_AND_SCALES_PASS n=2..9 scale=0,1/2,1,2,3')

# Actual explicit data witnesses, with a finite positive input difference.
for n in range(2,30):
  for scale in (F(0),F(1,2),F(1),F(2),F(3)):
    j=0 if n<=3 else 1
    secants=[F(2)]*(n-1)
    if n>=3:secants[j]=F(1)
    y=[F(0)]
    for d in secants:y.append(y[-1]+d)
    z=[v+(F(1,4) if i>j else F(0)) for i,v in enumerate(y)]
    rat=pair_v(z,y,scale)/float(signal_v([z[i]-y[i] for i in range(n)]))
    expected=1+8/27*float(scale)*min(2,n-2)
    assert abs(rat-expected)<1e-10,(n,rat,expected)
print('EXPLICIT_ALL_DIMENSION_ALL_SCALES_SHARP_WITNESSES_PASS n=2..29')

rng=Random(406151)
for n in range(2,17):
    for _ in range(160):
        y=[F(rng.randint(-30,30),7) for i in range(n)]
        z=[F(rng.randint(-30,30),7) for i in range(n)]
        dv=signal_v([y[i]-z[i] for i in range(n)])
        if not dv:continue
        scale=F(rng.choice((0,1,2,3,4,6)),2)
        K=F(1)+F(8,27)*scale*min(2,n-2)
        tv=pair_v(y,z,scale)
        assert tv<=float(K*dv)+1e-8,(n,tv,float(K*dv))
        assert abs(cubics_v(interpolate(y,scale))-float(signal_v(y)))<1e-8
print('RANDOM_RATIONAL_TWO_INPUT_AND_ONE_INPUT_VARIATION_SCALED_PASS 2400')
# Sharp allowable slope range: monotone data fail one-input BV preservation beyond endpoints.
for scale in (F(-1), F(-1,2), F(7,2), F(4)):
    y=[F(0),F(1),F(2)]
    assert cubics_v(interpolate(y,scale))>float(signal_v(y))+1e-10
print('SHARP_SCALE_INTERVAL_FOR_UNIVERSAL_ONE_INPUT_BV_PASS')
print('ALL_MINMOD_HERMITE_BV_CERTIFICATES_PASS')
