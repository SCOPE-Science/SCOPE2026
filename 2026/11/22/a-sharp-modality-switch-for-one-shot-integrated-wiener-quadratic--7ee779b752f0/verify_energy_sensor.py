"""Exact finite algebra plus independent quadrature checks for Gaussian path-energy sensing."""
import sympy as S
import mpmath as M

z,t,e=S.symbols('z t e', real=True, nonnegative=True)
K_B_left=t**2/2
K_B_right=t*z-z**2/2
K_X_left=z*t**2/2-t**3/6
K_X_right=t*z**2/2-z**3/6
AB=S.factor(S.integrate(K_B_left**2,(t,0,z))+S.integrate(K_B_right**2,(t,z,1)))
AX=S.factor(S.integrate(K_X_left**2,(t,0,z))+S.integrate(K_X_right**2,(t,z,1)))
assert S.expand(AB-z*z*(20-30*z+15*z*z-2*z**3)/60)==0
assert S.expand(AX-z**4*(105-105*z+35*z*z-2*z**3)/1260)==0
RB=AB/(z+e)
RX=AX/(z**3/S.Integer(3)+e)
MB=10*(1-z)**2*(4-z)
NB=z*(8*z**3-45*z**2+60*z-20)
MX=1260-1575*z+630*z**2-42*z**3
NX=z**3*(8*z**3-105*(1-z)**2)
assert S.factor(S.diff(RB,z)-z*(e*MB-NB)/(60*(e+z)**2))==0
assert S.factor(S.diff(RX,z)-z**3*(e*MX-NX)/(420*(3*e+z**3)**2))==0
assert S.factor(S.diff(NB,z)*MB-NB*S.diff(MB,z) + 20*(z-1)*(2*z*z-7*z+2)*(2*z**3-15*z*z+30*z-20)) == 0
assert S.factor(S.diff(NX,z)*MX-NX*S.diff(MX,z) +126*z*z*(2*z**3-35*z*z+105*z-105)*(4*z**3-45*z*z+75*z-30)) == 0
# Analytic certificate for the low-noise comparison, valid |y| <= 1/2.
y=S.symbols('y',real=True)
q=6*z**4-45*z**3+90*z*z-60*z+13
assert S.factor(q.subs(z,y+S.Rational(1,2))-(6*y**4+15*y*y-S.Rational(3,4)*y+S.Rational(1,4))-S.Rational(33,2)*y*y*(1-2*y))==0
assert S.factor(S.Rational(13,180)-AB/z-q/180)==0
assert S.factor(RX.subs(z,1).subs(e,S.Rational(8,273))-S.Rational(13,180))==0
P=168*z**5-1015*z**4+1680*z**3-1050*z*z+280*z-33
h=S.factor((RB-RX.subs(z,1)).subs(e,NB/MB))
E=S.factor(420*(S.Rational(1,3)+NB/MB)*AB-11*(NB/MB+z))
assert S.factor(E*MB + z*(2*z**3-15*z*z+30*z-20)*P/3)==0
assert P.subs(z,S.Rational(57779,100000))*P.subs(z,S.Rational(57780,100000))<0
# Independent check of prior energy variance via double covariance integral.
s,u=S.symbols('s u',real=True,nonnegative=True)
Ks_u=u*s*s/2-s**3/6
prior_var=S.factor(4*S.integrate(S.integrate(Ks_u**2,(u,s,1)),(s,0,1)))
assert prior_var==S.Rational(11,840)
assert S.factor(S.integrate(t**3/3,(t,0,1)))==S.Rational(1,12)
M.mp.dps=45
root=M.findroot(S.lambdify(z,P,'mpmath'),('.57779','.57780'))
eta=S.lambdify(z,NB/MB,'mpmath')(root)
assert abs(S.lambdify((z,e),RB,'mpmath')(root,eta)-S.lambdify((z,e),RX,'mpmath')(1,eta))<M.mpf('1e-37')
assert M.mpf('.11249')<eta<M.mpf('.11250')
# Compare exact covariance formulas to independent numerical integration at fixed nodes.
for point in [M.mpf('0.2'),M.mpf('0.47'),M.mpf('0.8'),M.mpf('1')]:
    directB=M.quad(lambda T:(T*T/2)**2,[0,point])+M.quad(lambda T:(T*point-point**2/2)**2,[point,1])
    directX=M.quad(lambda T:(point*T*T/2-T**3/6)**2,[0,point])+M.quad(lambda T:(T*point**2/2-point**3/6)**2,[point,1])
    assert abs(directB-S.lambdify(z,AB,'mpmath')(point))<M.mpf('1e-35')
    assert abs(directX-S.lambdify(z,AX,'mpmath')(point))<M.mpf('1e-35')
# Supplementary global mesh checks are not the proof of optimality.
for noise in [0,M.mpf('.005'),M.mpf('.029304'),M.mpf('.05'),M.mpf('.1'),eta,M.mpf('.15'),M.mpf('1'),M.mpf('10')]:
    values=[]
    for x in [M.mpf(i)/1000 for i in range(1,1001)]:
        values.append((S.lambdify((z,e),RB,'mpmath')(x,noise),'B',x))
        values.append((S.lambdify((z,e),RX,'mpmath')(x,noise),'X',x))
    score,mode,where=max(values)
    expected='X' if noise<eta else ('B' if noise>eta else 'tie')
    assert mode==expected or expected=='tie', (noise,mode,where,expected)
print('exact symbolic identities: PASS')
print('independent polynomial/quadrature/boundary checks: PASS')
print('supplementary 18,000 grid evaluations: PASS')
print('threshold x =',M.nstr(root,20))
print('threshold eta =',M.nstr(eta,20))
