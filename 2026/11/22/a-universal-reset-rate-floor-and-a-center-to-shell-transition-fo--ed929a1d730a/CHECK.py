"""Independent algebraic checks of Pearson-VII reset-source feasibility.

Requires Python 3 and SymPy. Checks cannot replace the all-parameter proof.
"""
import sympy as S

u,d,k,D,a,t,lam,r=S.symbols('u d k D a t lam r', positive=True)
s=S.symbols('s',real=True)
# Target p(x) proportional to (1+t)^(-u), t=|x|^2/a^2.
# L^*p/p divided by k is computed without assuming the result.
ratio=S.factor(d-2*u*t/(1+t) + D/(k*a*a)*(-2*u*d/(1+t)+4*u*(u+1)*t/(1+t)**2))
f=S.factor(ratio.subs(D,lam*k*a*a).subs(t,1/s-1))
f_expected=d-2*u+2*u*(1+lam*(2*u+2-d))*s-4*lam*u*(u+1)*s*s
assert S.simplify(f-f_expected)==0
lam_c=1/(2*u+d+2)
b=2*u+2-d
sv=(1+lam*b)/(4*lam*(u+1))
assert S.simplify(S.diff(f,s).subs(s,sv))==0
assert S.simplify(f.subs(s,1)-d*(1-2*u*lam))==0
fvertex=S.factor(f.subs(s,sv))
assert S.simplify(fvertex-(d-2*u+u*(1+lam*b)**2/(4*lam*(u+1))))==0
assert S.simplify((sv-1).subs(lam,lam_c))==0
assert S.simplify((fvertex-f.subs(s,1)).subs(lam,lam_c))==0
# Normalization using the exact beta law S~Beta(u-d/2,d/2).
ES=(u-d/2)/u
ES2=(u-d/2)*(u-d/2+1)/(u*(u+1))
assert S.simplify(f_expected.subs(s,0)+2*u*(1+lam*b)*ES-4*lam*u*(u+1)*ES2)==0
# Global reset-rate minimum, unique critical shape and universal zero-shell radius.
lam_opt=1/b
fopt=S.factor(fvertex.subs(lam,lam_opt))
assert S.simplify(fopt-d/(u+1))==0
assert S.simplify(sv.subs(lam,lam_opt)-b/(2*(u+1)))==0
assert S.simplify(((1/sv-1)/lam).subs(lam,lam_opt)-d)==0
assert S.simplify(S.diff(fvertex,lam)-u*(b*b-1/lam**2)/(4*(u+1)))==0
# At critical lam_c, q/p is proportional to (1-s)^2, i.e., quartic at origin.
assert S.factor(fvertex.subs(lam,lam_c)-f.subs(lam,lam_c)) == S.factor(4*lam_c*u*(u+1)*(s-1)**2)
# Exact rational representative probes, including candidate source positivity.
checks=0
for di in [1,2,3,5,8]:
 for ui in [S.Rational(di,2)+S.Rational(1,3),S.Rational(di,2)+S.Rational(3,2),di+2]:
  lc=S.factor(lam_c.subs({d:di,u:ui}))
  for li in [lc/3,lc,lc*2,1/b.subs({d:di,u:ui}),S.Rational(5,2)]:
   expr=S.factor(f.subs({d:di,u:ui,lam:li}))
   vtx=S.factor(sv.subs({d:di,u:ui,lam:li}))
   top=S.factor(expr.subs(s,1) if li<=lc else expr.subs(s,vtx))
   assert top>0
   assert S.simplify(top - S.Rational(di,ui+1))>=0
   for j in range(25):
    si=S.Rational(j,24)
    assert S.simplify(top-expr.subs(s,si))>=0
    checks+=1
print('PASS: independent differentiation, normalization, global minimum, critical zeros and',checks,'exact-rational radial tests')
