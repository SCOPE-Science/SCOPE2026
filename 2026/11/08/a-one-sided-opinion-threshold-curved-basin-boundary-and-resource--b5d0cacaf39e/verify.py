#!/usr/bin/env python3
"""Reproduce algebra and sample trajectories for a two-strategy opinion-feedback game."""
import sympy as S
from scipy.integrate import solve_ivp

x,y=S.symbols('x y',real=True)
v=4+3*y;c=12-2*y
uH=v-(v+c)*x/2;uD=v*(1-x)/2
F=S.expand(x*(1-x)*(v-c*x)/2)
H=S.expand((y*x*uH-(1-y)*(1-x)*uD)/2)
phi=v/c
assert S.simplify(F-x*(1-x)*(v-c*x)/2)==0
# Upper and lower clipping is inactive for the published Table 1 payoffs.
from math import comb
bern = [lambda k: S.binomial(2,k)*x**k*(1-x)**(2-k),
        lambda k: S.binomial(2,k)*y**k*(1-y)**(2-k)]
coeff=[[S.Integer(0),S.Rational(1,8),S.Integer(1)],
       [S.Integer(1),S.Rational(3,2),S.Rational(11,4)],
       [S.Integer(1),S.Integer(0),S.Rational(1,4)]]
bound=sum(coeff[i][j]*bern[0](i)*bern[1](j) for i in range(3) for j in range(3))
assert S.simplify(bound-(1+H))==0
assert all(a>=0 for row in coeff for a in row)
assert S.simplify(H.subs(y,1)-x*(14-17*x)/4)==0
assert S.simplify(S.Rational(49,68)-H.subs(y,1)-17*(x-S.Rational(7,17))**2/4)==0
assert S.simplify(H.subs(y,0)+(1-x)**2)==0
assert S.simplify(H.subs(y,S.Rational(1,2))+11*(2*x-1)**2/16)==0
assert S.simplify(S.diff(H,y,2)-(2*x*x+3)/2)==0
assert S.simplify(H.subs(x,phi)-v*(1-phi)*(y+phi-1)/4)==0
assert S.simplify(y+phi-1-(2*y-1)*(8-y)/c)==0
q={x:S.Rational(1,2),y:S.Rational(1,2)}
assert S.diff(F,x).subs(q)==-S.Rational(11,8)
assert S.diff(F,y).subs(q)==S.Rational(1,2)
assert S.diff(H,x).subs(q)==0
assert S.diff(H,y).subs(q)==S.Rational(15,16)
a=S.solve(S.Eq(2*S.Symbol('a')*S.diff(F,x).subs(q),S.Rational(1,2)*S.diff(H,y).subs(q)*S.Symbol('a')-S.Rational(11,8)),S.Symbol('a'))[0]
assert a==S.Rational(44,103)
assert S.factor(H.subs({x:S.Rational(7,10),y:1}))==S.Rational(147,400)
assert S.factor(H.subs({x:S.Rational(1,3),y:0}))==-S.Rational(4,9)

def ode(t,z):
    X,Y,N=z
    V=4+3*Y; C=12-2*Y
    uh=V-(V+C)*X/2
    ud=V*(1-X)/2
    h=(Y*X*uh-(1-Y)*(1-X)*ud)/2
    return [X*(1-X)*(V-C*X)/2, (1-Y)*max(h,0)-Y*max(-h,0), N*(1-N)*(3*X-1)]

def run(X,Y,N=.3,T=200):
    sol=solve_ivp(ode,(0,T),[X,Y,N],method='DOP853',rtol=2e-11,atol=1e-13,dense_output=False)
    assert sol.success
    return sol.y[:,-1]

if __name__=='__main__':
 print('exact critical point',q,'stable curvature',a)
 for ini in [(0.5,.45,.3),(.5,.7,.3),(.8,.5,.3),(.5,.5,.3),(.8,.51,.3),(.8,.8,.3)]:
  print(ini,run(*ini))
 print('VERIFY_OK')
