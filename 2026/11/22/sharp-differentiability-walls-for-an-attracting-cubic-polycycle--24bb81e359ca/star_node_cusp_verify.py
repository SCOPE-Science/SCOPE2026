"""Symbolic identities and numerical diagnostics for cubic invariant-circle cusp theorem.
Scientific tests are diagnostic; the infinite-parameter proof is in RESULT.md.
"""
import sympy as sp
from mpmath import mp
x,y,eps,omega=sp.symbols('x y eps omega',real=True)
r2=x*x+y*y
H=-(x*x+y*y)-eps*(x*x-y*y)
G=2*omega*x*y
q1=sp.expand(H*x-G*y)
q2=sp.expand(H*y+G*x)
assert sp.expand(x*q1+y*q2 - H*r2)==0
assert sp.expand(x*q2-y*q1-G*r2)==0
z,v=sp.symbols('z v',real=True)
alpha=(1-eps)/(2*omega); beta=(1+eps)/(2*omega)
A=(1+eps*z)/(omega*(1-z*z))
assert sp.simplify(A-beta/(1-z)-alpha/(1+z))==0
ve=1/(1+eps*z)
assert sp.simplify((1+eps*z)*ve-1)==0
assert sp.simplify(sp.diff(ve,z)+eps/(1+eps*z)**2)==0
# Check local forced first-order coefficient at z=-1 for alpha>1
c=eps/(1-eps)**2
kappa=2*alpha
assert sp.simplify(c*alpha/(alpha-1) - eps*(1-eps)/( (1-eps)**2*(1-eps-2*omega)))==0
mp.dps=65

def v_int(e,w,delta):
    e,w,delta=map(mp.mpf,(e,w,delta))
    a=(1-e)/(2*w); b=(1+e)/(2*w)
    z=-1+delta
    # integral in variable t=1-s; t from 0 to 2-delta
    I=mp.quad(lambda t: t**(b-1)*(2-t)**(-a-1),[0,1,2-delta])
    return (delta**a)/(w*((2-delta)**b))*I

def h_const(e,w):
    e=mp.mpf(e); w=mp.mpf(w); a=(1-e)/(2*w); b=(1+e)/(2*w)
    J= e*mp.quad(lambda s: (1-s)**b*(1+s)**(-a)/(1+e*s)**2,[-1,0,1])
    return 2**(a-b)*J

for w in ['1','0.5','0.25','0.125']:
    e=mp.mpf('0.5'); wmp=mp.mpf(w)
    a=(1-e)/(2*wmp); kap=2*a; r0=1/mp.sqrt(1-e)
    vals=[]
    for u in [mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025')]:
        t=2*mp.sin(u)**2
        v0=v_int('0.5',w,t)
        r=mp.sqrt(v0)
        if a<1:
            expected=h_const(e,w)/(2*r0)*u**kap
        elif a==1:
            expected=(2*e/(1-e)**mp.mpf('1.5'))*u*u*mp.log(1/u)
        else:
            expected=e*a/((a-1)*(1-e)**mp.mpf('1.5'))*u*u
        vals.append(float((r0-r)/expected))
    assert max(abs(v-1) for v in vals[-1:])<0.35,(w,vals)
    print('omega=',w,'alpha=',float(a),'kappa=',float(kap),'ratios=',vals)
print('STAR_NODE_CUSP_VERIFY_OK')
