#!/usr/bin/env python3
"""Optional exact rederivation of the angular formulas; requires SymPy >= 1.12."""
import sympy as S
A,B,t,u,z=S.symbols('A B t u z',positive=True)
# Numerator coordinates along axis (horizontal) and normal (vertical),
# before dividing both coordinates by sqrt(1+t**2).
p={'right':(A,-A*t),'top':(B*t,B),'left':(-A,A*t),'bottom':(-B*t,-B)}
def line(i,j):
    x,y=p[i];X,Y=p[j]
    return y+(Y-y)*(u-x)/(X-x)
left_top=line('left','top')
bot_right=line('bottom','right')
top_right=line('top','right')
def moment(high,low,l,r):
    # Exact chord-centre inertia contribution, where high>low for 0<z<1.
    integrand=S.cancel((high-low)*((high+low)/2)**2)
    return S.integrate(integrand,(u,l,r))
exact=S.factor(2*(moment(left_top,bot_right,0,B*t)+moment(top_right,bot_right,B*t,A))/(1+t*t)**2)
F=3*S.sqrt(3)*z*z*(19-15*z+32*z*z-32*z**3)/(128*(1+z)**3*(3+4*z*z))
G=3*S.sqrt(3)*z*z*(33-29*z+18*z*z-18*z**3)/(128*(1+z)**3*(4+3*z*z))
low=S.factor(exact.subs({A:S.sqrt(3)/2,B:S.Rational(3,4),t:2*S.sqrt(3)*z/3}, simultaneous=True))
high=S.factor(exact.subs({A:S.Rational(3,4),B:S.sqrt(3)/2,t:S.sqrt(3)*z/2}, simultaneous=True))
assert S.cancel(low-F)==0 and S.cancel(high-G)==0
Q=36*z**5-23*z**4+112*z**3-48*z*z+80*z-44
assert S.cancel(S.diff(G,z)+9*S.sqrt(3)*z*Q/(64*(z+1)**4*(3*z*z+4)**2))==0
P=17080*z**5-14424*z**4+10185*z**3-7589*z*z+1494*z+498
assert S.cancel(G.subs(z,S.Rational(1,2))-F-3*S.sqrt(3)*P/(128*513*(z+1)**3*(4*z*z+3)))==0
print('PASS: two exact chord-polynomial profiles, quintic derivative and Bernstein comparison identity')
