"""Numerical and algebraic checks for noisy-trap stationary covariance.

Requires mpmath. Run with: python checker.py
The argument is a mathematical consistency diagnostic, not an infinite proof.
"""
import mpmath as mp
mp.mp.dps = 48


def integ(a, b, f):
    return mp.quad(f, [a, b])


def raw(m, dk, kappa, dx, t):
    q = dk / m**2
    g = dk / m**3
    z = mp.exp(-m*t)
    def var(s):
        return 2*q*(s-(1-mp.exp(-m*s))/m)
    def integrand(u):
        cov = g*(1-mp.exp(-m*u))*(1-z)
        exponent = -kappa*(t+2*u)+2*var(u)+var(t)/2+2*cov
        return mp.exp(exponent)
    return 2*dx*mp.quad(integrand, [0, 1, mp.inf])


def moments(lam, c):
    # Uniformizing substitution y=x**(1/lam) removes the endpoint singularity.
    y = lambda x: mp.power(x, 1 / lam)
    w = lambda x: mp.exp(-c * (1 - y(x)))
    den = mp.quad(w, [0, 1])
    mean = mp.quad(lambda x: y(x) * w(x), [0, 1]) / den
    var = mp.quad(lambda x: (y(x) - mean)**2 * w(x), [0, 1]) / den
    return den / lam, mean, var


def compact(m, dk, kappa, dx, t):
    q=dk/m**2; b=dk/m**3; lam=2*(kappa-2*q)/m
    z=mp.exp(-m*t); c=2*b*(1+z)
    J_scaled,mean,var=moments(lam,c)
    C=2*dx/m*mp.exp(-(kappa-q)*t-3*b-b*z+c)*J_scaled
    h=kappa-q+q*z*(2*mean-1)
    return C,h,mean,var


def close(a, b, tolerance=mp.mpf('1e-19')):
    if abs(a-b) > tolerance*max(1,abs(a),abs(b)):
        raise AssertionError((mp.nstr(a,20),mp.nstr(b,20)))


count=0
for m,dk,kappa,dx in [
    (mp.mpf('1'),mp.mpf('.6'),mp.mpf('1.45'),mp.mpf('1')),
    (mp.mpf('2'),mp.mpf('1'),mp.mpf('1.6'),mp.mpf('.7')),
    (mp.mpf('.8'),mp.mpf('.045'),mp.mpf('.4'),mp.mpf('1.25')),
]:
    assert kappa > 2*dk/m**2
    for t in map(mp.mpf,['0','.4','1.3','3']):
        C,h,_,_=compact(m,dk,kappa,dx,t)
        close(C,raw(m,dk,kappa,dx,t));count+=1
        close(-mp.diff(lambda s:mp.log(compact(m,dk,kappa,dx,s)[0]),t), h);count+=1
        assert C>0 and h>0;count+=1
    close(-mp.diff(lambda s:compact(m,dk,kappa,dx,s)[0],mp.mpf(0)),dx);count+=1

# Example of an interior crossing of logarithmic relaxation rates.
m=mp.mpf(1);dk=mp.mpf('.6');kappa=mp.mpf('1.45');dx=mp.mpf(1)
q=dk/m**2; b=dk/m**3; lam=2*(kappa-2*q)/m
assert lam==mp.mpf('.5')
fun=lambda c: moments(lam,c)[1]-mp.mpf('.5')
cstar=mp.findroot(fun,(mp.mpf('1.5'),mp.mpf('2')))
assert 2*b<cstar<4*b
tr=mp.log(2*b/(cstar-2*b))/m
close(compact(m,dk,kappa,dx,tr)[1],kappa-q);count+=1
assert compact(m,dk,kappa,dx,tr/2)[1] > kappa-q
assert compact(m,dk,kappa,dx,tr*2)[1] < kappa-q
count+=2
close(cstar,mp.mpf('1.6920310427012196098012525033445'));count+=1
close(tr,mp.mpf('0.89153502635300631235259398607954'));count+=1

# The two same-parameter phase boundaries are characterized by a unique root.
for lam in map(mp.mpf,['.25','.5','.75']):
    fun=lambda c: moments(lam,c)[1]-mp.mpf('.5')
    cstar=mp.findroot(fun,(mp.mpf('.001'),mp.mpf('6')))
    assert cstar>0
    for b in [cstar/5,cstar/3,cstar*2/3]:
        for z in map(mp.mpf,['.001','.2','.5','.999']):
            s=2*b*(1+z); e=moments(lam,s)[1]
            sign=mp.sign(2*e-1)
            if abs(s-cstar)<mp.mpf('1e-40'):
                assert abs(e-mp.mpf('.5'))<mp.mpf('1e-40')
            else:
                assert sign==mp.sign(s-cstar)
            count+=1

# Strict monotonicity of the exponential-tilted mean via its variance.
for lam in map(mp.mpf,['.1','.6','1','2.3']):
    for c in map(mp.mpf,['.1','.5','2']):
        den,E,V=moments(lam,c)
        close(mp.diff(lambda u: moments(lam,u)[1],c),V);count+=1

# Non-degenerate long-lag coefficient and quadratic critical cancellation.
lam=mp.mpf('.5');root=mp.findroot(lambda c:moments(lam,c)[1]-.5,(1,3))
b=root/2; m=mp.mpf(1);q=b*m;dk=q*m**2;kappa=2*q+m*lam/2
_,E,V=moments(lam,2*b)
close(E,mp.mpf('.5'));count+=1
for t in [8,10,12]:
    h=compact(m,dk,kappa,1,mp.mpf(t))[1]
    ratio=(h-(kappa-q))/mp.exp(-2*m*t)
    close(ratio/(4*q*b*V),mp.mpf(1),mp.mpf('.002'));count+=1

print('PASS',count,'independent quadrature, derivative, sign, root, and critical asymptotic checks')
