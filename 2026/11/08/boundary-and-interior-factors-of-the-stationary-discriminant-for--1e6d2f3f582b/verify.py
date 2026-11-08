"""Exact checks for the stationary discriminant of fixed-pole rational functions.
Requires SymPy. This finite verification supplements the all-m proof.
"""
import sympy as sp

x = sp.symbols('x')

def factor_profile(m):
    poles = tuple(map(sp.Integer, range(m)))
    c = sp.symbols('c0:%d' % m)
    H = sum(c[j] * sp.prod((x-r)**2 for k, r in enumerate(poles) if k != j)
            for j in range(m))
    disc = sp.discriminant(H, x)
    parts = sp.factor_list(disc)[1]
    profile = sorted((sp.Poly(f, c).total_degree(), int(power)) for f, power in parts)
    expected = sorted([(1, 1)] * m + [(3*m-6, 1)])
    assert profile == expected, (m, profile, expected)
    assert sp.Poly(H, x).degree() == 2*m-2
    assert sp.Poly(disc, c).total_degree() == 4*m-6
    return profile

assert factor_profile(3) == [(1, 1)]*3 + [(3, 1)]
assert factor_profile(4) == [(1, 1)]*4 + [(6, 1)]

# Check a concrete ruling curve with n_1=n_2=2, L=1+t^2+t^4.
a,b,c,d,e = sp.symbols('a b c d e')
variables = (a,b,c,d,e)
L = 1+x**2+x**4
G = a*x**4+b*x**3+c*x**2+d*x+e
H = sp.expand(sp.diff(G,x)*L-G*sp.diff(L,x))
assert sp.degree(H,x) == 6
D = sp.discriminant(H,x)
factors = sp.factor_list(D)[1]
profile = sorted((sp.Poly(f,variables).total_degree(),int(p)) for f,p in factors)
assert profile == [(2,1),(2,1),(6,1)],profile
assert sp.Poly(D,variables).total_degree()==10
assert sp.resultant(G,L,x) != 0
quad_product = sp.prod(f for f,p in factors if sp.Poly(f,variables).total_degree()==2)
q_div, q_rem = sp.Poly(sp.resultant(G,L,x),*variables).div(sp.Poly(quad_product,*variables))
assert q_rem.is_zero and q_div.total_degree() == 0
# Verify direct factor identity up to scalar, using an exact rational specialization.
R = sp.resultant(G,L,x)
quo = sp.cancel(D / R)
assert sp.together(quo).as_numer_denom()[1].is_number
assert sp.Poly(sp.together(quo),variables).total_degree()==6

r = [sp.Integer(j) for j in range(4)]
t,u = sp.symbols('t u')
M = sp.Matrix([[(z-v)**(-k) for v in r] for z,k in ((t,2),(t,3),(u,2),(u,3))])
assert M.subs({t:4,u:5}).det() != 0
print('GENERAL_FIXED_POLES m=3,4: FACTORIZATION_OK')
print('SCROLL_(2,2): FACTOR_DEGREES_2_2_6_OK')
print('TWO_DOUBLE_ROOT_INCIDENCE: RANK_FOUR_WITNESS_OK')
print('CERTIFICATE_OK')
