"""Reproducibility checks for an exact two-periodic polynomial zero law.

Requires only Python 3 standard library. Numerical tests are illustrative and do
not replace the proof of the assertions for arbitrary parameters and degree.
"""
from fractions import Fraction as Q
from math import sin, sinh, cos, cosh, pi, log


def add(p, q):
    return [((p[i] if i < len(p) else 0) +
             (q[i] if i < len(q) else 0))
            for i in range(max(len(p), len(q)))]


def scale(p, s):
    return [s*v for v in p]


def mul_linear(p, const, power=1):
    result = [Q(0)] * (len(p) + power)
    for i, v in enumerate(p):
        result[i] += v * const
        result[i+power] += v
    return result


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def monic_family(a, b, c, degree):
    p0, p1 = [Q(1)], [-a, Q(1)]
    rows = [p0, p1]
    for n in range(1, degree):
        diag = -a if n % 2 else a
        d = b if n % 2 else c
        nxt = add(mul_linear(rows[-1], -diag), scale(rows[-2], -d))
        rows.append(trim(nxt))
    return rows[:degree+1]


def square_substitution(h):
    res = [Q(0)] * (2*(len(h)-1)+1)
    for i, v in enumerate(h):
        res[2*i] = v
    return res


def closed_even_odd(a,b,c,k):
    # H_k(y) = P_{2k}(sqrt(y)); G_k(y) = P_{2k+1}(sqrt(y))/(sqrt(y)-a).
    h = [[Q(1)], [-(a*a+b), Q(1)]]
    g = [[Q(1)], [-(a*a+b+c), Q(1)]]
    for j in range(1,k):
        h.append(trim(add(mul_linear(h[-1],-(a*a+b+c)),scale(h[-2],-b*c))))
        g.append(trim(add(mul_linear(g[-1],-(a*a+b+c)),scale(g[-2],-b*c))))
    even = square_substitution(h[k])
    odd = mul_linear(square_substitution(g[k]), -a)
    return trim(even),trim(odd)


def sratio(k,t):
    return sinh((k+1)*t)/sinh(k*t)


def cratio(k,t):
    return sin((k+1)*t)/sin(k*t)


def minimal_scaled(k,gamma):
    q = 1+gamma/k
    assert q>0
    if gamma > 1:
        lo,hi = 0.0,log(q)
        for _ in range(75):
            mid=(lo+hi)/2
            if sratio(k,mid)<q:lo=mid
            else:hi=mid
        theta = (hi+lo)/2
        return k*k*((q-1)**2-2*q*(cosh(theta)-1))
    if gamma == 1:
        return 1.0
    lo,hi=0.0,pi/(k+1)
    for _ in range(75):
        mid=(lo+hi)/2
        if cratio(k,mid)>q:lo=mid
        else:hi=mid
    theta=(hi+lo)/2
    return k*k*((q-1)**2+2*q*(1-cos(theta)))


def limit_scaled(gamma):
    if gamma == 1:return 1.0
    if gamma>1:
        lo,hi=0.0,2*gamma
        for _ in range(85):
            z=(lo+hi)/2
            value=z*cosh(z)/sinh(z) if z else 1
            if value<gamma:lo=z
            else:hi=z
        z=(lo+hi)/2
        return gamma*gamma-z*z
    lo,hi=0.0,pi
    for _ in range(85):
        w=(lo+hi)/2
        value=w*cos(w)/sin(w) if w else 1
        if value>gamma:lo=w
        else:hi=w
    w=(lo+hi)/2
    return gamma*gamma+w*w


def main():
    checks=0
    for a,b,c in [(Q(0),Q(1),Q(4)),(Q(2,3),Q(3,2),Q(7,5)),
                  (Q(-5,4),Q(7,3),Q(2,5))]:
        rows=monic_family(a,b,c,20)
        for k in range(1,10):
            even,odd=closed_even_odd(a,b,c,k)
            assert even == rows[2*k]
            assert odd == rows[2*k+1]
            checks+=2
    # All three finite-size phases of the level crossing.
    for k in range(1,17):
        edge = 1+1/k
        for q in [edge*.84,edge,edge*1.23]:
            # The characteristic polynomial at t=-1 changes sign once.
            F = (-1)**k * ((k+1)-k*q)
            if q<edge:assert F*(-1)**k>0
            elif q>edge:assert F*(-1)**k<0
            else:assert abs(F)<1e-12
            checks+=1
    # Critical scaling: doubled k approaches the analytical limit.
    for gamma in [-3.,-1.,0.,0.5,1.,1.3,2.,3.]:
        vals=[minimal_scaled(k,gamma) for k in (100,300,900)]
        exact=limit_scaled(gamma)
        assert abs(vals[-1]-exact) < abs(vals[0]-exact)+1e-6
        assert abs(vals[-1]-exact) < .06
        checks+=2
    print(f'PASS: {checks} exact/algebraic and numerical test assertions')

if __name__=='__main__':
    main()
