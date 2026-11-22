"""Exact finite algebra and high-precision numerical checks for two-node tensor-bridge cubature.
This script supplements, but does not replace, the dimension-uniform proof.
"""
from fractions import Fraction as F
from math import log, cosh

def k(a,b):
    return min(a,b)-a*b

def captured(points):
    d=len(points[0])
    assert len(points)==2 and len(points[1])==d
    p,q=[prod(k(x,x) for x in z) for z in points]
    z=prod(k(a,b) for a,b in zip(*points))
    g1,g2=p/(2**d),q/(2**d)
    det=p*q-z*z
    assert det>0
    return (q*g1*g1+p*g2*g2-2*z*g1*g2)/det

def prod(seq):
    t=F(1)
    for x in seq: t*=x
    return t

def diagonal_reduction(d,s):
    v=s/(1+s)**2
    return F(2,4**d)*(v**d)/(1+s**d)

def axis_reduction(d):
    return F(2,27)*F(1,16)**(d-1)

checks=0
# Exact kernel inverse versus closed diagonal formula, for diverse dimensions and locations.
for d in range(1,7):
    for den in range(3,12):
        for num in range(1,den):
            s=F(num,den)
            t=s/(1+s)
            pts=[[t]*d,[1-t]*d]
            assert captured(pts)==diagonal_reduction(d,s)
            checks+=1

# Exact separation of a one-coordinate pair, including arbitrary shared locations.
for d in range(2,6):
    for x in [F(1,4),F(1,3),F(1,2),F(2,3)]:
        for a,b in [(F(1,5),F(3,5)),(F(1,3),F(2,3)),(F(1,4),F(3,4))]:
            pts=[[x]*(d-1)+[a],[x]*(d-1)+[b]]
            expected=captured([[a],[b]])*(x*(1-x)/4)**(d-1)
            assert captured(pts)==expected
            checks+=1

for d in range(1,8):
    if d==1:
        pts=[[F(1,3)],[F(2,3)]]
    else:
        pts=[[F(1,2)]*(d-1)+[F(1,3)],[F(1,2)]*(d-1)+[F(2,3)]]
    assert captured(pts)==axis_reduction(d)
    checks+=1

# The unique root is bracketed by the continuous strictly decreasing function.
def root(d):
    low,high=0.0,1.0
    for _ in range(100):
        mid=(low+high)/2
        if 1-mid-2*mid**(d+1)>0: low=mid
        else: high=mid
    return (low+high)/2

last=1.0
for d in range(1,151):
    s=root(d)
    assert abs(1-s-2*s**(d+1))<2e-14
    # Normalized capture is 16^d * reduction; stable for large dimensions.
    phi=2*(4*s/(1+s)**2)**d/(1+s**d)
    ratio=phi/(F(32,27))
    assert ratio>=last-1e-12
    assert (ratio>1) == (d>1)
    assert ratio< F(27,16)
    last=ratio
    checks+=1

print('PASS: 379 exact Fraction identities plus 150 numerical root/trend spot checks')
print('d=2 optimal t=',root(2)/(1+root(2)))
print('d=2 diagonal capture=',2/16*(root(2)/(1+root(2))**2)**2/(1+root(2)**2))
print('d=2 one-axis capture=',float(axis_reduction(2)))
print('d=150 capture ratio to one-axis=',last)
