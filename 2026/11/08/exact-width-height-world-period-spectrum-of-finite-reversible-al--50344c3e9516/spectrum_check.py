"""Independent arithmetic check: orders of products of small symmetric groups.
Run: python spectrum_check.py
"""
from functools import lru_cache
from math import lcm


def partitions(n,mx=None):
    mx=n if mx is None else min(n,mx)
    if n==0:
        yield ()
    else:
        for k in range(mx,0,-1):
            for tail in partitions(n-k,k):
                yield (k,)+tail


def possible_layer_orders(width):
    return {lcm(*p) for n in range(1,width+1) for p in partitions(n)}


def prime_blocks(k):
    out=[];p=2
    while p*p<=k:
        if k%p==0:
            x=1
            while k%p==0:
                k//=p;x*=p
            out.append(x)
        p+=1
    if k>1:out.append(k)
    return out


def fit(blocks,capacity,bins):
    @lru_cache(None)
    def go(remaining,free):
        if not remaining:return True
        item=remaining[0]
        for i,s in enumerate(free):
            if item<=s:
                v=list(free);v[i]-=item
                if go(remaining[1:],tuple(sorted(v))):return True
        return False
    if any(x>capacity for x in blocks):return False
    return go(tuple(sorted(blocks,reverse=True)),tuple([capacity]*bins))


def check():
    tests=0
    for w in range(1,9):
        layer=possible_layer_orders(w)
        actual={1}
        universal=lcm(*range(1,w+1))
        for h in range(1,5):
            actual={lcm(a,b) for a in actual for b in layer}
            expected={d for d in range(1,universal+1) if universal%d==0 and fit(prime_blocks(d),w,h)}
            assert actual==expected, (w,h,actual^expected)
            tests+=1
    print('INDEPENDENT_PERIOD_SPECTRA_OK',tests)

if __name__=='__main__':check()
