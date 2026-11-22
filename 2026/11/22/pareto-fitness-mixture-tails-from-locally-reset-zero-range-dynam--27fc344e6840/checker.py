"""Independent numerical checks of the two Laplace transforms and moment limits.
Requires mpmath; pure stochastic-model mathematical reproducibility.
"""
from mpmath import mp
mp.dps = 35

def limiting_phi(u):
    u=mp.mpf(u)
    return mp.exp(-mp.exp(1/u)*mp.e1(1/u))

def integral_phi(u):
    u=mp.mpf(u)
    return mp.exp(-mp.quad(lambda t:mp.exp(-t)*mp.log1p(u*t),[0,1,10,mp.inf]))

def finite_phi(u,x,nu,C=1,alpha=2,beta=mp.mpf('0.1')):
    x=mp.mpf(x);nu=mp.mpf(nu);C=mp.mpf(C)
    l=1-x; r=C*x**nu;delta=x
    q=lambda z:(alpha+1)*z**alpha
    denom=lambda z:z+C*z**nu
    I=mp.quad(lambda z:(1-z)/denom(z),[0,mp.mpf('.01'),1])
    J=mp.quad(lambda z:q(z)/denom(z),[0,mp.mpf('.01'),1])
    rho=I/(1-beta*J)
    A=l+beta*rho*q(x)
    integrand=lambda t:mp.exp(-t)*mp.log1p(l*(-mp.expm1(-delta*t/r))/delta * (-mp.expm1(-mp.mpf(u)*r)))
    return mp.exp(-A/l*mp.quad(integrand,[0,1,10,mp.inf])),rho

checks=0
for u in (mp.mpf('.15'),mp.mpf('.6'),mp.mpf('1'),mp.mpf('3'),mp.mpf('10')):
    e=abs(limiting_phi(u)-integral_phi(u))
    assert e <mp.mpf('1e-27'),(u,e)
    checks+=1
for u in (mp.mpf('.2'),mp.mpf('1'),mp.mpf('3')):
    value,rho=finite_phi(u,mp.mpf('1e-9'),mp.mpf('0.65'))
    err=abs(value-limiting_phi(u))
    assert 0<rho<20 and err<mp.mpf('.003'),(u,err,rho)
    checks+=1
# Factorial cumulants at critical fitness: k!*(k-1)!; moments Bell polynomial.
kappa={k:mp.factorial(k)*mp.factorial(k-1) for k in range(1,5)}
assert kappa[1]==1 and kappa[2]==2 and kappa[3]==12
assert kappa[2]+kappa[1]**2==3
assert kappa[3]+3*kappa[2]*kappa[1]+kappa[1]**3==19
checks+=5
# Substitution t=1/nu in regularly varying mixture.
for nu in (mp.mpf('.35'),mp.mpf('.5'),mp.mpf('.67'),mp.mpf('.9')):
    a=1/nu
    assert a>1 and (a*nu-1)**2<mp.mpf('1e-40')
    checks+=1
print('PASS: %d numeric/algebraic consistency assertions' % checks)
print('Phi(1)=',mp.nstr(limiting_phi(1),22))
print('Tail amplitudes: nu=1/2 -> 3/C^2; nu=1/3 -> 19/C^3.')
