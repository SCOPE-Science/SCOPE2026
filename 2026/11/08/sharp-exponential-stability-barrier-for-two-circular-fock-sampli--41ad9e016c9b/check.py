"""Independent finite-dimensional checks for two-ring Fock spectral sampling.
Only numerical examples; the separate analytical proof establishes asymptotic claims.
"""
import math
import cmath
import random


def rate(s, a):
    if a == 0:
        return 0.0 if s == 0 else math.inf
    return a if s == 0 else a-s+s*math.log(s/a)


def bisect(f, lo, hi):
    flo = f(lo)
    for _ in range(110):
        mid = (lo+hi)/2
        if f(mid)*flo > 0:
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo+hi)/2

r = bisect(lambda x: x-1-math.e*math.log(x),math.e+0.00001,20)
a = bisect(lambda x: (r-1)*x-1-math.log(r*x),0.01,1/r)
b = r*a
s = math.e*a
R = a
assert abs((r-1)/math.log(r)-math.e) < 1e-12
assert abs(rate(0,a)-R)<1e-12
assert abs(rate(s,a)-R)<1e-12
assert abs(rate(s,b)-R)<1e-12
assert abs(rate(1,b)-R)<1e-12
assert 0<a<s<b<1

# The rate's Voronoi partition gives a global maximum at the endpoints and switch.
def cover_radius(a,b):
    if a>b: a,b=b,a
    if a==0: return max(0.0,b,rate(1,b)) # not used in random
    if abs(a-b)<1e-13:
        return max(rate(0,a),rate(1,a))
    switch=(b-a)/math.log(b/a)
    if switch >= 1:
        return max(rate(0,a),rate(1,a))
    if switch <= 0:
        return max(rate(0,b),rate(1,b))
    return max(rate(0,a), rate(switch,a),rate(1,b))

assert abs(cover_radius(a,b)-R)<1e-12
rng = random.Random(2608)
assertions = 7
for _ in range(15000):
    a0,b0 = math.exp(rng.uniform(-5,3)), math.exp(rng.uniform(-5,3))
    rc = cover_radius(a0,b0)
    assert rc>=R-1e-10, (a0,b0,rc)
    assertions+=1

# Independent direct Gram diagonalization at small dimensions.
for n in range(1,13):
    m=n+1
    for _ in range(10):
        aa,bb=rng.uniform(0.01,2*n+2),rng.uniform(0.01,2*n+2)
        # Construct complex observation vectors for each coefficient basis element.
        obs=[[math.exp(-t/2)*t**(k/2)/math.sqrt(math.factorial(k))*cmath.exp(2j*math.pi*k*j/m) / math.sqrt(m)
              for t in [aa,bb] for j in range(m)] for k in range(m)]
        for k in range(m):
            eig=sum(abs(z)**2 for z in obs[k])
            pred=(math.exp(-aa)*aa**k+math.exp(-bb)*bb**k)/math.factorial(k)
            assert abs(eig-pred)<1e-10
            assertions+=1
            for ell in range(k):
                cross=sum(v.conjugate()*w for v,w in zip(obs[k],obs[ell]))
                assert abs(cross)<1e-10
                assertions+=1

# Finite n optimal design's lower-bound exponent converges to the continuum rate.
for n in [20,50,100,200,500,1000,2000,4000]:
    t1,t2=n*a,n*b
    logs=[]
    for k in range(n+1):
        lg=math.lgamma(k+1)
        la=-t1+k*math.log(t1)-lg
        lb=-t2+k*math.log(t2)-lg
        mx=max(la,lb)
        logs.append(mx+math.log(math.exp(la-mx)+math.exp(lb-mx)))
    minlog=min(logs)
    assert 0 <=(-minlog/n)-R < (math.log(n)+6)/n
    if n>=100:
        assert abs(-minlog/n-R) < 0.04
        assertions+=1
    assertions+=1

print('TWO_RING_FOCK_CHECKS_PASS',assertions)
print('R,ratios,contact:',repr(R),repr(a),repr(b),repr(s),repr(r))
