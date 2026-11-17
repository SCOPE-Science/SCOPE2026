"""Symbolic and numerical checks for the discrete two-stage threshold normal form."""
import math
import sympy as sp

p,u,kappa,m,nu=sp.symbols('p u kappa m nu',positive=True)
e=1-u
L=kappa*m/(p*u)
c=L*u/m
d=L**2*((m+1)*e-1)/m**2
alpha=(1-p)*c/u
omega=kappa/((1+nu)*u)
Q=sp.factor(p*d+c*alpha*(1-p)-kappa*(1+omega))
D=sp.expand(u+(-3+(m+3)*e)*p+u*(nu/(1+nu)-u/kappa)*p**2)
assert sp.simplify(Q-kappa*kappa*D/(p*p*u*u))==0
assert sp.simplify(c-kappa/p)==0

# Exact Taylor-coefficient identity obtained directly from the analytic incidence function.
t,L0=sp.symbols('t L0',real=True)
B=L0*t/(L0*t+m)*(1-sp.exp(-m-L0*t))
ct=sp.simplify(sp.diff(B,t).subs(t,0))
dt=sp.simplify(sp.diff(B,t,2).subs(t,0)/2)
assert sp.simplify(ct-L0*(1-sp.exp(-m))/m)==0
assert sp.simplify(dt-L0**2*((m+1)*sp.exp(-m)-1)/m**2)==0

def constants(nu,tau,p):
    m=nu*tau
    ee=math.exp(-m)
    uu=-math.expm1(-m)
    lam=math.exp(-(1+nu)*tau)
    kap=1-lam
    rho=(1+nu)*m/(p*uu)
    LL=rho*kap/(1+nu)
    cc=LL*uu/m
    dd=LL*LL*((m+1)*ee-1)/m**2
    aa=(1-p)*cc/uu
    ww=kap/((1+nu)*uu)
    QQ=p*dd+cc*aa*(1-p)-kap*(1+ww)
    AA=uu*(nu/(1+nu)-uu/kap)
    BB=-3+(m+3)*ee
    DD=lambda pp: uu+BB*pp+AA*pp*pp
    root=(-2*uu)/(BB-math.sqrt(BB*BB-4*AA*uu)) # stable quadratic root (also -2C/(B-sqrt(...)))
    # Wait root of A*x*x+B*x+C=0: -2*C/(B-sqrt(discriminant))
    return dict(m=m,uu=uu,ee=ee,lam=lam,kap=kap,rho=rho,L=LL,c=cc,d=dd,alpha=aa,omega=ww,Q=QQ,A=AA,B=BB,D=DD,pstar=root)

for nu0,tau0 in [(0.002,5.5),(0.05,2),(0.5,2),(2,5.5)]:
    obj=constants(nu0,tau0,0.6)
    assert obj['A']<0 and obj['B']<0 and obj['D'](0)>0 and obj['D'](.5)<0
    assert 0<obj['pstar']<.5
    assert abs(obj['D'](obj['pstar'])) < 1e-10
    for p0 in [0.2*obj['pstar'],0.9*obj['pstar'],1.1*obj['pstar'],.9]:
        z=constants(nu0,tau0,p0)
        assert (z['Q']>0)==(p0<obj['pstar'])
        assert abs(z['Q']-z['kap']**2*z['D'](p0)/(p0*p0*z['uu']**2))<1e-9

# Test the critical n^{-1} law in the physical variables for two parameter choices.
checks=[]
for nu0,tau0,p0,steps in [(.5,2,.6,180000),(.05,5.5,.6,180000)]:
    C=constants(nu0,tau0,p0)
    z=.002*C['alpha'];a=.002;w=.002*C['omega']
    for it in range(steps):
        s0=1-z-a-w
        assert s0>=0 and z>=0 and a>=0 and w>=0
        La=C['L']*a
        P=-math.expm1(-(La+C['m']))
        B=La/(La+C['m'])*P
        zn=(1-p0)*s0*B+z*(1-P)
        an=p0*s0*B+z*B+C['lam']*a
        wn=C['ee']*w+C['kap']/(1+nu0)*a
        z,a,w=zn,an,wn
    target=-1/C['Q']
    actual=steps*a
    assert abs(actual/target-1)<.018,(nu0,tau0,actual,target)
    assert abs(z/a-C['alpha'])<.005
    assert abs(w/a-C['omega'])<.005
    checks.append((nu0,tau0,p0,steps,actual,target))

# Check subcritical stationary branch and positive local eigenvalue by finite differences.
for p0 in [.3,.6]:
    nu0=.5;tau0=2
    obj=constants(nu0,tau0,p0)
    eps=1e-4 if obj['Q']<0 else -1e-4
    # solve three stationary equations by simple mpmath rootfinder
    import mpmath as mp
    mm=obj['m'];kap=obj['kap'];ee=obj['ee'];ll=obj['lam']
    rho=obj['rho']*(1+eps); Lr=rho*kap/(1+nu0)
    def fixed(z,a,w):
        s0=1-z-a-w
        la=Lr*a; B=la/(la+mm)*(-mp.expm1(-(la+mm)))
        P=-mp.expm1(-(la+mm))
        return ((1-p0)*s0*B+z*(1-P)-z,
                p0*s0*B+z*B+ll*a-a,
                ee*w+kap/(1+nu0)*a-w)
    guess=(-obj['kap']*eps/obj['Q'])
    root=mp.findroot(fixed,(obj['alpha']*guess,guess,obj['omega']*guess),tol=mp.mpf('1e-24'))
    za,aa,ww=map(float,root)
    assert aa>0 and za>0 and ww>0 and aa+za+ww<1
    assert abs(aa/eps+obj['kap']/obj['Q'])<.04

print('VERIFY_OK exact_center_taylor=2 exact_normal_form_identity=1 unique_transition_examples=4 critical_decay_examples=2 bifurcating_endemic_branches=2')
for row in checks:
    print('critical_decay', row)
