"""Reproduce exact algebra and representative numerical checks of the rational-logistic two-cycle theorem.

Requires Python 3 and sympy. The exact polynomial identities below are valid for symbolic
parameters; the numerical samples are diagnostic only and not a substitute for the proof.
"""
import math
import sympy as sp

x, mu, lam = sp.symbols('x mu lam')
f = lambda z: mu*z*(1-z)/(1+lam*z)
H = mu**2-(3+lam)*mu-lam
Q = mu*(mu-lam)*x**2-(mu+1)*(mu-lam)*x+(mu+1)
den = (1+lam*x)*(1+lam*x+lam*mu*x*(1-x))
identity = -x*((mu+lam)*x-(mu-1))*Q/den
assert sp.cancel(f(f(x))-x-identity) == 0
assert sp.factor(sp.discriminant(Q,x)-(mu-lam)*(mu+1)*H) == 0
assert sp.factor(Q.subs(x,1)-(1+lam)) == 0

fp = sp.diff(f(x),x)
s = (mu+1)/mu
p = (mu+1)/(mu*(mu-lam))
# The symmetric derivative product is computed without substituting radicals.
u,v,S,P = sp.symbols('u v S P')
num = sp.expand(mu**2*(1-2*u-lam*u**2)*(1-2*v-lam*v**2))
den2 = sp.expand((1+lam*u)**2*(1+lam*v)**2)
def symmetric_reduction(expr):
    symmetric, rem, symbols = sp.symmetrize(expr,[u,v],formal=True)
    assert rem == 0
    return sp.factor(symmetric.subs({symbols[0][0]:s,symbols[1][0]:p}))
mult = sp.factor(symmetric_reduction(num)/symmetric_reduction(den2))
R = (mu-lam)*(mu+1)*H/(mu**2*(1+lam))
assert sp.factor(mult-(1-R)) == 0
assert sp.factor(sp.expand((mu-1)*(mu+1)*(mu**2-4*mu-1)-4*mu**2) -(mu**4-4*mu**3-6*mu**2+4*mu+1)) == 0

t = sp.symbols('t',positive=True)
mmax = (1+t)**2
assert sp.factor(R.subs({lam:t**2-1,mu:mmax})-4*(t**2+2*t+2)/(t+1)**2)==0
print('VERIFY_SYMBOLIC factorization=1 discriminant=1 boundaries=1 multiplier=1 endpoint=1 quartic=1')

for L in (0.,.1,.33,.5,.67,.9,1.):
    M1=(3+L+math.sqrt((1+L)*(9+L)))/2
    Mmax=(1+math.sqrt(1+L))**2
    def Rnum(M):return (M-L)*(M+1)*(M*M-(3+L)*M-L)/(M*M*(1+L))
    assert 1<M1<Mmax and Rnum(M1)<1e-11 and Rnum(Mmax)>2
    a,b=M1,Mmax
    for _ in range(80):
        m=(a+b)/2
        if Rnum(m)>2:b=m
        else:a=m
    M2=(a+b)/2
    assert M1<M2<Mmax and abs(Rnum(M2)-2)<1e-12
    for M in (M1+.2*(M2-M1),(M1+M2)/2,(M2+Mmax)/2):
        D=(M+1)*(M*M-(3+L)*M-L)/(M-L)
        low=(M+1-math.sqrt(D))/(2*M)
        high=(M+1+math.sqrt(D))/(2*M)
        fnum=lambda z:M*z*(1-z)/(1+L*z)
        fpnum=lambda z:M*(1-2*z-L*z*z)/(1+L*z)**2
        assert 0<low<high<1
        assert abs(fnum(low)-high)<2e-12 and abs(fnum(high)-low)<2e-12
        assert abs(fpnum(low)*fpnum(high)-(1-Rnum(M)))<2e-11
    print(f'VERIFY_NUMERIC lambda={L:.2f} mu1={M1:.11f} mu2={M2:.11f} mu_max={Mmax:.11f}')
print('VERIFY_OK exact_identities=6 lambda_cases=7 two_cycle_cases=21')
