"""Independent numerical diagnostics for a two-periodic Jacobi edge-binding law.
Requires Python 3 and mpmath. Diagnostics are not an infinite-dimensional proof.
"""
import mpmath as mp
mp.mp.dps = 55
checks = 0

def check(ok, info):
    global checks
    if not ok:
        raise AssertionError(info)
    checks += 1

def parameters(a, b, parity):
    d = a*b/(a+b)
    p = a if parity == 0 else b
    be = -a*b*(4*a+b)/(2*(a+b)**2)
    bo = -a*b*(3*a+2*b)/(2*(a+b)**2)
    return d, p, be if parity == 0 else bo

def threshold(m, a, b):
    return a * mp.sqrt(1 + 2*b/(m*(a+b)+2*a)) if m%2==0 else b*mp.sqrt(1+2*a/((m+1)*(a+b)))

def c_squared(k, m, a, b):
    if m%2==0:
        return a*a*(1+b*mp.expm1(4*k)/(a*(mp.exp(2*k)-mp.exp(-2*(m+1)*k))+b*(-mp.expm1(-2*m*k))))
    return b*b*(1+a*mp.expm1(4*k)/((a+b*mp.exp(2*k))*(-mp.expm1(-2*(m+1)*k))))

def outlier(m, a, b, xi):
    d, p, B = parameters(a,b,m%2)
    c = p+d/m+xi/m**2
    if c <= threshold(m,a,b):
        return None
    lo, hi = mp.mpf('0'), mp.mpf('0.01')
    while c_squared(hi,m,a,b)<c*c:
        hi*=2
    for _ in range(145):
        mid=(hi+lo)/2
        if c_squared(mid,m,a,b)<c*c:lo=mid
        else:hi=mid
    k=(lo+hi)/2
    edge = (a+b)/2
    gap = mp.sqrt(a*a+b*b+2*a*b*mp.cosh(2*k))/2-edge
    return k,gap

for aa,bb in [('1','2'),('3','1'),('0.3','2.4')]:
    a,b=mp.mpf(aa),mp.mpf(bb)
    for parity in (0,1):
        d,p,B=parameters(a,b,parity)
        for m in (100+parity, 250+parity, 500+parity):
            check(m%2==parity,('parity',m))
            C=threshold(m,a,b)
            check(abs(m*m*(C-p-d/m)-B)<mp.mpf('0.05'),('threshold',m,a,b))
            for xi in (B-mp.mpf('0.3'),B+mp.mpf('0.3'),B+mp.mpf('1.5')):
                result=outlier(m,a,b,xi)
                should_exist=xi>B
                check((result is not None)==should_exist,('existence',m,a,b,xi,result))
                if result is not None:
                    k,gap=result
                    gamma=(xi-B)/d
                    # Check convergence coarsely at finite depth, two asymptotic scales.
                    check(abs(m*m*k-gamma)<mp.mpf('0.12')*max(1,gamma),('kappa',m,a,b,xi,m*m*k,gamma))
                    check(abs(m**4*gap-(xi-B)**2/d) < mp.mpf('0.12')*max(1,(xi-B)**2/d),('gap',m,a,b,xi,m**4*gap,(xi-B)**2/d))
print('PARITY_QUARTIC_DIAGNOSTIC_OK',checks)
