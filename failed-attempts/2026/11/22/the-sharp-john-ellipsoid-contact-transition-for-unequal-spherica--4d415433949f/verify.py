"""Numerical diagnostics for the exact unequal-ball-lens John ellipsoid.

The analytic proof uses supporting-contact identities. The finite tests here
check the formulas and their geometric normalizations, not a universal proof.
"""
import math
import random


def parameters(R, r, s):
    assert R >= r > 0.0 and R-r < s < R+r
    if R == r:
        a = math.sqrt(R*R+s*s/12.0)-s/math.sqrt(3.0)
        b2 = a*a+(math.sqrt(3.0)/2.0)*a*s
        return "equal", s/2.0, a, math.sqrt(b2), 1/math.sqrt(3), -1/math.sqrt(3)
    sc = 1.5*(R*R-r*r)/R
    if s <= sc:
        delta = s-R
        a = (math.sqrt(delta*delta+3*r*r)-2*delta)/4
        b = math.sqrt(4*a*a+3*a*delta)
        return "pole", R-a, a, b, 1.0, -1/3

    def v_of(T):
        u = math.sqrt(T)
        v = -1.0/(3.0*u)
        J = (R*R-r*r)/(u*u-v*v)
        B = (r*r*u*u-R*R*v*v)/(u*u-v*v)
        return J*(u-v)/math.sqrt(B+J)

    lo, hi = R/(3*r), 1.0
    for _ in range(90):
        mid = (lo+hi)/2
        if v_of(mid) > s:
            lo = mid
        else:
            hi = mid
    u = math.sqrt((lo+hi)/2)
    v = -1/(3*u)
    J = (R*R-r*r)/(u*u-v*v)
    B = (r*r*u*u-R*R*v*v)/(u*u-v*v)
    a = B/math.sqrt(B+J)
    m = J*u/math.sqrt(B+J)
    return "two_latitudes", m, a, math.sqrt(B), u, v


def max_distance_squared(m, a, b, c):
    D = b*b-a*a
    tc = (a*(m-c)/D) if D > 0 else math.copysign(1, m-c)
    t = min(1.0, max(-1.0, tc))
    return (m+a*t-c)**2+b*b*(1-t*t)


def check(R, r, s):
    kind, m, a, b, u, v = parameters(R, r, s)
    assert 0 < a < b and -1 <= v < 0 < u <= 1
    tol = 3e-9*max(1.0, R*R)
    assert abs(max_distance_squared(m,a,b,0)-R*R) < tol, (R,r,s,kind,'large')
    assert abs(max_distance_squared(m,a,b,s)-r*r) < tol, (R,r,s,kind,'small')
    assert abs(u*v+1/3) < 2e-9
    p1 = -v/(u-v)
    p2 = u/(u-v)
    assert min(p1,p2)>0 and abs(p1+p2-1)<1e-12
    assert abs(p1*u+p2*v)<2e-12
    assert abs(p1*u*u+p2*v*v-1/3)<2e-9
    assert abs((p1*(1-u*u)+p2*(1-v*v))/2-1/3)<2e-9
    if kind == 'pole':
        assert abs(m+a-R) < tol
        assert abs(v+1/3)<2e-9
    elif kind == 'two_latitudes':
        assert R < 3*r and s>1.5*(R*R-r*r)/R
        assert u < 1 and v > -1
    return kind


def run():
    rng = random.Random(20261117)
    trials = 0
    counts = {}
    for ratio in [1,1.01,1.1,1.25,1.8,2,2.8,2.99,3,5,10]:
        R, r = ratio, 1.0
        for j in range(1,60):
            s = R-r+2*r*j/60
            kind=check(R,r,s)
            counts[kind] = counts.get(kind,0)+1
            trials+=1
        if R>r and R<3*r:
            sc=1.5*(R*R-r*r)/R
            gap=min(sc-(R-r),R+r-sc)
            for t in [sc,sc-1e-5*gap,sc+1e-5*gap]:
                kind=check(R,r,t)
                counts[kind] = counts.get(kind,0)+1
                trials+=1
            pole = parameters(R,r,sc)
            almost = parameters(R,r,sc+1e-7*gap)
            assert max(abs(pole[i]-almost[i]) for i in [1,2,3]) < 1e-3*R
    for _ in range(500):
        r=10**rng.uniform(-2,2)
        R=r*(1+9*rng.random())
        s=R-r+2*r*(0.002+0.996*rng.random())
        kind=check(R,r,s)
        counts[kind]=counts.get(kind,0)+1
        trials+=1
    # Published equal-ball normalization: R=1, center separation s=1.
    _,m,a,b,_,_=parameters(1.0,1.0,1.0)
    assert abs(m-.5)<1e-14
    assert abs(a-(math.sqrt(13)-2)/(2*math.sqrt(3)))<1e-13
    assert abs(b*b-(11-math.sqrt(13))/12)<1e-13
    # Ratio-three boundary: the two-latitude branch disappears exactly.
    for ratio in [3,3.1,5,20]:
        for j in range(1,20):
            R=ratio;r=1.0;s=R-r+2*j/20
            assert parameters(R,r,s)[0]=='pole'
    print('VERIFY_OK', 'parameter_cases=',trials, 'regimes=',counts,
          'boundary_checks=4', 'equal_lens=1')


if __name__=='__main__':
    run()
