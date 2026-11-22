#!/usr/bin/env python3
"""Reproducibility checks for Euclidean parallel bodies of regular polygons.

Uses independent boundary Green integrals and exact polynomial identities.
Requires Python 3 and SymPy. Finite quadrature is corroborative only.
"""
import math
import sympy as sp


def exact_polynomial_certificate():
    r, a, s, k = sp.symbols('r a s k', real=True)
    area = a + 2*r + k*r**2
    moment = (a*(a**2+s**2/3)/2 + 2*(a**2+s**2/3)*r
              + (2*a+k)*r**2 + 2*r**3 + k*r**4/2)
    q = sp.expand(sp.diff(moment, r)*area - 2*moment*sp.diff(area, r))
    proposed = 4*s**2*(a*k-1)*r/3 - 2*(k*(1+2*a**2)-3*a)*r**2 - 2*(a*k+k**2-2)*r**3
    # Substitute s^2=1-a^2 without prematurely discarding polynomial terms.
    residual = sp.Poly(sp.expand(q-proposed), s).rem(sp.Poly(s**2+a**2-1, s)).as_expr()
    assert sp.simplify(residual) == 0
    alpha = k*s
    A = sp.symbols('N')*s*area
    J = sp.symbols('N')*s*moment
    h = alpha*(a**2+s**2/3)-a*s
    g = alpha**2+alpha*a*s-2*s**2
    defect = sp.expand(2*alpha*sp.symbols('N')*J-A**2
        -sp.symbols('N')**2*(a*s*h+4*s*h*r+2*g*r**2))
    assert sp.simplify(defect) == 0
    return 2


def simpson(f, lower, upper, panels=512):
    step=(upper-lower)/panels
    return step/3*(f(lower)+f(upper)+4*sum(f(lower+i*step) for i in range(1,panels,2))
           +2*sum(f(lower+i*step) for i in range(2,panels,2)))


def by_boundary(n, r):
    """Independent Green boundary calculation: straight edges plus curved vertex arcs."""
    alpha=math.pi/n
    a=math.cos(alpha)
    s=math.sin(alpha)
    edge_x=a+r
    A_edge=edge_x*s
    J_edge=edge_x*s*(edge_x**2+s**2/3)/2
    A_arc=simpson(lambda th: (r*math.cos(th)+r*r)/2, -alpha, alpha)
    J_arc=simpson(lambda th: (1+2*r*math.cos(th)+r*r)*(r*math.cos(th)+r*r)/4,
                  -alpha, alpha)
    return n*(A_edge+A_arc), n*(J_edge+J_arc)


def by_disjoint_regions(n, r):
    """Direct area and radial-moment polynomials from polygon, strips and sectors."""
    alpha=math.pi/n
    a=math.cos(alpha);s=math.sin(alpha)
    area=n*a*s+2*n*s*r+math.pi*r*r
    moment=(n*a*s*(a*a+s*s/3)/2 + 2*n*s*(a*a+s*s/3)*r
            +(2*n*a*s+math.pi)*r*r+2*n*s*r**3+math.pi*r**4/2)
    return area,moment


def run():
    count=exact_polynomial_certificate()
    for n in (3,4,5,6,7,8,12,21,36):
        alpha=math.pi/n;a=math.cos(alpha);s=math.sin(alpha)
        f=alpha*(1+2*a*a)-3*a*s
        g=alpha*alpha+alpha*a*s-2*s*s
        h=alpha*(a*a+s*s/3)-a*s
        assert min(f,g,h)>0
        count+=3
        last=None
        for r in (0,.001,.05,.2,1,3,8):
            A,J=by_disjoint_regions(n,r)
            Ar,Jr=by_boundary(n,r)
            assert abs(A-Ar)<2e-9*max(1,A),(n,r,A,Ar)
            assert abs(J-Jr)<2e-9*max(1,J),(n,r,J,Jr)
            assert 2*math.pi*J-A*A>0
            cur=J/(A*A)
            if last is not None:
                assert cur<last,(n,r,last,cur)
                count+=1
            last=cur
            count+=3
    print('PASS:',count,'independent numeric/algebraic assertions')

if __name__=='__main__':
    run()
