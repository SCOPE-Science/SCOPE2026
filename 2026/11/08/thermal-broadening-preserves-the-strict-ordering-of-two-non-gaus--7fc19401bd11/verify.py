"""Exact symbolic verification of stationary reset-force cumulants and their optimizers.

Requires Python 3 and SymPy; run `python verify.py`.
"""
import sympy as s

b, q = s.symbols('b q', positive=True)
w = b + q*(b+1)
A = 205*b**4+1077*b**3+1694*b**2+876*b+180
K4 = 6*b**2*(7*b+3)/((b+2)*(b+3)*w**2)
K6 = 120*b**3*A/((b+2)**2*(b+3)**2*(b+4)*(b+5)*w**3)
P4 = (7*q+7)*b**4+(6-q)*b**3-(97*q+27)*b**2-141*q*b-36*q
P6 = (410*q+410)*b**9+(4871*q+5076)*b**8+(13097*q+19862)*b**7 + (7926-66193*q)*b**6 - (522631*q+132670)*b**5 - (1433038*q+330840)*b**4 - (1973436*q+278100)*b**3 - (1390392*q+59400)*b**2-457920*q*b-64800*q
H = -1435*b**8-8472*b**7+52694*b**6+602850*b**5+2114117*b**4+3534090*b**3+2901096*b**2+1014660*b+64800

def eq(a, c):
    assert s.cancel(a-c) == 0, 'Symbolic identity mismatch'

def generator_moments(rate, thermal):
    """Independent polynomial stationary generator balance, dimensionless units."""
    M = {(0,0): s.Integer(1)}
    for n in range(1,7):
        for i in range(n+1):
            j=n-i
            rhs=s.Integer(0)
            if i: rhs += i*rate*M[(i-1,j+1)]
            if j>=2: rhs += j*(j-1)*M[(i,j-2)]
            if i>=2: rhs += 2*thermal*i*(i-1)*M[(i-2,j)]
            M[(i,j)] = s.cancel(rhs/(i+(rate if j else 0)))
    return M

M=generator_moments(b,q)
V=2*(b+q*(b+1))/(b+1)
eq(M[(2,0)],V)
eq((M[(4,0)]-3*V**2)/V**2,K4)
eq((M[(6,0)]-15*M[(4,0)]*V+30*V**3)/V**3,K6)

# Independent exact rational parameter checks using generator recurrence.
checks=0
for bb in [s.Rational(1,5),s.Rational(1,2),s.Integer(1),s.Rational(9,4),s.Integer(3),s.Integer(5)]:
    for qq in [s.Integer(0),s.Rational(1,5),s.Integer(1),s.Integer(4)]:
        mm=generator_moments(bb,qq)
        vv=mm[(2,0)]
        eq((mm[(4,0)]-3*vv**2)/vv**2,K4.subs({b:bb,q:qq}))
        eq((mm[(6,0)]-15*mm[(4,0)]*vv+30*vv**3)/vv**3,K6.subs({b:bb,q:qq}))
        checks += 2

eq(s.diff(K4,b),-6*b*P4/((b+2)**2*(b+3)**2*w**3))
eq(s.diff(K6,b),-120*b**2*P6/((b+2)**3*(b+3)**3*(b+4)**2*(b+5)**2*w**4))
eq(s.diff(s.log(K6**2/K4**3),b),H/((b+2)*(b+3)*(b+4)*(b+5)*(7*b+3)*A))
eq(s.diff(s.log(K4),b)-s.diff(s.log(K4.subs(q,0)),b),2*q/(b*w))
eq(s.diff(s.log(K6),b)-s.diff(s.log(K6.subs(q,0)),b),3*q/(b*w))
eq(P4.subs(b,5),2*(542*q+2225))
eq(P6.subs(b,6),7776*(834743*q+2194554))

# Exact sign variations of coefficient lists, for nonnegative q including regime boundaries.
def changes(xs):
    xs=[s.sign(z) for z in xs if z]
    return sum(xs[i]!=xs[i+1] for i in range(len(xs)-1))
for qq in [s.Rational(0),s.Rational(1,100),s.Rational(1,8),s.Integer(1),s.Integer(10),s.Integer(1000)]:
    for P in [P4,P6]:
        coeffs=s.Poly(P.subs(q,qq),b).all_coeffs()
        assert changes(coeffs)==1
        checks+=1

# By positivity and Descartes, these numerical roots are illustrations, not a uniqueness proof.
for qq in [0,s.Rational(1,10),s.Integer(1),s.Integer(10),s.Integer(100)]:
    roots=[]
    for P in [P4,P6]:
        poly=s.Poly(P.subs(q,qq),b)
        intervals=poly.intervals(eps=s.Rational(1,100000000))
        positive=[(lo,hi) for (lo,hi),mult in intervals if hi>0 and lo>=0]
        assert len(positive)==1, (qq,positive)
        lo,hi=positive[0]
        roots.append((lo+hi)/2)
    assert 0<roots[0]<roots[1]<6, (qq,roots)
    checks+=1

# For 0 < b <= 5: b^8<=125b^5, b^7<=25b^5,
# hence H >= (602850-1435*125-8472*25)b^5 + other positive terms.
assert 602850-1435*125-8472*25 == 211675
print('PASS: symbolic stationary generator, cumulants, derivatives, thermal invariant, and root checks')
print('Rational/interval checks:',checks)
