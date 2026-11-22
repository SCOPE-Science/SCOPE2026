"""Reproduce finite arithmetic and high-precision diagnostics for a Rhaly commutator.

This program checks examples only. Infinite-inertia claims require the written proof.
Requires Python 3 and mpmath.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 70
checks = 0

def assert_close(x, y, tol=mp.mpf('1e-45')):
    global checks
    assert abs(x-y) <= tol * max(1, abs(x), abs(y)), (x,y)
    checks += 1

def a(n, s, beta=1):
    return mp.power(n+beta, -s)

def second(n, s, beta=1):
    return a(n,s,beta)-2*a(n+1,s,beta)+a(n+2,s,beta)

def q(n, s, beta=1):
    x, y, z = (a(n+k,s,beta) for k in range(3))
    return x*x+y*y-(n+1)*(x-2*y+z)**2 -(-2*y+z)**2-z*z

def K(i,j,s,beta=1):
    return mp.zeta(2*s,max(i,j)+beta) - (min(i,j)+1)*a(i,s,beta)*a(j,s,beta)

# Verify exact finite matrix-vector identities and asymptotic sign against direct calculations.
for s in (mp.mpf('1.25'),mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3')):
    for beta in (mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2')):
        for j in (40, 80, 160, 320):
            assert q(j,s,beta)>0, (s,beta,j,q(j,s,beta))
            checks+=1
            scaled = q(j,s,beta)*(j+1)/a(j,s,beta)**2
            assert abs(scaled-2*s)<mp.mpf('1.1')
            checks+=1
        for j in (40,80,160):
            assert K(j,j,s,beta)<0
            checks+=1

# Pairwise separation of normalized coordinate and finite-difference test vectors.
s = mp.mpf('2')
js = [100,10**5,10**8,10**11]
neg = mp.matrix(4)
pos = mp.matrix(4)
for p,i in enumerate(js):
    for r,j in enumerate(js):
        neg[p,r]=K(i,j,s)/mp.sqrt((-K(i,i,s))*(-K(j,j,s)))
        if p==r: pos[p,r]=1
        elif p<r:
            B=(i+1)*second(i,s)+2*(a(i+2,s)-a(i+1,s))
            pos[p,r] = -B*second(j,s)/mp.sqrt(q(i,s)*q(j,s))
        else:
            B=(j+1)*second(j,s)+2*(a(j+2,s)-a(j+1,s))
            pos[p,r] = -B*second(i,s)/mp.sqrt(q(i,s)*q(j,s))
for p in range(4):
    assert abs(neg[p,p]+1)<mp.mpf('1e-55')
    assert sum(abs(neg[p,r]) for r in range(4) if r!=p)<1
    assert sum(abs(pos[p,r]) for r in range(4) if r!=p)<1
    checks += 3

# Exact rational finite-tail-free quadratic identity: R v has two coordinates,
# and R^*v has j+3 coordinates.
for j in range(1,35):
    b=lambda k: Fraction(1,(k+1)**2)
    x,y,z = b(j),b(j+1),b(j+2)
    rv_sq=x*x+y*y
    rstarv_sq=(j+1)*(x-2*y+z)**2+(-2*y+z)**2+z*z
    formula=rv_sq-rstarv_sq
    # A separate hand-expanded polynomial in x,y,z.
    expanded=-(j+1)*(x*x+4*y*y+z*z-4*x*y+2*x*z-4*y*z) + x*x-3*y*y-2*z*z+4*y*z
    assert formula==expanded
    checks+=1

# A strict diagonal negativity coefficient and a positive three-point curvature coefficient.
for s in (mp.mpf('1.25'),mp.mpf('2.5')):
    n=10**5
    neg_scaled=K(n,n,s)/((n+1)*a(n,s)**2)
    positive_scaled=q(n,s)*(n+1)/a(n,s)**2
    assert abs(neg_scaled+2*(s-1)/(2*s-1))<mp.mpf('0.0002')
    assert abs(positive_scaled-2*s)<mp.mpf('0.0005')
    checks+=2
print('PASS',checks,'finite/high-precision diagnostics; infinite conclusion established in RESULT.md proof')
print('Coordinate Gram matrix diagonally dominant:',[str(sum(abs(neg[p,r]) for r in range(4) if r!=p))[:28] for p in range(4)])
print('Curvature Gram matrix diagonally dominant:',[str(sum(abs(pos[p,r]) for r in range(4) if r!=p))[:28] for p in range(4)])
