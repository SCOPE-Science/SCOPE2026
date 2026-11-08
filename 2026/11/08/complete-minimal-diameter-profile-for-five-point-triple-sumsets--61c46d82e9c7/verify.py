"""Exact, finite certificate of five-point threefold-sumset diameter profile."""
from itertools import combinations, combinations_with_replacement
from math import comb

EXPECTED = {
    13: (4, (0, 1, 2, 3, 4)),
    15: (5, (0, 1, 2, 3, 5)),
    16: (5, (0, 1, 2, 4, 5)),
    17: (6, (0, 1, 2, 3, 6)),
    18: (6, (0, 1, 3, 4, 6)),
    19: (6, (0, 1, 2, 5, 6)),
    20: (7, (0, 1, 2, 5, 7)),
    21: (7, (0, 1, 2, 6, 7)),
    22: (7, (0, 1, 3, 6, 7)),
    23: (8, (0, 1, 3, 6, 8)),
    24: (8, (0, 1, 3, 7, 8)),
    25: (8, (0, 1, 4, 7, 8)),
    26: (9, (0, 1, 3, 8, 9)),
    27: (10, (0, 1, 4, 9, 10)),
    28: (11, (0, 1, 6, 9, 11)),
    29: (11, (0, 1, 4, 9, 11)),
    30: (12, (0, 1, 4, 10, 12)),
    31: (13, (0, 1, 4, 11, 13)),
    32: (14, (0, 1, 9, 11, 14)),
    33: (16, (0, 1, 7, 12, 16)),
    34: (19, (0, 1, 5, 16, 19)),
    35: (23, (0, 1, 15, 18, 23)),
}

def triple_cardinality_pairs(A):
    return len({a+b+c for a,b,c in combinations_with_replacement(A,3)})

def triple_cardinality_bits(A):
    # Independent shift-and-union realization of the threefold sumset.
    v=1
    for _ in range(3):
        u=0
        for a in A:
            u|=v<<a
        v=u
    return v.bit_count()

def verify():
    mins={}
    nsets=0
    extremizers=[]
    for diameter in range(4,24):
        for interior in combinations(range(1,diameter),3):
            A=(0,*interior,diameter)
            count1=triple_cardinality_pairs(A)
            count2=triple_cardinality_bits(A)
            assert count1==count2, (A,count1,count2)
            nsets+=1
            if count1==35: extremizers.append(A)
            mins.setdefault(count1,diameter)
    assert nsets==comb(23,4)==8855
    assert mins=={t:d for t,(d,A) in EXPECTED.items()},(mins,EXPECTED)
    for size,(d,A) in EXPECTED.items():
        assert A[0]==0 and A[-1]==d and len(set(A))==5
        assert triple_cardinality_pairs(A)==size
        assert triple_cardinality_bits(A)==size
        assert mins[size]==d
    assert set(mins)=={13,*range(15,36)}
    assert max(mins.values())==23 and [s for s,d in mins.items() if d==23]==[35]
    assert set(extremizers)=={
        (0,1,15,18,23),(0,1,15,20,23),
        (0,3,8,22,23),(0,5,8,22,23)}
    assert len(extremizers)==4
    assert len({tuple(sorted(23-a for a in A)) for A in extremizers})==4
    print('VERIFIED_B3_EXTREMIZERS', extremizers)
    print('VERIFIED_NORMALIZED_SETS',nsets,'diameters=4..23')
    print('VERIFIED_PROFILE',[(s,mins[s]) for s in sorted(mins)])
    print('VERIFIED_NATHANSON_INTERVAL_LENGTH',max(mins.values())+1)
    print('VERIFY_OK exact_finite_exhaustion=True external_spectrum_theorem_required_for_unbounded_exclusion_of_14=True independent_audit=False')

if __name__=='__main__':verify()
