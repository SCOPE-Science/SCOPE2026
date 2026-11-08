"""Reproduce the exact polynomial identities and time-statistical formulas for a specified planar oscillator."""
from __future__ import annotations
import math
import sympy as s
from scipy.integrate import quad

x, y, h, w = s.symbols('x y h w', real=True, nonzero=True)
c = w*x*(x*x-h)/(2*h)
R = x*x+(y+c)**2
F = R-h
h1 = w*w*x**4-h*w*w*x*x+4*h*h
h2 = w*w*x**4-2*h*w*w*x*x+h*h*w*w+4*h*h
f3 = -w/(2*h)
f2 = -3*w*w*(x**3-h*x)/(4*h*h)
f1 = -s.Rational(3,8)*(w/h)**3*x**6 + 3*w**3*x**4/(4*h*h) - w*(3*w*w+20)*x*x/(8*h)+w
f0 = -x*h1*h2/(16*h**4)
Q = f3*y**3+f2*y*y+f1*y+f0
# The paper's vector field has xdot=y and ydot=Q.
Rdot = s.expand(s.diff(R,x)*y+s.diff(R,y)*Q)
assert s.factor(Rdot+w*R*(R-h)/h)==0
print('EXACT_BELATTAR_RADIAL_LAW_OK')

theta=s.symbols('theta',real=True)
xt=s.sqrt(h)*s.cos(theta)
yt=s.sqrt(h)*s.sin(theta)-c.subs(x,xt)
thetadot=-(1+w*s.sin(2*theta)/4)
assert s.trigsimp(-s.sqrt(h)*s.sin(theta)*thetadot-yt)==0
# Verify original ydot using the parametric x(t), y(t), theta'(t).
err=s.trigsimp(s.expand_trig(s.diff(yt,theta)*thetadot-Q.subs({x:xt,y:yt})))
print('error expression',s.simplify(err))
assert s.simplify(err)==0
print('EXACT_BELATTAR_ANGULAR_FLOW_OK')

for alpha in (.25,.6,.9,.98):
    delta=math.sqrt(1-alpha*alpha)
    period=2*math.pi/delta
    prob=lambda th:delta/(2*math.pi*(1+alpha*math.sin(2*th)))
    pieces=[0, math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4, 2*math.pi]
    integrate=lambda fn:sum(quad(fn,a,b,epsabs=2e-11,epsrel=1e-11,limit=150)[0] for a,b in zip(pieces[:-1],pieces[1:]))
    assert abs(integrate(prob)-1)<2e-9
    assert abs(integrate(lambda th:math.cos(th)**2*prob(th))-.5)<2e-9
    var=integrate(lambda th:(math.cos(th)**2-.5)**2*prob(th))
    assert abs(var-delta/(4*(1+delta)))<2e-9
    assert abs(integrate(lambda th:1/(1+alpha*math.sin(2*th)))-period)<2e-8
    # Analytic Cauchy law after gate-local angular tangent, checked at distinct quantiles.
    eta=math.sqrt((1-alpha)/(1+alpha))
    for z in [-3.,-.7,0.,.6,2.]:
        t=eta*z
        u=math.atan(t)
        theta_gate=3*math.pi/4+u
        dens_theta=prob(theta_gate)
        dens_z=dens_theta*(eta/(1+t*t))*2 # conditional probability in one gate
        assert abs(dens_z-1/(math.pi*(1+z*z)))<2e-12
    floquet=math.exp(-4*alpha*period) if 4*alpha*period<700 else 0
    assert floquet>=0
    print(f'NUMERIC_PERIOD_MOMENTS_AND_EXACT_CAUCHY_OK alpha={alpha} period={period:.10f} variance={var:.10f}')
print('BELATTAR_PHYSICAL_TIME_CHECK_OK')
