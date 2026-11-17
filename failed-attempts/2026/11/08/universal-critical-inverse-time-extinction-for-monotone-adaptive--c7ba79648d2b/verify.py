"""Algebraic and numerical checks for a critical adaptive SIS law.
Run: python verify.py. These finite checks supplement, not replace, the proof.
"""
import sympy as S
from scipy.integrate import solve_ivp

y=S.symbols('y',real=True)
xi,zeta,b0,c0,bp,cp=S.symbols('xi zeta b0 c0 bp cp',positive=True)
b=b0+bp*y;c=c0+cp*y
h=xi*c/(zeta*b+xi*c)
h0=S.simplify(h.subs(y,0));dh=S.simplify(S.diff(h,y).subs(y,0))
assert S.simplify(dh-xi*zeta*(cp*b0-c0*bp)/(zeta*b0+xi*c0)**2)==0
A=S.factor(1-dh/h0)
assert S.simplify(A-(1+zeta*(bp*c0-b0*cp)/(c0*(zeta*b0+xi*c0))))==0
# Exact constant-response critical branch: z=z0, y'= -y^2
T,Y0=S.symbols('T Y0', positive=True)
Y=Y0/(1+Y0*T)
assert S.simplify(S.diff(Y,T)+Y**2)==0

cases=[
    ('constant',lambda x:1.,lambda x:1.,0.,0.,1.,1.),
    ('linear avoidance',lambda x:1.+x,lambda x:2.-x,1.,-1.,2.,3.),
    ('links-break',lambda x:0.5+2*x,lambda x:1.,2.,0.,3.,2.),
    ('creation falls',lambda x:1.,lambda x:1./(1.+x),0.,-1.,1.,2.),
    ('zero baseline breaking',lambda x:x,lambda x:1.,1.,0.,2.,3.),
]
for name,b,c,bprime,cprime,zeta,xi in cases:
    H0=zeta*b(0)+xi*c(0); z0=xi*c(0)/H0
    hd=xi*zeta*(cprime*b(0)-c(0)*bprime)/H0**2
    tau=1/z0; a=1-tau*hd
    def rhs(t,state):
        y,z=state
        return [y*(-1+tau*(1-y)*z), -zeta*z*b(y)+xi*(1-z)*c(y)]
    sol=solve_ivp(rhs,(0,200000),[0.32,0.91],method='LSODA',rtol=1e-11,atol=1e-13,dense_output=True)
    assert sol.success, (name,sol.message)
    yy,zz=sol.sol(200000)
    rel=abs(200000*yy-1/a)/(1/a)
    zr=abs(200000*(zz-z0)-hd/a)
    print(name,'amplitude',1/a,'simulated',200000*yy,'rel.err',rel,'link scaled error',zr)
    assert rel < 0.005
    assert zr < 0.005
print('VERIFY_OK')
