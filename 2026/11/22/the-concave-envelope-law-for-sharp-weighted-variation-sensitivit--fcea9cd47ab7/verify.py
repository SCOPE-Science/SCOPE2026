"""Exact-arithmetic checks for the sharp weighted-variation isotonic modulus.

Run with Python 3 and no third-party dependencies.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def wmean(vals, masses):
    return sum((x*m for x,m in zip(vals,masses)), F(0))/sum(masses)


def pava(x,m):
    blocks=[]
    for i,(xi,mi) in enumerate(zip(x,m)):
        blocks.append([i,i,mi,mi*xi])
        while len(blocks)>1 and blocks[-2][3]/blocks[-2][2] > blocks[-1][3]/blocks[-1][2]:
            b=blocks.pop();a=blocks[-1]
            a[1]=b[1];a[2]+=b[2];a[3]+=b[3]
    out=[F(0)]*len(x)
    for a,b,mm,ss in blocks:
        for i in range(a,b+1): out[i]=ss/mm
    return out


def part_matrices(n,m):
    # Partitions into contiguous blocks; output row indices with averaging masses.
    for mask in range(1<<(n-1)):
        blocks=[];a=0
        for i in range(n-1):
            if mask & (1<<i):
                blocks.append((a,i));a=i+1
        blocks.append((a,n-1))
        yield blocks


def apply_partition(h,m,blocks):
    out=[F(0)]*len(h)
    for a,b in blocks:
        v=wmean(h[a:b+1],m[a:b+1])
        for i in range(a,b+1): out[i]=v
    return out


def var(h,w):
    return sum((wi*abs(y-x) for wi,x,y in zip(w,h,h[1:])),F(0))


def step(n,j):
    return [F(int(i>=j)) for i in range(n)]  # j is zero-based cut (between j-1 and j)


def envelope(m,w):
    n=len(m)
    t=[F(0)]
    for mass in m:t.append(t[-1]+mass)
    W=[F(0)]+w+[F(0)]
    out=[]
    for j in range(1,n):
        best=W[j];best_pair=(j,j)
        for p in range(j):
            for q in range(j+1,n+1):
                z=((t[q]-t[j])*W[p]+(t[j]-t[p])*W[q])/(t[q]-t[p])
                if z>best:best=z;best_pair=(p,q)
        out.append((best,best_pair))
    return out


def blocknorm(n,m,w,blocks):
    return max(var(apply_partition(step(n,j),m,blocks),w)/w[j-1] for j in range(1,n))


def exact_modulus(m,w):
    e=envelope(m,w)
    return max(v/w[j] for j,(v,pair) in enumerate(e)),e


def pair_witness(m,w):
    n=len(m)
    K,e=exact_modulus(m,w)
    j=max(range(1,n),key=lambda j:e[j-1][0]/w[j-1]);p,q=e[j-1][1]
    if p==q:
        x=[F(i) for i in range(n)]
    else:
        a=p  # zero-based starting index of pooled block
        b=q-1
        y=[F(i+1) if i<a or i>b else F(a+1) for i in range(n)]
        lam=[F(1) if a<=k<b else F(0) for k in range(n-1)]
        x=[]
        for i in range(n):
            d=(lam[i] if i<n-1 else F(0))-(lam[i-1] if i>0 else F(0))
            x.append(y[i]+d/m[i])
        assert pava(x,m)==y,(m,w,j,p,q,x,y,pava(x,m))
    h=step(n,j)
    eps=F(1,10000)
    xx=[x[i]+eps*h[i] for i in range(n)]
    got=var([a-b for a,b in zip(pava(xx,m),pava(x,m))],w)/var([eps*v for v in h],w)
    assert got==K,(m,w,j,p,q,K,got,x)
    return K,j,p,q


def verify():
    rng=Random(421113)
    cases=0;partition_tests=0; witness_tests=0
    for n in range(2,9):
        masses=[
            [F(1)]*n,
            [F(i+1) for i in range(n)],
            [F(2**(i%5)) for i in range(n)],
            [F(rng.randint(1,10)) for _ in range(n)]
        ]
        weights=[
            [F(1)]*(n-1),
            [F(2) if i%2==0 else F(1,2) for i in range(n-1)],
            [F(i+1) for i in range(n-1)],
            [F(rng.randint(1,10)) for _ in range(n-1)]
        ]
        for m in masses:
            for w in weights:
                K,e=exact_modulus(m,w)
                M=max(blocknorm(n,m,w,blocks) for blocks in part_matrices(n,m))
                assert K==M,(n,m,w,K,M)
                partition_tests+=1<<(n-1)
                pair_witness(m,w)
                witness_tests+=1
                cases+=1
    print('EXACT_ALL_CONTIGUOUS_ACTIVE_PARTITIONS_EQUAL_CHORD_ENVELOPE_PASS',cases,partition_tests)
    print('EXACT_KKT_PAIR_WITNESS_ATTAINS_GLOBAL_MODULUS_PASS',witness_tests)
    n=4;m=[F(1)]*n;w=[F(1),F(1,2),F(1)]
    K,j,p,q=pair_witness(m,w)
    assert (K,j,p,q)==(F(2),2,1,3)
    print('FOUR_SITE_SHARP_NONCONCAVE_WEIGHT_FACTOR_PASS',K)
    for n in range(2,9):
        m=[F(i+1) for i in range(n)]
        t=[F(0)]
        for x in m:t.append(t[-1]+x)
        w=[t[j]*(t[-1]-t[j]) for j in range(1,n)]
        K,_=exact_modulus(m,w)
        assert K==1
    print('MASS_COORDINATE_CONCAVE_STABILIZING_WEIGHTS_PASS')
    # Direct PAVA differences, not only derivatives and attained witnesses.
    trials=0
    for n in range(2,9):
        for _ in range(200):
            m=[F(rng.randint(1,7)) for i in range(n)]
            w=[F(rng.randint(1,7)) for i in range(n-1)]
            x=[F(rng.randint(-12,12)) for i in range(n)]
            y=[F(rng.randint(-12,12)) for i in range(n)]
            d=[a-b for a,b in zip(x,y)];V=var(d,w)
            if not V:continue
            output=[a-b for a,b in zip(pava(x,m),pava(y,m))]
            assert var(output,w)<=exact_modulus(m,w)[0]*V
            trials+=1
    print('EXACT_GLOBAL_TWO_INPUT_PAVA_STRESS_PASS',trials)
    print('ALL_WEIGHTED_ISOTONIC_VARIATION_CHECKS_PASS')

if __name__=='__main__':verify()
