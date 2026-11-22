"""Reproduce four-chip continuous-phase peak-sidelobe identities.
Requires only Python 3 standard library. Theorem is proved analytically in RESULT.md.
"""
import cmath
import math
import random

PI = math.pi

def simpson(f,a,b,fa,fm,fb):
    return (b-a)*(fa+4*fm+fb)/6

def integrate(f,a,b,tol=2e-10,depth=0,cache=None):
    if a==b: return 0.0
    m=(a+b)/2
    fa,fm,fb=f(a),f(m),f(b)
    s=simpson(f,a,b,fa,fm,fb)
    def recurse(a,b,fa,fm,fb,s,tol,depth):
        m=(a+b)/2
        lm=(a+m)/2; rm=(m+b)/2
        flm,frm=f(lm),f(rm)
        sl=simpson(f,a,m,fa,flm,fm)
        sr=simpson(f,m,b,fm,frm,fb)
        if abs(sl+sr-s) < 15*tol or depth >= 28:
            return sl+sr+(sl+sr-s)/15
        return (recurse(a,m,fa,flm,fm,sl,tol/2,depth+1)+
                recurse(m,b,fm,frm,fb,sr,tol/2,depth+1))
    return recurse(a,b,fa,fm,fb,s,tol,depth)

def cdf(s):
    if s<1: return 0.0
    if s>=3: return 1.0
    a=(s-1)/2
    b=min(1.0,s/2)
    def conditional(theta):
        x=math.sin(theta)
        if x<1e-15: return .5 if s==1 else 1.0
        q=(s*s-1-4*x*x)/(4*x)
        if q<=-1:return 0.0
        if q>=1:return 1.0
        return .5+math.asin(q)/PI
    return (2/PI)*(math.asin(a)+integrate(conditional,math.asin(a),math.asin(b)))

def main():
    rng=random.Random(20261117)
    n=100000
    thresholds=(1,1.1,1.5,2,2.5,2.9)
    counts={s:0 for s in thresholds}
    for k in range(n):
        th=[2*PI*rng.random() for j in range(4)]
        a=[cmath.exp(1j*t) for t in th]
        corr=[sum(a[j+t]*a[j].conjugate() for j in range(4-t)) for t in range(1,4)]
        peak=max(abs(c) for c in corr)
        for s in thresholds:
            counts[s] += peak<=s+1e-12
        delta=[th[j+1]-th[j] for j in range(3)]
        signed_cos=math.cos((delta[0]-delta[2])/2)
        x=abs(signed_cos)
        phi=delta[1]-(delta[0]+delta[2])/2
        v=1+4*x*x+4*signed_cos*math.cos(phi)
        assert abs(abs(corr[0])**2-v)<1e-10
        assert abs(abs(corr[1])-2*x)<1e-10
        assert abs(abs(corr[2])-1)<1e-10
    assert cdf(0.999)==0
    assert cdf(3)==1
    assert abs(cdf(1)-5/36)<2e-9
    print('Exact Barker probability: 5/36 =',5/36)
    for s in thresholds:
        exact=cdf(s)
        observed=counts[s]/n
        assert abs(exact-observed)<.009,(s,exact,observed)
        print('threshold',s,'analytic_CDF',format(exact,'.11f'),'direct_Monte_Carlo',observed)
    for eps in (1e-3,1e-4,1e-5):
        coeff=(cdf(1+eps)-5/36)/(eps*math.log(1/eps))
        print('near_atom epsilon',eps,'coefficient',format(coeff,'.11f'),'predicted_limit',format(1/PI**2,'.11f'))
        assert .09<coeff<.16
    print('PASS: 300000 direct algebraic residual checks, 6 distribution comparisons, exact atom and leading-log scaling checks')

if __name__=='__main__':main()
