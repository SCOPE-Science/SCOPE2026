"""Independent occupancy composition and three-symbol exponential-weight census."""
from math import comb, factorial
from itertools import product
from collections import defaultdict
from functools import lru_cache

def compositions(n,q):
    if q == 1:
        yield (n,)
    else:
        for k in range(n+1):
            for b in compositions(n-k,q-1):yield (k,)+b

def population_clock(m,h):
    q=len(m)
    active=[k>=h for k in m]
    if all(active):return (0,q)
    clock=0
    for i in range(q):
        if active[i] and not active[i-1]:
            k=0
            while k<q and active[(i+k)%q]:k+=1
            clock=max(clock,k-1+int(m[i-1]>0))
    return (clock,1)

def count_by_composition(n,q,h):
    out=defaultdict(int)
    for m in compositions(n,q):
        # Exact multinomial weight for this occupancy composition.
        den=1
        for k in m:den*=factorial(k)
        out[population_clock(m,h)]+=factorial(n)//den
    return dict(out)

def count_by_signature(n,q,h):
    # Exact labelled block counts from binomial convolution; no state updates.
    @lru_cache(None)
    def blocks(m,small,large):
        if small==large==0:return int(m==0)
        if small:
            return sum(comb(m,j)*blocks(m-j,small-1,large)
                       for j in range(1,min(h,m+1)))
        return sum(comb(m,j)*blocks(m-j,small,large-1)
                   for j in range(h,m+1))
    out=defaultdict(int)
    for s in product((0,1,2),repeat=q):
        if h==1 and 1 in s:continue
        active=[k==2 for k in s]
        if all(active):pair=(0,q)
        else:
            clock=0
            for i in range(q):
                if active[i] and not active[i-1]:
                    k=0
                    while k<q and active[(i+k)%q]:k+=1
                    clock=max(clock,k-1+int(s[i-1]==1))
            pair=(clock,1)
        out[pair]+=blocks(n,s.count(1),s.count(2))
    return {k:v for k,v in out.items() if v}

if __name__=='__main__':
    triples=0;weighted=0
    for q in range(3,8):
        for h in range(1,5):
            for n in range(2,15):
                x=count_by_composition(n,q,h)
                y=count_by_signature(n,q,h)
                assert x==y,(q,h,n,x,y)
                assert sum(x.values())==q**n
                sharp=min(q-2,n-1) if h==1 else min(q-1,(n-1)//h)
                assert max(t for t,p in x)==sharp
                triples+=1;weighted+=q**n
    print('PASS independent composition versus three-symbol labelled-weight census')
    print('q=3..7, threshold=1..4, n=2..14; sharp maxima checked')
    print('parameter_triples=',triples,sep='')
    print('weighted_configurations=',weighted,sep='')
