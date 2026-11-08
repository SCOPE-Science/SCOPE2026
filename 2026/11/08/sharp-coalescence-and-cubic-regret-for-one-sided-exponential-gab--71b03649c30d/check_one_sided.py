"""Recompute the published critical equations and test asymptotic optimizer separation.
Uses only the Python standard library; numerical tests corroborate but do not prove the theorem.
"""
import math


def coth(t):
    return 1.0 / math.tanh(t)


def csch(t):
    return 1.0 / math.sinh(t)


def fa(t, n):
    x=t/n
    return 1+t*csch(t)-x-x*coth(x)


def fb(t, n):
    x=t/n
    return 1+x-x*coth(x)-t*csch(t)


def bisect(f, lo, hi, n):
    a,b=f(lo,n),f(hi,n)
    assert a*b<0
    for _ in range(90):
        mid=(lo+hi)/2
        v=f(mid,n)
        if v==0:return mid
        if a*v<=0:hi=mid;b=v
        else:lo=mid;a=v
    return (lo+hi)/2


def fminus(t,n):
    x=t/n
    return math.exp(-x)*math.tanh(t/2)*x*csch(x)


def fplus(t,n):
    x=t/n
    return math.exp(x)*coth(t/2)*x*csch(x)

if __name__=='__main__':
    for n in (20,100,500,1000):
        L=math.log(2*n)
        a=bisect(fa, 0.5, 3*L+5,n)
        b=bisect(fb, 0.5, 3*L+5,n)
        k=math.asinh(n)
        assert a<k<b
        alpha=n*(k-a)/L
        beta=n*(b-k)/L
        lower_regret=(fminus(a,n)-fminus(k,n))/fminus(a,n)
        upper_regret=(fplus(k,n)-fplus(b,n))/fplus(b,n)
        rc1=18*n**3*lower_regret/L**2
        rc2=18*n**3*upper_regret/L**2
        print(f'n={n:4d} scaled_gaps=({alpha:.9f},{beta:.9f}) scaled_regrets=({rc1:.7f},{rc2:.7f})')
        assert 0.2<alpha<0.5 and 0.2<beta<0.5
        assert lower_regret>0 and upper_regret>0
    print('ONE_SIDED_GABOR_ASYMPTOTIC_CHECK_PASS orders=4')
