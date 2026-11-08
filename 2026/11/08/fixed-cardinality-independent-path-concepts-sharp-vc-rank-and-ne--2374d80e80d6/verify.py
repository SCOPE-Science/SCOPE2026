"""Reproducible finite checks for path-independent fixed-cardinality concepts.
Run with Python 3.10+: python verify.py
"""
from functools import lru_cache
from itertools import combinations
from math import comb, floor, log2

def independent(m):
    return (m & (m << 1)) == 0

def concepts(n, k):
    return tuple(m for m in range(1 << n) if m.bit_count() == k and independent(m))

def shattered(C, s):
    seen = {c & s for c in C}
    return len(seen) == (1 << s.bit_count())

def vc(C, n):
    return max((s.bit_count() for s in range(1 << n) if shattered(C, s)), default=0)

def ldim(C, n):
    # Exact recursion on every realizable subfamily of hypotheses.
    if not C:
        return -1
    idx = {m: i for i, m in enumerate(C)}
    supports = tuple(1 << j for j in range(n))
    labels = tuple(sum((1 << i) for i, c in enumerate(C) if c & q) for q in supports)
    allh = (1 << len(C)) - 1
    @lru_cache(None)
    def f(h):
        # One query can support a full binary node only when both branches nonempty.
        val = 0
        for mask in labels:
            a = h & mask
            b = h & (allh ^ mask)
            if a and b:
                val = max(val, 1 + min(f(a), f(b)))
        return val
    return f(allh)

def balanced_lower(k, r):
    b = [k // r + (i < (k % r)) for i in range(r)]
    return sum((x + 1).bit_length() - 1 for x in b)

def run():
    cases=0
    for n in range(1, 15):
        for k in range((n + 1)//2 + 1):
            C=concepts(n,k)
            assert len(C) == comb(n-k+1,k), (n,k,len(C))
            found=vc(C,n)
            predicted=min(k,n-2*k+1)
            assert found==predicted,(n,k,found,predicted)
            cases+=1
    print('VC_ALL_PARAMETERS_PASS', cases)
    # Full trace of gadget support plus independent-set padding.
    gad=0
    for n in range(1,22):
        for k in range((n+1)//2+1):
            r=n-2*k+1
            t=min(k,r)
            Q = sum(1 << (3*i) for i in range(t))
            assert 3*t-2 <= n or t==0
            for assignment in range(1 << t):
                mask=0
                for i in range(t):
                    mask |= 1 << (3*i+(0 if assignment & (1<<i) else 1))
                for j in range(k-t):
                    mask |= 1 << (3*t+2*j)
                assert independent(mask) and mask.bit_count()==k and (mask & Q)==sum((1<<(3*i)) for i in range(t) if assignment & (1<<i)),(n,k,assignment)
                assert mask.bit_length()<=n,(n,k,assignment)
                gad+=1
    print('GADGET_ALL_ASSIGNMENTS_PASS',gad)
    online=[]
    for n in range(1, 14):
        for k in range((n+1)//2+1):
            C=concepts(n,k)
            d=ldim(C,n)
            r=n-2*k+1
            low=balanced_lower(k,r)
            high=(len(C)).bit_length()-1
            assert low<=d<=high,(n,k,low,d,high)
            if r==1:
                assert d==(k+1).bit_length()-1,(n,k,d)
            online.append((n,k,d))
    print('LDIM_ALL_SMALL_PASS',len(online))
    print('LDIM_EXAMPLES', [v for v in online if v[0] in (6,8,10,12)])
    print('FIXED_SIZE_PATH_VC_ONLINE_PASS')

if __name__ == '__main__':
    run()
