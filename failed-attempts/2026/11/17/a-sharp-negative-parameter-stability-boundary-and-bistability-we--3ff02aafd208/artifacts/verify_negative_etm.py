#!/usr/bin/env python3
"""Exact rational and symbolic checks for the negative-parameter ETM-3D hysteresis theorem."""
import sympy as sp
r,x,a=sp.symbols('r x a',real=True); t=sp.symbols('t')
Q=8*x**4+8*r*x**3+(-6*r**2+10*r+35)*x**2+(-4*r**3+5*r**2+15*r)*x+(r**2-5)*(2*r**2-5*r-10)
P=594*r**8-2076*r**7-5948*r**6+20050*r**5+25505*r**4-66100*r**3-63325*r**2+77500*r+75000
F=3*a**3*r**2+2*a**2*r**2-10*a**2*r-40*a**2-18*a*r**2+20*a*r+85*a-10
assert sp.factor(sp.discriminant(Q,x)-12000*P)==0
assert sp.factor(sp.discriminant(F,a)-120*P)==0
print('exact_discriminants=2')
# Isolate every real discriminant zero by rational Sturm counts.
intervals=[(sp.Rational(-2011935,1000000),sp.Rational(-2011934,1000000)),
           (sp.Rational(-1308661,1000000),sp.Rational(-1308660,1000000)),
           (sp.Rational(2188758,1000000),sp.Rational(2188759,1000000)),
           (sp.Rational(3355161,1000000),sp.Rational(3355162,1000000))]
assert sp.Poly(P,r).count_roots(-sp.oo,sp.oo)==4
assert all(sp.Poly(P,r).count_roots(u,v)==1 for u,v in intervals)
print('isolated_discriminant_roots=4')
# Sample parameters in complementary intervals certify topology.
q=sp.Poly(Q,x)
assert sp.Poly(Q.subs(r,sp.Rational(-131,100)),x).count_roots(-sp.oo,sp.oo)==2
assert sp.Poly(Q.subs(r,sp.Rational(-131,100)),x).count_roots(0,sp.Rational(1,4))==2
assert sp.Poly(Q.subs(r,-1),x).count_roots(-sp.oo,sp.oo)==0
assert sp.Poly(Q.subs(r,sp.Rational(-3,2)),x).count_roots(-sp.oo,sp.oo)==2
assert sp.Poly(Q.subs(r,-3),x).count_roots(-sp.oo,sp.oo)==4
print('quartic_real_roots_sampled=4')
# The quartic never hits x=1/4 or x=0 over the open transcritical/fold interval.
for boundary in [0,sp.Rational(1,4)]:
 B=sp.Poly(Q.subs(x,boundary),r)
 assert B.count_roots(sp.Rational(-13118,10000),sp.Rational(-13086,10000))== (1 if boundary==0 else 0)
print('quartic_barrier_checked=2')
# At the origin, a simple zero eigenvalue occurs at r0=(5-sqrt(105))/4.
A=sp.Matrix([[-2,-r,0],[1,-1,r],[0,r,-5]])
assert sp.simplify(A.charpoly(t).as_expr()-(t**3+8*t**2+(17+r-r**2)*t+(10+5*r-2*r*r)))==0
r0=(5-sp.sqrt(105))/4
assert sp.simplify(10+5*r0-2*r0**2)==0
assert sp.simplify(sp.diff(Q,x).subs({x:0,r:r0})) != 0
assert sp.simplify(sp.diff(Q,r).subs({x:0,r:r0})) != 0
assert sp.Rational(-13118,10000)<r0<sp.Rational(-13117,10000)
print('origin_critical_eigenvalue=1')
# Characteristic coefficient and determinant identity at nonzero equilibria.
D=2*x*x+r*x+5-r*r
Y=5*x/D; Z=x*(r+x)/D
J=sp.Matrix([[-2,-r+Z,Y],[1-2*Z,-1,r-2*x],[Y,r+x,-5]])
coeff=sp.Poly(J.charpoly(t).as_expr(),t).all_coeffs()
assert coeff[1]==8
assert sp.factor(coeff[2]-(12+D+(r-Z)*(1-2*Z)-Y**2))==0
assert sp.factor((-J.det()-x*sp.diff(Q,x)/D)*D**2 /Q)==-(r*r+r*x+6*x*x-5)
print('jacobian_charpolynomial_identities=3')
# Weighted quadratic strict Lyapunov certificate; energy-neutral nonlinearity.
M=sp.Matrix([[-2*a,(1-a*r)/2,0],[(1-a*r)/2,-1,r*(3-a)/2],[0,r*(3-a)/2,5*a-10]])
assert sp.factor(-4*M.det()-F)==0
assert sp.factor(F.subs(a,0))==-10
assert sp.factor(F.subs(a,2))==-4*r**2
for rr,num in [(-1,2),(sp.Rational(-3,2),0),(sp.Rational(-3,1),0)]:
 assert sp.Poly(F.subs(r,rr),a).count_roots(0,2)==num
print('lyapunov_certificate_topology=5')
# Quantitative stability at each nonzero equilibrium in the wedge.
# For -1.312 < r < -1.308, 0 < x < 1/4,
# D>2.95, 0<Y<.424, |Z|<.112; hence c2>13.
# |Q_x|<70 implies |c3|< 6, so 8*c2>c3 for positive c3.
lo=sp.Rational(295,100); Rmax=sp.Rational(1312,1000); Xmax=sp.Rational(1,4)
assert 5-Rmax**2-Rmax*Xmax>lo
Ymax=5*Xmax/lo; Zmax=Rmax*Xmax/lo
assert Ymax<sp.Rational(424,1000) and Zmax<sp.Rational(112,1000)
c2low=12+lo-(Rmax+sp.Rational(112,1000))*(1+2*sp.Rational(112,1000))-sp.Rational(424,1000)**2
assert c2low>13
Qxmax=32*Xmax**3+24*Rmax*Xmax**2+2*(6*Rmax**2+10*Rmax+35)*Xmax+(4*Rmax**3+5*Rmax**2+15*Rmax)
assert Qxmax<70
assert Xmax*Qxmax/lo<6 and 8*c2low>6
print('rigorous_rational_interval_bounds=6')
# The exact saddle-node interval is strictly above the transcritical value.
assert r0<intervals[1][0]
print('bistable_wedge_order=1')
print('VERIFY_OK exact_sturm=1 exact_discriminants=2 quartic_topology=1 jacobian=3 lyapunov=1')
