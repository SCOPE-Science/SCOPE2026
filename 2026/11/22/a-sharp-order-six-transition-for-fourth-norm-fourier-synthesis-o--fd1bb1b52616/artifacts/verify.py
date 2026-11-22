#!/usr/bin/env python3
"""Independent finite-arithmetic and direct Fourier checks for a four-site synthesis constant.

No third-party modules are needed. The symbolic proof is given in RESULT.md;
this program exercises its arithmetic identities and finite sample witnesses.
"""
import cmath
import math
import random
from fractions import Fraction as Q

Q0=Q(0)

def add(a,b):
    z=[Q0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def mul(a,b):
    z=[Q0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def poly_for_order(m):
    fs=[[Q0] for _ in range(m)]
    for j,v in enumerate(([Q0,Q(1)],[Q(1,2),Q(-1)],[Q(1,2),Q(-1)],[Q0,Q(1)])):
        fs[j]=v
    conv=[]
    for k in range(m):
        total=[Q0]
        for i in range(m):
            total=add(total,mul(fs[i],fs[(k-i)%m]))
        conv.append(total)
    out=[Q0]
    for x in conv:out=add(out,mul(x,x))
    return out

EXPECTED={
  4:[Q(3,8),Q(-2),Q(12),Q(-32),Q(32)],
  5:[Q(3,8),Q(-2),Q(9),Q(-20),Q(20)],
  6:[Q(3,8),Q(-2),Q(9),Q(-24),Q(30)],
  7:[Q(3,8),Q(-2),Q(9),Q(-24),Q(28)],
}

def P(m,t):
    return sum(float(c)*t**i for i,c in enumerate(EXPECTED[min(m,7)]))

def cubic(m,t):
    return (60 if m==6 else 56)*t**3-36*t*t+9*t-1

def root(m):
    if m<=5:return .25
    lo,hi=.25,.5
    assert cubic(m,lo)<0<cubic(m,hi)
    for _ in range(80):
        mi=(lo+hi)*.5
        if cubic(m,mi)>0:hi=mi
        else:lo=mi
    return (lo+hi)*.5

def fourier(vals):
    n=len(vals)
    return [sum(v*cmath.exp(-2j*math.pi*k*x/n) for x,v in enumerate(vals))/math.sqrt(n) for k in range(n)]

def ratio(vals):
    h=fourier(vals)
    return max(map(abs,h))/sum(abs(z)**4 for z in h)**.25

checks=0
for m in range(4,20):
    poly=poly_for_order(m)
    assert poly==EXPECTED[min(m,7)],(m,poly)
    checks+=1
for m in [4,5,6,7]:
    tt=root(m)
    assert 0<tt<.5
    assert abs(P(m,tt)-min(P(m,x/4000) for x in range(-1000,3000)))<3e-6
    if m<=5:assert abs(tt-.25)<1e-15
    else:
        assert .25<tt<.5
        assert P(m,tt)<P(m,.25)-1e-4
    checks+=5

cases=[(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,2),(12,2),(12,3),(15,3),(21,3),(24,4),(25,5),(30,5)]
for n,d in cases:
    m=n//math.gcd(n,d)
    if m<4:continue
    tt=root(m)
    vals=[0j]*n
    for j,weight in enumerate((tt,.5-tt,.5-tt,tt)):
        vals[(j*d)%n]=complex(weight)
    r=ratio(vals)
    target=(n*P(m,tt))**(-.25)
    assert abs(r-target)<2e-10,(n,d,r,target)
    checks+=1

rng=random.Random(20260921)
for n,d in [(4,1),(5,1),(6,1),(7,1),(12,2),(21,3)]:
    m=n//math.gcd(n,d)
    optimum=(n*P(m,root(m)))**(-.25)
    for _ in range(120):
        f=[0j]*n
        for j in range(4):
            f[j*d%n]=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        assert ratio(f)<=optimum+2e-10,(n,d)
        checks+=1

# Nonuniformity and torsion threshold: exact derivative at t=1/4.
assert [sum(i*EXPECTED[m][i]*Q(1,4)**(i-1) for i in range(1,5)) for m in (4,5,6,7)] == [Q0,Q0,Q(-1,8),Q(-1,4)]
checks+=4
print(f'VERIFY_OK exact_polynomials=16 roots=4 group_cases={len(cases)} randomized=720 assertions={checks}')
