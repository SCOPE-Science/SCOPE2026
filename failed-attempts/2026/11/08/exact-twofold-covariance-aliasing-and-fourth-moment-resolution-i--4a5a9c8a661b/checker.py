"""Symbolic and independent matrix checks for a two-state intermittently confined diffusion."""
import sympy as sp
import mpmath as mp

k, nu, D, t = sp.symbols('k nu D t', positive=True)
S = k + 2*nu
P = k*nu
Q = sp.Matrix([[-nu,nu],[nu,-nu-k]])
assert sp.simplify(Q**2 + S*Q + P*sp.eye(2)) == sp.zeros(2)

u20, u21 = sp.symbols('u20 u21')
sol2 = sp.solve([2*D + nu*(u20-u21)-2*k*u21, 2*D + nu*(u21-u20)], [u20,u21])
# These equations are for conditional moments E[X^2 | S=s] (not joint moments).
assert sp.simplify(sol2[u21] - 2*D/k) == 0
assert sp.simplify(sol2[u20] - (2*D/k+2*D/nu)) == 0
v = sp.Matrix([sol2[u20]/2, sol2[u21]/2])
m2 = sp.factor(sum(v))
assert sp.simplify(m2 - D*S/P) == 0
assert sp.simplify((sp.ones(1,2)*Q*v)[0] + D) == 0
assert sp.simplify((sp.ones(1,2)*Q**2*v)[0]) == 0
assert sp.simplify((sp.ones(1,2)*Q**3*v)[0] - D*P) == 0

w0,w1=sp.symbols('w0 w1')
sol4=sp.solve([12*D*sol2[u21]+nu*(w0-w1)-4*k*w1,12*D*sol2[u20]+nu*(w1-w0)],[w0,w1])
m4=sp.factor((sol4[w0]+sol4[w1])/2)
assert sp.simplify(m4-6*D**2/k**2*(2+3*k/nu+2*k**2/nu**2)) == 0
assert sp.simplify(m4-3*D**2/P**2*(S**2+3*S*k-4*P)) == 0

kd, nud=2*nu,k/2
assert sp.simplify(S.subs({k:kd,nu:nud}, simultaneous=True)-S) == 0
assert sp.simplify(P.subs({k:kd,nu:nud}, simultaneous=True)-P) == 0
m4dual=sp.factor(m4.subs({k:kd,nu:nud},simultaneous=True))
assert sp.simplify(m4-m4dual-9*D**2*S/P**2*(k-kd))==0

k_inv=sp.factor((m4*P**2/(3*D**2)-S**2+4*P)/(3*S))
assert sp.simplify(k_inv-k)==0

mp.mp.dps=60
for kk, nn, dd in [(1,1,1), (2,sp.Rational(1,2),1), (sp.Rational(5,3),sp.Rational(7,4),sp.Rational(9,5)),(sp.Rational(1,3),3,2),(8,2,1),(5,1,sp.Rational(2,3))]:
    kk,nn,dd=map(sp.Rational,(kk,nn,dd))
    sv=kk+2*nn;pv=kk*nn
    ul=(mp.mpf(str(sv))-mp.sqrt(mp.mpf(str(sv**2-4*pv))))/2
    vl=(mp.mpf(str(sv))+mp.sqrt(mp.mpf(str(sv**2-4*pv))))/2
    # mpmath rational helper
    def f(q):return mp.mpf(int(sp.numer(q)))/mp.mpf(int(sp.denom(q)))
    ul=(f(sv)-mp.sqrt(f(sv**2-4*pv)))/2
    vl=(f(sv)+mp.sqrt(f(sv**2-4*pv)))/2
    DD=f(dd)
    def closed(tt):return DD/(vl-ul)*(vl/ul*mp.exp(-ul*tt)-ul/vl*mp.exp(-vl*tt))
    QQ=mp.matrix([[-f(nn),f(nn)],[f(nn),-f(nn)-f(kk)]])
    V=mp.matrix([[f(dd/kk+dd/nn)],[f(dd/kk)]])
    for T in [0,mp.mpf('0.01'),mp.mpf('.14'),mp.mpf('1.25'),mp.mpf('5')]:
        Cmat=(mp.matrix([[1,1]])*mp.expm(QQ*T)*V)[0]
        assert abs(Cmat-closed(T)) < mp.mpf('1e-48'), (kk,nn,T)
        # Compare dual parameter model from independent generator.
        k2=2*nn;n2=kk/2
        Q2=mp.matrix([[-f(n2),f(n2)],[f(n2),-f(n2)-f(k2)]])
        V2=mp.matrix([[f(dd/k2+dd/n2)],[f(dd/k2)]])
        C2=(mp.matrix([[1,1]])*mp.expm(Q2*T)*V2)[0]
        assert abs(Cmat-C2) < mp.mpf('1e-48')
    assert abs(closed(mp.mpf('0'))-DD*f(sv/pv))<mp.mpf('1e-48')
    if kk!=2*nn:
        assert m4.subs({k:kk,nu:nn,D:dd})!=m4.subs({k:2*nn,nu:kk/2,D:dd})
print('PASS symbolic moment generator, covariance ODE, duality, exact inverse, and 30 independent matrix-exponential comparisons')
print('Example (k,nu,D)=(1,1,1) versus (2,1/2,1): C(0)=3, C\'(0)=-1, C\'\'\'(0)=1, m4=42 versus 69')
