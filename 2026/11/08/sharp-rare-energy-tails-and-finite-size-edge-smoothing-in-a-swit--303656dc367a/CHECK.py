#!/usr/bin/env python3
"""Independent numerical diagnostics for the stationary switching-trap energy formulas.
Analytical arguments in RESULT.md, not these finite checks, establish the theorem.
Run: python CHECK.py (requires mpmath 1.3 or newer).
"""
import mpmath as mp
mp.mp.dps = 45


def model(a, b, p, q):
    a, b, p, q = [mp.mpf(t) for t in (a, b, p, q)]
    width=b-a
    beta=mp.beta(p,q)
    bar=a+width*p/(p+q)
    def density_u(u):
        return (a+width*u)*u**(p-1)*(1-u)**(q-1)/(bar*beta)
    def g(v):
        u=(v-a)/width
        return density_u(u)/width
    def rate(s, v):
        return (s/v-1-mp.log(s/v))/2
    def f(s, n):
        n=mp.mpf(n)
        pref=(n/2)**(n/2)*s**(n/2-1)/mp.gamma(n/2)
        def integrand(u):
            v=a+width*u
            return density_u(u)*v**(-n/2)*mp.exp(-n*s/(2*v))
        return pref*mp.quad(integrand,[0,mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.9'),mp.mpf('0.99'),1])
    def edge_const(lower):
        t=a if lower else b
        theta=p if lower else q
        c=t/(bar*beta*width**theta)
        return c*mp.gamma(theta/2)*(2*t)**theta/(4*mp.sqrt(mp.pi)*t)
    def out_const(s, lower):
        t=a if lower else b
        theta=p if lower else q
        k=(a-s)/(2*a*a) if lower else (s-b)/(2*b*b)
        c=t/(bar*beta*width**theta)
        return c*mp.gamma(theta)/(2*mp.sqrt(mp.pi)*s*k**theta)
    return a,b,p,q,density_u,g,rate,f,edge_const,out_const


def close(x, y, tol):
    assert abs(x-y) <= tol*max(mp.mpf('1'),abs(x),abs(y)), (mp.nstr(x,14),mp.nstr(y,14),tol)


def verify(params):
    a,b,p,q,du,g,rate,f,edge,out=model(*params)
    beta=mp.beta(p,q)
    width=b-a
    bare=a+width*p/(p+q)
    close(mp.quad(du,[0,mp.mpf('0.5'),1]), 1, mp.mpf('1e-13'))
    # The size-biased beta moments, rather than ordinary beta moments,
    # are the moments of the physical stationary mixing variance.
    for k in (1,2,3):
        direct=mp.quad(lambda u:du(u)*(a+width*u)**k,[0,mp.mpf('0.5'),1])
        poly=sum(mp.binomial(k+1,j)*a**(k+1-j)*width**j*mp.rf(p,j)/mp.rf(p+q,j) for j in range(k+2))/bare
        close(direct,poly,mp.mpf('1e-12'))
    count=4
    for n in (240,450,1000):
        sminus=a*mp.mpf('0.58')
        splus=b*mp.mpf('1.65')
        for s,lower in ((sminus,True),(splus,False)):
            theta=p if lower else q
            asym=out(s,lower)*n**(mp.mpf('0.5')-theta)*mp.exp(-n*rate(s,a if lower else b))
            ratio=f(s,n)/asym
            assert mp.mpf('0.55') < ratio < mp.mpf('1.55'), (params,n,s,mp.nstr(ratio,10))
            count += 1
        for s,lower in ((a,True),(b,False)):
            theta=p if lower else q
            asym=edge(lower)*n**((1-theta)/2)
            ratio=f(s,n)/asym
            assert mp.mpf('0.6') < ratio < mp.mpf('1.5'),(params,n,s,mp.nstr(ratio,10))
            count += 1
    # The two smoothed scaling functions hold for z of either sign.
    for z in (-1,1):
        n=450
        for lower in (True,False):
            t=a if lower else b
            theta=p if lower else q
            c=t/(bare*beta*width**theta)
            scaled_s=t+mp.mpf(z)*t/mp.sqrt(n)
            def limit_integrand(y):
                d=(mp.mpf(z)*t-y) if lower else (mp.mpf(z)*t+y)
                return y**(theta-1)*mp.exp(-d*d/(4*t*t))
            limit=c/(2*mp.sqrt(mp.pi)*t)*mp.quad(limit_integrand,[0,1,4,mp.inf])
            actual=f(scaled_s,n)*n**((theta-1)/2)
            assert mp.mpf('0.57') < actual/limit < mp.mpf('1.55'), (params,lower,z,mp.nstr(actual/limit,10))
            count += 1
    return count

if __name__=='__main__':
    totals=0
    # Covers both divergent and vanishing endpoint heights and unequal rate ratios.
    for args in (('0.3333333333333333333333333','1','0.75','1.4'),
                 ('0.25','1.25','1.55','0.65')):
        totals+=verify(args)
    print('PASS:', totals, 'numerical identities/asymptotic checks over two parameter regimes; analytic proof is in RESULT.md')
