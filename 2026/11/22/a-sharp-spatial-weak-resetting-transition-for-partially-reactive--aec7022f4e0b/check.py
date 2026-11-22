"""Exact polynomial and independent event-based checks for finite-interval persistent search."""
from math import comb
import sympy as sp

s, c, x, y = sp.symbols('s c x y', positive=True)
check_count=0

def verify(expr):
    global check_count
    assert sp.cancel(sp.together(expr)) == 0, sp.factor(expr)
    check_count+=1

# The time unit is the inverse tumble rate, and the spatial unit is half the interval.
g=s*(1-x)+sp.Rational(1,2)
f=sp.expand(c*(s+sp.Rational(1,2))+sp.integrate(2*s*g,(x,0,x)))
G_end=1+f.subs(x,1)-g.subs(x,1)
G=sp.expand(G_end+2*s*sp.integrate(f.subs(x,y),(y,x,1)))
F=sp.expand(c*G.subs(x,0)+2*s*sp.integrate(G-g,(x,0,x)))
Delta=sp.expand(F-2*f*f)
verify(sp.diff(g,x)+s)
verify(sp.diff(f,x)-2*s*g)
verify(g.subs(x,1)-sp.Rational(1,2))
verify(f.subs(x,0)-c*g.subs(x,0))
verify(sp.diff(G,x)+2*s*f)
verify(sp.diff(F,x)-2*s*(G-g))
verify(G.subs(x,1)-1-f.subs(x,1)+g.subs(x,1))
verify(F.subs(x,0)-c*G.subs(x,0))
verify(Delta.subs(x,1)-(c*(3-6*s*s-4*s**3)-(6*s*s+4*s**3+2*s**4))/6)
verify(Delta.subs(x,0)-c*(8*s**3+12*s*s+6*s+3)/6)
coefs=[sp.expand(Delta).coeff(x,k) for k in range(5)]
b=[sp.expand(sum(coefs[k]*sp.Rational(comb(j,k),comb(4,k)) for k in range(j+1))) for j in range(5)]
verify(b[0]-c*(8*s**3+12*s*s+6*s+3)/6)
verify(b[1]-(4*c*s**3+12*c*s*s+9*c*s+6*c+8*s**4+12*s**3)/12)
verify(b[1]-b[2]-s*(8*c*s*s+10*c*s+3*c+8*s**3+4*s*s+2*s)/12)
verify(b[2]-b[3]-s*(2*s+1)*(2*c*s+3*c+2*s*s+4*s)/12)
verify(b[3]-b[4]-s*(2*c*s+c+2*s*s+2*s)/4)
verify(Delta-sum(comb(4,j)*b[j]*x**j*(1-x)**(4-j) for j in range(5)))
# Direct comparison with the independently derived uniform-start moments:
mbar=sp.integrate(f,(x,0,1))
Fbar=sp.integrate(F,(x,0,1))
verify(Fbar-2*mbar*mbar-(c*(30*s*s+45*s+45)+(16*s**4+45*s**3-15*s*s))/90)
# Independent published uniform-start variance (Jeon-Go-Kim, arXiv:2310.04016, Eq. 113).
n=(c-1)/2
paper_var=(sp.Rational(3,4)+2*s+sp.Rational(37,12)*s*s+
           sp.Rational(5,2)*s**3+sp.Rational(28,45)*s**4+
           n*(1+2*s+4*s*s+sp.Rational(8,3)*s**3)+
           n*(n+1)*(1+2*s)**2)
verify(Fbar-mbar*mbar-paper_var)
# The sign of the weak-reset coefficient is the negative sign of Delta.
from scipy.optimize import brentq
import math
P=lambda t:3-6*t*t-4*t**3
Q=lambda t:6*t*t+4*t**3+2*t**4
s0=brentq(P,.1,1)
sinf=brentq(lambda t:P(t)-Q(t),.1,1)
assert .59<s0<.60 and .43<sinf<.44
check_count+=1
for k in [.01,.1,.4,1,4,15,100]:
    def v(t):return P(t)/math.tanh(k*t/2)-Q(t)
    root=brentq(v,sinf,s0,xtol=1e-14)
    assert sinf<root<s0
    assert v(root-1e-5)>0 and v(root+1e-5)<0
    check_count+=3
    for t in [root*.7,root*1.05,root*1.5]:
        cc=1/math.tanh(k*t/2)
        poly=sp.Poly(Delta.subs({s:t,c:cc}),x)
        import numpy as np
        roots=[z.real for z in np.roots([float(z) for z in poly.all_coeffs()]) if abs(z.imag)<1e-6 and 0<z.real<1]
        if t<root: assert len(roots)==0
        else: assert len(roots)==1
        check_count+=1
print('passed',check_count,'symbolic/independent polynomial checks')
print('s_unreactive_limit',float(s0),'s_perfect_limit',float(sinf))
print('k1',brentq(lambda t:P(t)/math.tanh(t/2)-Q(t),sinf,s0))
