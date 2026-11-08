"""Exact symbolic checks for the inflection divisor of symmetric Kummer-conic curves.
Run: python verify_flex.py (requires SymPy)."""
import sympy as sp
x,y,z,X,Y,Z,n=sp.symbols('x y z X Y Z n')
q=X**2+Y**2+Z**2+X*Y+X*Z+Y*Z
v=(X,Y,Z)
e1=X+Y+Z
e2=X*Y+Y*Z+Z*X
e3=X*Y*Z
M=sp.Matrix([[(n-1)*sp.diff(q,a)*int(i==j) + n*a*sp.diff(q,a,b) for j,b in enumerate(v)] for i,a in enumerate(v)])
R=sp.expand(M.det())
A=2*(n-1)**2*(2*n-1)
B=(n-1)*(2*n-1)*(4*n-1)
C=(2*n-1)**2*(5*n-1)
assert sp.expand(R - (A*e1**3+B*e1*e2+C*e3))==0
assert sp.expand(q-(e1**2-e2))==0
assert sp.factor(A+B-3*(n-1)*(2*n-1)**2)==0
T=-3*(n-1)/(5*n-1)
t=sp.symbols('t')
assert sp.factor(sp.discriminant(t**3-t**2+t-T,t)+48*(11*n**2-16*n+6)/(5*n-1)**2)==0
assert sp.det(sp.hessian(q,v)) == 4
assert sp.discriminant(t**2+t+1,t)==-3
for nn in [3,4,5]:
    F=x**(2*nn)+y**(2*nn)+z**(2*nn)+x**nn*y**nn+x**nn*z**nn+y**nn*z**nn
    Hv=sp.hessian(F,(x,y,z)).det()
    residual=sp.expand(R.subs({n:nn,X:x**nn,Y:y**nn,Z:z**nn}))
    assert sp.expand(Hv-nn**3*(x*y*z)**(nn-2)*residual)==0
    print('HESSIAN_IDENTITY',nn,'PASS')
for nn in [3,4,5,6,10,20]:
    tt=sp.Rational(-3*(nn-1),5*nn-1)
    roots_poly=t**3-t**2+t-tt
    assert sp.gcd(roots_poly,sp.diff(roots_poly,t))==1
    assert tt!=0
    print('SIX_SIMPLE_BASE_POINTS',nn,'PASS')
print('SYMBOLIC_COEFFICIENT_IDENTITY: PASS')
print('UNIFORM_DISCRIMINANT_IDENTITY: PASS')
print('SMOOTH_BASE_CONIC_AND_AXIS_TRANSVERSALITY: PASS')
print('ALL_CHECKS_PASSED')
