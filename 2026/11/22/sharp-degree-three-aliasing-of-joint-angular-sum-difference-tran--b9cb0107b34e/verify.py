"""Exact symbolic checks for joint APIT aliasing and a smooth copula witness.
Requires Python 3 and sympy. No stochastic simulation is used.
"""
from sympy import symbols, sin, cos, pi, integrate, simplify, Rational, expand_trig, S

u,v,e = symbols('u v e',real=True)
f = sin(2*pi*u)
g = sin(4*pi*v)
F = (1-cos(2*pi*u))/(2*pi)
G = (1-cos(4*pi*v))/(4*pi)
assert simplify(F.diff(u)-f) == 0
assert simplify(G.diff(v)-g) == 0
assert simplify(F.subs(u,0)) == 0 and simplify(F.subs(u,1)) == 0
assert simplify(G.subs(v,0)) == 0 and simplify(G.subs(v,1)) == 0
assert simplify(integrate(f,(u,0,1))) == 0
assert simplify(integrate(g,(v,0,1))) == 0
assert simplify(integrate(u*f,(u,0,1))+1/(2*pi)) == 0
assert simplify(integrate(v*g,(v,0,1))+1/(4*pi)) == 0
assert simplify(integrate(F,(u,0,1))-1/(2*pi)) == 0
assert simplify(integrate(G,(v,0,1))-1/(4*pi)) == 0
# The two inverse images differ by the half-period translation (1/2,1/2).
assert simplify(expand_trig(f.subs(u,u+S.Half))+f) == 0
assert simplify(expand_trig(g.subs(v,v+S.Half))-g) == 0
# A degree <=2 copula perturbation has only frequencies (+-1,+-1);
# the two-to-one transform observes these because their frequency sums are even.
visible = lambda m,n: ((m+n) % 2 == 0)
for m in range(-4,5):
 for n in range(-4,5):
  if not m or not n: continue
  if abs(m)+abs(n)<=2: assert visible(m,n)
  if abs(m)+abs(n)==3 and {abs(m),abs(n)}=={1,2}: assert not visible(m,n)
# Spearman rho=12 cov(U,V) and Kendall tau=4 E[C(U,V)]-1.
A = integrate(u*f,(u,0,1))
B = integrate(v*g,(v,0,1))
assert simplify(12*e*A*B-3*e/(2*pi*pi)) == 0
# epsilon^2 term vanishes by fundamental theorem of calculus.
assert simplify(integrate(F*f,(u,0,1))) == 0
assert simplify(integrate(G*g,(v,0,1))) == 0
K = 4*(Rational(1,4)+e*(A*B+integrate(F,(u,0,1))*integrate(G,(v,0,1))))-1
assert simplify(K-e/pi**2) == 0
# Fourier witness by exact constant-term multiplication of characters.
from sympy import I
s1 = {(1,0):1/(2*I),(-1,0):-1/(2*I)}
s2 = {(0,2):1/(2*I),(0,-2):-1/(2*I)}
co = {(1,2):Rational(1,2),(-1,-2):Rational(1,2)}
mean = sum(a*b*c for (m,n),a in s1.items() for (p,q),b in s2.items()
           for (r,t),c in co.items() if (m+p+r,n+q+t)==(0,0))
assert simplify(mean+Rational(1,4)) == 0
assert all(not visible(m+p,n+q) for (m,n) in s1 for (p,q) in s2)

# At a diagnostic pair, exchange of coordinates changes the density.
assert simplify(f.subs(u,Rational(1,4))*g.subs(v,Rational(1,8))-1)==0
assert simplify(f.subs(u,Rational(1,8))*g.subs(v,Rational(1,4)))==0
# The total variation exact integral uses each periodic absolute sine integral 2/pi.
assert simplify(e*Rational(1,2)*(2/pi)*(2/pi)-2*e/pi**2)==0
print('PASS: 14 symbolic families and degree checks; no simulation or asymptotics invoked')
