"""Exact small-graph checks for edge-subdivided hard-core occupancy identities."""
from fractions import Fraction
from math import exp, lgamma, log, log1p
from itertools import combinations

def graphs(n):
    complete = [(i,j) for i in range(n) for j in range(i+1,n)]
    cycle = sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)}) if n>=3 else []
    star = [(0,j) for j in range(1,n)]
    return [('complete',complete),('cycle',cycle),('star',star)]

def moments_original(n,edges,z):
    d=[0]*n
    for u,v in edges:d[u]+=1;d[v]+=1
    m=len(edges)
    coeff={}
    for mask in range(1<<n):
        subset={i for i in range(n) if mask>>i&1}
        incident=sum(1 for u,v in edges if u in subset or v in subset)
        val=z**len(subset)*(1+z)**(m-incident)
        coeff[mask]=val
    return coeff

def brute(n,edges,z):
    E=[(u,n+i) for i,(u,v) in enumerate(edges)]+[(v,n+i) for i,(u,v) in enumerate(edges)]
    m=len(edges)
    total=Fraction(0)
    weights={mask:Fraction(0) for mask in range(1<<n)}
    for bits in range(1<<(n+m)):
        if any(bits>>u&1 and bits>>v&1 for u,v in E):continue
        wt=z**bits.bit_count()
        total+=wt
        weights[bits&((1<<n)-1)]+=wt
    return total,weights

def check():
    checks=0
    for n in range(3,6):
        for name,edges in graphs(n):
            for z in (Fraction(1,5), Fraction(1,2),Fraction(3,4)):
                w=moments_original(n,edges,z)
                Z=sum(w.values())
                zb,wb=brute(n,edges,z)
                assert Z==zb and all(w[k]==wb[k] for k in w),(n,name,z)
                checks+=1
                # exact conditional-activity factorization
                degree=[sum(i in edge for edge in edges) for i in range(n)]
                m=len(edges)
                for mask,v in w.items():
                    a=[i for i in range(n) if mask>>i&1]
                    e=sum(u in a and v in a for u,v in edges)
                    expected=(1+z)**m * z**len(a) * (1+z)**(-sum(degree[i] for i in a)+e)
                    assert v==expected
                    checks+=1
    # numerical universal TV upper bound for many dense/sparse host graphs
    for n in range(3,9):
        for name,edges in graphs(n):
            for c in (Fraction(1,2),Fraction(1),Fraction(2)):
                z=c/n
                w=moments_original(n,edges,z)
                Z=sum(w.values())
                deg=[sum(i in edge for edge in edges) for i in range(n)]
                ws=[z*(1+z)**(-d) for d in deg]
                prod=Fraction(1)
                for ww in ws:prod*=1+ww
                tv=Fraction(0)
                for mask,ww in w.items():
                    q=Fraction(1,1)
                    for i,t in enumerate(ws):q*=t/(1+t) if mask>>i&1 else 1/(1+t)
                    tv+=abs(ww/Z-q)
                tv/=2
                C=(float(c)**3/2)*exp(float(c)*exp(float(c)/2))
                assert float(tv)<C/n+1e-14,(n,name,c,tv,C/n)
                checks+=1
    # Complete-graph reduction, evaluated separately at increasing sizes.
    # Mean and cross-covariance converge to +e^-1 and -e^-1 at c=1.
    previous_mean_dev = 2.0
    previous_cov_dev = 2.0
    for n in (15,30,60,120,240):
        z=1/n; p=z/(1+z)
        log_weights=[]
        for k in range(n+1):
            log_weights.append(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
                               + k*log(z) + ((n-k)*(n-k-1)//2)*log1p(z))
        mx=max(log_weights)
        probs=[exp(t-mx) for t in log_weights]
        sm=sum(probs)
        probs=[v/sm for v in probs]
        mean=sum(k*probs[k] for k in range(n+1))
        ymean=sum(((n-k)*(n-k-1)/2)*p*probs[k] for k in range(n+1))
        kymean=sum(k*((n-k)*(n-k-1)/2)*p*probs[k] for k in range(n+1))
        cov=kymean-mean*ymean
        err_mean=abs(mean-exp(-1))
        err_cov=abs(cov+exp(-1))
        assert err_mean<previous_mean_dev and err_cov<previous_cov_dev
        previous_mean_dev,previous_cov_dev=err_mean,err_cov
        checks+=1
    print('ALL_NEW_CHECKS_PASSED',checks)

if __name__=='__main__':check()
