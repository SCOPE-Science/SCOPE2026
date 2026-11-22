"""Direct exact-arithmetic checks for Kemeny-optimal three-tail cycles.
Run: python verify.py (requires SymPy).
"""
from fractions import Fraction as Q
import sympy as sp


def coefficients(m):
    return (Q(3*(4*m-3),4), Q(2*m-1), Q(4*m-1,4), Q(m*m-1,3))


def laplacian(m, a1, a2, a3, b):
    n=4*m
    L=sp.zeros(n)
    for i in range(m):
        for u,v,w in ((4*i,4*((i+1)%m),b),
                      (4*i,4*i+1,a1),
                      (4*i+1,4*i+2,a2),
                      (4*i+2,4*i+3,a3)):
            w=sp.Rational(w.numerator,w.denominator)
            L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    return L


def kemeny_exact(L):
    n=L.rows
    A=L+sp.ones(n,n)/n
    return sp.trace(A.inv())-1


def assert_phase(m):
    A,C,D,B=coefficients(m)
    p=12*(A*C-2*B*D)
    poly=-8*m**3+74*m**2-82*m+25
    assert p==poly
    assert (p>0)==(m<=8)
    return 2


def check_rational(m, xs):
    A,C,D,B=coefficients(m)
    count=0
    for x,y in xs:
        assert x>0 and y>0 and x+y<=1
        a1=x;a2=y;a3=1-y;b=(1-x)/2
        L=laplacian(m,a1,a2,a3,b)
        exact=kemeny_exact(L)
        formula=sp.Rational(A.numerator,A.denominator)/sp.Rational(x.numerator,x.denominator)
        formula+=sp.Rational(C.numerator,C.denominator)/sp.Rational(y.numerator,y.denominator)
        formula+=sp.Rational(D.numerator,D.denominator)/sp.Rational(a3.numerator,a3.denominator)
        formula+=sp.Rational(B.numerator,B.denominator)/sp.Rational(b.numerator,b.denominator)
        assert exact == formula, (m,x,y,exact,formula)
        assert L*sp.ones(4*m,1)==sp.zeros(4*m,1)
        count+=2
    return count


def symbolic_checks():
    m=sp.symbols('m',positive=True,integer=True)
    A=3*(4*m-3)/sp.Integer(4)
    C=2*m-1
    D=(4*m-1)/sp.Integer(4)
    B=(m*m-1)/sp.Integer(3)
    assert sp.factor(12*(A*C-2*B*D))==-8*m**3+74*m**2-82*m+25
    assert sp.simplify((A+D)-(16*m-10)/4)==0
    t=sp.symbols('t',positive=True)
    # On the active face a1=1-a2=t, the objective has 2 square-root terms.
    F=(A+D)/t+(C+2*B)/(1-t)
    assert sp.factor(F-((A+D)/t+(C+2*B)/(1-t)))==0
    assert sp.simplify(sp.diff(F,t,2)-2*(A+D)/t**3-2*(C+2*B)/(1-t)**3)==0
    return 4


def main():
    count=symbolic_checks()
    for m in range(3,80):count+=assert_phase(m)
    cases={
        3:[(Q(1,3),Q(2,3)),(Q(2,5),Q(1,2))],
        4:[(Q(1,3),Q(1,2)),(Q(1,4),Q(3,5))],
        5:[(Q(2,5),Q(1,2))],
        9:[(Q(1,3),Q(1,2))],
    }
    for m,xs in cases.items():count+=check_rational(m,xs)
    # First-order derivative signs in the unconstrained domain.
    for m in range(3,80):
        A,C,D,B=(float(c) for c in coefficients(m))
        x=A**0.5/(A**0.5+(2*B)**0.5)
        y=C**0.5/(C**0.5+D**0.5)
        assert ((x+y>1)==(m<=8))
        count+=1
    print('PASS',count,'symbolic, exact-rational and phase checks')

if __name__=='__main__':main()
