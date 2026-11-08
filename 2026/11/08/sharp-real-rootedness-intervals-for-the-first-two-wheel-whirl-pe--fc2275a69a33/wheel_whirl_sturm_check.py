"""Exact rational verification of the rank-four wheel--whirl root pencil.
Requires Python 3 and SymPy. All root counts use exact Sturm arithmetic.
"""
from math import comb
import sympy as sp

z, lam = sp.symbols('z lam')

def crown_ehrhart(q, r=4):
    mat = sp.Matrix([[min(i,j) for j in range(1,q+2)] for i in range(1,q+2)])
    return int(sp.trace(mat**r))

def direct_count(q, r=4):
    from itertools import product
    # Choose odd coordinates. For every adjacent odd pair, count the even coordinate.
    return sum(__import__('math').prod(q+1-max(v[i],v[(i+1)%r]) for i in range(r))
               for v in product(range(q+1), repeat=r))

for q in range(4):
    assert crown_ehrhart(q) == direct_count(q)

L = [crown_ehrhart(q) for q in range(9)]
h = [sum((-1)**(k-j)*comb(9,k-j)*L[j] for j in range(k+1)) for k in range(9)]
assert h == [1,38,263,484,263,38,1,0,0]

C = z * sum(comb(3,i)**2*z**i for i in range(4))
P = sum(h[i]*z**i for i in range(7)) - lam*C
assert sp.expand(P - (z**6+38*z**5+(263-lam)*z**4+(484-9*lam)*z**3+(263-9*lam)*z**2+(38-lam)*z+1)) == 0
D = sp.factor(sp.discriminant(P,z)/16)
D_expected = (540*lam**9 + 253179*lam**8 + 20881044*lam**7
- 2104879564*lam**6 + 38517032576*lam**5 + 505358362624*lam**4
- 43739303378944*lam**3 + 1148331013439488*lam**2
- 15876704476069888*lam + 73794715169849344)
assert sp.expand(D-D_expected)==0
polyD = sp.Poly(D,lam)
assert polyD.count_roots(-sp.oo,sp.oo)==3
intervals = [(sp.Rational(-313,10),sp.Rational(-312,10)),
             (sp.Rational(816,100),sp.Rational(817,100)),
             (sp.Rational(3696,100),sp.Rational(3697,100))]
for a,b in intervals:
    assert polyD.count_roots(a,b)==1
for value, negcount in [(-32,4),(0,6),(9,4)]:
    p = sp.Poly(P.subs(lam,value),z)
    assert p.count_roots(-sp.oo,0)==negcount
    assert p.count_roots(0,sp.oo)==0
assert intervals[2][0] > sp.Rational(263,9) # further parameter values have a negative z^2 coefficient

# Non-published independent test: P_0 is monic reciprocal and real-rooted.
assert all(h[i]==h[6-i] for i in range(7))
# Auxiliary first-rank polynomial, to distinguish the special reciprocal situation.
P3 = 1+(11-lam)*z+(24-4*lam)*z**2+(11-lam)*z**3+z**4
assert sp.expand(sp.discriminant(P3,z)-12*(lam-8)*(lam-2)*(lam**2-6*lam+33)**2)==0

print('PASS: direct crown counts, independent generating transform, exact discriminant,')
print('three global Sturm isolation intervals, and negative-root sample counts.')
print('h4 =', h[:7]); print('discriminant degree =',polyD.degree())
print('critical intervals =',intervals)
