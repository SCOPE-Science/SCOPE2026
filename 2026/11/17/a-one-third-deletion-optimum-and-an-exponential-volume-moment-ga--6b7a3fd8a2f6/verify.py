"""Independent exact and numerical checks for cycle-edge forest polytope volumes.

Requires Python 3 and sympy. Run: python forest_volume_verify.py
"""
from itertools import combinations
from math import comb, factorial, exp, lgamma, log, sqrt
from fractions import Fraction
from sympy import Matrix


def component_sizes(n, retained):
    adj=[[] for _ in range(n)]
    for j in retained:
        k=(j+1)%n
        adj[j].append(k); adj[k].append(j)
    seen=set(); out=[]
    for start in range(n):
        if start in seen: continue
        stack=[start];seen.add(start);size=0
        while stack:
            i=stack.pop();size+=1
            for j in adj[i]:
                if j not in seen:
                    seen.add(j);stack.append(j)
        out.append(size)
    return out


def gram_det(n, retained):
    cols=[]
    for j in retained:
        col=[0]*n; col[j]=1;col[(j+1)%n]=-1
        cols.append(col)
    B=Matrix(n,len(cols),lambda a,b:cols[b][a])
    return int((B.T*B).det())

checks=0
for n in range(3,11):
    for m in range(1,n):
        s=0
        for deleted in combinations(range(n),m):
            left=set(range(n))-set(deleted)
            d=gram_det(n,sorted(left))
            prod=1
            for c in component_sizes(n,left):prod*=c
            assert d==prod, (n,m,deleted,d,prod)
            s+=d;checks+=1
        exact=comb(n+m-1,n-m)*n//m
        assert (comb(n+m-1,n-m)*n)%m==0
        assert s==exact,(n,m,s,exact)
        ratio=Fraction(factorial(m-1)*factorial(n+m-1),factorial(2*m-1)*factorial(n-1))
        assert s==comb(n,m)*ratio
        checks+=1
    vals=[Fraction(factorial(m-1)*factorial(n+m-1),factorial(2*m-1)*factorial(n-1)) for m in range(1,n)]
    mx=max(vals)
    expected={n//3} if n%3!=2 else {n//3,n//3+1}
    assert {i+1 for i,v in enumerate(vals) if v==mx}==expected
    checks+=1

for d in (0.1,1/3,0.5,0.8):
    z=(1-d)/(1+d)
    ps=[d*(1-d)**(s-1) for s in range(1,1000)]
    qs=[(1-z)**2*s*z**(s-1) for s in range(1,1000)]
    mu=sum(p*log(s) for s,p in enumerate(ps,1))
    var=sum(p*(log(s)-mu)**2 for s,p in enumerate(ps,1))
    cov=sum(p*(s-1/d)*(log(s)-mu) for s,p in enumerate(ps,1))
    tau=var-cov**2/((1-d)/d**2)
    gap=(1+d)*log(1+d)-d*log(d)-2*d*log(2)-d*mu
    kl=sum(p*log(p/q) for p,q in zip(ps,qs) if p>0 and q>0)
    assert tau>0 and gap>0 and abs(gap-d*kl)<1e-12
    checks+=1
for n in (100,300,900):
    m=n//3;d=m/n
    exact=lgamma(m)+lgamma(n+m)-lgamma(2*m)-lgamma(n)
    expo=n*((1+d)*log(1+d)-d*log(d)-2*d*log(2))
    rel=exp(exact-expo)/sqrt(2/(1+d))
    assert abs(rel-1)<0.007
    checks+=1
# Check that exact finite conditional fluctuations approach the predicted slope.
def composition_log_moments(n,m):
    state=[(0.,0.,0.) for _ in range(n+1)]
    state[0]=(1.,0.,0.)
    for _ in range(m):
        nxt=[[0.,0.,0.] for _ in range(n+1)]
        for a,(count,total,square) in enumerate(state):
            if count==0: continue
            for b in range(1,n-a+1):
                ell=log(b)
                v=nxt[a+b]
                v[0]+=count
                v[1]+=total+count*ell
                v[2]+=square+2*ell*total+count*ell*ell
        state=[tuple(x) for x in nxt]
    cnt,total,square=state[n]
    assert abs(cnt/comb(n-1,m-1)-1)<1e-9
    return total/cnt, square/cnt-(total/cnt)**2

variance_ratios=[]
for n in (30,60,120):
    m=n//3
    p=m/n
    probs=[p*(1-p)**(s-1) for s in range(1,300)]
    mu=sum(prob*log(s) for s,prob in enumerate(probs,1))
    vari=sum(prob*(log(s)-mu)**2 for s,prob in enumerate(probs,1))
    cov=sum(prob*(s-1/p)*(log(s)-mu) for s,prob in enumerate(probs,1))
    tau2=vari-cov**2/((1-p)/p**2)
    observed_mean, observed_var=composition_log_moments(n,m)
    assert abs(observed_mean-m*mu)<1.
    variance_ratios.append(observed_var/(m*tau2))
    checks+=1
assert 0.8<variance_ratios[0]<variance_ratios[1]<variance_ratios[2]<1.05
print('PASS',checks,'exact Gram, moment, conditional fluctuation, KL and Stirling checks')
