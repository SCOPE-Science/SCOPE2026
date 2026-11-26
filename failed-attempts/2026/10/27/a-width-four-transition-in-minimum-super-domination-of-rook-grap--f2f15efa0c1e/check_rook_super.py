#!/usr/bin/env python3
"""Independent finite checks for optimal super domination of rook graphs.
Run: python3 check_rook_super.py (Python 3.9+, standard library only).
"""
from itertools import product, combinations
from math import comb, factorial


def neighbors(p, q):
    return [sum(1 << j for j in range(p*q)
                if j != i and (j // q == i // q or j % q == i % q))
            for i in range(p*q)]


def direct_super_complement(mask, nbs):
    """Use the graph-definition private-neighbor condition, not any row/column lemma."""
    private_targets = 0
    for d, nb in enumerate(nbs):
        if mask & (1 << d):
            continue
        hit = nb & mask
        if hit and not (hit & (hit - 1)):
            private_targets |= hit
    return private_targets == mask


def local_incidence_rule(mask, p, q):
    rows = [sum(bool(mask & (1 << (i*q+j))) for j in range(q)) for i in range(p)]
    cols = [sum(bool(mask & (1 << (i*q+j))) for i in range(p)) for j in range(q)]
    zero_rows = 0 in rows
    zero_cols = 0 in cols
    return all((rows[i] == 1 and zero_cols) or (cols[j] == 1 and zero_rows)
               for i in range(p) for j in range(q) if mask & (1 << (i*q+j)))


def surj(p, q):
    return sum((-1)**j * comb(p,j) * (p-j)**q for j in range(p+1))


def proposed(p,q):
    assert 2 <= p <= q
    h = max(q, p+q-4)
    count = 0
    if h == q:
        count += p**q-surj(p,q)
        if p==q:
            count += p**p-surj(p,p)
    if p>=4 and p+q-4 == h:
        count += p*q*(p-1)*(q-1)
    return h,count


def candidate_optimal_complements(p,q):
    h,_ = proposed(p,q)
    masks = set()
    if h == q:
        for row_for_column in product(range(p), repeat=q):
            if len(set(row_for_column)) < p:
                masks.add(sum(1 << (row_for_column[j]*q+j) for j in range(q)))
        if p==q:
            for col_for_row in product(range(q), repeat=p):
                if len(set(col_for_row)) < q:
                    masks.add(sum(1 << (i*q+col_for_row[i]) for i in range(p)))
    if p>=4 and p+q-4==h:
        for center_row in range(p):
            for empty_row in range(p):
                if empty_row==center_row: continue
                for center_col in range(q):
                    for empty_col in range(q):
                        if empty_col==center_col: continue
                        # Construct the two disjoint star sets without duplicate cells.
                        mask=sum(1<<(center_row*q+j) for j in range(q) if j not in (center_col,empty_col))
                        mask+=sum(1<<(i*q+center_col) for i in range(p) if i not in (center_row,empty_row))
                        masks.add(mask)
    return masks


def main():
    total=0
    for p,q in ((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)):
        nbs=neighbors(p,q)
        h,N=proposed(p,q)
        expected=candidate_optimal_complements(p,q)
        assert len(expected)==N,(p,q,len(expected),N)
        oracle_opt=set()
        for mask in range(1<<(p*q)):
            direct=direct_super_complement(mask,nbs)
            local=local_incidence_rule(mask,p,q)
            assert direct==local, (p,q,mask,direct,local)
            if mask.bit_count()==h and direct:
                oracle_opt.add(mask)
            assert not (mask.bit_count()>h and direct),(p,q,mask)
        assert oracle_opt==expected,(p,q,len(oracle_opt),len(expected))
        total+=1<<(p*q)
        print(f'{p}x{q}: max omitted={h}; optimal complements={N}; verified {1<<(p*q)} subsets')
    # Larger first mixed-dominant square: exhaustive relevant levels, not all its 2^25 subsets.
    p=q=5; nbs=neighbors(p,q); h,N=proposed(p,q)
    expected=candidate_optimal_complements(p,q)
    assert len(expected)==N==400
    opt=set()
    scanned=0
    for k in (h,h+1):
        for inds in combinations(range(p*q),k):
            mask=sum(1<<i for i in inds)
            direct=direct_super_complement(mask,nbs)
            assert direct==local_incidence_rule(mask,p,q)
            if direct:
                assert k==h,(k,inds)
                opt.add(mask)
            scanned+=1
    assert opt==expected,(len(opt),len(expected))
    print(f'5x5: max omitted={h}; optimal complements={N}; verified {scanned} subsets of sizes 6,7')
    print(f'PASS: {total+scanned} direct-definition checks; equality classification and counts agree.')

if __name__=='__main__':
    main()
