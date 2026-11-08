"""Exact finite tests for sharp centered Laplace envelopes on uniform star graphs.

This checker supplies finite corroboration only. The all-order proof is in RESULT.md.
"""
from fractions import Fraction
from math import ceil, cosh, exp, expm1, log, sinh, tanh
from itertools import product

def value(n, k, r):
    """Centered MGF at tilt t=(n+1)log(r), with k positive leaves."""
    N = n + 1
    return (1 + (n-k) * r ** (-N) + k * r ** N) * r ** (n-2*k) / N

def x_value(n, r):
    N = n + 1
    return 1 / (r*r-1) - (1+n*r**(-N)) / (r**N-r**(-N))

def ceil_fraction(x):
    return -(-x.numerator // x.denominator)

def check_exact():
    total=0; ties=0
    for n in range(2,13):
        for r in [Fraction(1001,1000),Fraction(11,10),Fraction(5,4),Fraction(3,2),Fraction(2),Fraction(4),Fraction(20)]:
            x = x_value(n,r)
            k = max(0,min(n,ceil_fraction(x)))
            vs = [value(n,j,r) for j in range(n+1)]
            winners = [j for j,v in enumerate(vs) if v==max(vs)]
            predicted = ([k,k+1] if x.denominator==1 and 0 <= x <= n-1 else [k])
            assert winners==predicted,(n,r,x,k,winners,predicted)
            if n<=9:
                allvals=[]
                for signs in product((-1,1),repeat=n):
                    j=sum(s==1 for s in signs)
                    allvals.append(value(n,j,r))
                assert max(allvals)==max(vs)
            total+=1;ties+=len(winners)-1
    print('EXACT_RATIONAL_TILTS_AND_ALL_SIGNING_OPTIMIZERS_OK',total,'tie_instances',ties)

def check_initial_variance():
    for n in range(2,201):
        N=n+1
        vals=[Fraction(n,N)-Fraction((2*k-n)**2,N*N) for k in range(n+1)]
        k=n//2
        expected=Fraction(n,N)-Fraction(n%2,N*N)
        assert max(vals)==expected
        winners=[j for j,v in enumerate(vals) if v==expected]
        assert winners==([k] if n%2==0 else [k,k+1])
    print('EXACT_SMALL_T_VARIANCE_PARITY_OK',199)

def check_staircase():
    for n in range(3,29):
        N=n+1
        def x(t):
            return 1/expm1(2*t/N)-(1+n*exp(-t))/(2*sinh(t))
        ts=[.00001,.001,.01,.1,.5,1,2,3,6,12,20,35,50,90]
        xs=[x(t) for t in ts]
        assert all(a>b for a,b in zip(xs,xs[1:])),(n,xs)
        assert all(0<a<(n-1)/2 for a in xs)
        ks=[ceil(u) for u in xs]
        assert all(a>=b for a,b in zip(ks,ks[1:])),(n,ks)
    print('MONOTONE_TILT_PROFILE_SAMPLES_OK',26)

def check_limit():
    for t in [0.2,0.5,1.,2.,4.]:
        n=100000
        N=n+1
        r=exp(t/N)
        # stable x(t) using expm1
        from math import expm1
        x=1/expm1(2*t/N)-(1+n*exp(-t))/(2*sinh(t))
        k=ceil(x)
        a=(2*k-n)/N
        mgf=exp(-a*t)*(1+n*cosh(t)+(2*k-n)*sinh(t))/N
        limiting=(sinh(t)/t)*exp(t/tanh(t)-1)
        p=1/(2*t)-1/expm1(2*t)
        assert abs(k/n-p)<3e-5,(t,k/n,p)
        assert abs(mgf-limiting)/limiting<5e-5,(t,mgf,limiting)
    print('LARGE_STAR_LIMIT_SAMPLES_OK',5)

def check_threshold_ties():
    for n in range(4,15):
        N=n+1
        def x(t):
            return 1/expm1(2*t/N)-(1+n*exp(-t))/(2*sinh(t))
        for j in range(1,n//2):
            low=1e-6; high=100.
            for _ in range(70):
                mid=(low+high)/2
                if x(mid)>j:low=mid
                else:high=mid
            t=(low+high)/2
            assert abs(x(t)-j)<2e-9,(n,j,t,x(t))
            # comparison made in logarithmic scale, avoiding a large positive exponential
            def logf(k):
                return log(1+(n-k)*exp(-t)+k*exp(t)) -log(N) - (2*k-n)*t/N
            vals=[logf(k) for k in range(n+1)]
            assert abs(vals[j]-vals[j+1])<2e-9,(n,j,vals[j],vals[j+1])
            assert all(vals[k]<vals[j]-1e-10 for k in range(n+1) if k not in (j,j+1)),(n,j,vals)
    print('NUMERICAL_TILT_SWITCHING_TIES_OK',sum(n//2-1 for n in range(4,15)))

if __name__=='__main__':
    check_exact();check_initial_variance();check_staircase();check_threshold_ties();check_limit()
    print('ALL_STAR_LAPLACE_ENVELOPE_TESTS_OK')
