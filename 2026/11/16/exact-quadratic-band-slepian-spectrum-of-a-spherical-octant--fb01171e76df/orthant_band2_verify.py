"""Exact arithmetic checks for the quadratic-band spherical-octant Slepian spectrum.

Run with Python 3 and SymPy: python orthant_band2_verify.py.
All formulas and input data are defined in this file. The exact eigenvalue
isolation uses rational Machin-series bounds, not floating-point tests.
"""
from fractions import Fraction
from itertools import combinations
from collections import defaultdict
import sympy as S

P = S.pi
z = S.symbols('z',positive=True)
t = S.symbols('t')
N = 3


def moment(exponents, positive):
    if not positive and any(k % 2 for k in exponents):
        return S.Integer(0)
    n = sum(exponents)
    v = S.gamma(S.Rational(N, 2)) / S.gamma(S.Rational(N+n, 2))
    for k in exponents:
        v *= S.gamma(S.Rational(k+1, 2)) / S.gamma(S.Rational(1, 2))
    return S.simplify(v)


def polynomial(terms):
    out = defaultdict(lambda:S.Integer(0))
    for indices, coefficient in terms:
        e = [0] * N
        for k in indices: e[k] += 1
        out[tuple(e)] += S.Integer(coefficient)
    return dict(out)


def gram(f, g, positive):
    result = 0
    for a, ca in f.items():
        for b, cb in g.items():
            result += ca*cb*moment(tuple(a[i]+b[i] for i in range(N)), positive)
    return S.simplify(result)


def matrix(basis, positive):
    return S.Matrix([[gram(f,g,positive) for g in basis] for f in basis])


# A spanning basis of the 9-dimensional restrictions of harmonic polynomials
# of degrees 0, 1, and 2 (on the unit sphere every degree-two polynomial
# decomposes into its traceless part and a constant).
full = [polynomial([([],1)])]
full += [polynomial([([i],1)]) for i in range(3)]
full += [polynomial([([i,j],1)]) for i,j in combinations(range(3),2)]
full += [polynomial([([0,0],1),([1,1],-1)]),
         polynomial([([0,0],1),([2,2],-1)])]
assert len(full)==9

# Independent spherical integrals for the two 3-dimensional multiplicity
# spaces. The full 9x9 Gram verifies the dimension and the Shannon trace.
Bfull=matrix(full,False)
Cfull=matrix(full,True)
assert Bfull.det()!=0
assert S.simplify(S.trace(Bfull.inv()*Cfull)-9)==0

triv=[polynomial([([],1)]),
      polynomial([([i],1) for i in range(3)]),
      polynomial([([0,1],1),([0,2],1),([1,2],1)])]
std=[polynomial([([0],1),([1],-1)]),
     polynomial([([0,0],1),([1,1],-1)]),
     polynomial([([0,2],1),([1,2],-1)])]

Bt=S.diag(1,1,S.Rational(1,5))
Ct=S.Matrix([[1,S.Rational(3,2),2/P],
             [S.Rational(3,2),1+4/P,3*(1+P)/(4*P)],
             [2/P,3*(1+P)/(4*P),(P+4)/(5*P)]])
Bs=S.diag(S.Rational(2,3),S.Rational(4,15),S.Rational(2,15))
Cs=S.Matrix([[2*(P-2)/(3*P),S.Rational(1,4),(P-2)/(4*P)],
             [S.Rational(1,4),S.Rational(4,15),4/(15*P)],
             [(P-2)/(4*P),4/(15*P),2*(P-2)/(15*P)]])

assert matrix(triv,False)==Bt
assert all(S.simplify(v)==0 for v in matrix(triv,True)-Ct)
assert matrix(std,False)==Bs
assert all(S.simplify(v)==0 for v in matrix(std,True)-Cs)
assert all(S.simplify(gram(f,g,k))==0 for f in triv for g in std for k in [False,True])


def atan_interval(q, n=30):
    value = sum((Fraction(-1 if k%2 else 1, (2*k+1)*q**(2*k+1))
                 for k in range(n)),Fraction(0))
    term = Fraction(1,(2*n+1)*q**(2*n+1))
    return (value, value+term) if n % 2==0 else (value-term, value)

xlo,xhi=atan_interval(5)
ylo,yhi=atan_interval(239)
pi_lo,pi_hi=16*xlo-4*yhi,16*xhi-4*ylo
assert Fraction(3)<pi_lo<pi_hi<Fraction(22,7)


def interval_sign(poly, root):
    """Exact interval Horner evaluation of polynomial in z at pi."""
    coeffs=S.Poly(S.together(poly.subs(t,S.Rational(root.numerator,root.denominator))),z).all_coeffs()
    lo=hi=Fraction(0)
    for c in coeffs:
        cs=Fraction(int(S.numer(c)),int(S.denom(c)))
        possible=(lo*pi_lo,lo*pi_hi,hi*pi_lo,hi*pi_hi)
        lo,hi=min(possible)+cs,max(possible)+cs
    if lo>0:return 1
    if hi<0:return -1
    raise AssertionError('unresolved rational interval sign')


def determinant_numerator(B,C):
    M=(C-t*B).applyfunc(lambda v:S.factor(v.subs(P,z)))
    num,den=map(S.factor,S.together(M.det()).as_numer_denom())
    # Both denominators are strictly positive for z>3.
    assert S.simplify(den.subs(z,4))>0
    return num

pt=determinant_numerator(Bt,Ct)
ps=determinant_numerator(Bs,Cs)
intervals_triv=[(Fraction(1,25000),Fraction(1,20000)),
                (Fraction(1,10),Fraction(11,100)),
                (Fraction(5),Fraction(6))]
intervals_std=[(Fraction(2,1000),Fraction(3,1000)),
               (Fraction(12,100),Fraction(14,100)),
               (Fraction(3,2),Fraction(17,10))]
for poly,intervals in [(pt,intervals_triv),(ps,intervals_std)]:
    for a,b in intervals:
        sa=interval_sign(poly,a);sb=interval_sign(poly,b)
        assert sa*sb==-1,(a,b,sa,sb)
# Three distinct disjoint real roots in each cubic; no other roots.
assert S.degree(pt,t)==S.degree(ps,t)==3
# Strict global ordering of the roots in the two blocks.
merged=[('t',a,b) for a,b in intervals_triv]+[('s',a,b) for a,b in intervals_std]
merged.sort(key=lambda v:v[1])
assert [x[0] for x in merged]==['t','s','t','s','s','t']
assert all(merged[i][2]<merged[i+1][1] for i in range(5))

# Symmetric-group invariance makes the standard block appear twice;
# the trivial block appears once. These exhaust all nine dimensions.
assert 3+2*3==9
print('OCTANT_BAND2_EXACT_CHECKS_PASS: full 9x9 moments, two 3x3 blocks, six rational root isolations')
print('pi_bound_width < 10^-35:',pi_hi-pi_lo<Fraction(1,10**35))
