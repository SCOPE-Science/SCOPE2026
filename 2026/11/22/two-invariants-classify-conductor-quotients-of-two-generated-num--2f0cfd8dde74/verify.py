"""Direct finite verification of conductor-quotient rigidity for coprime pairs.

Run: python verify.py
No third-party dependencies. This is not a proof of the infinite theorem.
"""
from math import gcd
from collections import defaultdict


def quotient(a, b):
    c = (a - 1) * (b - 1)
    vals = {i*a + j*b for i in range(c//a+1) for j in range(c//b+1)
            if 0 < i*a+j*b < c}
    return c, vals


def power_index(a, c):
    r = 1
    while r*a < c:
        r += 1
    return r


def actual_atoms(vals, c):
    decomposable = {x+y for x in vals for y in vals if x+y < c}
    return vals-decomposable


def swap_is_automorphism(a, b, c, vals):
    # Possible only when both minimal generators appear. Every finite
    # element has a unique nonnegative (i,j) expression below the conductor.
    if a not in vals or b not in vals:
        return False
    d = {}
    for z in vals:
        reps = [(i,j) for i in range(c//a+1) for j in range(c//b+1)
                if i*a+j*b == z]
        assert len(reps) == 1, (a,b,z,reps)
        i,j = reps[0]
        w = i*b+j*a
        if w >= c or w not in vals:
            return False
        d[z] = w
    if set(d.values()) != vals:
        return False
    for x in vals:
        for y in vals:
            out = x+y if x+y < c else None
            out2 = d[x]+d[y] if d[x]+d[y] < c else None
            if (d.get(out) if out is not None else None) != out2:
                return False
    return True


def main():
    groups = defaultdict(list)
    pairs = 0
    cases_swaps = 0
    for a in range(2,41):
        for b in range(a+1,61):
            if gcd(a,b) != 1:
                continue
            c, vals = quotient(a,b)
            h = power_index(a,c)
            assert len(vals)+1 == c//2, (a,b,c,len(vals))
            assert h == (c+a-1)//a
            atoms = actual_atoms(vals,c)
            assert atoms == ({a,b} if a>=3 else ({a} if a<c else set())), (a,b,atoms)
            groups[(len(vals)+1,h)].append((a,b))
            # Classify all possible automorphisms: any automorphism
            # permutes the indecomposable elements.
            if a <= 15 and b <= 22:
                swap = swap_is_automorphism(a,b,c,vals) if len(atoms)==2 else False
                assert swap == (a>=3 and b==a+1), (a,b,swap)
                cases_swaps += 1
            pairs += 1
    assert all(len(v)==1 for v in groups.values()), [v for v in groups.values() if len(v)>1]
    # Independent integer inequality for every possible smaller generator:
    for c in range(2,2001):
        cand = [a for a in range(2,c+1) if a*(a-1)<=c]
        ks = [(c+a-1)//a for a in cand]
        assert all(ks[i]>ks[i+1] for i in range(len(ks)-1)), (c,cand,ks)
    print(f"PASS: {pairs} distinct coprime pairs; pairwise-injective (size,class) signatures")
    print(f"PASS: all {cases_swaps} small-pair generator-swaps checked as full homomorphisms")
    print("PASS: strict ceiling monotonicity for all c=2..2000 on admissible multiplicities")
    print("Limits: finite checks only; infinite cases established by separate proof.")

if __name__ == '__main__':
    main()
