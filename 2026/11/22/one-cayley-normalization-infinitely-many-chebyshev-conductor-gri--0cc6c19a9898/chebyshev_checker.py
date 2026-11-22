#!/usr/bin/env python3
"""Exact arithmetic diagnostics for Chebyshev--Cayley surface identities.

Requires sympy. This is a finite supplement to the algebraic proof, not an
exhaustive verification over every Chebyshev index.
"""
import sympy as s
x,y,z,u,v,w=s.symbols('x y z u v w')
for m,n in [(2,2),(2,3),(3,5),(4,4),(5,6)]:
    Ym=s.chebyshevt(m,y); Zn=s.chebyshevt(n,z)
    Um=s.chebyshevu(m-1,y); Vn=s.chebyshevu(n-1,z)
    assert s.expand(Ym**2-1-(y**2-1)*Um**2)==0
    assert s.expand(Zn**2-1-(z**2-1)*Vn**2)==0
    assert s.expand(s.diff(Ym,y)-m*Um)==0
    assert s.expand(s.diff(Zn,z)-n*Vn)==0
    F=x**2+Ym**2+Zn**2-2*x*Ym*Zn-1
    identity=(x-Ym*Zn)**2-(y**2-1)*(z**2-1)*Um**2*Vn**2
    assert s.expand(F-identity)==0
    assert s.degree(Um,y)==m-1 and s.degree(Vn,z)==n-1
    assert s.degree(s.gcd(Um,s.diff(Um,y)),y)==0
    assert s.degree(s.gcd(Vn,s.diff(Vn,z)),z)==0
    assert Um.subs(y,1)==m and Vn.subs(z,1)==n
    assert Um.subs(y,-1)==(-1)**(m-1)*m
    assert Vn.subs(z,-1)==(-1)**(n-1)*n
    n_double=m+n-2; n_cross=(m-1)*(n-1); n_pinch=2*n_double
    print(f'm={m}, n={n}: components={n_double}, crossings={n_cross}, pinch={n_pinch}, isolated A1=4')
# Exact local Jacobian equations after characteristic-zero unit changes.
models={
'ordinary_double_curve': u**2-v**2,
'pinch_point':u**2-v**2*w,
'crossing_of_double_curves':u**2-v**2*w**2,
'isolated_node':u**2-v*w,
}
for name,F in models.items():
    derivatives=[s.diff(F,t) for t in (u,v,w)]
    GB=s.groebner(derivatives,u,v,w)
    # Known generators of the scheme-theoretic critical ideals.
    expected={
        'ordinary_double_curve':[u,v],
        'pinch_point':[u,v*w,v**2],
        'crossing_of_double_curves':[u,v*w**2,v**2*w],
        'isolated_node':[u,v,w],
    }[name]
    for g in derivatives+expected:
        assert GB.reduce(g)[1]==0
    G2=s.groebner(expected,u,v,w)
    for g in derivatives:
        assert G2.reduce(g)[1]==0
    print(name,': Jacobian generators=',expected)
print('All exact finite symbolic diagnostics passed.')
