"""Reproduce exact identities, a Taylor sign certificate, and independent widths.
Python 3 with SymPy for exact symbolic algebra; no network access.
"""
import math
import sympy as sp

z = sp.symbols('z', real=True)
L = sp.pi / 3
A = 2 * L + sp.sqrt(3)
Q = A * (1 - sp.cos(z)) + z * sp.cos(z) - (1 + sp.sqrt(3)*z) * sp.sin(z)
Qp = sp.diff(Q, z)
F = 2 * Qp * sp.sin(z)*sp.sin(2*L-z) - Q*sp.sin(2*L-2*z)
F_short = (-sp.Rational(5,2)*z*sp.sin(z) - sp.sqrt(3)*z*sp.cos(z)/2
           + 2*sp.pi*sp.sin(z)/3 - (2*sp.pi/3 + sp.sqrt(3))*sp.sin(2*z+sp.pi/3)
           + sp.sin(3*z+sp.pi/6) + (1 + sp.sqrt(3)*sp.pi/3)*sp.cos(z))
assert sp.simplify(sp.expand_trig(sp.trigsimp(sp.expand_trig(F-F_short)))) == 0
H = sp.diff(F_short,z)*z - 2*F_short
assert all(sp.simplify(sp.diff(H,z,k).subs(z,0)) == 0 for k in range(3))
coeffs = {
    3:(sp.pi-4*sp.sqrt(3))/3,
    4:sp.Rational(55,24) - 5*sp.sqrt(3)*sp.pi/12,
    5:-sp.pi/4 + 103*sp.sqrt(3)/40,
    6:-sp.Rational(569,360)+7*sp.sqrt(3)*sp.pi/60,
    7:-57*sp.sqrt(3)/56+sp.pi/24,
    8:sp.Rational(389,896)-17*sp.sqrt(3)*sp.pi/1344,
    9:-17*sp.pi/5184+9581*sp.sqrt(3)/51840,
}
for k,c in coeffs.items():
    assert sp.simplify(sp.diff(H,z,k).subs(z,0)/sp.factorial(k)-c)==0
# Rational upper/lower bounds for pi, sqrt(3) used in the proof.
assert sp.Rational(157,50)<sp.pi<sp.Rational(22,7)
assert sp.Rational(173,100)<sp.sqrt(3)<sp.Rational(7,4)
assert coeffs[3] < -sp.Rational(5,4)
assert coeffs[4] < sp.Rational(1,20)
assert coeffs[5] < sp.Rational(15,4)
assert coeffs[6] < 0 and coeffs[7] < 0
assert coeffs[8] < sp.Rational(1,2)
assert coeffs[9] < sp.Rational(1,3)
a=sp.Rational(11,21)
assert sp.pi/6<a
# F^(10) < 64000, F^(11) < 186000 on [0,pi/6], via trig amplitudes.
C1=sp.Rational(27,8) # (5+sqrt3)/2 bound
C2=sp.Rational(44,21)+sp.Rational(7,4) # 2*pi/3+sqrt3 bound
C3=sp.Rational(44,21)
C4=sp.Rational(17,6)
assert C1*11 + C3 + C2*2**10 + 3**10 + C4 < 64000
assert C1*12 + C3 + C2*2**11 + 3**11 + C4 < 186000
assert 186000 + 8*64000 < 10**6
upper= (-sp.Rational(5,4) + a/20 + sp.Rational(15,4)*a*a
        + a**5/2 + a**6/3 + sp.Rational(10**6,math.factorial(10))*a**7)
assert upper < 0
# Therefore (z F' - 2 F)/z^3 < 0 on the whole interval 0<z<=pi/6.
# No finite grid is being used to deduce this continuous conclusion.
assert sp.simplify(sp.limit(F/z**2,z,0) - (sp.sqrt(3)*sp.pi/2-sp.Rational(9,4)))==0
assert sp.sqrt(3)*sp.pi/2 - sp.Rational(9,4)>0
assert sp.simplify(Q.subs(z,sp.pi/6) -(2-sp.sqrt(3))*(sp.pi/3-1))==0
assert sp.simplify(Qp.subs(z,sp.pi/6))==0
# Strict sign at z=pi/6 follows because Q>0 and sin(pi/3)>0.
assert (sp.pi/3-1)>0
# The reflection comparison is cos(2(L-z)) - cos(2z) < 0 when z<L/2.

# Independent polygonal-width quadrature; this checks the asymptotic normalization.
pi=math.pi; rt3=math.sqrt(3); ell=pi/3
kap=pi*(2*pi+3*rt3)/36; delta0=math.sqrt(kap-1)
AA=2*ell+rt3

def gg(theta):
    qq=AA*(1-math.cos(theta))+theta*math.cos(theta)-(1+rt3*theta)*math.sin(theta)
    return rt3*qq/(2*AA*math.sqrt(math.sin(theta)*math.sin(2*ell-theta)))

def ff(theta):
    qq=AA*(1-math.cos(theta))+theta*math.cos(theta)-(1+rt3*theta)*math.sin(theta)
    qp=(2*ell-theta)*math.sin(theta)-rt3*theta*math.cos(theta)
    return 2*qp*math.sin(theta)*math.sin(2*ell-theta)-qq*math.sin(2*ell-2*theta)
lo,hi=0.45,0.46
assert ff(lo)>0 and ff(hi)<0
for _ in range(70):
    mid=(lo+hi)/2
    if ff(mid)>0: lo=mid
    else: hi=mid
theta=(lo+hi)/2
ratio=math.sin(2*ell-theta)/math.sin(theta)
C=kap/(3*delta0)*gg(theta)
assert .45267 < theta < .45269
assert 2.2805 < ratio < 2.2808
assert .03320 < C < .03323

def direct_deviation(s,t,steps=30000):
    vertices=((s,0.),(1.,0.),(.5,rt3/2.),(t/2.,rt3*t/2.))
    summ=sumsq=0.
    for j in range(steps):
        a=(j+.5)*2*pi/steps
        co,si=math.cos(a),math.sin(a)
        w=[x*co+y*si for x,y in vertices]
        width=max(w)-min(w)
        summ+=width; sumsq+=width*width
    mean=summ/steps;second=sumsq/steps
    return math.sqrt(max(0.,second/mean**2-1.))
for rr in (ratio,1.,2.,4.):
    ep=.0005
    d=direct_deviation(ep*math.sqrt(rr),ep/math.sqrt(rr))
    phi=math.atan2(rt3/(2*math.sqrt(rr)),math.sqrt(rr)-1/(2*math.sqrt(rr)))
    predicted=kap/(3*delta0)*gg(phi)
    slope=(delta0-d)/ep
    # Finite-size error is O(epsilon); numerical quadrature is a cross-check only.
    assert abs(slope-predicted) < .001
print('PASS: exact trig and Taylor identities; all-angle sign certificate; unique optimum; four quadrature cross-checks')
print('theta = %.15f, s/t = %.15f, decrease/epsilon = %.15f' % (theta,ratio,C))
