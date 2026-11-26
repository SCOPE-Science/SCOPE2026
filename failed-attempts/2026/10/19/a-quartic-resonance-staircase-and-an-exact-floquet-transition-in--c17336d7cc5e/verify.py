#!/usr/bin/env python3
"""Supplementary finite checks for the quartic constant-action resonance theorem.

Only Python 3 standard library is needed. Finite checks supplement the proof.
"""
from fractions import Fraction as F
from math import isqrt, sqrt, pi, floor

checks = 0

def test(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

def multiply(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def w_at_s(a, e, s):
    return a*(1-(1+e)*s+e*s*s)

def deriv_squared(a, e, s):
    return 4*a*a*s*(2*e*s-(1+e))**2

def half_levels(L, U, low_open=True, high_closed=True):
    # Exact independent integer enumeration; all test ranges are bounded.
    lo = floor(float(L))-3
    hi = floor(float(U))+3
    return sum((L < F(m)+F(1,2) if low_open else L <= F(m)+F(1,2)) and
               (F(m)+F(1,2) <= U if high_closed else F(m)+F(1,2) < U)
               for m in range(lo,hi+1))

# Exact Jacobian matrix identity at 81 rational (kick, twist-slope) pairs.
for q0 in [F(1,8),F(1,3),F(1),F(5,2),F(7),F(-3),F(0),F(17,3),F(19,10)]:
    for d0 in [F(0),F(1),F(-1),F(2,5),F(5,3),F(4),F(-7),F(13,6),F(-29,10)]:
        J0 = ((1-q0*d0,d0),(-q0,1))
        Jhalf = ((1+q0*d0,d0),(q0,1))
        A = multiply(Jhalf,J0)
        test(det(A)==1,'return determinant')
        test(A[0][0]+A[1][1]==2-(q0*d0)**2,'return trace')
        test(det(J0)==1 and det(Jhalf)==1,'one-step determinants')

# At the exact test parameters, integer levels and squared actions are algebraic.
a=F(1,2); e=F(2); q=F(1,8)  # q = 2*pi*b, hence b = 1/(16*pi)
wc=F(-1,16)
rc2=F(3,4)
for m in range(0,201):
    d=9+16*m
    root=sqrt(d)
    s=(3+root)/4
    test(abs(float(w_at_s(a,e,F(s)))-(m+0.5))<1e-9,'resonance level')
    test(s>float(rc2),'outer root')
    d2=float(deriv_squared(a,e,F(s)))
    tau=2-float(q*q)*d2
    if m<=4: test(-2<tau<2,'elliptic m<=4')
    if m>=5: test(tau< -2,'hyperbolic m>=5')

# Exact rational inequalities prove the first spectral change occurs between m=4 and m=5.
# y4 < 17/10 because sqrt(73) < 4*(17/10)^2 - 3.
bound4=4*F(17,10)**2-3
bound5=4*F(44,25)**2-3
test(bound4>0 and bound4**2>73,'m4 upper bound')
test(bound5>0 and bound5**2<89,'m5 lower bound')
Wprime=lambda y: y*(4*y*y-3)
test(Wprime(F(17,10))<16,'m4 subcritical')
test(Wprime(F(44,25))>16,'m5 supercritical')
test(w_at_s(a,e,F(0))==F(1,2),'central orbit resonance')
test(deriv_squared(a,e,F(0))==0,'central parabolic derivative')

# Check the exact floor count with independent quadratic-root enumeration.
for aa in [F(1,4),F(1,2),F(3,4),F(1)]:
    for ee in [F(1,2),F(1),F(2),F(3),F(4)]:
        rcs=(1+ee)/(2*ee)
        wc0=-aa*(ee-1)**2/(4*ee)
        for R in [F(2),F(5,2),F(3),F(7,2)]:
            if R*R<rcs: continue
            C=2*half_levels(wc0,aa,low_open=False,high_closed=False)+int(aa==F(1,2))
            expected=C+2*(floor(w_at_s(aa,ee,R*R)-F(1,2))-floor(wc0-F(1,2)))
            # Enumerate *all* half-integer levels and solve the quadratic in s.
            total=0
            for m in range(floor(float(wc0))-4, floor(float(w_at_s(aa,ee,R*R)))+4):
                level=F(m)+F(1,2)
                disc=(1-ee)**2+4*ee*level/aa
                if disc<0: continue
                sqrt_disc=sqrt(float(disc))
                s1=(float(1+ee)-sqrt_disc)/(2*float(ee))
                s2=(float(1+ee)+sqrt_disc)/(2*float(ee))
                roots=[s1,s2]
                if disc==0:roots=roots[:1]
                for s in roots:
                    if s< -1e-10 or s>float(R*R)+1e-10: continue
                    if abs(s)<1e-10:total+=1
                    else:total+=2
            test(total==expected, f'root census a={aa},eps={ee},R={R}: {total}!={expected}')

# Closed-strip endpoint: at y=+/-2 the m=10 pair must count.
test(w_at_s(a,e,F(4))==F(21,2),'endpoint level m=10')
test((3+isqrt(9+16*10))/4==4,'exact squared endpoint')
C=1
R=F(2)
N=C+2*(floor(w_at_s(a,e,R*R)-F(1,2))-floor(wc-F(1,2)))
test(N==23,'closed-strip count 23')

# Real-map consistency at selected exact-square levels (floating sin(pi) tolerance only).
for m in [0,1,10,40,100]:
    sq=(3+sqrt(9+16*m))/4
    for y in [sqrt(sq),-sqrt(sq)]:
        twist=float(w_at_s(a,e,F(sq)))
        x0=0.0
        x1=(x0+twist)%1.0
        y1=y-1/(16*pi)*__import__('math').sin(2*pi*x0)
        x2=(x1+float(w_at_s(a,e,F(y1*y1))))%1.0
        y2=y1-1/(16*pi)*__import__('math').sin(2*pi*x1)
        test(abs(x1-0.5)<2e-10 and min(abs(x2),abs(1-x2))<2e-10 and abs(y2-y)<2e-10,'two-step map')

print(f'PASS: {checks} reproducibility assertions; exact identities plus finite examples.')
print('This script does not replace the infinite analytic proof in RESULT.md.')
