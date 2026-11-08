"""Exact finite proof certificate for the minimum-size coextinction moment twins.
Standard Python 3; no external dependencies.

Each nonzero bit mask is the set of pollinator neighbors of one plant.
The union of masks must cover all pollinators. Plant and pollinator
permutations are the only permitted isomorphisms.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, permutations
from fractions import Fraction

def permute_mask(mask, permutation):
    return sum(1 << permutation[j] for j in range(len(permutation)) if mask & (1 << j))

def canonical(rows, m):
    return min(tuple(sorted(permute_mask(r, pi) for r in rows))
               for pi in permutations(range(m)))

def connected(rows, m):
    seen_plants, seen_pollinators = {0}, set()
    while True:
        pl, po = set(seen_plants), set(seen_pollinators)
        for i in seen_plants:
            po.update(j for j in range(m) if rows[i] & (1 << j))
        for j in po:
            pl.update(i for i, row in enumerate(rows) if row & (1 << j))
        if pl == seen_plants and po == seen_pollinators:
            return len(pl) == len(rows) and len(po) == m
        seen_plants, seen_pollinators = pl, po

def moments(rows):
    degrees = tuple(sorted(r.bit_count() for r in rows))
    unions = tuple(sorted((rows[i] | rows[j]).bit_count()
                          for i in range(len(rows)) for j in range(i + 1, len(rows))))
    # This signature is equivalent to knowing the first two factorial moments
    # as polynomials in the independent pollinator-extinction probability q.
    return degrees, unions

def law_bernstein(rows, m):
    """At each extinct count r, histogram of the number of served plants.
    Bernstein coefficients uniquely determine the entire law for all q.
    """
    mask = (1 << m) - 1
    p = len(rows)
    out = [[0] * (p+1) for _ in range(m+1)]
    for extinct in range(1 << m):
        served = sum(bool(row & (mask ^ extinct)) for row in rows)
        out[extinct.bit_count()][served] += 1
    return tuple(tuple(v) for v in out)

def all_classes(p, m, require_connected):
    classes = set()
    for rows in combinations_with_replacement(range(1, 1 << m), p):
        union = 0
        for r in rows: union |= r
        if union != (1 << m)-1: continue
        if require_connected and not connected(rows, m): continue
        classes.add(canonical(rows, m))
    return sorted(classes)

def collisions(classes, m):
    groups = defaultdict(list)
    for rows in classes: groups[moments(rows)].append(rows)
    out = []
    for members in groups.values():
        for i, a in enumerate(members):
            for b in members[i+1:]:
                if law_bernstein(a, m) != law_bernstein(b, m):
                    out.append((a,b))
    return sorted(out)

def labelled_exhaustion(p, m):
    # Independent certificate: no isomorphism reduction at all.
    groups = {}
    covered = 0
    for a in range(1, 1 << m):
        for b in range(1, 1 << m):
            for c in range(1, 1 << m):
                for d in range(1, 1 << m):
                    rows=(a,b,c,d)
                    if (a|b|c|d) != (1 << m)-1: continue
                    covered += 1
                    s=moments(rows)
                    law=law_bernstein(rows, m)
                    old=groups.setdefault(s,law)
                    assert law == old, (rows,s,law,old)
    return covered, len(groups)

def exact_witness():
    a=(3,5,6,15)
    b=(3,5,9,15)
    assert connected(a,4) and connected(b,4)
    assert a != canonical(b,4)
    assert moments(a)==moments(b)==((2,2,2,4),(3,3,3,4,4,4))
    # Direct enumeration independent of inclusion-exclusion: at q=1/2,
    # all 16 extinction configurations are equally likely.
    la=law_bernstein(a,4)
    lb=law_bernstein(b,4)
    pa=sum(Fraction(la[r][4], 1<<4) for r in range(5))
    pb=sum(Fraction(lb[r][4], 1<<4) for r in range(5))
    assert pa==Fraction(1,2) and pb==Fraction(9,16) and pb-pa==Fraction(1,16)
    # Exact polynomial for P(all four plants served) via inclusion-exclusion.
    def coverage_coeffs(rows):
        coeff=[0]*5
        for plant_subset in range(1<<4):
            union=0
            for i in range(4):
                if plant_subset & (1<<i):union |= rows[i]
            coeff[union.bit_count()] += (-1)**plant_subset.bit_count()
        return tuple(coeff)
    ca=coverage_coeffs(a)
    cb=coverage_coeffs(b)
    assert ca==(1,0,-3,2,0),ca
    assert cb==(1,0,-3,3,-1),cb
    assert tuple(y-x for x,y in zip(ca,cb))==(0,0,0,1,-1)
    return la,lb,ca,cb

def main():
    n,sg=labelled_exhaustion(4,3)
    print('independent labelled 4x3 census:',n,'valid labeled matrices;',sg,'moment signatures; all have unique laws')
    x=all_classes(4,3,False)
    assert len(x)==42 and not collisions(x,3)
    print('4x3 side-preserving isomorphism classes:',len(x),'; no moment-indistinguishable law differences')
    expected_44=[((1,7,7,14),(1,7,11,13)),((3,5,6,15),(3,5,9,15)),
       ((3,5,7,14),(3,5,11,13)),((3,5,11,13),(3,7,7,12))]
    expected_53=[((1,3,3,3,6),(1,3,3,5,5))]
    for p,m,nclasses,expected in [(4,4,150,expected_44),(5,3,76,expected_53)]:
        classes=all_classes(p,m,True)
        hits=collisions(classes,m)
        assert len(classes)==nclasses,(p,m,len(classes))
        assert hits==expected,(p,m,hits)
        print(f'connected {p}x{m}: {len(classes)} unlabeled classes; {len(hits)} unordered moment-twin pairs with different laws')
        for a,b in hits:print(' ',a,b)
    _,_,ca,cb=exact_witness()
    print('witness exact all-plant-service probabilities:',ca,cb)
    print('witness tail gap: q^3 (1-q), maximum 27/256 at q=3/4')
    print('PASS')
if __name__=='__main__':main()
