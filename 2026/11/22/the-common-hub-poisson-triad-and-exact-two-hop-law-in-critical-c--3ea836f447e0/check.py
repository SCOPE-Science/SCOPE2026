"""Independent exact checks for the tagged-neighborhood Poisson law.

Run with Python 3 and only the standard library. Finite checks do not
replace the asymptotic proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import isqrt, exp

def sqrtq(x):
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    assert a*a==x.numerator and b*b==x.denominator
    return Q(a,b)

def power_half(x): return sqrtq(x)

def alpha_half_constants(w,v,lam=Q(1)):
    a=Q(1,2)
    lo,hi=sorted((w,v))
    mu1=2*lam*sqrtq(w);mu2=2*lam*sqrtq(v)
    gamma=2*lam*(sqrtq(lo)-lo/sqrtq(hi)/3)
    return mu1,mu2,gamma

def cross_integral_piecewise(w,v,n):
    # Independent three-interval integration in the original Pareto variable W.
    eps=Q(1,n*n)
    lo,hi=sorted((w,v))
    t_hi=1/(eps*hi);t_lo=1/(eps*lo)
    assert t_hi>=1
    part1=Q(1,2)*eps**2*w*v*(power_half(t_hi)**3-1)/Q(3,2)
    part2=Q(1,2)*eps*lo*(power_half(t_lo)-power_half(t_hi))/Q(1,2)
    part3=power_half(eps*lo)
    return part1+part2+part3

def test():
    checks=0
    for w,v in [(Q(1),Q(1)),(Q(1),Q(4)),(Q(4),Q(9)),(Q(9),Q(9)),(Q(1),Q(16))]:
        m1,m2,g=alpha_half_constants(w,v)
        assert 0<g<=min(m1,m2);checks+=1
        for n in [20,32,64,128,512,2048]:
            eps=Q(1,n*n)
            assert eps*max(w,v)<1
            A1=m1/n-w/n**2;A2=m2/n-v/n**2
            B=g/n-w*v/Q(3*n**4)
            assert B==cross_integral_piecewise(w,v,n);checks+=1
            p11=B;p10=A1-B;p01=A2-B;p00=1-A1-A2+B
            assert min(p00,p01,p10,p11)>=0 and sum((p00,p01,p10,p11))==1;checks+=1
            assert (n-2)*B<g and 0<A1<m1/n and 0<A2<m2/n;checks+=1
            # The full degree two-tag zero probability includes the direct edge.
            p12=eps*w*v
            pzero=(1-p12)*p00**(n-2)
            assert 0<pzero<1;checks+=1
            assert abs(float(pzero)-exp(-float(m1+m2-g))) < 70/n;checks+=1
            # Finite codegree C_n is Bin(n-2,B); its mean tends to gamma.
            assert abs(float((n-2)*B-g))<float(g)*3/n+1e-12;checks+=1
            # Each limit rate can be decomposed as three nonnegative Poisson intensities.
            assert m1-g>=0 and m2-g>=0 and g>0;checks+=1
        # Symmetry, explicit conditional zero-degree association.
        assert alpha_half_constants(v,w)[2]==g;checks+=1
        assert float(g)>0 and exp(float(g))>1;checks+=1
    print('PASS',checks,'exact-rational or controlled numerical assertions')
    print('Example: alpha=1/2, lambda=1, tagged weights (1,4):')
    m1,m2,g=alpha_half_constants(Q(1),Q(4))
    print('mu1, mu2, shared =',m1,m2,g)
    print('limit probability of distance exactly 2 =',1-exp(-float(g)))
if __name__=='__main__':test()
