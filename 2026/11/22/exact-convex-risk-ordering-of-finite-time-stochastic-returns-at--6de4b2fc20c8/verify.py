"""Independent finite-parameter checks for linear-return risk ordering.

Requires mpmath (the analytic theorem and its proof do not depend on this code).
"""
from mpmath import mp

mp.dps = 40
checks = 0

def close(a, b, atol=mp.mpf('1e-18'), rtol=mp.mpf('1e-15')):
    global checks
    assert abs(a-b) <= atol+rtol*max(abs(a),abs(b)), (a,b)
    checks += 1

def ispositive(x, tol=0):
    global checks
    assert x > tol, x
    checks += 1

def ig_pdf(t, ell, a, d):
    return ell/mp.sqrt(4*mp.pi*d*t**3)*mp.exp(-(ell-a*t)**2/(4*d*t))

def ig_laplace(s, ell, a, d):
    lam = 2*s/(a+mp.sqrt(a*a+4*d*s))
    return mp.exp(-ell*lam)

def call(ell,a,d,strike):
    return mp.quad(lambda t:(t-strike)*ig_pdf(t,ell,a,d),[strike,mp.inf])

ell=mp.mpf('0.8'); a=mp.mpf('3'); ds=[mp.mpf('.25'),mp.mpf('1.5')]
for d in ds:
    close(mp.quad(lambda t:ig_pdf(t,ell,a,d),[0,ell/a,2*ell/a,mp.inf]),1)
    close(mp.quad(lambda t:t*ig_pdf(t,ell,a,d),[0,ell/a,2*ell/a,mp.inf]),ell/a)
    close(mp.quad(lambda t:t*t*ig_pdf(t,ell,a,d),[0,ell/a,2*ell/a,mp.inf])-(ell/a)**2,2*d*ell/a**3)
    for s in [mp.mpf('.1'),mp.mpf('1'),mp.mpf('3')]:
        close(mp.quad(lambda t:mp.exp(-s*t)*ig_pdf(t,ell,a,d),[0,ell/a,2*ell/a,mp.inf]),ig_laplace(s,ell,a,d))
for z in [mp.mpf('.01'),mp.mpf('.1'),mp.mpf('.3'),mp.mpf('.7'),mp.mpf('1.5'),mp.mpf('3')]:
    ispositive(call(ell,a,ds[1],z)-call(ell,a,ds[0],z),mp.mpf('1e-22'))

D=mp.mpf('1'); L=mp.mpf('1'); x=mp.mpf('.3'); rate=mp.mpf('2')

def green(t,y):
    k=mp.sqrt(t/D)
    return mp.sinh(k*min(x,y))*mp.sinh(k*(L-max(x,y)))/(D*k*mp.sinh(k*L))

def q(t):
    k=mp.sqrt(t/D)
    return (mp.sinh(k*x)+mp.sinh(k*(L-x)))/mp.sinh(k*L)

def H(s,d):
    return rate*(mp.quad(lambda y:green(rate+s,y)*ig_laplace(s,abs(y-x),a,d),[0,x])+
                 mp.quad(lambda y:green(rate+s,y)*ig_laplace(s,abs(y-x),a,d),[x,L]))

def T_laplace(s,d):
    return q(rate+s)/(1-H(s,d))

q0=q(rate)
EZ=rate/q0*(mp.quad(lambda y:green(rate,y)*(x-y),[0,x])+mp.quad(lambda y:green(rate,y)*(y-x),[x,L]))
close(H(0,ds[0]),1-q0)
close(H(0,ds[1]),1-q0)
close(T_laplace(0,ds[0]),1)
close(T_laplace(0,ds[1]),1)
mean0=(1-q0)/(rate*q0)+EZ/a
for d in ds:
    close(-mp.diff(lambda s:T_laplace(s,d),0),mean0,mp.mpf('1e-14'))
    for s in [mp.mpf('.02'),mp.mpf('.2'),mp.mpf('1'),mp.mpf('2')]:
        close(T_laplace(s,d),q(rate+s)/(1-H(s,d)))
for s in [mp.mpf('.02'),mp.mpf('.2'),mp.mpf('1'),mp.mpf('2')]:
    ispositive(T_laplace(s,ds[1])-T_laplace(s,ds[0]))
var1=mp.diff(lambda s:T_laplace(s,ds[0]),0,2)-mean0*mean0
var2=mp.diff(lambda s:T_laplace(s,ds[1]),0,2)-mean0*mean0
close(var2-var1,2*(ds[1]-ds[0])*EZ/a**3,mp.mpf('1e-13'))
close(2*(ds[1]-ds[0])*EZ/a**3,2*(ds[1]-ds[0])*(a*EZ)/a**4)
print('PASS',checks,'independent quadrature / transform assertions')
print('q =',mp.nstr(q0,20),'E Z =',mp.nstr(EZ,20))
print('mean =',mp.nstr(mean0,20))
print('var(d1) =',mp.nstr(var1,20),'var(d2) =',mp.nstr(var2,20))
print('variance change =',mp.nstr(var2-var1,20))
