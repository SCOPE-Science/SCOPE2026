"""Symbolic and finite-example checks for a sinusoidal-feedback supply-chain flow.

The global root counts and asymptotic sink law rely on the accompanying proof,
not on finite numerical sampling.
"""
import math
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

x,a,m,c,r,p,lam=sp.symbols('x a m c r p lam', real=True)
J=sp.Matrix([[-a,m,0],[r+p*sp.cos(x)-a*x*x/(m*c),-1,-x],[a*x/m,x,-c]])
poly=sp.Poly((lam*sp.eye(3)-J).det(),lam)
B=r-a/m
C=a/(m*c)
expected=[1,a+c+1,a*(1+c)+c-m*r-m*p*sp.cos(x)+(1+a/c)*x*x,-m*c*(B-3*C*x*x+p*sp.cos(x))]
assert all(sp.simplify(u-v)==0 for u,v in zip(poly.all_coeffs(),expected))
assert sp.simplify(J.det()-m*c*(B-3*C*x*x+p*sp.cos(x)))==0

av,mv,cv,rv=12.,14.,7.,55.
bv=rv-av/mv; Cval=av/(mv*cv)
R=math.sqrt(bv/Cval)
for amp in (100000., 10000000.):
    top=brentq(lambda q:Cval*q**3-bv*q-amp, R, 1e5)
    countpos=0; sinkspos=0; tested=0
    for j in range(0,math.ceil(top/(2*math.pi))+3):
        l=2*math.pi*j;h=(2*j+1)*math.pi;mid=(l+h)/2
        # beyond R: each of the two sides of the lobe is strictly concave
        if l<R or l>=top:continue
        peak=minimize_scalar(lambda t: -(amp*math.sin(t)-Cval*t**3+bv*t),bounds=(l+1e-9,h-1e-9),method='bounded')
        peakx=peak.x
        if -peak.fun<=0:continue
        roots=[brentq(lambda t:amp*math.sin(t)-Cval*t**3+bv*t,l,peakx),brentq(lambda t:amp*math.sin(t)-Cval*t**3+bv*t,peakx,h)]
        countpos+=2
        for rt in roots:
            A2=av*(1+cv)+cv-mv*rv-mv*amp*math.cos(rt)+(1+av/cv)*rt*rt
            A3=-mv*cv*(bv-3*Cval*rt**2+amp*math.cos(rt))
            stable=A2>0 and A3>0 and (av+cv+1)*A2>A3
            if stable:sinkspos+=1
            tested+=1
    assert countpos>=2 and sinkspos>=2
    print(f'p={amp:g} positive_equilibria_outside_R={countpos} positive_sinks_outside_R={sinkspos} predicted_total_sinks~{top/(math.pi):.3f}')
    print('normalized sinks ratio', 2*sinkspos/(amp**(1/3)))
# asymptotic positive-lobe minimum for large j
j=100;t=(2*j+.5)*math.pi
P=lambda xx:Cval*xx**3-bv*xx
res=minimize_scalar(lambda xx:P(xx)/math.sin(xx),bounds=(2*j*math.pi+1e-5,t),method='bounded', options={'xatol':1e-11})
assert abs((t-res.x)-3/t)<1e-4
assert abs(res.fun-(Cval*t**3-(bv+4.5*Cval)*t))<0.2
print('fold asymptotics checked',res.x,res.fun)
print('VERIFY_OK jacobian_characteristic=4 determinant_identity=1 finite_large_p_cases=2 lobe_sinks_checked=',tested,'fold_asymptotics=1')
