"""Independent integer-triple spectrum and alpha-renaming orbit check."""
from collections import defaultdict, Counter
from itertools import product, combinations

def signature(a):
    # By the prefix and k-gram de Bruijn flow identity, this is the full
    # k-abelian signature for length>=3; here k=3.
    if len(a)<3:
        return tuple(a)
    q=5
    counts=[0]*125
    for i in range(len(a)-2):
        x,y,z=a[i:i+3]
        counts[x*q*q+y*q+z]+=1
    return (tuple(a[:2]),tuple(counts))

def expected_families(q):
    s=set()
    for a in range(q):
        for b in range(q):
            if b!=a:
                x=(a,a,a,b,a,a,b,a,a,a)
                y=(a,a,b,a,a,a,a,b,a,a)
                s.add(tuple(sorted((x,y))))
        for b,c in combinations([x for x in range(q) if x!=a],2):
            x=(a,a,b,c,a,a,c,b,a,a)
            y=(a,a,c,b,a,a,b,c,a,a)
            s.add(tuple(sorted((x,y))))
    return s

for n in range(1,11):
    fibers=defaultdict(list)
    for seed in product(range(5),repeat=(n+1)//2):
        w=seed+tuple(reversed(seed)) if n%2==0 else seed+tuple(reversed(seed[:-1]))
        fibers[signature(w)].append(w)
    collision=[tuple(sorted(f)) for f in fibers.values() if len(f)>1]
    if n<10:
        assert not collision, (n,len(collision))
    else:
        assert all(len(f)==2 for f in collision)
        assert set(collision)==expected_families(5)
        assert len(collision)==50
        assert len(fibers)==3075
    # independently reconstruct full 1- and 2-gram counts from 3-grams
    if n>=3:
        for f in fibers.values():
            for w in f:
                triple=Counter(tuple(w[i:i+3]) for i in range(n-2))
                bigram=Counter(tuple(w[i:i+2]) for i in range(n-1))
                derived=Counter()
                for tri,c in triple.items():derived[tri[:2]]+=c
                derived[w[-2:]]+=1
                assert derived==bigram
print('VERIFY_INDEPENDENT_OK q=5 n=1..10 verified_second_order_projection')
