"""Exact algebraic certificate for a degree-five ellipse minimax threshold.

Requires SymPy. Run: python3 check.py
"""
import sympy as sp
A,h,v=sp.symbols('A h v',real=True)
sq=sp.sqrt(5)
T=lambda k,z:sp.chebyshevt(k,z)
Q=2*sp.prod(T(k,A) for k in range(1,6))
P=256*v**4+(128-64*sq)*v**3-(104+88*sq)*v**2-(56+32*sq)*v-(5+3*sq)
certified_coefficients=0
for ell in range(1,6):
    expr=(-1)**ell*(sp.Rational(1,2)*(1+(-1)**ell*T(5,A+h)/T(5,A))
      +sum(T(k,A+h)*sp.cos(sp.pi*k*ell/5)/T(k,A) for k in range(1,5)))
    numerator=sp.Poly(sp.cancel(Q*expr).expand(),h)
    assert numerator.nth(0)==0
    for j in range(1,6):
        coefficient=sp.Poly(sp.expand(numerator.nth(j)),A)
        parity={e[0]%2 for e,cf in coefficient.terms()}
        assert len(parity)==1
        parity=next(iter(parity))
        shifted=sp.Poly(sp.expand(sum(cf*(1+v)**((e[0]-parity)//2)
                        for e,cf in coefficient.terms())),v)
        if ell==2 and j==1:
            assert sp.expand(shifted.as_expr()-(1-sq)*(1+v)**2*P)==0
            continue
        for cf in shifted.all_coeffs():
            b=sp.expand(cf).coeff(sq)
            a=sp.expand(cf)-b*sq
            assert a.is_Rational and b.is_Rational
            # 2 < sqrt(5) < 9/4 give positive exact rational lower bound.
            lower=a+b*(sp.Rational(9,4) if b<0 else sp.Rational(2))
            assert lower>0,(ell,j,cf,lower)
            certified_coefficients+=1
assert sp.Poly(P,v).degree()==4
p=sp.Poly(P,v)
coeffs=list(reversed(p.all_coeffs()))
assert all(sp.N(x)<0 for x in coeffs[:4])
assert 128-64*sq<0 and p.LC()==256
assert P.subs(v,1)<0 and P.subs(v,2)>0
print('ELLIPSE_DEGREE5_THRESHOLD_PASS', 'strict_positivity_coefficients='+str(certified_coefficients), 'exceptional_quartic=PASS', 'unique_positive_root=PASS')
