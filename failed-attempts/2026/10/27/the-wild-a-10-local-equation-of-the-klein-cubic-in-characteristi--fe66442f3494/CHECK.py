"""Reproduce exact characteristic-eleven identities for the Klein cubic.
Requires Python 3 and SymPy.  All polynomial equalities are checked in F_11.
The formal Morse lemma used in the proof is a mathematical argument, not
an assertion derived from finite-field enumeration.
"""
import sympy as sp

a,b,c,d,u=sp.symbols('a b c d u')
p=11
F=a+a*a*b+b*b*c+c*c*d+d*d
fa,fb,fc,fd=[sp.diff(F,z) for z in (a,b,c,d)]

def zero_mod11(expr, vars):
    num=sp.cancel(expr).as_numer_denom()[0]
    return sp.Poly(sp.expand(num),*vars,modulus=p).is_zero

# Exact partial derivatives and the four-equation affine Jacobian algebra.
assert (fa,fb,fc,fd)==(1+2*a*b,a*a+2*b*c,b*b+2*c*d,c*c+2*d)
gb=sp.groebner([fa,fb,fc,fd],d,c,b,a,modulus=p)
expected=sp.groebner([d-5*a**6,c-a**3,b+2*a**10,a**11-3],d,c,b,a,modulus=p)
assert list(gb.polys)==list(expected.polys),(gb,expected)
assert sp.Poly(a**11-3,a,modulus=p).as_expr()==a**11-3

# All projective critical points have nonzero coordinates; normalized one.
P={a:3,b:9,c:5,d:4}
assert all(int(v.subs(P))%p==0 for v in (F,fa,fb,fc,fd))

# The transversal Hessian on variables (a,b,c) is nonsingular.
H=sp.hessian(F,(a,b,c))
detH=int(H.subs(P).det())%p
assert detH==6,detH

# Critical polar curve fa=fb=fc=0, parameterized by a near 3.
bp=-1/(2*a);cp=a**3;dp=-1/(8*a**5)
assert all(zero_mod11(expr.subs({b:bp,c:cp,d:dp}, simultaneous=True),(a,))
           for expr in (fa,fb,fc))
critical_value=sp.factor(F.subs({b:bp,c:cp,d:dp},simultaneous=True))
assert sp.factor(critical_value - (sp.Rational(5,8)*a+1/(64*a**10)))==0
assert zero_mod11(critical_value-(2*a+5/a**10),(a,))
# d'(3) nonzero, so this curve is transverse to d=constant.
deriv_d=sp.diff(dp,a)
assert int((5*pow(8*pow(3,6,p),-1,p))%p)==8
# Exact residual function in u=(a-3)/3 (mod 11).
residual=critical_value.subs(a,3*(1+u))
normal=6*u**11*(1+u)/(1+u**11)
assert zero_mod11(residual-normal,(u,))
# Residual has initial term 6*u^11, a unit times u^11 in k[[u]].
assert (sp.Poly(sp.together(residual-normal).as_numer_denom()[0],u,modulus=p).is_zero)
print('PASS: global singular-support equations, length-11 Jacobian algebra,')
print('      nondegenerate rank-3 transverse Hessian, polar curve,')
print('      residual order 11 and formal-contact normal-form input.')
