"""Independent direct profile calculations and de Bruijn sharpness witnesses."""
from collections import Counter
from itertools import product

def debruijn(k,q):
    a=[0]*(k*q+1)
    seq=[]
    def db(t,p):
        if t>k:
            if k%p==0:
                seq.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,q):
                a[t]=j
                db(t+1,t)
    db(1,1)
    return tuple(seq+seq[:k-1])

def full_profile(w):
    return Counter(zip(w,w[1:],w[2:]))

def deltas_direct(w,q):
    base=full_profile(w)
    ans=set()
    for i in range(len(w)):
        for f in range(q):
            if f==w[i]:continue
            new=w[:i]+(f,)+w[i+1:]
            d=full_profile(new)
            d.subtract(base)
            ans.add(tuple(sorted((x,v) for x,v in d.items() if v)))
    return ans

def local_delta(w,i,f):
    start=max(i-2,0)
    stop=min(i,len(w)-3)
    old=Counter(w[j:j+3] for j in range(start,stop+1))
    new=list(w);new[i]=f
    d=Counter(tuple(new[j:j+3]) for j in range(start,stop+1))
    d.subtract(old)
    return tuple(sorted((x,v) for x,v in d.items() if v))

def dels_fast(w,q):
    return {local_delta(w,i,f) for i in range(len(w)) for f in range(q) if f!=w[i]}

def M(q): return (q-1)*(q**5-q*q-4*q+4)

for q in (2,3,4):
    w=debruijn(5,q)
    assert len(w)==q**5+4
    assert len({w[i:i+5] for i in range(len(w)-4)})==q**5
    v=deltas_direct(w,q)
    assert len(v)==M(q),(q,len(v),M(q))
    assert v==dels_fast(w,q)
    print('q=%d: deBruijn length=%d directly observed %d profiles = sharp capacity'%(q,len(w),len(v)))

for q,length in ((2,11),(3,7),(4,6)):
    m=M(q)
    maxseen=0
    for w in product(range(q),repeat=length):
        v=deltas_direct(w,q)
        assert v==dels_fast(w,q)
        maxseen=max(maxseen,len(v))
        assert len(v)<=m
    print('q=%d: independently enumerated %d words of length=%d, max profile count %d'%(q,q**length,length,maxseen))

# Repeat-order-five de Bruijn witness can be padded by repeating an existing
# symbol at its right end: its five-gram coverage survives and boundaries
# remain isolated, hence every subsequent length also attains the bound.
for q in (2,3,4):
    w=debruijn(5,q)
    for append in range(1,4):
        v=dels_fast(w+(w[-1],)*append,q)
        assert len(v)==M(q)
print('PASS direct profiles and sharpness')
