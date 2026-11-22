#!/usr/bin/env python3
"""Finite independent checks for a robust common-determinant team split.

The proof in RESULT.md is the universal justification; this code checks finite cases.
Only the Python standard library is needed.
"""
from fractions import Fraction
from itertools import product


def cell_formula(team, r, s):
    """Exact optimum deletion ratio with free overlap, via row/column crosses."""
    if not team:
        return Fraction(0)
    fibers = {}
    for a, y, z in team:
        fibers.setdefault(a, set()).add((y, z))
    choices = []
    for fiber in fibers.values():
        opts = []
        for y,z in product(range(r), range(s)):
            e = sum(v != y and w != z for v,w in fiber)
            b = sum(v != y and w == z for v,w in fiber)
            opts.append((e, b))
        choices.append(opts)
    best = Fraction(1)
    for chosen in product(*choices):
        e = sum(a for a,b in chosen)
        b = sum(b for a,b in chosen)
        denom = len(team) - b
        if denom:
            best = min(best, Fraction(e, denom))
    return best


def semantic_brute(team):
    """Search all overlapped decompositions, not just disjoint partitions."""
    n = len(team)
    if not n: return Fraction(0)
    best = Fraction(1)
    for mode in product((1,2,3), repeat=n):
        left = [v for v,sel in zip(team,mode) if sel&1]
        right = [v for v,sel in zip(team,mode) if sel&2]
        z_by_x = {}
        ok = True
        for x,y,z in right:
            if x in z_by_x and z_by_x[x] != z:
                ok = False; break
            z_by_x[x] = z
        if not ok: continue
        freq = {}
        for x,y,z in left:
            freq.setdefault(x,{}).setdefault(y,0)
            freq[x][y] += 1
        err = len(left) - sum(max(vals.values()) for vals in freq.values())
        ratio = Fraction(err,len(left)) if left else Fraction(0)
        if ratio < best: best=ratio
        if best == 0: break
    return best


def decision_by_fiber_max(team,r,s,p):
    """Independent implementation of the polynomial-time criterion."""
    if not team: return True
    data={}
    for x,y,z in team:
        data.setdefault(x,set()).add((y,z))
    score=Fraction(0)
    for edges in data.values():
        row=[sum(v==y for v,w in edges) for y in range(r)]
        col=[sum(w==z for v,w in edges) for z in range(s)]
        score+=max(Fraction(row[y])+(1-p)*(col[z]-int((y,z) in edges))
                   for y,z in product(range(r),range(s)))
    return score >= (1-p)*len(team)


def run():
    total = 0
    for a,r,s in ((1,2,2),(1,2,3),(1,3,3),(2,2,2)):
        universe=list(product(range(a),range(r),range(s)))
        worst=Fraction(-1)
        extremizers=[]
        for mask in range(1 << len(universe)):
            team=[v for i,v in enumerate(universe) if mask >> i & 1]
            f=cell_formula(team,r,s)
            b=semantic_brute(team)
            assert f==b, (a,r,s,team,f,b)
            for p in (Fraction(0), Fraction(1,5), Fraction(1,3),
                      Fraction(2,5), Fraction(1,2), Fraction(2,3),
                      Fraction(4,5), Fraction(1)):
                assert decision_by_fiber_max(team,r,s,p)==(f<=p), (a,r,s,team,p,f)
            if team:
                if f>worst: worst=f;extremizers=[mask]
                elif f==worst: extremizers.append(mask)
            total+=1
        sharp=Fraction((r-1)*(s-1), r*s-r+1)
        assert worst==sharp,(a,r,s,worst,sharp)
        expected=[]
        fiber_mask=(1<<(r*s))-1
        for pattern in range(1,1<<a):
            expected.append(sum(fiber_mask << (k*r*s) for k in range(a) if pattern>>k & 1))
        assert sorted(extremizers)==sorted(expected), (a,r,s,extremizers,expected)
        print(f'CHECK a={a} r={r} s={s} subsets={1 << len(universe)} sharp={sharp} nonempty_fibers_full=True')
    print('SEMANTIC_AND_EXTREMAL_CHECKS_OK',total)

if __name__=='__main__': run()
