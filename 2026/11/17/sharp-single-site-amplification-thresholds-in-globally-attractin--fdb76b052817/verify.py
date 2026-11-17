#!/usr/bin/env python3
"""Finite numerical checks of exact single-site response identities (not an infinite proof)."""
import math

def log_sum(n, v):
    if v <= 0:
        return 0.0
    logs=[2*j*math.log(v)-2*math.lgamma(j+1) for j in range(n)]
    m=max(logs)
    return m+math.log(sum(math.exp(q-m) for q in logs))

def gain2(n, kappa, u):
    if u == 0:
        return 1.0
    return math.exp(-2*u+log_sum(n,kappa*u))

def ratio(n, v):
    return log_sum(n,v)/(2*v)

def gamma(n):
    # Grid to find local candidate, then golden-section refinement.
    steps=3000
    lo=0.02
    hi=3*n
    vs=[lo+(hi-lo)*j/steps for j in range(steps+1)]
    k=max(range(len(vs)),key=lambda j:ratio(n,vs[j]))
    a=vs[max(0,k-1)]
    b=vs[min(steps,k+1)]
    inv=(math.sqrt(5)-1)/2
    x=b-inv*(b-a);y=a+inv*(b-a)
    for _ in range(90):
        if ratio(n,x)<ratio(n,y):a=x;x=y;y=a+inv*(b-a)
        else:b=y;y=x;x=b-inv*(b-a)
    v=(a+b)/2
    return ratio(n,v),v

def check():
    thresholds=[]
    for n in [2,3,4,5,8,16,32,64,100]:
        g,v=gamma(n)
        k=1/g
        rho=1/math.cos(math.pi/(n+1))
        assert k>rho
        assert gain2(n,k,v/k)>0.9999999999
        assert abs(gain2(n,k,v/k)-1)<1e-9
        assert gain2(n,0.985*k,v/k)<1
        assert gain2(n,1.015*k,v/k)>1
        thresholds.append((n,k,v,rho))
    assert all(thresholds[i+1][1]<thresholds[i][1] for i in range(len(thresholds)-1))
    for n,k,v,rho in thresholds:
        print('n=%3d critical=%.12f reactive=%.12f tangency_v=%.8f' %(n,k,rho,v))
    u=0.7968121300200199
    k2=math.exp(u)/math.sqrt(u)
    assert abs(k2-thresholds[0][1])<1e-8
    assert abs((1-u)*math.exp(2*u)-1)<1e-12
    # Taylor-exponential alternating components at one terminal impulse.
    n=7;k=2.1;u=0.8
    comps=[math.exp(-u)*(-k*u)**(n-1-i)/math.factorial(n-1-i) for i in range(n)]
    assert abs(sum(t*t for t in comps)-gain2(n,k,u))<1e-12
    print('VERIFY_OK n_cases=9 onset_tangencies=9 two_species_lambert=1 exact_exponential_components=7')
if __name__=='__main__':check()
