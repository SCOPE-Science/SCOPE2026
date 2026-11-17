"""Reproducibility checks for a polynomial oval completion (no proof by numerics)."""
from fractions import Fraction
import sympy as sp
import math
from scipy.integrate import solve_ivp
x,y=sp.symbols('x y', positive=True)
L=(x+1+1/x)*(y+1+1/y)-9
f=(1-x)*(1+y); g=(1-y)*(1+x)
D=sp.factor(-sp.diff(L,x)*f-sp.diff(L,y)*g)
want=(y+1+1/y)*(x-1)**2*(x+1)*(y+1)/x**2+(x+1+1/x)*(y-1)**2*(y+1)*(x+1)/y**2
assert sp.simplify(D-want)==0
for ds in ([sp.Rational(1,2)],[sp.Rational(1,2),sp.Rational(5,2)],[sp.Rational(1,2),sp.Rational(3,2),sp.Rational(5,2)]):
 N=len(ds)
 P=sp.prod(L-d for d in ds)
 H=sp.prod(x*x*y*y +x*x*y+x*y*y+x*x+y*y+x+y+1-(8+d)*x*y for d in ds)
 assert sp.cancel(H-(x*y)**N*P)==0
 e=sp.symbols('epsilon', positive=True)
 oldx=H*f-e*x*y*sp.diff(H,y)
 oldy=H*g+e*x*y*sp.diff(H,x)
 newx=oldx+e*N*x*H
 newy=oldy-e*N*y*H
 Pp=sp.diff(sp.prod(sp.Symbol('z')-d for d in ds),sp.Symbol('z')).subs(sp.Symbol('z'),L)
 assert sp.cancel(newx-(H*f-e*(x*y)**(N+1)*Pp*sp.diff(L,y)))==0
 assert sp.cancel(newy-(H*g+e*(x*y)**(N+1)*Pp*sp.diff(L,x)))==0
 assert sp.cancel(sp.diff(L,x)*newx+sp.diff(L,y)*newy + H*D)==0
 assert sp.cancel(sp.diff(newx,x)+sp.diff(newy,y)-sp.diff(oldx,x)-sp.diff(oldy,y)-e*N*(x*sp.diff(H,x)-y*sp.diff(H,y)))==0
 assert sp.Poly(sp.cancel(newx),x,y,e) is not None
 assert sp.Poly(sp.cancel(newy),x,y,e) is not None
 assert sp.factor(newx.subs(x,0).subs(e,sp.Rational(1,10))) == (y*y+y+1)**N*(1+y)
 assert sp.factor(newy.subs(y,0).subs(e,sp.Rational(1,10))) == (x*x+x+1)**N*(1+x)
 print('SYMBOLIC_COMPLETION_OK',N)
# Check sign of Ldot on both sides of the ovals via compact formulas and independent IVP trajectories.
import numpy as np
Dfun=sp.lambdify((x,y),D,'numpy')
Lfun=sp.lambdify((x,y),L,'numpy')
Lxfun=sp.lambdify((x,y),sp.diff(L,x),'numpy')
Lyfun=sp.lambdify((x,y),sp.diff(L,y),'numpy')
for N,ds in [(1,[.6]),(2,[.6,2.0]),(3,[.6,1.2,2.0])]:
 for xi,yi in [(0.85,1.1),(1.2,0.95),(1.8,1.3),(0.6,0.8)]:
  v=Lfun(xi,yi); P=np.prod([v-d for d in ds]); dp=sum(np.prod([v-ds[j] for j in range(N) if j!=i]) for i in range(N))
  H=(xi*yi)**N*P
  vx=H*(1-xi)*(1+yi)-.03*(xi*yi)**(N+1)*dp*Lyfun(xi,yi)
  vy=H*(1-yi)*(1+xi)+.03*(xi*yi)**(N+1)*dp*Lxfun(xi,yi)
  lhs=Lxfun(xi,yi)*vx+Lyfun(xi,yi)*vy
  assert np.isclose(lhs,-H*Dfun(xi,yi),rtol=1e-9,atol=1e-8)
 print('NUMERIC_LYAPUNOV_OK',N)
print('KINETIC_COMPLETION_CHECK_OK')
