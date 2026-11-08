"""Exact symbolic checks for two postcritically finite M-map parameters.

Run: python checker.py (requires sympy).
The proof of the infinite lap-count identity is in RESULT.md; these checks
verify its finite algebraic inputs, not substitute for the induction.
"""
from sympy import symbols, Matrix, factor, Rational, Poly, simplify

p,z=symbols('p z')
F_left=4*p**3-4*p+1
F_right=4*p**3-4*p**2+4*p-1
h=(4*p-1)/(4*p**2)
assert simplify(h-p+F_left/(4*p**2))==0
assert simplify(h-(1-p)-F_right/(4*p**2))==0
assert Poly(F_left,p).count_roots(Rational(269,1000),Rational(270,1000))==1
assert Poly(F_right,p).count_roots(Rational(319,1000),Rational(320,1000))==1
assert F_left.subs(p,Rational(1,4))>0 and F_left.subs(p,Rational(1,2))<0
assert F_right.subs(p,Rational(1,4))<0 and F_right.subs(p,Rational(1,2))>0
# The only positive roots in (1/4,1/2); derivatives are signed throughout.
assert simplify(F_left.diff(p)-4*(3*p*p-1))==0
assert simplify(F_right.diff(p)-4*(3*p*p-2*p+1))==0
A_left=Matrix([[1,1,1,1],[0,1,1,1],[0,1,1,1],[1,1,1,1]])
A_right=Matrix([[1,1,1,1],[0,0,0,1],[0,0,0,1],[1,1,1,1]])
assert simplify(A_left.charpoly(z).as_expr()-z*z*(z*z-4*z+2))==0
assert simplify(A_right.charpoly(z).as_expr()-z*z*(z*z-2*z-2))==0
ones=Matrix([1]*4)
for A,seed,aa,bb in [(A_left,[4,14],4,-2),(A_right,[4,10],2,2)]:
 vals=[]
 for n in range(1,12):
  vals.append(int((ones.T*A**(n-1)*ones)[0]))
 assert vals[:2]==seed
 assert all(vals[i+2]==aa*vals[i+1]+bb*vals[i] for i in range(len(vals)-2))
 print('lap_counts:',vals)
print('MMAP_CRITICAL_RESONANCE_EXACT_IDENTITIES_OK')
