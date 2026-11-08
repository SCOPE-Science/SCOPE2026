#!/usr/bin/env python3
"""Independent exhaustive trace enumeration for the open-neighborhood rook theorem.

Usage: python VERIFY.py
This finite check supports, but does not prove, the all-parameter theorem.
"""
from itertools import combinations
from math import comb


def C(a, b):
    return comb(a, b) if a >= b >= 0 else 0


def predicted(m, n):
    pairs = (m*C(n,2) if m>=2 and n>=3 else 0)
    pairs += (n*C(m,2) if n>=2 and m>=3 else 0)
    pairs += (2*C(m,2)*C(n,2) if m>=2 and n>=2 and max(m,n)>=3 else 0)
    triples = (m*C(n,3)+m*(m-1)*C(n,2)*(n-2) if m>=2 and n>=4 else 0)
    triples += (n*C(m,3)+n*(n-1)*C(m,2)*(m-2) if n>=2 and m>=4 else 0)
    return [1, m*n if m*n >= 2 else 0, pairs, triples]


def shape_support(cells, m, n):
    if len(cells) != 3:
        return False
    rows = [i for i, j in cells]
    cols = [j for i, j in cells]
    if len(set(rows)) == 1:
        return m>=2 and n>=4
    if len(set(cols)) == 1:
        return n>=2 and m>=4
    for i in set(rows):
        if rows.count(i)==2:
            repeated = [c for r,c in cells if r==i]
            extra = [(r,c) for r,c in cells if r!=i]
            if extra and extra[0][1] not in repeated:
                return m>=2 and n>=4
    for j in set(cols):
        if cols.count(j)==2:
            repeated = [r for r,c in cells if c==j]
            extra = [(r,c) for r,c in cells if c!=j]
            if extra and extra[0][0] not in repeated:
                return n>=2 and m>=4
    return False


def trace_shattered(support, board, neigh):
    # Construct every trace directly, without relying on the claimed shape criterion.
    wanted = (1 << len(support)) - 1
    seen = 0
    for q in range(len(board)):
        trace = 0
        for k, v in enumerate(support):
            if v in neigh[q]:
                trace |= 1 << k
        seen |= 1 << trace
        if seen == (1 << (1 << len(support))) - 1:
            return True
    return False


def check(m, n, check_four):
    board = [(i,j) for i in range(m) for j in range(n)]
    neigh = [{v for v in range(len(board)) if v!=u and (board[u][0]==board[v][0] or board[u][1]==board[v][1])} for u in range(len(board))]
    counts = [1,0,0,0]
    cases = 0
    for k in range(1, 4):
        for support in combinations(range(len(board)),k):
            actual = trace_shattered(support, board, neigh)
            if actual: counts[k]+=1
            cases += 1
            if k==3:
                classified = shape_support([board[u] for u in support],m,n)
                assert actual==classified,(m,n,support,actual,classified)
    assert counts==predicted(m,n),(m,n,counts,predicted(m,n))
    fourths = 0
    if check_four:
        for support in combinations(range(len(board)),4):
            assert not trace_shattered(support,board,neigh),(m,n,support)
            fourths += 1
    return cases, fourths, counts


def main():
    cases=fourths=boards=0
    selected=[]
    for m in range(1,9):
        for n in range(m,9):
            use_four = (m*n<=36) or (m,n) in {(3,7),(4,7),(5,7)}
            a,b,c = check(m,n,use_four)
            boards+=1; cases+=a; fourths+=b
            if (m,n) in {(1,1),(2,2),(2,4),(3,3),(3,4),(4,4),(6,7)}:
                selected.append((m,n,c))
    print('EXACT_TRACE_AND_TRIPLE_SHAPE_CLASSIFICATION_PASS', 'boards=',boards,'supports=',cases)
    print('FOUR_POINT_EXCLUSIONS_PASS', 'supports=',fourths)
    for m,n,c in selected:print('PROFILE',m,n,c)
    print('ALL_RECTANGULAR_ROOK_OPEN_SHATTERING_CHECKS_PASS')

if __name__ == '__main__': main()
