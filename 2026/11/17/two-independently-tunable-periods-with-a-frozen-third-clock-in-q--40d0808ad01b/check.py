"""Reproducibility checks for three fixed circular limit cycles.

Requires Python 3, mpmath and sympy. These finite computations support, but do not
replace, the analytic submersion proof in RESULT.md.
"""
import mpmath as mp
mp.mp.dps = 55


def geometry(r, s):
    a = 1 + r*r - s*s
    disc = a*a - 4*r*r
    assert disc > 0
    I = 2*mp.pi/mp.sqrt(disc)
    rho = (a - mp.sign(a)*mp.sqrt(disc))/2
    return a, I, rho


def derivatives(r, s, lam, beta, gamma, alpha=0):
    a, _, _ = geometry(r, s)
    def B(th):
        return gamma + lam*r*r + alpha*r*mp.cos(th) + beta*r*mp.sin(th)
    def f3(th):
        return abs(a - 2*r*mp.cos(th))
    return tuple(mp.quad(fun, [0, mp.pi, 2*mp.pi]) for fun in [
        lambda th: -r*mp.cos(th)/(f3(th)*B(th)**2),
        lambda th: -1/(f3(th)*B(th)**2),
    ])


def periods(r, s, lam, beta, gamma, alpha=0):
    a, _, _ = geometry(r, s)
    return mp.quad(lambda th: 1/(abs(a-2*r*mp.cos(th)) *
                     (gamma+lam*r*r+alpha*r*mp.cos(th)+beta*r*mp.sin(th))),
                   [0,mp.pi,2*mp.pi])


def three_circle_period(r1, r2, s, lam):
    h = lambda a: mp.sign(a)/mp.sqrt(a*a-4*s*s)
    a1, a2 = 1+s*s-r1*r1,1+s*s-r2*r2
    return 2*mp.pi*abs(h(a2)-h(a1))/(abs(lam)*(r2*r2-r1*r1))


# Representative geometry with the off-centre disk external to the concentric pair.
s, r1, r2 = map(mp.mpf, ['0.25', '0.25', '0.5'])
lam, beta, gamma = map(mp.mpf, ['1', '0.1', '10'])
assert 0 < r1 < r2 and r2+s < 1
u1, v1 = derivatives(r1,s,lam,beta,gamma)
u2, v2 = derivatives(r2,s,lam,beta,gamma)
det = u1*v2-v1*u2
assert det < mp.mpf('-0.00138') and det > mp.mpf('-0.00139')
T1,T2 = (periods(r,s,lam,beta,gamma) for r in [r1,r2])
T3 = three_circle_period(r1,r2,s,lam)
assert abs(T1-mp.mpf('0.72101547737624116926')) < mp.mpf('1e-18')
assert abs(T2-mp.mpf('0.95716091637545473617')) < mp.mpf('1e-18')
assert abs(T3-mp.mpf('13.62997409314274704357')) < mp.mpf('1e-18')

# Test asymptotic Jacobian coefficient for exterior, nested, mixed branches.
for s,r1,r2 in [
    ('0.25','0.25','0.5'),
    ('0.25','0.5','2.0'),
    ('1.5','0.25','3.0'),
    ('1.5','2.7','4.0'),
]:
    s,r1,r2 = map(mp.mpf,[s,r1,r2]); lam=mp.mpf('1'); beta=mp.mpf('0.1')
    _,I1,rho1 = geometry(r1,s)
    _,I2,rho2 = geometry(r2,s)
    assert rho1 != rho2
    coefficient = I1*I2*(rho1-rho2)
    gam = mp.mpf('2000')
    da1,dg1 = derivatives(r1,s,lam,beta,gam)
    da2,dg2 = derivatives(r2,s,lam,beta,gam)
    empirical = gam**4*(da1*dg2-dg1*da2)
    assert abs(empirical/coefficient-1) < mp.mpf('0.15'), (s,r1,r2,empirical,coefficient)
    print('radius pair',mp.nstr(r1,4),mp.nstr(r2,4),
          's=',mp.nstr(s,4),'scaled ratio=',mp.nstr(empirical/coefficient,12))

print('TESTS PASS; representative determinant',mp.nstr(det,25))
print('T1, T2, frozen T3:', *(mp.nstr(z,22) for z in [T1,T2,T3]))

# Exact polynomial identities required for circle invariance and cofactors.
import sympy as sp
x,y = sp.symbols('x y')
r1s,r2s,ss,ls,als,bes,gs = sp.symbols(
    'r1 r2 s lam alpha beta gamma', real=True)
f1 = x*x + y*y - r1s*r1s
f2 = x*x + y*y - r2s*r2s
f3 = (x-1)**2 + y*y - ss*ss
B = ls*(x*x+y*y) + als*x + bes*y + gs
A = ls*f1*f2 - f3*B
P, Q = y*A, ls*f1*f2 - x*A
for f,k in [(f1,2*ls*y*f2),(f2,2*ls*y*f1),(f3,2*y*B)]:
    assert sp.expand(sp.diff(f,x)*P+sp.diff(f,y)*Q-k*f) == 0
print('Exact symbolic invariance checks PASS')
