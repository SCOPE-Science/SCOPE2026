"""Numerical diagnostics for the Brownian proportional-reset stationary density.

Requirements: Python 3.9+ and mpmath 1.3+. The mathematical proof does not
rely on these finite numerical integrations.
"""
import mpmath as mp

mp.mp.dps = 42
CHECKS = 0

def check(ok, note):
    global CHECKS
    if not ok:
        raise AssertionError(note)
    CHECKS += 1

def rel_close(a, b, tol=mp.mpf('1e-16')):
    return abs(a-b) <= tol*max(1,abs(a),abs(b))

def poch(x, q, n):
    return mp.fprod(1-x*q**j for j in range(n))

def stationary_phi(k, c):
    # Direct characteristic product; 90 terms gives tiny truncation for c <= 0.6.
    return mp.fprod(1+(c**j*k)**2 for j in range(90))**(-1)

def stationary_derivative(n, c):
    f=lambda k:(k**(2*n))*stationary_phi(k,c)
    return ((-1)**n/mp.pi)*mp.quad(f,[0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192])

def closed_derivative(n, c, p0):
    return (-1)**n*p0*c**(-n*n)*mp.fprod(1-c**(2*j+1) for j in range(n))

for c0 in ('0.5','0.6'):
    c=mp.mpf(c0)
    q=c*c
    p0=mp.mpf('0.5')*poch(c,q,170)/poch(q,q,170)
    # Exact published Dirichlet/Laplace series at zero.
    sm=mp.fsum(((-1)**j)*c**(j*j)/poch(q,q,j) for j in range(90))
    p0_series=sm/(2*poch(q,q,170))
    check(rel_close(p0,p0_series,mp.mpf('1e-25')), 'q-binomial height')
    for n in range(5):
        a=stationary_derivative(n,c)
        b=closed_derivative(n,c,p0)
        check(rel_close(a,b,mp.mpf('1e-14')), ('Fourier derivative',c0,n, mp.nstr(a,15),mp.nstr(b,15)))
    # All-order recurrence tested at 12 consecutive derivative orders.
    for n in range(12):
        b=closed_derivative(n,c,p0)
        nxt=closed_derivative(n+1,c,p0)
        check(rel_close(nxt,(1-c**(-(2*n+1)))*b,mp.mpf('1e-24')), 'pantograph jet recurrence')
    # Sharp normalized derivative product approaches positive limit.
    limit=poch(c,q,170)
    for n in (1,3,8,20,50):
        ratio=(-1)**n*closed_derivative(n,c,p0)/p0*c**(n*n)
        check(rel_close(ratio,poch(c,q,n),mp.mpf('1e-25')), 'normalized derivative')
        check(ratio >= limit and ratio > 0,'positive product tail')
print('PASS:',CHECKS,'symbolic-product and Fourier-integral diagnostic assertions')
