#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
import math

def cycles_and_counts(p):
    n=len(p)
    seen=[False]*n
    sizes=[]
    for i in range(n):
        if not seen[i]:
            j=i; s=0
            while not seen[j]:
                seen[j]=True; s+=1; j=p[j]
            sizes.append(s)
    counts={}
    for s in sizes:
        counts[s]=counts.get(s,0)+1
    return len(sizes),counts

def rising(theta,n):
    z=Fraction(1)
    for i in range(n): z*=theta+i
    return z

def meanK(theta,m):
    return sum((theta/(theta+i) for i in range(m)),Fraction(0))

def meanAr(theta,n,r):
    # theta/r * n!/(n-r)! * Gamma(theta+n-r)/Gamma(theta+n)
    # evaluate with rising factorials exactly.
    fall=1
    for j in range(n-r+1,n+1): fall*=j
    return Fraction(fall,r)*theta*rising(theta,n-r)/rising(theta,n)

_wr_cache={}
def weighted_rows(n,theta):
    key=(n,theta)
    if key in _wr_cache:
        return _wr_cache[key]
    rows=[]; Z=Fraction(0)
    for p in permutations(range(n)):
        K,c=cycles_and_counts(p)
        w=theta**K
        rows.append((K,c,w))
        Z+=w
    assert Z==rising(theta,n)
    _wr_cache[key]=(rows,Z)
    return rows,Z

def threshold(n,theta):
    tail=Fraction(0)
    for r in range(1,n+1):
        tail += theta/(theta+n-r)
        if 1-tail<=0:
            return r
    raise AssertionError

def float_threshold(n,theta):
    s=0.0
    for r in range(1,n+1):
        s += theta/(theta+n-r)
        if 1.0-s<=0.0: return r

def log_meanAr(theta,n,r):
    return math.log(theta)-math.log(r)+math.lgamma(n+1)-math.lgamma(n-r+1)+math.lgamma(theta+n-r)-math.lgamma(theta+n)

def run():
    permutation_parameter_evals=0
    mean_checks=0
    palm_checks=0
    covariance_checks=0
    threshold_checks=0
    asymptotic_checks=0
    thetas=[Fraction(1,2),Fraction(1),Fraction(2)]
    for n in range(2,8):
        for theta in thetas:
            rows,Z=weighted_rows(n,theta)
            permutation_parameter_evals += math.factorial(n)
            EK=sum((w*K for K,c,w in rows),Fraction(0))/Z
            assert EK==meanK(theta,n)
            for r in range(1,n+1):
                EA=sum((w*c.get(r,0) for K,c,w in rows),Fraction(0))/Z
                assert EA==meanAr(theta,n,r)
                mean_checks+=1
                # Palm tests f=1,K,K^2 and all point indicators.
                for mode in ('one','K','K2'):
                    if mode=='one': f=lambda k: 1
                    elif mode=='K': f=lambda k: k
                    else: f=lambda k: k*k
                    lhs=sum((w*c.get(r,0)*f(K) for K,c,w in rows),Fraction(0))/Z
                    # enumerate smaller permutation exactly
                    if n-r==0:
                        rhs=f(1)
                    else:
                        small,Zs=weighted_rows(n-r,theta)
                        rhs=sum((w*f(1+K) for K,c,w in small),Fraction(0))/Zs
                    assert lhs==EA*rhs
                    palm_checks+=1
                for t in range(1,n+1):
                    lhs=sum((w*c.get(r,0)*(1 if K==t else 0) for K,c,w in rows),Fraction(0))/Z
                    if n-r==0:
                        rhs=Fraction(1 if t==1 else 0)
                    else:
                        small,Zs=weighted_rows(n-r,theta)
                        rhs=sum((w*(1 if 1+K==t else 0) for K,c,w in small),Fraction(0))/Zs
                    assert lhs==EA*rhs
                    palm_checks+=1
                EKA=sum((w*K*c.get(r,0) for K,c,w in rows),Fraction(0))/Z
                cov=EKA-EK*EA
                target=EA*(Fraction(1)+meanK(theta,n-r)-meanK(theta,n))
                assert cov==target
                covariance_checks+=1
            # exact threshold geometry
            cs=[Fraction(1)+meanK(theta,n-r)-meanK(theta,n) for r in range(1,n+1)]
            assert all(cs[i]>cs[i+1] for i in range(len(cs)-1))
            assert cs[0]>0 and cs[-1]<0
            t=threshold(n,theta)
            assert all(x>0 for x in cs[:t-1])
            assert cs[t-1]<=0
            assert all(x<0 for x in cs[t:])
            threshold_checks+=1
    # Asymptotic threshold and profile sanity checks.
    for theta in (0.5,1.0,2.0,5.0):
        xstar=1-math.exp(-1/theta)
        for n in (1000,10000):
            t=float_threshold(n,theta)
            assert abs(t/n-xstar)<0.01
            asymptotic_checks+=1
        for x in (0.2,0.45,0.7):
            n=20000
            r=max(1,min(n-1,round(x*n)))
            tail=sum(theta/(theta+i) for i in range(n-r,n))
            bracket=1-tail
            scaled=n*math.exp(log_meanAr(theta,n,r))*bracket
            target=(theta/x)*((1-x)**(theta-1))*(1+theta*math.log(1-x))
            assert abs(scaled-target) < 0.03*(1+abs(target))
            asymptotic_checks+=1
    print('VERIFY_OK '
          f'permutation_parameter_evals={permutation_parameter_evals} '
          f'mean_checks={mean_checks} palm_checks={palm_checks} '
          f'covariance_checks={covariance_checks} threshold_checks={threshold_checks} '
          f'asymptotic_checks={asymptotic_checks}')

if __name__=='__main__': run()
