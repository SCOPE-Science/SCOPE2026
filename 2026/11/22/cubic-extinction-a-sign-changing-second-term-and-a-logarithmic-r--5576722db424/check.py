"""Reproduce symbolic coefficients and finite trajectory diagnostics for the stated discrete map."""
import math
import sympy as sp

v, w, d, m, g = sp.symbols('v w d m g', positive=True)
A = d*m*(g+1)/g**2
B = A*(g-1)/g
C = A*(1-1/g+1/g**2+m/g)
kappa = m*(g+1)/g**2
V = v + d*m*v**2*(g*w-(g+1)*v)/(g*(g+v)*(1-v+w))
W = (1-d*(1-v+w))*w + V-v
assert sp.simplify(V-v-d*m*v**2*(g*w-(g+1)*v)/(g*(g+v)*(1-v+w)))==0
ser = sp.series(V.subs(w,-kappa*v**3),v,0,6).removeO().expand()
assert sp.simplify(ser.coeff(v,3)+A)==0
assert sp.simplify(ser.coeff(v,4)+B)==0
assert sp.simplify(ser.coeff(v,5)+C)==0
assert sp.simplify(sp.series((W+kappa*V**3).subs(w,-kappa*v**3),v,0,4).removeO())==0
assert sp.simplify((2*C+3*A**2)/(2*A)).subs(g,1)==1+m+3*d*m

def iterate(gam, mm, dd, n=140000):
    x,y = .9,.1
    for i in range(n):
        xx=x+dd*x*(1-x-y)
        yy=y+dd*y*(mm-mm*y/(gam*x)-mm*gam/(gam+y))
        x,y=xx,yy
        assert x>0 and y>0
    aa=dd*mm*(gam+1)/gam**2
    lead=1/math.sqrt(2*aa)
    next_coeff=-gam*(gam-1)/(2*dd*mm*(gam+1))
    assert abs(y*math.sqrt(n)-lead)<.008
    assert abs((1-x-y)/y**3-mm*(gam+1)/gam**2)<.14
    assert abs(n*(y-lead/math.sqrt(n))-next_coeff)<.14
    if gam==1:
        z=1/y**2-4*dd*mm*n-(1+mm+3*dd*mm)*math.log(n)
        assert math.isfinite(z)
    return n,y,x
for pars in ((1.,1.,1.),(2.,1.,.8),(.5,2.,1.5)):
    print(pars,iterate(*pars))
print('PASS: exact formal coefficient identities and finite diagnostic trajectories')
