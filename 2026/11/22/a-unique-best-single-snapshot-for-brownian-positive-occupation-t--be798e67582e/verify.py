"""Reproduce the exact Brownian occupation snapshot calculations.

Requires mpmath 1.3.0. Numerical work checks exact identities but is not
an exhaustive proof of uniqueness; see the monotonicity proof in RESULT.md.
"""
import mpmath as m

m.mp.dps = 45
P = m.pi
C = P * (2*m.log(2)-1)/4


def H(r):
    z = m.sqrt(m.expm1(r))
    return 2*(z-m.atan(z))


def G(r):
    return H(2*r)-2*H(r)


def AA(x):
    return (m.mpf(3)/2*x*m.sqrt(1-x*x)
            +m.asin(x)/2-x*x*m.acos(x))


def DD(x):
    return (m.asin(m.sqrt(x))/4-2*x*x*m.acos(m.sqrt(x))
            +(10*x-1)*m.sqrt(x*(1-x))/4)


def Vclosed(x):
    return (AA(x)-DD(x)-C*x*x/2)/P


def Vintegrals(x):
    j1 = 2*m.quad(lambda s: m.sqrt(1-s*s)-s*m.acos(s), [0,x])
    j2 = 4*m.quad(lambda s: m.sqrt(s*(1-s))-s*m.acos(m.sqrt(s)), [0,x])
    return (j1-j2-C*x*x/2)/P


def series(x, count=2000):
    # arcsin(z)=sum c_n z^(2n+1)
    val=m.mpf(0)
    c=m.mpf(1)
    for n in range(count):
        if n==0:
            a=2*m.sqrt(x)-4*x/3
        else:
            a=x/(n+m.mpf('1.5'))+(x-x**(n+m.mpf('.5')))/(n-m.mpf('.5'))
        val+=c*a*a
        c*=(2*n+1)**2/(2*m.mpf(n+1)*(2*n+3))
    return val/(2*P)


def tail_bound(N):
    a=m.mpf(N)-m.mpf('0.5')
    return (a**(-3)+a**(-2)/2)/P


# Monotonic scalar root; brackets also independently check the claimed digits.
lo=m.mpf('0.1'); hi=m.mpf('1.0')
assert G(lo)<C<G(hi)
for _ in range(270):
    mid=(lo+hi)/2
    if G(mid)<C: lo=mid
    else: hi=mid
r=(lo+hi)/2
x=m.exp(-r)
assert abs(G(r)-C)<m.mpf('1e-40')
assert abs(x-m.mpf('0.5895851109072423924723090754'))<m.mpf('1e-27')

# Elementary derivative and integral identities on unrelated test inputs.
for q in (m.mpf('.1'),m.mpf('.3'),m.mpf('.8'),m.mpf('1.5')):
    assert abs(m.diff(H,q)-m.sqrt(m.expm1(q)))<m.mpf('1e-40')
    assert abs(m.diff(G,q)-2*(m.sqrt(m.expm1(2*q))-m.sqrt(m.expm1(q))))<m.mpf('1e-39')
for z in (m.mpf('.1'),m.mpf('.3'),m.mpf('.5'),m.mpf('.6'),m.mpf('.9'),m.mpf('1.0'),x):
    assert abs(Vintegrals(z)-Vclosed(z))<m.mpf('1e-38')
    assert abs(series(z,1400)-Vclosed(z))<tail_bound(1400)

# Confirm the derivative sign and exact endpoint benchmark.
for rtest in (m.mpf('.1'),m.mpf('.3'),m.mpf('.9'),m.mpf('1.1')):
    expect=m.exp(-2*rtest)*(C-G(rtest))/P
    actual=m.diff(lambda y:Vclosed(m.exp(-y)),rtest)
    assert abs(actual-expect)<m.mpf('1e-39')
assert abs(Vclosed(1)-(1-m.log(2))/4)<m.mpf('1e-40')
assert abs((m.mpf(1)/8)-m.mpf('0.125'))<m.mpf('1e-40')

risk=m.mpf(1)/8-Vclosed(x)
print('unique root r =',m.nstr(r,35))
print('optimal x =',m.nstr(x,35))
print('captured variance =',m.nstr(Vclosed(x),35))
print('Bayes minimum risk =',m.nstr(risk,35))
print('fraction of occupation variance explained =',m.nstr(8*Vclosed(x),35))
print('terminal captured variance =',m.nstr(Vclosed(m.mpf(1)),35))
print('finite numerical tests and exact derivative residuals: PASS')
