"""Exact algebraic consistency checks for a three-piece convex rectangle division.

Run: python3 verify.py
Requires SymPy >= 1.10. These checks supplement the analytic proof
of the lower bound, which is given in RESULT.md.
"""
import sympy as S
l = S.symbols('l', real=True, positive=True)
fv = 1 + (l*l - S.Rational(3,4))**2/(4*l*l)
gv = 1 + l*l/9
fh = l*l + (1-3*l*l/4)**2/4
gh = l*l + S.Rational(1,9)
root2 = (S.Integer(5) + 2*S.sqrt(13))/12
l0 = S.sqrt(root2)
checks = [
 (S.factor(fv-gv), (2*l-3)*(2*l+3)*(20*l*l-9)/(576*l*l)),
 (S.factor(fh-fv), 3*(l-1)*(l+1)*(3*l**4+11*l*l+3)/(64*l*l)),
 (S.factor(gh-fv), (432*l**4-296*l*l-81)/(576*l*l)),
 (S.factor(fv-l*l), -(48*l**4-40*l*l-9)/(64*l*l)),
 (S.factor(fv-(1+l*l/4)), -3*(8*l*l-3)/(64*l*l)),
 (S.factor(fv- (l*l+S.Rational(1,4))), S.factor(fv-l*l-S.Rational(1,4))),
 (S.simplify(fv.subs(l,1)), S.Rational(65,64)),
 (S.simplify(fv.subs(l,S.Rational(3,2))),S.Rational(5,4)),
 (S.simplify(gv.subs(l,S.Rational(3,2))),S.Rational(5,4)),
 (S.simplify(fv.subs(l,l0)-l0*l0),S.Integer(0)),
 (S.simplify(fh.subs(l,1)-fv.subs(l,1)),S.Integer(0)),
 (S.simplify(gh.subs(l,1)-fv.subs(l,1)),S.Rational(55,576)),
]
for i,(a,b) in enumerate(checks,1):
 assert S.simplify(a-b)==0, ('identity',i,a,b)
# Proof-sign certificates in the relevant ranges.
# fv-gv has sign l-3/2 because other factors are strictly positive for l>=1.
# fh-fv >=0 for l>=1 by the second factorization.
# gh-fv >0 for l>=1: numerator strictly increases and equals 55 at l=1.
# fv-l^2 <=0 iff l>=l0: 48*l^4-40*l^2-9 increases beyond l=1.
# For horizontal sides at 1<=l<=l0, 0 <= fv-l^2 <=1/64.
for p in [S.Rational(1),S.Rational(101,100),S.Rational(11,10),
          S.Rational(5,4),S.Rational(3,2),S.Rational(7,4),
          S.Rational(2),S.Rational(5),S.Rational(10)]:
 d2 = fv.subs(l,p) if p<=S.Rational(3,2) else gv.subs(l,p)
 assert d2 < p*p+S.Rational(1,4)
 assert d2 - 1 < p*p/4
 if p>= S.Rational(3,2): assert d2==gv.subs(l,p)
 else: assert d2==fv.subs(l,p)
 if p<=l0:
  assert 0<=d2-p*p<=S.Rational(1,64)
  assert d2<1+p*p/4
  assert fh.subs(l,p)>=d2
  assert gh.subs(l,p)>=d2
 elif p>l0:
  assert d2<p*p
# Exact equal-diameter construction in the first branch.
u = (l*l-S.Rational(3,4))/(2*l)
assert S.simplify(1+u*u-fv)==0
assert S.simplify((l-u)**2+S.Rational(1,4)-fv)==0
assert S.simplify(1+(l/3)**2-gv)==0
print('PASS:',len(checks),'symbolic identities, 9 branch checks, 3 construction identities')
print('switch ratio=3/2; horizontal long-side exclusion root=',S.N(l0,18))
