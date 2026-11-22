#!/usr/bin/env python3
"""Independent exact and numerical checks for coaxial-ball covariance identities.
Requires sympy>=1.11 and mpmath>=1.2.  Not an exhaustive proof.
"""
from fractions import Fraction
from math import isclose
import sympy as S
import mpmath as mp

mp.mp.dps = 60
checks = 0

def check(test, message):
    global checks
    if not bool(test):
        raise AssertionError(message)
    checks += 1

# An exact three-active-ball example, with center coordinates -1, 0, +1
# and squared radii 4, 2, 4. The active center changes 1 -> 0 -> -1.
z = S.symbols('z', real=True)
fmid = 2-z*z
fend = 3-2*z-z*z
B0 = 2*(S.integrate(fmid, (z,0,S.Rational(1,2))) +
        S.integrate(fend, (z,S.Rational(1,2),1)))
B2 = 2*(S.integrate(z*z*fmid, (z,0,S.Rational(1,2))) +
        S.integrate(z*z*fend, (z,S.Rational(1,2),1)))
Bperp = 2*(S.integrate(fmid*fmid, (z,0,S.Rational(1,2))) +
           S.integrate(fend*fend, (z,S.Rational(1,2),1)))
check(B0 == S.Rational(17,6), 'volume coefficient')
check(S.simplify(B2/B0-S.Rational(139,680)) == 0, 'axial variance')
check(S.simplify(Bperp/(4*B0)-S.Rational(573,1360)) == 0, 'transverse variance')
check(S.simplify(Bperp/(4*B0)-B2/B0-S.Rational(59,272)) == 0, 'variance gap')

# On a symmetric three-ball interval, the exact two interface terms equal the gap.
# The negative half mass below -1/2 is explicit, by symmetry.
p_left = (S.integrate(fend,(z,S.Rational(1,2),1)))/B0
first_tail_mean = (S.integrate(z*fend,(z,S.Rational(1,2),1)))/B0
# Formula Cov(Z,1_{Z>u})= E[Z 1_{Z>u}] for symmetric centered measure.
check(S.simplify(2*first_tail_mean-S.Rational(59,272)) == 0, 'exact positive interface sum')
check(p_left > 0 and p_left < 1, 'both nontrivial interface masses')

# Check a full sphere, unequal two-ball, three-active and four-active families
# independently using the original cross-section moments, and the interface sum.
families = [
    ([(0, S.Rational(9,4))], 'single'),
    ([(S.Rational(-3,10),S.Rational(49,25)),
      (S.Rational(4,5),S.Rational(81,25))], 'unequal pair'),
    ([(-1,4),(0,2),(1,4)], 'three active'),
    ([(-3,13),(-1,3),(1,3),(3,13)], 'four active'),
]

def geometry(centers_sq):
    lines=[(mp.mpf(str(S.Rational(c))),mp.mpf(str(S.Rational(r2)))) for c,r2 in centers_sq]
    left=max(c-mp.sqrt(r2) for c,r2 in lines)
    right=min(c+mp.sqrt(r2) for c,r2 in lines)
    assert left<right
    raw=[left,right]
    for i,(c,rr) in enumerate(lines):
        for cc,RR in lines[i+1:]:
            if c!=cc:
                x=(RR-cc*cc-rr+c*c)/(2*(c-cc))
                if left<x<right:raw.append(x)
    raw=sorted(raw)
    # Dedupe crossing abscissae from a candidate all-pairs set.
    breaks=[raw[0]]
    for x in raw[1:]:
        if abs(x-breaks[-1])>mp.mpf('1e-45'):breaks.append(x)
    pieces=[]
    for a,b in zip(breaks,breaks[1:]):
        x=(a+b)/2
        c,rr=min(lines,key=lambda v: rr_f(v,x))
        pieces.append((a,b,c,rr))
    merged=[]
    for a,b,c,rr in pieces:
        if merged and merged[-1][2]==c and abs(merged[-1][1]-a)<mp.mpf('1e-40'):
            merged[-1]=(merged[-1][0],b,c,rr)
        else:merged.append((a,b,c,rr))
    return merged

def rr_f(v,x):
    c,r2=v
    return r2-(x-c)**2

def evaluate(segments,d):
    power=mp.mpf(d-1)/2
    def integrate(fun):
        return sum(mp.quad(lambda x:fun(x,c,r2),[a,b]) for a,b,c,r2 in segments)
    radius=lambda x,c,r2:max(mp.mpf('0'), r2-(x-c)**2)
    zer=integrate(lambda x,c,r2:radius(x,c,r2)**power)
    Ex=integrate(lambda x,c,r2:x*radius(x,c,r2)**power)/zer
    axial=integrate(lambda x,c,r2:(x-Ex)**2*radius(x,c,r2)**power)/zer
    perp=integrate(lambda x,c,r2:radius(x,c,r2)**(power+1))/zer/(d+1)
    Ec=integrate(lambda x,c,r2:c*radius(x,c,r2)**power)/zer
    Exc=integrate(lambda x,c,r2:x*c*radius(x,c,r2)**power)/zer
    jump=mp.mpf('0')
    for j in range(len(segments)-1):
        t=segments[j][1]
        dl=segments[j][2]-segments[j+1][2]
        tail=integrate(lambda x,c,r2:(x-Ex)*radius(x,c,r2)**power * (1 if x>t else 0))/zer
        jump+=dl*tail
    return axial,perp,perp-axial,-(Exc-Ex*Ec),jump

for spec,label in families:
    segs=geometry(spec)
    check(segs[0][0]<segs[-1][1],f'nondegenerate {label}')
    check(all(a<b for a,b,c,r2 in segs),f'ordered {label}')
    check(all(segs[i][2]>segs[i+1][2] for i in range(len(segs)-1)), f'decreasing centers {label}')
    for d in [2,3,4,5,7,9]:
        a,p,g,c,j=evaluate(segs,d)
        for val in [a,p]:check(val>0, f'positive moments {label} dim {d}')
        tol=mp.mpf('1e-22')
        check(abs(g-c)<tol,f'covariance exact identity {label} dim {d}')
        check(abs(g-j)<tol,f'interface exact identity {label} dim {d}')
        if len(segs)>1:
            check(g>0,f'strict gap {label} dim {d}')
        else:check(abs(g)<tol, f'ball equality {label} dim {d}')

print('VERIFY_OK assertions=',checks)
