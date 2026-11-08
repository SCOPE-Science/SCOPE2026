"""Exact-rational checks for a drift-midpoint theta-Maruyama invariant-moment classification.

Run with Python 3, using only the standard library. This is a finite
consistency test; the theorem for all real parameters is proved separately.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def statistics(r, t, scale=F(1)):
    # r = b^2/a, t = a*h/2, scale = sigma^2/a.
    assert 0 < r < 2 and t > 0 and scale > 0
    EA2 = ((1-t)**2 + 2*r*t) / (1+t)**2
    EA4 = ((1-t)**4 + 12*r*t*(1-t)**2 + 12*r*r*t*t) / (1+t)**4
    EC2 = 2*t*scale/(1+t)**2
    EC4 = 3*EC2*EC2
    D = (2-3*r)*(1+t*t) + 3*r*(2-r)*t
    V2 = scale/(2-r)
    V4 = None
    if D > 0:
        V4 = 3*scale*scale*(1+t*t+r*t)/((2-r)*D)
    return EA2, EA4, EC2, EC4, D, V2, V4

rs = [F(1,100),F(1,8),F(1,3),F(1,2),F(2,3),F(7,10),
      F(3,4),F(9,10),F(1),F(9,8),F(7,6),F(3,2),F(19,10)]
ts = [F(1,20),F(1,10),F(1,4),F(1,2),F(2,3),F(1),
      F(3,2),F(2),F(4),F(10),F(20)]
scales = [F(1,4),F(1),F(9,5)]

for r,t,scale in product(rs,ts,scales):
    EA2,EA4,EC2,EC4,D,V2,V4=statistics(r,t,scale)
    check(EA2 < 1,'second moment contractivity')
    check((1-EA2)*V2 == EC2,'exact invariant second moment')
    check((1-EA4)*(1+t)**4 == 4*t*D,'fourth-moment polynomial factor')
    check((EA4 < 1) == (D > 0),'fourth criterion')
    if V4 is not None:
        check((1-EA4)*V4 == 6*EA2*EC2*V2+EC4,
              'fourth moment recursion')
        check(V4 >= V2*V2,'Jensen fourth moment lower bound')
        check(V4/V2**2-3 == 6*r*((1-t)**2+r*t)/D,
              'stationary excess kurtosis')
    if r < F(2,3):
        V4true=3*scale*scale/((2-r)*(2-3*r))
        check(V4 is not None,'physical finite-fourth region')
        check(V4 / V4true == 1 - 4*r*t/D,
              'sharp fourth moment deficit')
        check(0 < V4 < V4true,'strict fourth moment underestimation')
    if r == F(2,3):
        check(V4 is not None,'critical continuous moment fake regularization')
    if r >= F(7,6):
        check(V4 is None,'above maximal random fourth stability threshold')

# The 0<r<2/3, r=2/3, 2/3<r<2/sqrt(3), r>=2/sqrt(3)
# classification follows from D/t=(2-3r)*(t+1/t)+3r*(2-r),
# with the AM-GM inequality t+1/t >= 2.
r=F(1)
for t,expected_finite in [(F(1,4),False),(F(1,2),True),
                           (F(1),True),(F(2),True),(F(4),False)]:
    check((statistics(r,t)[4] > 0)==expected_finite,
          'non-monotone 4th moment stability window')

EA2,EA4,EC2,EC4,D,V2,V4=statistics(F(1),F(1))
check(EA2==F(1,2),'benchmark multiplier second moment')
check(EA4==F(3,4),'benchmark multiplier fourth moment')
check(V2==1,'benchmark invariant variance')
check(V4==9,'benchmark invariant fourth moment')
check(D==1,'benchmark stability denominator')

print('PASS:',checks,'exact-rational assertions')
print('Benchmark r=t=1: EA2=1/2, EA4=3/4, variance=1, fourth moment=9')
print('Finite fourth-moment window at r=1: (3-sqrt(5))/2 < t < (3+sqrt(5))/2')
