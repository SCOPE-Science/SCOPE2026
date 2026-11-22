"""Symbolic algebra checks of three-energy crossover and critical bounds.

Requires SymPy; run ``python symbolic_check.py``.
"""
import sympy as s
r,a,b,c = s.symbols('r a b c', positive=True)
f = lambda x: r/(r+x)
K=f(a+b+c)-f(a+b)*f(c)-f(a+c)*f(b)-f(b+c)*f(a)+2*f(a)*f(b)*f(c)
p=a+b+c
e2=a*b+a*c+b*c
e3=a*b*c
D=(r+a)*(r+b)*(r+c)*(r+a+b)*(r+a+c)*(r+b+c)*(r+p)
assert s.factor(K*D+a*b*c*r*(2*r**3+2*p*r**2-p*e2+e3))==0
assert s.factor(K.subs({b:a,c:a})-2*(r/a)*(1-r/a)/((r/a+1)**3*(r/a+2)*(r/a+3)))==0
m,x,y=s.symbols('m x y', positive=True)
a1,b1,c1=m,m+x,m+y
Q=(a1+b1+c1)*(a1*b1+a1*c1+b1*c1)-a1*b1*c1
bound=6*m*m*(x+y)+2*m*(x*x+3*x*y+y*y)+x*y*(x+y)
assert s.expand(Q-2*(a1+b1+c1)*m*m-2*m**3-bound)==0
# At fixed sum, smoothing a pair increases the threshold-defining cubic constant.
t,d=s.symbols('t d',positive=True)
# fixed third coordinate c, rates (a,b) with sum t and product d
assert s.expand((t+c)*(d+t*c)-c*d -(t*d+t*c*(t+c)))==0
print('PASS: 4 symbolic identities')
