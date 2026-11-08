#!/usr/bin/env python3
"""Direct finite-prime Fourier verification of a normalized rank-one matrix set."""
import itertools, cmath, collections, math

def count_rank(a, d, e, p):
    a = [[a[i * e + j] % p for j in range(e)] for i in range(d)]
    r = 0
    for j in range(e):
        pivot = next((k for k in range(r, d) if a[k][j]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(z * inv) % p for z in a[r]]
        for k in range(d):
            if k != r:
                t = a[k][j]
                a[k] = [(v - t * w) % p for v, w in zip(a[k], a[r])]
        r += 1
    return r

def matrix_rank_count(d,e,r,q):
    if r == 0: return 1
    return math.prod((q**d-q**j)*(q**e-q**j) for j in range(r)) // math.prod(q**r-q**j for j in range(r))

def verify(p,m,n):
    d,e=m-1,n-1
    vals=range(p)
    u=[x for x in itertools.product(vals,repeat=m) if sum(x)%p==1]
    v=[x for x in itertools.product(vals,repeat=n) if sum(x)%p==1]
    support={tuple((a*b)%p for a in x for b in y) for x in u for y in v}
    assert len(support)==p**(d+e)
    obs=collections.Counter()
    for a in itertools.product(vals,repeat=m*n):
        tally=[0]*p
        for z in support: tally[sum(x*y for x,y in zip(a,z))%p]+=1
        f=sum(cnt*cmath.exp(2j*math.pi*t/p) for t,cnt in enumerate(tally))
        if abs(f)<1e-8: obs[0]+=1
        else:
            found=False
            for r in range(min(d,e)+1):
                mod=p**(d+e-r)
                if abs(abs(f)-mod)<1e-7:
                    obs[mod]+=1;found=True;break
            assert found,(p,m,n,tally,f)
    expect=collections.Counter({p**(d+e-r):p**(2*r+1)*matrix_rank_count(d,e,r,p) for r in range(min(d,e)+1)})
    expect[0]=p**(m*n)-sum(expect.values())
    assert obs==expect,(p,m,n,obs,expect)
    return len(obs)

if __name__=='__main__':
    cases=[(2,2,2),(2,2,3),(2,3,2),(2,3,3),(3,2,2),(3,2,3),(3,3,2),(5,2,2)]
    for p,m,n in cases:
        bands=verify(p,m,n)
        print(f'PASS q={p} m={m} n={n} spectral_bands={bands}')
    print('NORMALIZED_SEGRE_CONVOLUTION_PASS cases=',len(cases))
