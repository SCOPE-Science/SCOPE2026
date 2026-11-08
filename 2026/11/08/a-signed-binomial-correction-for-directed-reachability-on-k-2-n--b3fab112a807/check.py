"""Exact finite checks for a uniformly independently biased oriented K_{2,n}."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import comb, log

def direct(n,p):
    # Orient the edges {s,bi} and {t,bi} independently from hubs to bi with chance p.
    out = defaultdict(F)
    for bits in product((0,1), repeat=2*n):
        weight = F(1)
        arcs = [[] for _ in range(n+2)]
        for i in range(n):
            b=i+2
            for j,h in enumerate((0,1)):
                bit=bits[2*i+j]
                weight *= p if bit else 1-p
                if bit: arcs[h].append(b)
                else: arcs[b].append(h)
        reached={0}; queue=[0]
        while queue:
            for v in arcs[queue.pop()]:
                if v not in reached:
                    reached.add(v);queue.append(v)
        out[(len(reached & set(range(2,n+2))),int(1 in reached))]+=weight
    return out

def formula(n,p):
    # G(z,w)= A(z)^n + w*(C(z)^n-B(z)^n)
    q=1-p*(1-p); c=p*(2-p)
    A=[comb(n,k)*p**(2*k)*(1-p)**(n-k) for k in range(n+1)]
    B=[comb(n,k)*p**k*(1-p)**(2*(n-k)) for k in range(n+1)]
    C=[comb(n,k)*c**k*((1-p)**2)**(n-k) for k in range(n+1)]
    return {(k,0):A[k] for k in range(n+1)} | {(k,1):C[k]-B[k] for k in range(n+1)}

def binomial(n,r):return [comb(n,k)*r**k*(1-r)**(n-k) for k in range(n+1)]

def run():
    checks=0
    for n in range(1,7):
        for p in (F(1,4), F(1,3),F(1,2),F(2,3), F(3,4)):
            q=1-p*(1-p);a=p*(1-p);c=p*(2-p)
            d=direct(n,p); f=formula(n,p)
            for key,val in f.items():assert d.get(key,F(0))==val, (n,p,key,d.get(key),val);checks+=1
            assert sum(f.values())==1;checks+=1
            agg=[f[k,0]+f[k,1] for k in range(n+1)]
            base=binomial(n,c)
            for k in range(n+1):
                delta=agg[k]-base[k]
                expected=comb(n,k)*(p**(2*k)*(1-p)**(n-k)-p**k*(1-p)**(2*(n-k)))
                assert delta==expected;checks+=1
                # exact threshold from products, no floating point comparison
                if p**k >= (1-p)**(n-k):assert delta>=0;checks+=1
                else:assert delta<0;checks+=1
            mean=sum(k*agg[k] for k in range(n+1))
            assert mean==n*(c-a*q**(n-1));checks+=1
            if n>=2:
                b_cov=sum(k*(k-1)*agg[k] for k in range(n+1))/F(n*(n-1))- (mean/n)**2
                proposed=a*a*q**(n-2)*(1+2*(1-p)**2-q**n)
                assert b_cov==proposed,(n,p,b_cov,proposed);checks+=1
                assert b_cov>0;checks+=1
            total_variation=sum(abs(agg[k]-base[k]) for k in range(n+1))/2
            assert total_variation==sum(max(F(0),agg[k]-base[k]) for k in range(n+1));checks+=1
            assert total_variation<=q**n;checks+=1
    print(f'VERIFY_OK {checks} exhaustive weighted-orientation and rational identities')
if __name__=='__main__':run()
