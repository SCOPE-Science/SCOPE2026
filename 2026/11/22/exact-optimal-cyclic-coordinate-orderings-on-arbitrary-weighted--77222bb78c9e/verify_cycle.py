"""Supplementary finite verification of the weighted odd-cycle Gauss--Seidel theorem.

The infinite all-order statement follows from the supplied proof, NOT this finite test.
Requires Python 3, numpy and sympy. No network or external files.
"""
from itertools import permutations
from fractions import Fraction
import numpy as np
import sympy as sp

def cycle_matrix(weights, diagonal):
    n = len(weights)
    A = sp.diag(*diagonal)
    for i, w in enumerate(weights):
        j = (i+1) % n
        A[i,j] = A[j,i] = -w
    return A

def splitting(A, order):
    n = A.rows
    P = A.extract(order, order)
    D = sp.diag(*[P[i,i] for i in range(n)])
    L = sp.zeros(n)
    U = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            if i > j: L[i,j] = P[i,j]
            if i < j: U[i,j] = P[i,j]
    return D,L,U

def ascent(order):
    n=len(order)
    loc={vertex:k for k,vertex in enumerate(order)}
    return sum(loc[i] < loc[(i+1) % n] for i in range(n))

def exact_identity(n, weights, diagonal, order):
    A = cycle_matrix(weights, diagonal)
    D,L,U = splitting(A,order)
    x=sp.symbols('x',positive=True)
    f=(x*x*(D+L)+U).det(method='berkowitz')
    W=sp.diag(*diagonal)-A
    a=ascent(order)
    wprod=sp.prod(weights)
    rhs=x**n*((x*sp.diag(*diagonal)-W).det(method='berkowitz')
        - wprod*(x**(2*a-n)+x**(n-2*a)-2))
    assert sp.simplify(f-rhs)==0, f'failed identity {n},{order}'

# Exact symbolic determinant checks on unequal weights and diagonal shifts.
for n in [5,7]:
    weights=list(map(sp.Integer, [1,2,3,4,5,6,7][:n]))
    diagonal=[sp.Integer(weights[(i-1)%n]+weights[i]+2+i%3) for i in range(n)]
    for order in [list(range(n)),list(range(0,n,2))+list(range(1,n,2))]:
        exact_identity(n,weights,diagonal,order)
print('EXACT_IDENTITY_CHECKS=4 PASS')

# Exact five-cycle characteristic polynomials, checked without floating point.
A5=cycle_matrix([1]*5,[3]*5)
t=sp.symbols('t')
for order,expected in [([0,1,2,3,4],t*(243*t**4-136*t**3+15*t**2-1)),
                       ([0,2,4,1,3],t**2*(243*t**3-135*t**2+14*t-1))]:
    D,L,U=splitting(A5,order)
    assert sp.expand((t*(D+L)+U).det()-expected)==0
popt=243*t**3-135*t**2+14*t-1
pworst=243*t**4-136*t**3+15*t**2-1
assert popt.subs(t,sp.Rational(4473,10000))<0<popt.subs(t,sp.Rational(4474,10000))
assert pworst.subs(t,sp.Rational(4679,10000))<0<pworst.subs(t,sp.Rational(4680,10000))
print('EXACT_POLYNOMIALS_AND_BRACKETS=4 PASS')

# A separate floating implementation constructs sequential coordinate updates.
# Every permutation is evaluated; grouping by cyclic ascents is compared.
for n in [5,7]:
    weights=np.array([1.0+0.11*i+0.013*(i%2) for i in range(n)])
    A=np.diag([weights[(i-1)%n]+weights[i]+0.9+0.17*(i%3) for i in range(n)])
    for i in range(n): A[i,(i+1)%n]=A[(i+1)%n,i]=-weights[i]
    grouped={}
    for order in permutations(range(n)):
        T=np.eye(n)
        for i in order:
            single=np.eye(n)
            single[i,:]-=A[i,:]/A[i,i]
            T=single@T
        spectral_radius=np.max(np.abs(np.linalg.eigvals(T)))
        grouped.setdefault(ascent(order),[]).append(spectral_radius)
    for a,rates in grouped.items():
        assert max(rates)-min(rates)<1e-9,(n,a)
    mid=n//2
    levels=sorted(set(abs(n-2*a) for a in grouped))
    meanrate={k:np.mean([v for a,vals in grouped.items() if abs(n-2*a)==k for v in vals]) for k in levels}
    assert all(meanrate[levels[j]] < meanrate[levels[j+1]]-1e-10 for j in range(len(levels)-1))
    best=sum(len(v) for a,v in grouped.items() if a in (mid,mid+1))
    assert best == 2*n*int(sp.eulerian(n-1,(n-3)//2)) if hasattr(sp,'eulerian') else best == (110 if n==5 else 4228)
    print(f'NUMERICAL_ALL_PERMUTATIONS_n={n}: {sp.factorial(n)} permutations, {len(levels)} strictly ranked classes; optimal_count={best} PASS')
print('ALL_TESTS_PASS')
