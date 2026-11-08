"""Supplementary finite diagnostics for Berezin convexity rigidity."""
from fractions import Fraction
from math import pi, cos, sin

checks = 0
for b in [Fraction(-2,5), Fraction(0), Fraction(3,8)]:
    for a in [Fraction(1,10), Fraction(1,5)]:
        for m in [2,3,4,5]:
            for num in range(1, 16):
                r = Fraction(num,40)
                t = r*r
                A = b + a*r**(m-1)
                B = (1-t)/(1-t*A)
                assert 1-B == t*(1-A)/(1-t*A)
                assert 0 < B <= 1
                checks += 2

for b,a,m in [(0.,.5,2),(.35,.2,3),(-.4,.3,4),(.2,-.3,6),(.2+.15j,.3,2),(-.2+.3j,.2,3)]:
    for r in [.1,.2,.4,.6]:
        for j in range(48):
            z = r*complex(cos(2*pi*j/48),sin(2*pi*j/48))
            phi = b*z+a*z**m
            B = (1-r*r)/(1-z.conjugate()*phi)
            assert abs(B)<=1+1e-12
            checks+=1
    z = .4*complex(cos(pi/(2*(m-1))),sin(pi/(2*(m-1))))
    B = (1-abs(z)**2)/(1-z.conjugate()*(b*z+a*z**m))
    assert abs(((B-1)/(b-1)).imag)>1e-7
    checks+=1

for c in [-1.,-.5,0.,.2,.75,1.]:
    values = [(1-r*r)/(1-c*r*r) for r in [0.,.1,.25,.5,.75,.99]]
    assert all(v>0 and v<=1 for v in values)
    assert all(values[i+1]<=values[i] for i in range(len(values)-1))
    checks+=2
print('PASS:', checks, 'finite supplementary checks')
