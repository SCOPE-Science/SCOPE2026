from itertools import permutations,combinations
from math import comb,factorial
from functools import lru_cache

def chain_trace_counts(n,max_k=None):
    domain=list(range(1, (1<<n)-1))
    all_concepts=[]
    for p in permutations(range(n)):
        a=0; row=0
        for i in p[:-1]:
            a |= 1<<i
            row|=1<<domain.index(a)
        all_concepts.append(row)
    assert len(all_concepts)==factorial(n)
    if max_k is None:max_k=n-1
    counts=[]
    for k in range(max_k+1):
        nshattered=0
        for sup in combinations(range(len(domain)),k):
            trace=set()
            for c in all_concepts:
                t=0
                for j,i in enumerate(sup):
                    if c>>i&1:t|=1<<j
                trace.add(t)
                if len(trace)==1<<k:break
            shap=all((domain[sup[i]]&domain[sup[i+1]]==domain[sup[i]]) for i in range(k-1))
            if len(trace)==1<<k:
                assert shap,(n,k,sup,'nonchain shattered')
                nshattered+=1
            else:
                assert not shap,(n,k,sup,'chain not shattered')
        counts.append(nshattered)
    stir=[[0]*(n+2) for _ in range(n+1)]
    stir[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            stir[i][j]=j*stir[i-1][j]+stir[i-1][j-1]
    expect=[factorial(k+1)*stir[n][k+1] for k in range(max_k+1)]
    assert counts==expect,(n,counts,expect)
    print('n',n,'up to k',max_k,'counts',counts,'checked supports',sum(comb(2**n-2,k) for k in range(max_k+1)),flush=True)

for n in range(2,6):chain_trace_counts(n)
print('BOOLEAN_MAXIMAL_CHAINS_TRACE_PASS')
