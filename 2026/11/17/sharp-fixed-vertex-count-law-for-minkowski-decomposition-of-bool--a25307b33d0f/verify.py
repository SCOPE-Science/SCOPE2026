"""Standalone exact checks for fixed-cardinality decomposability of Boolean vertex sets."""
from itertools import combinations
from math import comb, factorial


def active(S, d):
    return all(any((x >> j) & 1 for x in S) and
               any(not ((x >> j) & 1) for x in S) for j in range(d))


def product_split(S, d):
    # Fix coordinate zero in the first block to count each unordered bipartition once.
    for bits in range(1, 1 << d):
        if not (bits & 1) or bits == (1 << d) - 1:
            continue
        a = {x & bits for x in S}
        b = {x & (((1 << d) - 1) ^ bits) for x in S}
        if len(a) * len(b) == len(S):
            return True
    return False


def active_count(d, k):
    return sum((-1)**j * comb(d, j) * 2**j *
               (comb(2**(d-j), k) if k <= 2**(d-j) else 0)
               for j in range(d+1))


def d4(d):
    return 2**(d-3)*(2**d-2) if d >= 2 else 0


def d6(d):
    return (8**d - 6**d - 3*4**d + 5*2**d)//12


def d9(d):
    return (12**d - 6*8**d + 4*6**d + 9*4**d - 12*2**d)//72


def recurrence(d_max, k_max):
    a = {(d, k): active_count(d, k) for d in range(1, d_max+1)
         for k in range(2, min(2**d,k_max)+1)}
    i = {}
    from itertools import product
    def partitions(seq):
        if not seq:
            yield []
            return
        first,*rest = seq
        for p in partitions(rest):
            yield [[first]]+[b[:] for b in p]
            for j in range(len(p)):
                cp=[b[:] for b in p]
                cp[j]=[first]+cp[j]
                yield cp
    for d in range(1,d_max+1):
        for k in range(2,min(2**d,k_max)+1):
            composite=0
            for part in partitions(list(range(d))):
                if len(part)<2: continue
                # multiply cardinalities of the blocks to k
                def walk(j, prod, mult):
                    if j==len(part):
                        return mult if prod==k else 0
                    total=0
                    for v in range(2, min(k//prod, 2**len(part[j]))+1):
                        if k % (prod*v)==0:
                            total += walk(j+1,prod*v,mult*i.get((len(part[j]),v),0))
                    return total
                composite += walk(0,1,1)
            i[(d,k)]=a[d,k]-composite
    return a,i


if __name__=='__main__':
    a, i = recurrence(5, 10)
    nchecks=0
    for d in range(1,5):
        reported={}
        for k in range(2, min(2**d,10)+1):
            n_active=n_dec=0
            for S in combinations(range(1 << d), k):
                if active(S,d):
                    n_active+=1
                    n_dec+=product_split(S,d)
            assert n_active==a[(d,k)],(d,k,n_active,a[(d,k)])
            assert n_dec==a[(d,k)]-i[(d,k)],(d,k,n_dec,a[(d,k)]-i[(d,k)])
            if k==4: assert n_dec==d4(d)
            if k==6: assert n_dec==d6(d)
            if k==9: assert n_dec==d9(d)
            nchecks+=2
            reported[k]=(n_active,n_dec)
        print('dimension',d,'counts (active, decomposable)',reported)
    for d in range(1,6):
        if d>=2: assert a[(d,4)]-i[(d,4)]==d4(d)
        if d>=3: assert a[(d,6)]-i[(d,6)]==d6(d)
        if d>=4: assert a[(d,9)]-i[(d,9)]==d9(d)
        nchecks+=3
    print('PASS',nchecks,'exact cross-checks; direct subset enumeration through dimension four')
