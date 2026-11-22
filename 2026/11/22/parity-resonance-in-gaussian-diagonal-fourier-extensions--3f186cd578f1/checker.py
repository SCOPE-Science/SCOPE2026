"""Numerical cross-checks for Gaussian diagonal extension Fourier formulas.

This finite checker is supplementary: the infinite-dimensional statements are
proved analytically in RESULT.md. Uses only Python's standard library.
"""
from math import exp, cos, pi, sqrt
from fractions import Fraction


def theta(s, x, cutoff=55):
    return sum(exp(-s * (n-x)**2) for n in range(-cutoff, cutoff+1))


def multiplier(s, x):
    t = theta(s, x)
    return theta(2*s, x)/(t*t)


def direct(a, b, k):
    costs = [a*m*m+b*(k-m)*(k-m) for m in range(-55, 56)]
    base = min(costs)
    ws = [exp(-(cost-base)) for cost in costs]
    return sum(w*w for w in ws)/sum(ws)**2


def run():
    checks=0
    for s in (0.5, 0.8, 1.5, 3.0, 7.0, 16.0):
        for h in range(21):
            x=h/40
            left=theta(s,x)**2
            right=theta(2*s,0)*theta(2*s,x)+theta(2*s,0.5)*theta(2*s,x-0.5)
            assert abs(left-right) < 4e-10, (s,x,left,right)
            checks+=1
        vals=[multiplier(s,h/40) for h in range(21)]
        assert all(vals[i]>vals[i+1]+1e-13 for i in range(20)),(s,vals)
        checks+=20
    for a,b in ((.6,1.2),(1,3),(2,1),(6,11)):
        s=a+b
        alpha=b/s
        for k in range(-12,13):
            assert abs(direct(a,b,k)-multiplier(s,alpha*k))<3e-10,(a,b,k)
            checks+=1
    for s in (.5, 2, 6, 13):
        for q in range(2,11):
            for p in range(1,q):
                if Fraction(p,q).denominator!=q: continue
                values=[multiplier(s,p*k/q) for k in range(q)]
                target=multiplier(s,(q//2)/q)
                assert abs(min(values)-target)<2e-10,(s,p,q)
                assert abs(max(values)-multiplier(s,0))<2e-10,(s,p,q)
                checks+=2
    for q in (3,5,7):
        s=100.0
        val=multiplier(s,0)/multiplier(s,(q//2)/q)
        rate=2*exp(-s/q)
        assert abs((val-1)/rate-1)<0.03,(q,val,rate)
        checks+=1
    for s in (8.0,16.0):
        ratio=multiplier(s,0)/multiplier(s,0.5)
        assert 1.0<ratio<2.01
        checks+=1
    print(f'PASS {checks} supplementary checks')


if __name__=='__main__':
    run()
