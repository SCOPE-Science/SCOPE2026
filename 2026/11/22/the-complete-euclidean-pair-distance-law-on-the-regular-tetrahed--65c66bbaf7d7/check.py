"""Reproduce independent analytic and numerical checks of the unit-tetrahedron wireframe distance law.
Requires only Python >=3.9 standard library. Run: python check.py
"""
from math import asin, sqrt, pi

T1=1/sqrt(2)
T2=sqrt(3)/2

def components(r):
    """Conditional CDF for same, vertex-adjacent and disjoint edge pairs."""
    if r <= 0:
        return (0., 0., 0.)
    if r >= 1:
        return (1., 1., 1.)
    same=2*r-r*r
    if r <= T2:
        adjacent=2*pi*r*r/(3*sqrt(3))
    else:
        adjacent=(4*r*r/sqrt(3)*asin(sqrt(3)/(2*r))
                  -4*pi*r*r/(3*sqrt(3)) + 2*sqrt(r*r-.75))
    if r <= T1:
        opposite=0.
    elif r <= T2:
        opposite=pi*(r*r-.5)
    else:
        rho2=r*r-.5
        opposite=(2*sqrt(r*r-.75) +4*rho2*asin(1/(2*sqrt(rho2)))
                  -pi*rho2)
    return (same, adjacent, opposite)

def cdf(r):
    s,a,o=components(r)
    return s/6+2*a/3+o/6

def simpson(f,a=0,b=1,n=4000):
    assert n%2==0
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+(2*j-1)*h) for j in range(1,n//2+1))
            +2*sum(f(a+2*j*h) for j in range(1,n//2)))*h/3

def independent_components(r):
    """Independently integrate actual coordinate-section lengths in the parameter squares."""
    s=2*r-r*r if 0 < r < 1 else float(r>=1)
    def adj_slice(x):
        z=r*r-3*x*x/4
        if z<=0:return 0.
        h=sqrt(z)
        return max(0.,min(1.,x/2+h)-max(0.,x/2-h))
    def opp_slice(x):
        z=r*r-.5-(x-.5)**2
        if z<=0:return 0.
        h=sqrt(z)
        return max(0.,min(1.,.5+h)-max(0.,.5-h))
    return s,simpson(adj_slice),simpson(opp_slice)

if __name__ == '__main__':
    # Structural edge-pair counts on the complete graph K4.
    edges=[(a,b) for a in range(4) for b in range(a+1,4)]
    counts=[0,0,0]
    for x in edges:
        for y in edges:
            common=len(set(x)&set(y))
            counts[{2:0,1:1,0:2}[common]]+=1
    assert counts==[6,24,6]
    print('PASS: 36 ordered edge pairs split as',counts)

    rs=[.025,.09,.2,.35,.5,.68,T1-.01,T1,T1+.01,.78,.84,T2-.008,T2,T2+.008,.91,.95,.985,.998]
    max_error=0.
    for r in rs:
        actual=components(r)
        independent=independent_components(r)
        err=max(abs(x-y) for x,y in zip(actual,independent))
        max_error=max(max_error,err)
        assert err < 0.00008, (r,actual,independent,err)
        assert -1e-12 <= cdf(r) <= 1+1e-12
    print('PASS: 18 independent, 1D-section quadrature comparisons; maximum absolute error',max_error)

    # Unique second-moment decomposition from conditional quadratic forms.
    m=(1/6)*(1/6)+(2/3)*(5/12)+(1/6)*(2/3)
    assert abs(m-5/12)<1e-14
    moment_quad=simpson(lambda r:2*r*(1-cdf(r)),n=16000)
    assert abs(moment_quad-5/12)<2e-7,(moment_quad,m)
    print('PASS: exact squared moment 5/12 and independent tail integral',moment_quad)

    # The threshold cusp coefficient is verified using independent integral geometry.
    # For delta=r^2-3/4, the side caps have 8/9 delta^(3/2) and 4/3 delta^(3/2)
    # at first order, respectively (per cap).
    assert abs((2/3)*(-2*8/9)+(1/6)*(-4*4/3)+56/27)<1e-13
    for delta in [.004,.001,.0002]:
        r=sqrt(.75+delta)
        s,a,o=components(r)
        baseline=(s/6+(2/3)*2*pi*r*r/(3*sqrt(3))+(1/6)*pi*(r*r-.5))
        measured=(cdf(r)-baseline)/delta**1.5
        assert abs(measured+56/27) < .03,(delta,measured)
    print('PASS: coefficient -56/27 of the interior 3/2 singularity')

    for eps in [.003,.001,.0003]:
        ratio=(1-cdf(1-eps))/eps**2
        assert abs(ratio-25/6)<.07,(eps,ratio)
    print('PASS: sharp upper-tail coefficient 25/6 from three corner contributions')
    print('ALL CHECKS PASSED')
