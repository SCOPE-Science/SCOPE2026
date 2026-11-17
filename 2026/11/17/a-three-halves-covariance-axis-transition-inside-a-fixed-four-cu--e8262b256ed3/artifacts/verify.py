"""Exact rational reproduction of four-cube section volume and covariance checks.

Needs Python 3, NumPy, SciPy, and SymPy. Floating arithmetic is used only
for determining convex-hull triangles; every subsequent vertex, determinant,
volume, and moment calculation is rational and exact. A non-degenerate list of
rational profiles avoids hull degeneracy except the t=1 octahedral boundary.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
from scipy.spatial import ConvexHull
import sympy as sp


def det3(a, b, c):
    return (a[0] * (b[1]*c[2]-b[2]*c[1])
            - a[1] * (b[0]*c[2]-b[2]*c[0])
            + a[2] * (b[0]*c[1]-b[1]*c[0]))


def section_vertices(t):
    normal = (F(1), F(1), t, t)
    out = set()
    for free in range(4):
        fixed = [j for j in range(4) if j != free]
        for signs in product((-1, 1), repeat=3):
            x = [F(0)]*4
            for j, s in zip(fixed, signs):
                x[j] = F(s)
            x[free] = -sum(normal[j]*x[j] for j in fixed)/normal[free]
            if -1 <= x[free] <= 1:
                out.add(tuple(x))
    return sorted(out)


def profile(t):
    t = F(t)
    vertices = section_vertices(t)
    hull = ConvexHull(np.asarray([list(map(float, v[:3])) for v in vertices]))
    volume6 = F(0)
    raw = [F(0)]*3
    forms = ((F(1),F(-1),F(0),F(0)),
             (F(0),F(0),F(1),F(-1)),
             (-t,-t,F(1),F(1)))
    for simplex in hull.simplices:
        v = [vertices[j] for j in simplex]
        det = abs(det3(v[0][:3],v[1][:3],v[2][:3]))
        volume6 += det
        # A tetrahedron (0,v1,v2,v3) has average square of a linear form:
        # [sum_i ell(vi)^2 + (sum_i ell(vi))^2] / 20.
        for i, ell in enumerate(forms):
            values = [sum(ell[j]*w[j] for j in range(4)) for w in v]
            raw[i] += det*(sum(s*s for s in values)+sum(values)**2)/20
    normsq = (F(2), F(2), 2*(t*t+1))
    eigenvalues = [x/volume6/l for x,l in zip(raw,normsq)]
    predicted = [(5*t-1)/(5*(3*t-1)),
                 (10*t**3-10*t**2+5*t-1)/(5*t*t*(3*t-1)),
                 (t*t+1)*(5*t-3)/(5*t*t*(3*t-1))]
    assert eigenvalues == predicted, (t,eigenvalues,predicted)
    assert volume6 == 16*(3*t-1)/t, (t,volume6)
    assert len(vertices) == (6 if t==1 else 8), (t,len(vertices))
    return len(vertices), len(hull.simplices)


def verify_symbolic():
    t=sp.symbols('t',positive=True)
    a=(5*t-1)/(5*(3*t-1))
    b=(10*t**3-10*t**2+5*t-1)/(5*t*t*(3*t-1))
    c=(t*t+1)*(5*t-3)/(5*t*t*(3*t-1))
    assert sp.factor(b-a)==(t-1)*(5*t*t-4*t+1)/(5*t*t*(3*t-1))
    assert sp.factor(b-c)==(t-1)*(5*t*t-2*t-2)/(5*t*t*(3*t-1))
    assert sp.simplify((c-a)-(t-1)*(3-2*t)/(5*t*t*(3*t-1)))==0
    u=sp.symbols('u',real=True)
    i0=sp.integrate((1-u)*(1-u/t),(u,0,1))
    ia=sp.integrate((1-u)**3*(1-u/t),(u,0,1))
    ib=sp.integrate((1-u)*(1-u/t)**3,(u,0,1))
    i2=sp.integrate(u*u*(1-u)*(1-u/t),(u,0,1))
    assert sp.simplify((sp.Rational(2,3)*ia/i0)-a)==0
    assert sp.simplify((sp.Rational(2,3)*ib/i0)-b)==0
    assert sp.simplify((2*(t*t+1)*i2/(t*t*i0))-c)==0
    volume=8*sp.sqrt(2*(t*t+1))*(3*t-1)/(3*t*t)
    assert sp.simplify(sp.diff(volume,t)-8*sp.sqrt(2)*(t-1)*(t-2)/(3*t**3*sp.sqrt(t*t+1)))==0
    assert sp.simplify((b/a).subs(t,sp.Rational(3,2))-sp.Rational(142,117))==0
    assert sp.simplify((b/c).subs(t,2)-sp.Rational(7,5))==0


if __name__ == '__main__':
    verify_symbolic()
    profiles = ['1','11/10','5/4','7/5','3/2','8/5','7/4','2','9/4','5/2','3','4','7','10','17']
    count=0
    simplices=0
    for frac in profiles:
        v,f=profile(F(frac))
        count+=v
        simplices+=f
    print('FOUR_CUBE_PAIR_SECTION_CHECKS_PASSED profiles=%d vertices=%d tetrahedra=%d' %
          (len(profiles),count,simplices))
