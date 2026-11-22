#!/usr/bin/env python3
"""Verify twelve explicit biclique orientations for consecutive-size stars."""
import json
from pathlib import Path

def semigroup(k, limit):
    return {i*k+j*(k+1) for i in range(limit//k+1)
            for j in range(limit//(k+1)+1) if i*k+j*(k+1)<=limit}

def check():
    cases=json.loads((Path(__file__).with_name('certificates.json')).read_text('utf-8'))
    expected=set()
    for k in (4,5):
        conductor=k*(k-1)
        all_small=semigroup(k,conductor)
        assert conductor in all_small and conductor-1 not in all_small
        holes=[x for x in range(1,conductor) if x not in all_small]
        expected_holes={4:[1,2,3,6,7,11], 5:[1,2,3,4,7,8,9,13,14,19]}[k]
        assert holes==expected_holes
        expected.update((k,a,b) for a in holes for b in holes
                        if a<=b and a+b>=k*k-1)
        assert len({p for p in expected if p[0]==k})=={4:3,5:9}[k]
    assert len(expected)==12
    actual=[(c['k'],c['a'],c['b']) for c in cases]
    assert len(actual)==len(set(actual))==12
    assert set(actual)==expected
    print('SEMIGROUP_AND_EXCEPTION_COVERAGE_PASS')
    for case in cases:
        k,a,b=case['k'],case['a'],case['b']
        masks=case['masks']
        assert all(isinstance(v,int) and not isinstance(v,bool) for v in masks)
        assert len(masks)==a and all(0<=mask<(1<<b) for mask in masks)
        degrees_left=[b-mask.bit_count() for mask in masks]
        degrees_right=[sum((mask>>j)&1 for mask in masks) for j in range(b)]
        assert sum(degrees_left)+sum(degrees_right)==a*b
        S=semigroup(k,max(a,b))
        assert all(d in S for d in degrees_left+degrees_right)
    print('TWELVE_EXPLICIT_ORIENTATIONS_PASS')
    for k in (4,5):
        a,b=k-1,k*(k-1)-1
        assert a<k and b not in semigroup(k,b)
        assert a+b==k*k-2
    print('SHARP_OBSTRUCTIONS_PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    check()
