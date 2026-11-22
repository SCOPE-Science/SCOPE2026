"""Exact transfer identity and zero-field Curie coefficient (requires SymPy)."""
import sympy as sp
z, l = sp.symbols('z l')
T = sp.Matrix([
    [1/z, z, z, z**3 + z],
    [1/z, 0, z+1/z, z],
    [1/z, z+1/z, 0, z],
    [1/z+z**(-3), 1/z, 1/z, z],
])
a = z+1/z
P = (l+a)*(l**3-2*a*l**2-3*l+z**3+z**(-3))
assert sp.simplify(T.charpoly(l).as_expr()-P)==0
assert sp.simplify(P.subs(z,1)-(l+1)*(l+2)*(l**2-5*l+2))==0
L=(5+sp.sqrt(17))/2
assert sp.simplify(P.subs({z:1,l:L}))==0
assert sp.simplify(sp.diff(P,z).subs({z:1,l:L}))==0
curie=sp.simplify(-sp.diff(P,z,2).subs({z:1,l:L})/(3*L*sp.diff(P,l).subs({z:1,l:L})))
assert sp.simplify(curie-(sp.Rational(29,24)-33*sp.sqrt(17)/136))==0
for n in range(3,10):
    observed=sp.trace(T.subs(z,1)**n)
    formula=sp.expand(L**n+((5-sp.sqrt(17))/2)**n+(-1)**n+(-2)**n)
    assert sp.simplify(observed-formula)==0
    assert observed>0
expected = {
3:{-3:4,-1:39,1:39,3:4},
4:{-4:9,-2:108,0:216,2:108,4:9},
5:{-5:11,-3:220,-1:740,1:740,3:220,5:11},
6:{-6:20,-4:462,-2:2235,0:3640,2:2235,4:462,6:20},
}
for n,h in expected.items():
    actual=sp.expand(sp.trace(T**n))
    exact=sum(weight*z**M for M,weight in h.items())
    assert sp.simplify(actual-exact)==0
print('TRANSFER IDENTITY, INFINITE-SIZE CURIE COEFFICIENT AND COUNTS: PASS')
