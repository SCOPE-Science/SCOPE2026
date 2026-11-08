"""Independent numerical checks for Gaussian-derivative two-tone STFT zeros.
Only Python's standard library is required. Analytical proof is in RESULT.md.
"""
from math import exp, sqrt, log, atanh, pi, cos, sin
from cmath import exp as cexp


def hermite_prob(n, x):
    if n == 0: return 1.0
    u, v = 1.0, x
    for j in range(1, n):
        u, v = v, x*v - j*u
    return v


def H(n, c):
    if c <= n: return 0.0
    v = sqrt(1-n/c)
    return 2*(c*v - n*atanh(v))


def F(u, n, c, ell):
    return ell+n*log(abs((u-1)/(u+1)))+2*c*u


def fp(u, n, c):
    return 2*c+2*n/(u*u-1)


def bisect(fn, a, b, steps=100):
    fa, fb = fn(a), fn(b)
    assert fa * fb < 0, (a,b,fa,fb)
    for _ in range(steps):
        m = (a+b)/2
        if fn(m) * fa <= 0: b=m
        else: a=m; fa=fn(m)
    return (a+b)/2


def predicted_roots(n,c,ell):
    B = 5+abs(ell)/c+3*n/c
    intervals = [(-B,-1-1e-12),(1+1e-12,B)]
    if c>n:
        v=sqrt(1-n/c)
        intervals += [(-1+1e-12,-v),(-v,v),(v,1-1e-12)]
    else: intervals += [(-1+1e-12,1-1e-12)]
    out=[]
    for a,b in intervals:
        if F(a,n,c,ell)*F(b,n,c,ell)<0:
            out.append(bisect(lambda u:F(u,n,c,ell),a,b))
    return sorted(out)


def simpson_complex(fn,a,b,count=4800):
    assert count%2==0
    h=(b-a)/count
    val=fn(a)+fn(b)
    for j in range(1,count):val += (4 if j%2 else 2)*fn(a+j*h)
    return val*h/3


def integral(n,c,ell,t,xi):
    w=sqrt(c)
    def fun(s):
        # (-1)^n He_n(s-t) exp(-(s-t)^2/2) = n-th Gaussian derivative.
        z=s-t
        g=(-1)**n*hermite_prob(n,z)*exp(-z*z/2)
        return (exp(ell)*cexp(1j*w*s)+cexp(-1j*w*s))*g*cexp(-1j*xi*s)
    return simpson_complex(fun,t-15,t+15)


def closed(n,c,ell,t,xi):
    w=sqrt(c)
    return (sqrt(2*pi)*1j**n*cexp(-1j*xi*t)*(
        exp(ell)*(xi-w)**n*exp(-(xi-w)**2/2)*cexp(1j*w*t)
        +(xi+w)**n*exp(-(xi+w)**2/2)*cexp(-1j*w*t)))


def check():
    count=0
    for n in (1,2,3,5):
        for c in (n*0.72,n*1.16,n*2.3):
            h=H(n,c)
            for ell in ((-0.7*h,0.,0.7*h,-1.4*h,1.4*h) if h>0 else (-0.8,0.,0.8)):
                rs=predicted_roots(n,c,ell)
                expected=5 if h>0 and abs(ell)<h else 3
                assert len(rs)==expected, (n,c,ell,rs)
                assert all(abs(F(u,n,c,ell))<5e-10 for u in rs)
                signs=[(-1 if fp(u,n,c)>0 else 1) for u in rs]
                assert sum(signs)==-1, (n,c,ell,signs)
                # Phase factor has unit modulus, hence one unique time per cylinder.
                for u in rs:
                    mod=exp(-F(u,n,c,ell))
                    assert abs(mod-1)<1e-8
                count+=1
    for n,c,ell,t,xi in [(1,1.5,0.3,0.2,0.4),(2,2.8,-0.7,0.8,0.2),
                         (3,5.2,0.8,0.7,-0.6),(4,3.3,0.1,0.6,1.1)]:
        assert abs(integral(n,c,ell,t,xi)-closed(n,c,ell,t,xi))<1e-8
    for n in (1,2,4):
        for delta in (1e-3,1e-4,1e-5):
            target=4*delta**1.5/(3*sqrt(n))
            assert abs(H(n,n+delta)/target-1)<1e-3
    for n in (1,2,4):
        c=2*n;v=sqrt(1-n/c);h=H(n,c)
        assert abs(F(-v,n,c,h))<1e-12
        assert abs(F(v,n,c,-h))<1e-12
        assert abs(fp(v,n,c))<1e-12
    print('ALL_CUSP_ZERO_CHECKS_PASSED',count,'simple-root configurations')


if __name__ == '__main__': check()
