#!/usr/bin/env python3
"""Direct, exhaustive closed-neighborhood DET identifying-code census of P(13).

No third-party modules. The polynomial is counted over every one of 2**13 sensor masks,
not over a sample of orbit representatives.
"""
from collections import Counter
from itertools import combinations

Q=13
SQ={x*x % Q for x in range(1,Q)}
assert SQ=={1,3,4,9,10,12}
C=[sum(1 << v for v in range(Q) if u==v or (v-u)%Q in SQ)
   for u in range(Q)]
ALL=(1<<Q)-1


def det_identifying(mask):
    if any((mask&C[u]).bit_count()<2 for u in range(Q)):
        return False
    for u,v in combinations(range(Q),2):
        one=(C[u]&~C[v])&mask
        other=(C[v]&~C[u])&mask
        if one.bit_count()<2 and other.bit_count()<2:
            return False
    return True


def main():
    good=[mask for mask in range(1<<Q) if det_identifying(mask)]
    counts=Counter(mask.bit_count() for mask in good)
    expected={9:364,10:286,11:78,12:13,13:1}
    assert dict(counts)==expected, (counts,expected)
    print('vertices',Q,'edges',sum(int((u-v)%Q in SQ) for u in range(Q) for v in range(u)))
    print('all_tested',1<<Q)
    print('det_code_polynomial',','.join(f'{k}:{counts[k]}' for k in sorted(counts)))
    print('total_det_codes',len(good))
    print('minimum_size',min(counts),'optimal_count',counts[min(counts)])
    example=next(mask for mask in good if mask.bit_count()==9)
    print('example_optimum',','.join(str(x) for x in range(Q) if example>>x&1))
    failures=Counter()
    good_masks=set(good)
    for mask in range(1<<Q):
        if mask not in good_masks:
            failures[mask.bit_count()]+=1
    print('failure_spectrum',','.join(f'{k}:{failures[k]}' for k in sorted(failures)))
    assert all(det_identifying(m) for m in good)
    print('direct_verification_PASS')

if __name__=='__main__':
    main()
