#!/usr/bin/env python3
"""Finite checks for polynomial-weight generalized Aluthge iteration."""
import math

def transform_direct(logs, t):
    return [(1-t)*logs[j]+t*logs[j+1] for j in range(len(logs)-1)]

def binomial_expectations(n, t, jcount, beta=1.0):
    # Stable binomial law via forward recursion from log probabilities, no scipy.
    modes = []
    k0 = int((n+1)*t)
    probs = [0.0]*(n+1)
    logp = math.lgamma(n+1)-math.lgamma(k0+1)-math.lgamma(n-k0+1)+k0*math.log(t)+(n-k0)*math.log1p(-t)
    probs[k0]=math.exp(logp)
    for k in range(k0,n):
        probs[k+1]=probs[k]*(n-k)/(k+1)*t/(1-t)
    for k in range(k0,0,-1):
        probs[k-1]=probs[k]*k/(n-k+1)*(1-t)/t
    assert abs(math.fsum(probs)-1)<1e-11
    logs=[-beta*math.fsum(probs[k]*math.log(j+k+1) for k in range(n+1)) for j in range(jcount)]
    return logs

def main():
    checks=0
    for t in (0.2,0.35,0.7):
        for n in range(1,9):
            arr=[-math.log(j+1) for j in range(250+n)]
            for _ in range(n):
                arr=transform_direct(arr,t)
            exact=binomial_expectations(n,t,200)
            for j in range(100):
                assert abs(arr[j]-exact[j])<2e-12
                checks+=1
            for j in range(1,99):
                assert exact[j-1]>=exact[j]-2e-13
                checks+=1
    beta=1.0;p=2.0;t=0.35
    predicted=t**(1-beta*p)/(beta*p-1)
    predicted_norm=t**(-beta)
    for n in (80,200,600,1600):
        arr=binomial_expectations(n,t,10000,beta)
        weights=[math.exp(x) for x in arr]
        w_n=(n+1)**(-beta)
        normratio=weights[0]/w_n
        powerratio=math.fsum(x**p for x in weights)/(n*w_n**p)
        # Tail beyond 10000 is <= sum_{j>10000}(j+1)^-2;
        # omitted error normalized is small for these n.
        assert abs(normratio/predicted_norm-1)<0.1
        assert abs(powerratio/predicted-1)<0.1
        threshold=0.5*weights[0]
        count=sum(x>threshold for x in weights)/n
        assert abs(count-t)<0.03
        checks+=3
    print('REGULAR_ALUTHGE_POWER_CHECKS_OK',checks)

if __name__=='__main__':
    main()
