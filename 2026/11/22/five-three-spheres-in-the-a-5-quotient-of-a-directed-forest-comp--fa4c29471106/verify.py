#!/usr/bin/env python3
"""Exact integral orbit-chain verification for five-label directed forests.

Usage: python3 verify.py (standard library only).
"""
from collections import Counter
from itertools import combinations, permutations, product

N = 5
ARCS = tuple((i, j) for i in range(N) for j in range(N) if i != j)
ARC_ID = {arc: i for i, arc in enumerate(ARCS)}


def is_forest(mask):
    parent = [-1] * N
    for i, (_, dst) in enumerate(ARCS):
        if mask & (1 << i):
            if parent[dst] >= 0:
                return False
            parent[dst] = ARCS[i][0]
    for v in range(N):
        encountered = set()
        x = v
        while x != -1:
            if x in encountered:
                return False
            encountered.add(x)
            x = parent[x]
    return True


def all_forests():
    result = []
    for k in range(1, N):
        for comb in combinations(range(len(ARCS)), k):
            mask = sum(1 << i for i in comb)
            if is_forest(mask):
                result.append(mask)
    assert Counter(m.bit_count() for m in result) == {1: 20, 2: 150, 3: 500, 4: 625}
    return result


def flags_of(faces):
    flags = set()
    for face in faces:
        bits = [i for i in range(len(ARCS)) if face >> i & 1]
        for k in range(1, len(bits) + 1):
            for labels in product(range(k), repeat=len(bits)):
                if set(labels) != set(range(k)):
                    continue
                chain = []
                mask = 0
                for j in range(k):
                    for i, label in zip(bits, labels):
                        if label == j:
                            mask |= 1 << i
                    chain.append(mask)
                flags.add(tuple(chain))
    assert Counter(map(len, flags)) == {1: 1295, 2: 12050, 3: 25500, 4: 15000}
    return flags


def perms(alternating):
    result = []
    for p in permutations(range(N)):
        parity = sum(p[i] > p[j] for i in range(N) for j in range(i+1, N)) % 2
        if alternating and parity:
            continue
        result.append((p, tuple(ARC_ID[p[u], p[v]] for u, v in ARCS)))
    assert len(result) == (60 if alternating else 120)
    return result


def quotient(faces, flags, group):
    # Transform complete face masks, not only independent face-orbit labels.
    trans = []
    for _, ids in group:
        trans.append({m: sum(1 << ids[i] for i in range(len(ARCS)) if m >> i & 1) for m in faces})
    reps = [[] for _ in range(4)]
    which = {}
    for flag in sorted(flags, key=lambda f: (len(f), f)):
        if flag in which:
            continue
        k = len(flag)-1
        idx = len(reps[k])
        reps[k].append(flag)
        for lookup in trans:
            which[tuple(lookup[x] for x in flag)] = (k, idx)
    assert len(which) == len(flags)
    ncells = [len(x) for x in reps]
    offsets = [sum(ncells[:i]) for i in range(4)]
    boundary = {k: {} for k in range(1, 4)}
    for k in range(1, 4):
        for j, flag in enumerate(reps[k]):
            coeffs = {}
            for i in range(k+1):
                shorter = flag[:i]+flag[i+1:]
                d, ix = which[shorter]
                assert d == k-1
                row = offsets[d]+ix
                coeffs[row] = coeffs.get(row,0) + (-1)**i
            boundary[k][offsets[k]+j] = {r:v for r,v in coeffs.items() if v}
    # Integral chain identity, checked without reduction or floating-point arithmetic.
    for k in (2,3):
        for c, terms in boundary[k].items():
            total = Counter()
            for r, coef in terms.items():
                for q, v in boundary[k-1].get(r,{}).items():
                    total[q] += coef*v
            assert all(x==0 for x in total.values()), (k,c,total)
    return ncells, offsets, boundary


def reduce_unit_pairs(ncells, offsets, boundary):
    """Integral elementary chain cancellations with unimodular coefficients.

    For a pivot ±1 in ∂k at (row a, column b), replace every
    other column c with c-(∂c[a]/∂b[a]) b, then delete a and b.
    The adjacent chain differentials lose the deleted basis generator.
    """
    C = {k: {b: terms.copy() for b,terms in boundary[k].items()} for k in (1,2,3)}
    R = {k: {} for k in (1,2,3)}
    for k in C:
        for b, col in C[k].items():
            for a, coef in col.items():
                R[k].setdefault(a,{})[b] = coef
    pivots = []
    while True:
        options = []
        for k in (1,2,3):
            for b, col in C[k].items():
                for a, val in col.items():
                    if abs(val)==1:
                        cost = (len(col)-1)*(len(R[k][a])-1)
                        options.append((cost,k,a,b))
        if not options:break
        _,k,a,b=min(options)
        coefficient=C[k][b][a]
        assert abs(coefficient)==1
        col=C[k][b].copy()
        row=R[k][a].copy()
        for c,value in row.items():
            if c==b:continue
            multiplier=value//coefficient
            for x,v in col.items():
                z=C[k][c].get(x,0)-multiplier*v
                if z:
                    C[k][c][x]=z
                    R[k].setdefault(x,{})[c]=z
                else:
                    C[k][c].pop(x,None)
                    R[k][x].pop(c,None)
        for x in C[k][b]:
            R[k][x].pop(b,None)
        C[k].pop(b)
        R[k].pop(a)
        if k>1:
            for x in C[k-1].pop(a,{}):
                R[k-1][x].pop(a,None)
        if k<3:
            for c in R[k+1].pop(b,{}):
                C[k+1][c].pop(b,None)
        pivots.append((k,a,b,coefficient))
    # Chain-condition on all surviving differentials.
    for k in (2,3):
        for b, col in C[k].items():
            total=Counter()
            for a,v in col.items():
                for r,w in C[k-1].get(a,{}).items():
                    total[r]+=v*w
            assert all(v==0 for v in total.values())
    remainder={0:ncells[0]-sum(k==1 for k,_,_,_ in pivots)}
    for k in (1,2,3):
        remainder[k]=len(C[k])
    assert sum(remainder.values())+2*len(pivots)==sum(ncells)
    return remainder,C,pivots


def burnside_euler(faces, group):
    total=0
    values={}
    for p,ids in group:
        lef=0
        for face in faces:
            selected=[i for i in range(len(ARCS)) if face>>i & 1]
            moved=[ids[i] for i in selected]
            if set(moved)!=set(selected):
                continue
            pos={j:i for i,j in enumerate(selected)}
            parity=sum(pos[moved[i]]>pos[moved[j]] for i in range(len(moved)) for j in range(i+1,len(moved)))%2
            lef+=(-1)**(len(selected)-1+parity)
        total+=lef
        key=tuple(sorted(cycle_lengths(p)))
        values.setdefault(key,[]).append(lef)
    assert total%len(group)==0
    return total//len(group), {str(k):(len(v),tuple(sorted(set(v)))) for k,v in sorted(values.items())}


def cycle_lengths(p):
    seen=set()
    for i in range(N):
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j);j=p[j];n+=1
        yield n


def main():
    fs=all_forests()
    flags=flags_of(fs)
    for alternating in (True,False):
        g=perms(alternating)
        cells,offs,d=quotient(fs,flags,g)
        rem,b,ops=reduce_unit_pairs(cells,offs,d)
        euler,contributions=burnside_euler(fs,g)
        assert euler==sum((-1)**i*n for i,n in enumerate(cells))
        assert all(not any(b[k][c] for c in b[k]) for k in (1,2,3))
        if alternating:
            assert cells==[27,206,425,250]
            assert len(ops)==451
            assert rem=={0:1,1:0,2:0,3:5}
            assert euler==-4
            assert contributions=={
                '(1, 1, 1, 1, 1)':(1,(-255,)),
                '(1, 1, 3)':(20,(0,)),
                '(1, 2, 2)':(15,(1,)),
                '(5,)':(24,(0,))}
        else:
            assert cells==[19,121,226,125]
            assert rem=={0:1,1:0,2:0,3:2}
            assert euler==-1
        print(('A5' if alternating else 'S5'),
              'cells',cells,'unit_pairs',len(ops),'minimal_integral_chain_ranks',rem,
              'euler',euler)
    print('PASS_A5_COMPLETE_DIRECTED_FOREST_QUOTIENT_FIVE_THREE_SPHERES')

if __name__=='__main__':main()
