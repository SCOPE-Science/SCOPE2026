"""Independent exact-arithmetic checks for runner-up geodesic squared-distance gaps.

No external dependencies. Exact half-plane clipping tests the proposed distribution
for sampled rational shears and thresholds against all lattice vectors within
an explicitly finite test box. The written proof, not finite enumeration, handles
all lattice vectors.
"""
from fractions import Fraction as F


def clip(poly, a, b, c):
    """Intersect a rational convex polygon with a*x+b*y <= c."""
    if not poly:
        return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        dp = a*p[0] + b*p[1] - c
        dq = a*q[0] + b*q[1] - c
        if dp <= 0:
            out.append(p)
        if (dp < 0 < dq) or (dp > 0 > dq):
            lam = dp/(dp-dq)
            out.append((p[0] + lam*(q[0]-p[0]),p[1] + lam*(q[1]-p[1])))
        elif dp == 0 and dq > 0:
            pass
        elif dp > 0 and dq == 0:
            out.append(q)
    return out


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])))/2


def direct_cdf(t, eps, cutoff):
    # X = x dot (1,0), Y = x dot (t,1); determinant is one.
    poly = [(F(-3),F(-3)),(F(3),F(-3)),(F(3),F(3)),(F(-3),F(3))]
    vlist = sorted(((m,n) for m in range(-cutoff,cutoff+1)
                     for n in range(-cutoff,cutoff+1) if (m,n)!=(0,0)),
                   key=lambda z: (z[0]+z[1]*t)**2+z[1]**2)
    for m,n in vlist:
        squared=(m+n*t)**2+n**2
        poly=clip(poly,F(m),F(n),(squared-eps)/2)
        if not poly:
            return F(1)
    return 1-area(poly)


def formula(t,eps):
    eps=F(eps)
    return 1-(1-eps)*(1+t*t-eps)+max(F(0),abs(t)-eps/2)**2


def main():
    shears=[F(0),F(1,20),F(1,10),F(1,4),F(2,5),F(1,2)]
    thresholds=[F(0),F(1,100),F(1,20),F(1,5),F(1,4),F(1,2),F(3,4),F(9,10),F(1)]
    count=0
    for t in shears:
        for eps in thresholds:
            for cutoff in (2,4):
                measured=direct_cdf(t,eps,cutoff)
                expected=formula(t,eps)
                assert measured==expected, (t,eps,cutoff,measured,expected)
                count+=1
        assert formula(t,F(0)) == 0
    # Exact slope formula, including one-sided square-limit cusp.
    for t in shears:
        if t>0:
            h=min(t,F(1,10000))
            v=(formula(t,h)-formula(t,F(0)))/h
            assert v == 2-t+t*t-F(3,4)*h
    # The two analytic formulas coincide with matching first derivatives at eps=2t.
    for t in shears:
        h=2*t
        if h<=1:
            left=(2-t+t*t)*h-F(3,4)*h*h
            right=1-(1-h)*(1+t*t-h)
            assert left==right
            assert (2-t+t*t)-F(3,2)*h == (2+t*t)-2*h
    print('GEODESIC_GAP_RATIONAL_CLIPPING_OK',count,'exact comparisons; no exhaustive-lattice claim')


if __name__=='__main__':
    main()
