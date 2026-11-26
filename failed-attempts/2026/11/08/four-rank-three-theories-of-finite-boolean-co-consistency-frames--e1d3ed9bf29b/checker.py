"""Exact rank-three back-and-forth profiles for finite co-consistency frames.

Run: python3 compat_checker.py; uses only Python standard library.
"""
from itertools import combinations


def pair_type(a, b, c, d):
    # A\B, B\A, A&B, U\(A|B), with A and B nonempty.
    if a == b == 0:
        # A = B: 00 iff d>0; 11 iff another nonempty subset exists.
        assert c > 0
        return (1, 1, (1 if d else 0) | (8 if c+d >= 2 else 0))
    assert a+c>0 and b+c>0
    m = (1 if d else 0)
    if b and (c or b >= 2 or d): m |= 2  # 01
    if a and (c or a >= 2 or d): m |= 4  # 10
    if c == 0 or c >= 2 or (a+b+d >= 2): m |= 8  # 11
    return (0, int(c>0), m)


def unary_rank2(k, l):
    out = set()
    for c in range(k+1):
        a = k-c
        for b in range(l+1):
            d = l-b
            if c+b:
                out.add(pair_type(a,b,c,d))
    return frozenset(out)


def theory_rank3(n):
    return frozenset(unary_rank2(k,n-k) for k in range(1,n+1))


def brute_pair_type(n, A, B):
    s = 0
    for C in range(1,1<<n):
        if C!=A and C!=B:
            s |= 1 << ((2 if C&A else 0) | (1 if C&B else 0))
    return (int(A==B), int(bool(A&B)), s)


def from_masks(n,A,B):
    full=(1<<n)-1
    return pair_type((A&~B).bit_count(),(B&~A).bit_count(),(A&B).bit_count(),(full&~(A|B)).bit_count())


def verify():
    # Full brute source test for every pair up to 7 atoms.
    tested=0
    for n in range(1,8):
        for A in range(1,1<<n):
            for B in range(1,1<<n):
                assert from_masks(n,A,B)==brute_pair_type(n,A,B),(n,A,B)
                tested+=1
    # Independent unary orbit-vs-direct finite check.
    for n in range(1,8):
        for k in range(1,n+1):
            A=(1<<k)-1
            direct=frozenset(from_masks(n,A,B) for B in range(1,1<<n))
            assert direct == unary_rank2(k,n-k),(n,k)
    # Finite truncation lemma: for any a,c <= arbitrary,
    # pair signatures depend only on min(a,2) etc. Feasible
    # a+c=k,b+d=l; beyond 4 counts yield no new capped pairs.
    # Show any k>=4 pattern is represented at k=4 (and vice versa),
    # with full q2 signature sets independent of the other side.
    # We check the finite base rectangle and a substantial extension.
    for k in range(1,31):
        for l in range(0,31):
            want=unary_rank2(min(k,4),min(l,4))
            assert unary_rank2(k,l)==want,(k,l)
    classes=[]
    for n in range(1,31):
        t=theory_rank3(n)
        if t not in classes:classes.append(t)
        assert classes.index(t)==min(n,4)-1
    assert len(classes)==4
    # Show explicit pointed-type sets are universal for each category.
    assert unary_rank2(1,2)==unary_rank2(1,10)
    assert unary_rank2(2,1)==unary_rank2(10,1)
    assert unary_rank2(2,2)==unary_rank2(10,10)
    assert unary_rank2(3,0)==unary_rank2(10,0)
    # Construct exact nested-rank 3 thresholds via finite combinatorial witnesses.
    for n in range(1,9):
        masks=range(1,1<<n)
        disjoint2=any(A&B==0 for A in masks for B in masks)
        disjoint3=any(A&B==0 and A&C==0 and B&C==0 for A in masks for B in masks for C in masks)
        has_both=any(A.bit_count()>=2 and n-A.bit_count()>=2 for A in masks)
        assert (disjoint2,disjoint3,has_both)==(n>=2,n>=3,n>=4)
    print('COMPAT_RANK3_VERIFIED', 'direct_pair_checks=',tested,'q3_classes=',len(classes),'threshold=4')

if __name__=='__main__':verify()
