#!/usr/bin/env python3
"""Independent finite-dimensional direct moment checker for balanced sign chambers.
No random integration: magnitude fourth moments and sign averages are evaluated independently.
"""
import math
from itertools import combinations
from functools import lru_cache
import numpy as np

@lru_cache(None)
def mag_moment(n, exponents):
    s=sum(exponents)
    val=math.gamma(n/2)/math.gamma((n+s)/2)
    for p in exponents:
        val*=math.gamma((p+1)/2)/math.gamma(.5)
    return val

def direct_gram(n):
    # Frobenius-orthonormal trace-free symmetric basis.
    A=[]
    # Diagonal difference basis from standard Helmert contrasts.
    for m in range(1,n):
        vec=np.zeros(n)
        vec[:m]=1/math.sqrt(m*(m+1))
        vec[m]=-m/math.sqrt(m*(m+1))
        A.append(np.diag(vec))
    for i,j in combinations(range(n),2):
        mat=np.zeros((n,n));mat[i,j]=mat[j,i]=1/math.sqrt(2)
        A.append(mat)
    signs=[]
    for inds in combinations(range(n),n//2):
        ss=-np.ones(n);ss[list(inds)]=1
        signs.append(ss)
    signs=np.array(signs)
    @lru_cache(None)
    def m4(idxs):
        ids=list(idxs)
        ee=tuple(ids.count(i) for i in range(n))
        odd=[i for i,e in enumerate(ee) if e%2]
        sg=np.prod(signs[:,odd],axis=1).mean() if odd else 1.
        return sg*mag_moment(n,ee)
    N=len(A);G=np.zeros((N,N)); coeff=[]
    for M in A:
        terms=[(i,i,float(M[i,i])) for i in range(n) if M[i,i]]
        terms += [(i,j,2*float(M[i,j])) for i in range(n) for j in range(i+1,n) if M[i,j]]
        coeff.append(terms)
    for a in range(N):
        for b in range(a,N):
            tot=sum(u*v*m4(tuple(sorted((i,j,k,l)))) for i,j,u in coeff[a] for k,l,v in coeff[b])
            G[a,b]=G[b,a]=tot*n*(n+2)/2
    return G

def predicted(n):
    p=math.pi
    u=1-4*(n-2)/(p*(n-1))+6*(n-2)/(p*p*(n-1))
    b=1-2*(n-4)/(p*(n-1))-12/(p*p*(n-1))
    c=1+4/(p*(n-1))+12/(p*p*(n-1)*(n-3))
    gamma2=2*(n-2)/(p*p*(n-1)**2)
    half=math.sqrt((1-b)**2+4*gamma2)/2
    lm=(1+b)/2-half;lp=(1+b)/2+half
    return sorted([u]+[lm]*(n-1)+[lp]*(n-1)+[c]*(n*(n-3)//2)),dict(trivial=u,standard_low=lm,standard_high=lp,edge=c)

if __name__=='__main__':
    for n in [4,6,8,10]:
        G=direct_gram(n)
        ev=np.linalg.eigvalsh(G)
        ref,br=predicted(n)
        assert len(ref)==len(ev)==n*(n+1)//2-1
        err=max(abs(ev-ref))
        assert err<2e-12,(n,err)
        assert (br['standard_low']<br['trivial'])==(n<=10)
        assert br['edge']>max(br['standard_high'],br['trivial'])
        assert ev[0]>0
        print(f'd={n} dimension={len(ev)} max_spectral_error={err:.2e} branches='+str({k:round(v,9) for k,v in br.items()}))
    print('BALANCED_ORTHANT_QUADRATIC_DIRECT_MOMENTS_PASS')
