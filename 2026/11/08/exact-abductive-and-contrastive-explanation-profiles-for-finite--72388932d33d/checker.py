"""Exhaustive direct enumeration of persistence explanation sets."""
from itertools import product
from math import comb

def compliant(w):
    return all(w[i] <= w[i+1] for i in range(len(w)-1))

def direct_profiles(w):
    n = len(w)
    label = compliant(w)
    wa, wc = set(), set()
    words = list(product((0,1), repeat=n))
    for mask in range(1<<n):
        agree = [v for v in words if all(v[i]==w[i] for i in range(n) if mask>>i & 1)]
        if all(compliant(v)==label for v in agree):
            wa.add(mask)
        unlocked = [v for v in words if all(v[i]==w[i] for i in range(n) if not(mask>>i & 1))]
        if any(compliant(v)!=label for v in unlocked):
            wc.add(mask)
    minimal=lambda family: {m for m in family if not any((k!=m and k&m==k) for k in family)}
    return minimal(wa),minimal(wc)

def predicted_profiles(w):
    n=len(w)
    if not compliant(w):
        ax={ (1<<i)|(1<<j) for i in range(n) for j in range(i+1,n) if w[i]==1 and w[j]==0}
        cx=set()
        for c in range(n+1):
            if (c==0 and w[0]==1) or (c==n and w[-1]==0) or (0<c<n and w[c-1]==0 and w[c]==1):
                mask=sum((1<<i) for i in range(n) if (i<c and w[i]==1) or (i>=c and w[i]==0))
                cx.add(mask)
        return ax,cx
    if all(x==0 for x in w):
        return { (1<<(n-1))-1}, {1<<i for i in range(n-1)}
    if all(x==1 for x in w):
        return {((1<<n)-1)^1}, {1<<i for i in range(1,n)}
    a = w.index(1)
    base = sum((1<<i) for i in range(n) if i not in (a-1,a))
    ax={base|(1<<(a-1)),base|(1<<a)}
    cx={1<<i for i in list(range(a-1))+list(range(a+1,n))}
    cx.add((1<<(a-1))|(1<<a))
    return ax,cx

for n in range(1,9):
    counts={}
    for w in product((0,1),repeat=n):
        actual=direct_profiles(w)
        predicted=predicted_profiles(w)
        assert actual==predicted, (n,w,actual,predicted)
        if not compliant(w):
            d=sum(w[i]==1 and w[i+1]==0 for i in range(n-1))
            inv=sum(w[i]==1 and w[j]==0 for i in range(n) for j in range(i+1,n))
            assert len(actual[0])==inv and len(actual[1])==d+1
            counts[d]=counts.get(d,0)+1
        else:
            assert len(actual[1])==n-1
            assert len(actual[0])==(1 if w.count(0) in (0,n) else 2)
    for d,c in counts.items():
        assert c==comb(n+1,2*d+1),(n,d,c,comb(n+1,2*d+1))
    assert sum(counts.values())==2**n-n-1
    print('n',n,'verified',2**n,'words, violating distribution',sorted(counts.items()))
print('ALL_CHECKS_OK')
