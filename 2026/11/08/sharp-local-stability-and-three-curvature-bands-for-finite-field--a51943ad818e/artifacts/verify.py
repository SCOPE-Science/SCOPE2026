#!/usr/bin/env python3
"""Reproducible exact checks for the cubic-graph extension stability theorem.

Requires SymPy (see requirements.txt). The universal theorem is proved in
RESULT.md; finite checks below test its normalization and algebra.
"""
from collections import defaultdict
from random import Random
import sympy as sp

I = sp.I


def norm2(x):
    return sp.expand(x * sp.conjugate(x))


def q_from_collisions(g, p):
    """Direct character-orthogonality fibers over a prime field."""
    fibers = defaultdict(lambda: sp.Integer(0))
    for a in range(p):
        for b in range(p):
            fibers[((a + b) % p, (a**3 + b**3) % p)] += g[a] * g[b]
    return sp.expand(sum(norm2(v) for v in fibers.values()))


def q_closed(g, p):
    S = sum(norm2(z) for z in g)
    P4 = sum(norm2(z) ** 2 for z in g)
    R = sum(norm2(g[j]) * norm2(g[-j % p]) for j in range(p))
    B = sum(g[j] * g[-j % p] for j in range(p))
    return sp.expand(2*S*S - P4 - 2*R + norm2(g[0])**2 + norm2(B))


def deficit_terms(g, p):
    m = (p - 1) // 2
    S = sp.expand(sum(norm2(z) for z in g))
    a = norm2(g[0]); D = 2*p + 1
    r = [sp.expand(norm2(g[j]) + norm2(g[-j % p])) for j in range(1, m+1)]
    b = [sp.simplify(2*sp.sqrt(norm2(g[j])*norm2(g[-j % p]))) for j in range(1, m+1)]
    w = [g[0]**2] + [2*g[j]*g[-j % p] for j in range(1, m+1)]
    T = a + sum(b)
    variance = 2*(a - 3*S/sp.Integer(D))**2 + sp.Rational(3,2)*sum((v-4*S/sp.Integer(D))**2 for v in r)
    phase = sp.expand(T*T - norm2(sum(w)))
    pair_imbalance = sum((r[j]-b[j])*(S+T-(r[j]+b[j])/2) for j in range(m))
    delta = (3-sp.Rational(6,D))*S*S-q_closed(g,p)
    assert sp.simplify(delta-variance-phase-pair_imbalance)==0
    for term in (variance, phase, pair_imbalance):
        assert float(sp.N(term,15)) >= -1.e-10
    return True


def exact_hessian(p):
    """Compare every coefficient of the quadratic Taylor polynomial."""
    m=(p-1)//2; D=2*p+1
    A=sp.sqrt(sp.Rational(3,D)); B=sp.sqrt(sp.Rational(2,D))
    u=sp.symbols('u:'+str(p), real=True)
    v=sp.symbols('v:'+str(p), real=True)
    e=sp.symbols('e', real=True)
    f=[(A if j==0 else B)+e*(u[j]+I*v[j]) for j in range(p)]
    a=[sp.expand(z*sp.conjugate(z)) for z in f]
    S=sp.Add(*a)
    C=3-sp.Rational(6,D)
    Bsum=f[0]**2 + 2*sum(f[j]*f[p-j] for j in range(1,m+1))
    E=2*a[0]**2+sum(a[j]**2+a[p-j]**2+4*a[j]*a[p-j] for j in range(1,m+1))
    delta=sp.expand((C-2)*S*S + E - Bsum*sp.conjugate(Bsum))
    assert sp.simplify(delta.coeff(e,0))==0
    assert sp.simplify(delta.coeff(e,1))==0
    ue=u[0]**2+sum((u[j]+u[p-j])**2/2 for j in range(1,m+1))
    ve=v[0]**2+sum((v[j]+v[p-j])**2/2 for j in range(1,m+1))
    uo=sum((u[j]-u[p-j])**2/2 for j in range(1,m+1))
    wu=A*u[0]+B*sum(u[1:]); wv=A*v[0]+B*sum(v[1:])
    expect=sp.Rational(24,D)*(ue-wu**2)+(4-sp.Rational(8,D))*uo+4*(ve-wv**2)
    assert sp.expand(delta.coeff(e,2)-expect)==0
    assert sp.Rational(24,D)<4-sp.Rational(8,D)<4
    # The fixed orthogonal decomposition has three bands of dimension m,
    # with zero modes: real radial, imaginary phase, and m odd phases.
    assert m*3+(m+2)==2*p
    return True


def local_gap_numeric(p):
    D=2*p+1
    A=sp.sqrt(sp.Rational(3,D)); B=sp.sqrt(sp.Rational(2,D))
    h=[A]+[B]*(p-1)
    # Antipodally even amplitude perturbation perpendicular to h.
    u=[(sp.Integer(1) if j==0 else 0)-A*h[j] for j in range(p)]
    eps=sp.Rational(1,3000)
    v=[h[j]+eps*u[j] for j in range(p)]
    nrm=sp.sqrt(sum(x*x for x in v))
    f=[x/nrm for x in v]
    S=sum(x*x for x in f)
    assert sp.simplify(S-1)==0
    delta=(3-sp.Rational(6,D))*S*S-q_closed(f,p)
    # All entries are positive; their closest torus point has their same
    # phases, hence is the positive real extremizer h.
    dist2=sum((f[j]-h[j])**2 for j in range(p))
    ratio=sp.N(delta/dist2,45)
    assert abs(float(ratio-sp.Rational(24,D)))<0.005, (p,ratio)
    return ratio


def main():
    rnd=Random(17031)
    collision=0; deficit=0; exact=0
    values=[0,1,-1,2,-2,I,-I,2*I,-2*I,1+I,1-I]
    for p in (5,7,11):
        for _ in range(12):
            f=[sp.sympify(rnd.choice(values)) for _ in range(p)]
            assert sp.expand(q_from_collisions(f,p)-q_closed(f,p))==0
            collision+=1
            deficit_terms(f,p); deficit+=1
        exact_hessian(p); exact+=1
        print('SHARP_LOCAL_GAP',p,local_gap_numeric(p))
    print('CUBIC_CURVE_STABILITY_VERIFY_PASS', 'collision',collision,'deficit',deficit,'hessian',exact)

if __name__=='__main__':
    main()
