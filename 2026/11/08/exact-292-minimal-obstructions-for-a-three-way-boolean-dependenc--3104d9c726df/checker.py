"""Exact finite certificate for 2+2 Boolean tuple-dependence triple disjunction.

Run with Python 3: python3 checker.py
The mathematical proof of the classification is separate from these tests.
"""
from collections import Counter
from random import Random


def rectangle_tests(p,q):
    return [(sum(1<<(i*q+j) for i in range(p) if a>>i&1 for j in range(q) if b>>j&1),2*a.bit_count()+b.bit_count()) for a in range(1,1<<p) for b in range(1,1<<q)]


def admissible(mask,tests):
    return all((mask&area).bit_count()<=capacity for area,capacity in tests)


def split_by_matching(mask,p,q):
    """Independent augmenting-path algorithm assigning edges to two X and one Y slots."""
    slots=[-1]*(2*p+q)
    choices=[(2*i,2*i+1,2*p+j) for i in range(p) for j in range(q) if mask>>(i*q+j)&1]
    def try_assign(e,seen):
        for slot in choices[e]:
            if slot in seen:continue
            seen.add(slot)
            if slots[slot]<0 or try_assign(slots[slot],seen):
                slots[slot]=e
                return True
        return False
    return all(try_assign(e,set()) for e in range(len(choices)))


def analytic_class(mask):
    deg=[sum(bool(mask>>(i*4+j)&1) for j in range(4)) for i in range(4)]
    columns=[sum(bool(mask>>(i*4+j)&1) for i in range(4)) for j in range(4)]
    e=mask.bit_count()
    if e==11:
        return sorted(deg)==[0,3,4,4] and sorted(columns)==[2,3,3,3]
    if e==12:
        return deg==[3,3,3,3] and sorted(columns)==[0,4,4,4]
    if e==13:
        return sorted(deg)==[3,3,3,4] and min(columns)>=2
    return False


def main():
    t44=rectangle_tests(4,4)
    minimal=[];satisfying=0
    for mask in range(1<<16):
        if admissible(mask,t44):
            satisfying+=1
        elif all(admissible(mask^(1<<bit),t44) for bit in range(16) if mask>>bit&1):
            minimal.append(mask)
    hist=dict(sorted(Counter(mask.bit_count() for mask in minimal).items()))
    assert hist=={11:48,12:4,13:240},hist
    assert len(minimal)==292 and satisfying==64591
    assert all(analytic_class(mask) for mask in minimal)
    assert sum(analytic_class(mask) for mask in range(1<<16))==292
    # The matching test uses a different algorithm than the rectangle conditions.
    for mask in minimal:
        assert not split_by_matching(mask,4,4)
        for bit in range(16):
            if mask>>bit&1:
                assert split_by_matching(mask^(1<<bit),4,4)
    rand=Random(0x3514)
    sampled={rand.randrange(1<<16) for _ in range(3000)}
    sampled.update(range(0,1<<16,231))
    for mask in sampled:
        assert admissible(mask,t44)==split_by_matching(mask,4,4)
    for p,q in ((1,4),(2,2),(2,4),(3,3)):
        tests=rectangle_tests(p,q)
        for mask in range(1<<(p*q)):
            assert admissible(mask,tests)==split_by_matching(mask,p,q)
    assert all(admissible(mask,rectangle_tests(2,4)) for mask in range(1<<8))
    # Distinguish the three-way team property from ordinary FD closure profiles.
    rows_bad=[4*i+j for i in range(4) for j in range(3)]
    rows_good=[4*i+j for i in range(4) for j in range(4) if i!=j]
    def fd_profile(rows):
        diffs={a^b for idx,a in enumerate(rows) for b in rows[idx+1:]}
        return tuple(15^sum((1<<bit) for bit in range(4)
                        if any((d&antecedent)==0 and (d>>bit&1) for d in diffs))
                     for antecedent in range(16))
    assert fd_profile(rows_bad)==fd_profile(rows_good)
    bad=sum(1<<k for k in rows_bad)
    good=sum(1<<k for k in rows_good)
    assert not admissible(bad,t44) and admissible(good,t44)
    print('TRIPLE_DEPENDENCE_RECTANGLE_CLASSIFICATION_OK')
    print('All 65536 Boolean four-variable teams enumerated; satisfying',satisfying)
    print('Inclusion-minimal false teams by size',hist,'total',len(minimal))
    print('Independent matching vs Hall: 292 circuits and all single-edge deletions,',len(sampled),'4x4 samples, all <=3x3 small teams')
    print('Closed-form row/column characterization verified on all 65536 teams')
    print('Same ordinary four-bit FD closure, opposite split-disjunction truth: verified')

if __name__=='__main__':main()
