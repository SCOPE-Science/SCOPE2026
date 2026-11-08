"""Exact symbolic checks of a three-phase feedback absorption-time theorem.

Requires sympy. Run: python verify.py
"""
import sympy as s

p,q,x,y,t = s.symbols('p q x y t', real=True)
t = 1+q
A=t-x
B=t**2-2*t*x+y
C=t**3-3*t**2*x+t*(x**2+2*y)
P=s.expand(10*A*C-9*B**2)
coeff=[s.expand(P).coeff(q,j) for j in range(5)]
assert s.simplify(coeff[0]-(1-4*x+4*x**2-10*x**3+2*y+16*x*y-9*y**2))==0
assert s.simplify(coeff[1]-2*(2-6*x+4*x**2-5*x**3+(8*x+2)*y))==0
assert s.simplify(coeff[2]-2*(3-6*x+2*x**2+y))==0
assert s.simplify(coeff[3]-4*(1-x))==0
assert coeff[4]==1
assert s.simplify(coeff[0].subs(y,(4*x-1)/9)-s.Rational(2,3)*(1-3*x)*(5*x**2-3*x+1))==0

a=s.symbols('a')
def ratio(aa,prob):
    e1=sum(aa)
    e2=aa[0]*aa[1]+aa[0]*aa[2]+aa[1]*aa[2]
    e3=s.prod(aa)
    r=1-prob
    a2=e1**2-r*e2
    a3=e1**3-2*r*e1*e2+r**2*e3
    a4=e1**4-3*r*e1**2*e2+r**2*(e2**2+2*e1*e3)
    return s.factor(s.Rational(4,3)*a2*a4/a3**2)

Re=ratio([1,1,1],p)
Rb=ratio([1,1,0],p)
assert s.simplify(Re-12*(p+2)*(5*p**2+17*p+5)/(p**2+16*p+10)**2)==0
assert s.simplify(Rb-(p+3)*(p**2+10*p+5)/(12*(p+1)**2))==0
Q=p**4+48*p**3+148*p**2+16*p-60
assert s.simplify(Re-Rb-(1-p)**3*Q/(12*(p+1)**2*(p**2+16*p+10)**2))==0
assert Q.subs(p,0)<0 and Q.subs(p,1)>0
assert s.simplify(s.diff(Q,p)-(4*p**3+144*p**2+296*p+16))==0
assert Q.subs(p,s.Rational(5425,10000))<0<Q.subs(p,s.Rational(5426,10000))

pert=ratio([1+a,1-a,1],p)
curvature=s.factor(s.diff(pert,a,2).subs(a,0)/2)
expected=4*(1-p)**3*(50-10*p-13*p**2)/(p**2+16*p+10)**3
assert s.simplify(curvature-expected)==0
example=s.factor(Re.subs(p,s.Rational(5,8))-ratio([1,1,s.Rational(1,16)],s.Rational(5,8)))
assert example==s.Rational(8340,345550921) and example>0

# Exact rational sample tests supplement, but do not replace, the infinite proof.
for i in range(1,31):
    aa=[s.Rational(i+1,7),s.Rational(2*i+1,19),s.Rational(3*i+2,11)]
    prob=s.Rational(i-1,31)
    assert ratio(aa,prob)>=s.Rational(6,5)
print('PASS: symbolic polynomial, Schur-bound substitution, local Hessian, critical polynomial, exact witness and 30 rational samples')
