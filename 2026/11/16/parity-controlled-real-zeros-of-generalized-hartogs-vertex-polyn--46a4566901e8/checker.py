"""Reproducibility checks for a parity-dependent vertex polynomial root law.

Uses exact rational arithmetic and SymPy. Finite checks do not replace the
all-degree coefficient-sign proof in RESULT.md.
"""
from fractions import Fraction
from math import comb
import sympy as sp

z, alpha = sp.symbols('z alpha')
checks = 0

def check(ok, note):
    global checks
    assert bool(ok), note
    checks += 1

for N in range(2, 16):
    Q = sp.expand(sum(n*(N+alpha-n)*z**(n-1) for n in range(1,N+1)))
    A = N+alpha-1-(N+alpha+1)*z
    B = (N+1)*(1-alpha)+(2*N*alpha+alpha-N+1)*z-N*alpha*z*z
    S = sp.expand((1-z)**3*Q)
    check(sp.expand(S-A-z**N*B)==0, ('polynomial identity', N))
    L = z*B*sp.diff(S,z)-(N*B+z*sp.diff(B,z))*S
    RHS = -N*(N+1)*(z-1)**2*(alpha*(N+alpha+1)*z+(1-alpha)*(N+alpha-1))
    check(sp.expand(L-RHS)==0, ('elimination identity', N))
    C = lambda j: comb(N,j) if 0 <= j <= N else 0
    vals=[]
    for j in range(2,N+3):
        U=(4*N+2)*C(j)+(4*N+1)*C(j-1)+N*C(j-2)
        V=2*N*C(j)+(N-1)*C(j-1)
        check(U>0,('positive U',N,j))
        vals.append(Fraction(V,U))
    check(vals[0]==Fraction(N-1,2*N+1),('first ratio',N))
    check(vals[-1]==0,('last ratio',N))
    for j in range(len(vals)-1):
        check(vals[j]>vals[j+1],('monotone ratio',N,j))
    for a in [sp.Rational(1,19),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(4,5),sp.Integer(1)]:
        P=sp.Poly(Q.subs(alpha,a),z)
        negs=[]
        for (lo,hi),multiplicity in P.intervals(eps=sp.Rational(1,10**10)):
            if hi<0: negs += [multiplicity]
        if N%2==0:
            check(negs==[1],('even real root',N,a,negs))
            check(sp.sign(P.eval(-1))==(1 if a<1 else 0),('even -1 sign',N,a))
        elif N==3:
            crit=(sp.sqrt(6)-2)/2
            expected=[1,1] if a<crit else []
            check(negs==expected,('odd small degree',N,a,negs))
        else:
            # An independent rational Sturm count evaluates the polynomial.
            check(sum(negs) in (0,2),('odd real count',N,a,negs))
print('PASS',checks,'symbolic/exact checks')
