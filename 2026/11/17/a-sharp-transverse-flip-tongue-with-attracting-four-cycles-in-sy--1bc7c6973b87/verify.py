"""Reproduce analytic Taylor identities and near-cusp numerical checks.
Usage: python verify.py (requires SymPy and mpmath; see requirements.txt).
Numerical fixed points check examples, not universal existence.
"""
import sympy as sp
import mpmath as mp

d = sp.symbols('d', positive=True)
q = sp.sqrt(2)
a = d*(q-1)
b = d*(q+1)
k = q/d
Ea = (q+1)/(q-1)
Eb = 1/Ea

def A1(s,e): return e*(1-s)
def B(s,e): return e*(s*k*k/2-k)
def C(s,e): return e*(1-k*s)
def C1(s,e): return e*(k*s-k-1)
def D(s,e): return e*(k*k/2-s*k**3/6)

m = (1-a)*(1-b)
H = A1(b,Eb)*B(a,Ea) + B(b,Eb)*C(a,Ea)**2
P = C1(b,Eb)*A1(a,Ea)*C(a,Ea)+C(b,Eb)*C1(a,Ea)
T = C1(b,Eb)*B(a,Ea)*C(a,Ea)+C(b,Eb)*D(a,Ea)+D(b,Eb)*C(a,Ea)**3
gamma = sp.cancel(T+P*H/(1-m))
target = 2*((2+q)*d*d + 6*(1+q)*d+8+4*q)/(3*d*d*(8-d*d))
for name,lhs,rhs in [
    ('H',H,1+q),('P',P,4+3*q-(1+q)*d),
    ('T',T,(2+q-(9+6*q)*d)/(3*d*d)),('gamma',gamma,target)]:
    assert sp.simplify(sp.radsimp(lhs-rhs)) == 0, name
print('EXACT_TAYLOR_OK identities=4')

mp.mp.dps=60
d0=2*mp.asinh(1)
h0=mp.sqrt(2)*d0
k0=mp.sqrt(2)/d0
mm=(d0-mp.sqrt(2))**2-1
ge=mp.mpf(str(sp.N(target.subs(d,sp.N(2*sp.asinh(1),60)),50)))
assert -1<mm<1 and mp.mpf('2.18')<ge<mp.mpf('2.19') and 0<k0<1
print('CUSP_OK d0=',mp.nstr(d0,14),'gamma=',mp.nstr(ge,14),'tangent=',mp.nstr(mm,12))
for delta_d in [mp.mpf('0.0001'),mp.mpf('0.001'),mp.mpf('0.01')]:
    dd=d0+delta_d
    hh=dd/mp.tanh(dd/2)
    aa=hh-dd
    kk=mp.sinh(dd)/(2*dd)
    DD=mp.sinh(dd/2)**2-1
    def F(s,v):
        e=mp.exp(hh-s)
        return e*(s*mp.cosh(kk*v)-v*mp.sinh(kk*v)), e*(v*mp.cosh(kk*v)-s*mp.sinh(kk*v))
    def G(s,v): return F(*F(s,v))
    initial_v=mp.sqrt(DD/ge)
    ss,vv=mp.findroot(lambda s,v:(G(s,v)[0]-s,G(s,v)[1]+v),(aa+DD,initial_v))
    assert vv>0 and mp.fabs(vv-initial_v)<mp.mpf('.002')
    GS=G(ss,vv)
    assert mp.fabs(GS[0]-ss)<mp.mpf('1e-45') and mp.fabs(GS[1]+vv)<mp.mpf('1e-45')
    A=mp.matrix([[mp.diff(lambda s:G(s,vv)[0],ss),mp.diff(lambda v:G(ss,v)[0],vv)],
                 [mp.diff(lambda s:G(s,vv)[1],ss),mp.diff(lambda v:G(ss,v)[1],vv)]])
    # Eigenvalues of D(S G), whose square gives F^4 multipliers.
    Bmat=mp.matrix([[A[0,0],A[0,1]],[-A[1,0],-A[1,1]]])
    ev=mp.eig(Bmat,left=False,right=False)
    assert all(mp.fabs(t)<1 for t in ev)
    positivity=(ss>vv) and (F(ss,vv)[0]>mp.fabs(F(ss,vv)[1]))
    assert positivity
    print('EXCHANGE_4_OK delta_d=',mp.nstr(delta_d,6),'v=',mp.nstr(vv,12),'return_radii=',','.join(mp.nstr(abs(z)**2,10) for z in ev))
print('VERIFY_OK exact_taylor=4 local_orbits=3')
