#!/usr/bin/env python3
"""Exact verification of the primitive period-three Hessian-cycle fields.
Requires SymPy (tested with 1.13+). No external services or input files.
"""
import sympy as S
x, z, w = S.symbols('x z w')
F1 = x**6 + 84*x**5 + 11040*x**4 - 47936*x**3 + 204288*x**2 - 33792*x + 4096
F2 = 19*x**6 + 912*x**5 + 18240*x**4 - 54272*x**3 + 47616*x**2 + 3072*x + 4096
F3 = (37*x**12 + 15540*x**11 + 2026416*x**10 - 30549568*x**9
      + 86526720*x**8 + 656409600*x**7 + 378470400*x**6
      - 4591042560*x**5 + 6717505536*x**4 - 4462477312*x**3
      + 1588592640*x**2 + 25165824*x + 16777216)
A = z**2 + 84*z + 10512
B = z**2 + 48*z + 1008
C = z**4 + 420*z**3 + 57456*z**2 + 174528*z + 269568

def h(v):
    return S.cancel((4-v)**3/(27*v**2))

# The equality of rational maps is exact in Q(x), not a numerical test.
t = x
for _ in range(3):
    t = h(t)
num, den = S.fraction(S.cancel(t-x))
expected = (x-1)*(7*x**2+4*x+16)*F1*F2*F3
assert S.rem(S.Poly(num,x,domain=S.QQ), S.Poly(expected,x,domain=S.QQ)).is_zero
assert S.degree(num,x) == S.degree(expected,x) == 27
assert S.gcd(S.Poly(num,x,domain=S.QQ),S.Poly(den,x,domain=S.QQ)).degree()==0
assert S.degree(F1,x)==6 and S.degree(F2,x)==6 and S.degree(F3,x)==12

# Rabin irreducibility test: polynomial over F_5 of degree n is irreducible
# iff x^(5^n)=x mod f and gcd(f, x^(5^(n/l))-x)=1 for l|n prime.
def irreducible_mod5(expr, var):
    p=5
    f=S.Poly(expr,var,modulus=p).monic()
    n=f.degree()
    y=S.Poly(var,var,modulus=p)
    for prime,_ in S.factorint(n).items():
        a=y
        for _ in range(n//prime):
            a=S.rem(a**5,f)
        if S.gcd(f,a-y).degree()!=0:
            return False
    a=y
    for _ in range(n):
        a=S.rem(a**5,f)
    return S.rem(a-y,f).is_zero

for expr, var in ((F1,x),(F2,x),(F3,x),(C,z)):
    assert irreducible_mod5(expr,var)
for f in (F1,F2,F3):
    assert f.subs(x,0)!=0 and f.subs(x,4)!=0

# For each periodic root alpha, compute alpha+h(alpha)+h^2(alpha)
# by exact inverses in Q[x]/(f). This verifies its cycle-sum polynomial.
for f, target in ((F1,A),(F2,B),(F3,C)):
    mod=S.Poly(f,x,domain=S.QQ)
    h1=S.rem(S.Poly((4-x)**3,x,domain=S.QQ)*
              S.invert(S.Poly(27*x*x,x,domain=S.QQ),mod),mod)
    numer=S.rem(S.Poly((4-x)**3,x,domain=S.QQ).compose(h1),mod)
    denom=S.rem(S.Poly(27*x*x,x,domain=S.QQ).compose(h1),mod)
    h2=S.rem(numer*S.invert(denom,mod),mod)
    tr=S.rem(S.Poly(x,x,domain=S.QQ)+h1+h2,mod)
    test=S.rem(S.Poly(target,z,domain=S.QQ).compose(tr),mod)
    assert test.is_zero, ('bad cycle sum',S.degree(f,x))

assert S.discriminant(A,z)==-3*108**2
assert S.discriminant(B,z)==-3*24**2
# The degree-four cycle field has D4 Galois closure:
assert S.factor(S.discriminant(C,z))==S.Integer(2)**24*S.Integer(3)**20*7**2*37*211**2
p=S.Poly(C,z,domain=S.QQ).monic()
a,b,c,d=p.all_coeffs()[1:]
res=S.factor(w**3-b*w**2+(a*c-4*d)*w+(4*b*d-a*a*d-c*c))
assert S.rem(S.Poly(res,w),S.Poly(w-288,w)).is_zero
factor7=S.factor_list(S.Poly(C,z,modulus=7),modulus=7)[1]
assert sorted(q.degree() for q,m in factor7 for _ in range(m))==[1,1,2]
# A quartic irreducible mod 5, a transposition mod 7 and a rational
# cubic-resolvent root imply D4 (not C4 or V4).
print('HESSIAN_PERIOD3_EIGHT_CYCLE_DESCENT_VERIFIED')
print('primitive point degrees: 6, 6, 12')
print('cycle field degrees: 2, 2, 4; first two Q(sqrt(-3)); last D4 closure')
