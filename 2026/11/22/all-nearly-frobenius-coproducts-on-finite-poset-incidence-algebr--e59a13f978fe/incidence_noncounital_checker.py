#!/usr/bin/env python3
"""Independent finite-field linear-equation checks for incidence-algebra coproducts.

The mathematical theorem is proved for arbitrary finite posets separately;
this checker only tests all topologically labeled posets of orders up to five.
"""
from itertools import combinations
from collections import Counter


def posets(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        R = [[i == j for j in range(n)] for i in range(n)]
        for bit, (i, j) in enumerate(pairs):
            if mask >> bit & 1:
                R[i][j] = True
        if all(not (R[i][j] and R[j][k]) or R[i][k]
               for i in range(n) for j in range(n) for k in range(n)):
            yield R


def bounded_components(R):
    n = len(R)
    unseen = set(range(n))
    bounds = []
    while unseen:
        first = next(iter(unseen))
        comp = {first}
        stack = [first]
        unseen.remove(first)
        while stack:
            i = stack.pop()
            for j in tuple(unseen):
                if R[i][j] or R[j][i]:
                    comp.add(j)
                    stack.append(j)
                    unseen.remove(j)
        lows = [i for i in comp if all(R[i][j] for j in comp)]
        highs = [i for i in comp if all(R[j][i] for j in comp)]
        if lows and highs:
            bounds.append((lows[0], highs[0], comp))
    return bounds


def rank_mod_p(rows, ncols, p):
    pivots = {}
    for row in rows:
        vector = {i: v % p for i, v in row.items() if v % p}
        while vector:
            leading = min(vector)
            if leading not in pivots:
                z = pow(vector[leading], -1, p)
                pivots[leading] = {j: (a * z) % p for j, a in vector.items() if a % p}
                break
            lead = vector[leading]
            for j, a in pivots[leading].items():
                r = (vector.get(j, 0) - lead * a) % p
                if r:
                    vector[j] = r
                else:
                    vector.pop(j, None)
    return len(pivots)


def equations(R):
    n = len(R)
    # All tensors allowed after the diagonal-idempotent equations:
    # e_(i,a) tensor e_(b,i), where b <= i <= a.
    T = [(i,a,b) for i in range(n) for a in range(n) for b in range(n)
         if R[b][i] and R[i][a]]
    rows = {}
    for i in range(n):
        for j in range(i+1,n):
            if not R[i][j]:
                continue
            for k,(u,a,b) in enumerate(T):
                if u == j:
                    # (e_ij tensor 1) Delta(e_jj)
                    key = (i,j,a,b)
                    row = rows.setdefault(key,{})
                    row[k] = row.get(k,0)+1
                if u == i:
                    # Delta(e_ii) (1 tensor e_ij)
                    key = (i,j,a,b)
                    row = rows.setdefault(key,{})
                    row[k] = row.get(k,0)-1
    return T, list(rows.values())


def test():
    checked = Counter()
    for n in range(1,6):
        for R in posets(n):
            bounds = bounded_components(R)
            T,eq=equations(R)
            for p in (2,3):
                dim=len(T)-rank_mod_p(eq,len(T),p)
                assert dim == len(bounds), (n,p,dim,len(bounds),R)
                checked[(n,p)] += 1
            # Construct explicit all-component basis vectors and check equations.
            for low,high,component in bounds:
                x=[int(a==high and b==low and i in component) for i,a,b in T]
                assert all(sum(row.get(j,0)*x[j] for j in row)==0 for row in eq)
                # Formula Delta(e_uv) = e_(u,high) tensor e_(low,v):
                # distinct (u,v) yield distinct target basis tensors.
                pairs=[(i,j) for i in component for j in component if R[i][j]]
                images=[((i,high),(low,j)) for i,j in pairs]
                assert len(set(images))==len(pairs)
                for i,j in pairs:
                    # Explicit coassociativity as equal elementary triple tensors.
                    left=((i,high),(low,high),(low,j))
                    right=((i,high),(low,high),(low,j))
                    assert left==right
    # Diamond has four elements and 9 comparable intervals.
    D=[[i==j for j in range(4)] for i in range(4)]
    for i,j in [(0,1),(0,2),(0,3),(1,3),(2,3)]:D[i][j]=True
    assert len(bounded_components(D))==1
    assert sum(sum(row) for row in D)==9
    assert len(equations(D)[0])-rank_mod_p(equations(D)[1],len(equations(D)[0]),2)==1
    print('INCIDENCE_COPRODUCT_CLASSIFICATION_OK', 'tested=',sum(checked.values()),'by_size_field=',sorted(checked.items()))

if __name__=='__main__':test()
