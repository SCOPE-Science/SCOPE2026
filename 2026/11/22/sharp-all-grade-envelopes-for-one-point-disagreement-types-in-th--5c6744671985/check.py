"""Exact finite checks for sharp disagreement-grade envelopes.
The proof is analytic; these checks are finite sanity tests, not its substitute.
"""
from itertools import permutations
from math import factorial


def folded(n,k):
    return tuple((k+1-j if j<=k else j-k) if j%2 else (j+k if j<=n-k else 2*n-k+1-j) for j in range(1,n+1))


def spectrum_prefix(n, p):
    masks = [0]
    for v in p:
        masks.append(masks[-1] | (1 << (v-1)))
    out = [0]*(n+1)
    for i in range(n+1):
        a = (1 << i)-1
        for b in masks:
            out[(a^b).bit_count()]+=1
    return out


def spectrum_direct(n,p):
    out=[0]*(n+1)
    for i in range(n+1):
        for j in range(n+1):
            count = sum((t<=i) != (p.index(t)<j) for t in range(1,n+1))
            out[count]+=1
    return out

for n in range(1,81):
    for k in range(n+1):
        p=folded(n,k)
        assert sorted(p)==list(range(1,n+1)), (n,k,'not permutation')
        c=spectrum_prefix(n,p)
        assert c[k]==(k+1)*(n-k+1), (n,k,'not upper sharp',c)
        # Check the entire critical rectangle, not only its total size.
        masks=[0]
        for v in p:masks.append(masks[-1] | (1<<(v-1)))
        for u in range(n-k+1):
            for v in range(k+1):
                i,j=u+v,u+k-v
                intersection=((1<<i)-1 & masks[j]).bit_count()
                assert intersection==u,(n,k,u,v,intersection)
    if n<=15:
        for k in range(n+1):
            assert spectrum_prefix(n,folded(n,k))==spectrum_direct(n,folded(n,k))
print('FOLDED_CONSTRUCTORS_OK n=1..80 all k, grid identities')

for n in range(1,10):
    cnt=0; win=[0]*(n+1)
    for p in permutations(range(1,n+1)):
        c=spectrum_prefix(n,p)
        assert sum(c)==(n+1)**2
        for k,z in enumerate(c):
            lo=2*min(k+1,n-k+1)
            hi=(k+1)*(n-k+1)
            assert lo<=z<=hi,(n,p,k,z,lo,hi)
            if z==hi:win[k]+=1
        if n<=5:
            assert c==spectrum_direct(n,p)
        cnt+=1
    print('n',n,'exhaustive_perms',cnt,'upper_equal_cases',win)
    assert cnt==factorial(n)
print('VERIFY_OK')
