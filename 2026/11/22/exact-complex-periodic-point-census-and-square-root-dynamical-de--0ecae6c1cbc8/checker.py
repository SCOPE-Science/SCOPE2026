"""Reproduce finite algebraic checks for the polynomial delay map.

The analytic proof of all-period claims is in RESULT.md; finite tests are not a substitute.
"""
import sympy as s

u, v = s.symbols('u v')
a=s.Rational(1,3)
c=s.Integer(2)
p=[u,v]
for n in range(2,9):
    p.append(s.expand(a*p[n-1]+c*p[n-2]*(1-p[n-2])))

for n in range(1,8):
    d=max(s.Poly(p[n],u,v).total_degree(),s.Poly(p[n+1],u,v).total_degree())
    assert d==2**((n+1)//2),(n,d)

for n in range(1,8):
    left=s.Poly(p[n]-u,u,v)
    right=s.Poly(p[n+1]-v,u,v)
    dn=left.total_degree()
    en=right.total_degree()
    lead1=sum(coeff*u**exps[0]*v**exps[1] for exps,coeff in left.terms() if sum(exps)==dn)
    lead2=sum(coeff*u**exps[0]*v**exps[1] for exps,coeff in right.terms() if sum(exps)==en)
    if n%2==0:
        assert lead1.subs(v,0)!=0 and lead1.subs(u,0)==0
        assert lead2.subs(u,0)!=0
    else:
        assert lead2.subs(v,0)!=0 and lead2.subs(u,0)==0
        assert lead1.subs(u,0)!=0
    assert dn*en==2**n
    print(f'n={n}: degrees=({dn},{en}), Bezout product={dn*en}')

z=s.symbols('z')
f=z
for k in range(1,7):
    f=s.Poly(4*f*(1-f),z).as_expr()
    fixed=s.Poly(f-z,z)
    assert fixed.degree()==2**k
    assert s.gcd(fixed,fixed.diff()).degree()==0
    print(f'logistic witness k={k}: {fixed.degree()} distinct simple roots')
print('FINITE ALGEBRAIC CHECKS PASSED')
