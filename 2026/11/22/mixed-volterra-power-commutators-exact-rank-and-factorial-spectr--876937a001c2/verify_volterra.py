"""Exact finite checks for mixed Volterra-adjoint commutator polynomial identities.

Requires Python 3 and SymPy. These finite checks supplement an analytical proof.
"""
from math import factorial, prod
import sympy as S

x, y, t = S.symbols('x y t')
checks = 0

def kernel(m, n):
    # The displayed formula is the true integral kernel on 0 < x < y < 1.
    a = S.integrate((x-t)**(m-1)*(y-t)**(n-1), (t, 0, x))
    b = S.integrate((t-x)**(n-1)*(t-y)**(m-1), (t, y, 1))
    return S.Poly(S.expand((a-b)/(factorial(m-1)*factorial(n-1))),x,y)

for m in range(1, 6):
    for n in range(1, 6):
        p = kernel(m,n)
        L=m+n-1
        # The reverse triangular piece on x>y must equal the same polynomial.
        a=S.integrate((x-t)**(m-1)*(y-t)**(n-1),(t,0,y))
        b=S.integrate((t-x)**(n-1)*(t-y)**(m-1),(t,x,1))
        q=S.Poly(S.expand((a-b)/(factorial(m-1)*factorial(n-1))),x,y)
        assert p==q, (m,n,'triangle')
        checks+=1
        assert p.total_degree() <= L
        checks+=1
        size=L+1
        coeff=S.Matrix([[p.coeff_monomial(x**i*y**j) for j in range(size)] for i in range(size)])
        assert coeff.rank() == 2*min(m,n), (m,n,'rank', coeff.rank())
        checks+=1
        if m<=n:
            supp=list(range(m))+list(range(n,L+1))
            for i in range(L+1):
                target=S.Rational((-1)**(m-1-i), factorial(i)*factorial(L-i)) if i<m else (S.Rational((-1)**(i-m),factorial(i)*factorial(L-i)) if i>=n else 0)
                assert p.coeff_monomial(x**i*y**(L-i))==target, (m,n,i,'top-degree coefficient')
                checks+=1
            minor=coeff.extract(supp,supp)
            assert minor.det()!=0, (m,n,'minor')
            checks+=1

for m in range(1,6):
    p=kernel(m,m); N=2*m
    A=S.Matrix([[p.coeff_monomial(x**i*y**j) for j in range(N)] for i in range(N)])
    H=S.Matrix([[S.Rational(1,i+j+1) for j in range(N)] for i in range(N)])
    T=A*H
    fac=prod(factorial(i) for i in range(N))
    fac_big=prod(factorial(i) for i in range(2*N))
    assert A.det()==S.Rational((-1)**m, fac**2)
    checks+=1
    assert T.det()==S.Rational((-1)**m*fac**2,fac_big)
    checks+=1
    assert S.expand(p.as_expr()-p.as_expr().subs({x:y,y:x},simultaneous=True))==0
    checks+=1
    assert S.expand(p.as_expr()+p.as_expr().subs({x:1-x,y:1-y},simultaneous=True))==0
    checks+=1
    cp=T.charpoly().as_expr()
    z=next(iter(T.charpoly().gens))
    assert S.expand(cp.subs(z,-z)-cp)==0
    checks+=1

print(f'VOL_TERRA_MIXED_EXACT_OK {checks} checks; 25 mixed pairs and five self-adjoint determinants')
