"""Exact, dependency-free finite checks of balanced aperiodic-word Fourier spectra.
Run: python3 check_exact.py
"""
from itertools import combinations
from math import comb

def least_period_full(x,n):
    for d in range(1,n):
        if n%d==0 and all(((x>>i)&1)==((x>>(i%d))&1) for i in range(n)):
            return d
    return n

def fwht(values):
    a=values[:]
    step=1
    while step<len(a):
        for start in range(0,len(a),2*step):
            for j in range(start,start+step):
                u,v=a[j],a[j+step]
                a[j],a[j+step]=u+v,u-v
        step*=2
    return a

def run(m):
    n=2*m
    f=[0]*(1<<n)
    for picks in combinations(range(n),m):
        x=sum(1<<i for i in picks)
        if least_period_full(x,n)==n:
            f[x]=1
    spectrum=fwht(f)
    B=sum(f)
    assert all((spectrum[s]==0)==(s.bit_count()%2==1) for s in range(1<<n))
    assert sum(v*v for v in spectrum)==(1<<n)*B
    M=(m+1)*comb(m,(m-1)//2)//m
    R=comb(2*m,m)-B
    assert min(abs(v) for v in spectrum if v) >= M-R
    assert max(abs(v) for v in spectrum)==B
    if m in (3,5,7):
        assert R==2
        assert min(abs(v) for v in spectrum if v)==M-2
        for s,actual in enumerate(spectrum):
            t=s.bit_count()
            if t%2:
                assert actual==0
                continue
            j=t//2
            K=(-1)**j*comb(2*m,m)*comb(m,j)//comb(2*m,2*j)
            eps=(-1)**sum((s>>i)&1 for i in range(0,n,2))
            assert actual==K-2*eps
        min_multiplicity=sum(abs(v)==M-2 for v in spectrum)
        assert min_multiplicity==comb(2*m,m-1)+comb(m,(m-1)//2)
    print('m',m,'support',B,'rank',sum(bool(v) for v in spectrum),
          'min_positive',min(abs(v) for v in spectrum if v),'max',B)

for m in (3,5,7,9):
    run(m)
print('CHECK_EXACT_PASS')
