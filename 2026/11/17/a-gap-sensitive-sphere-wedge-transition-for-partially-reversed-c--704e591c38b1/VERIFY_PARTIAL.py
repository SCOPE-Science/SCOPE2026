#!/usr/bin/env python3
"""Finite exact face and modular-chain checks for partial reverse rotations."""
from itertools import combinations
from math import comb


def words_for_rotations(n, starts, direction):
    out = set()
    for start in starts:
        perm = tuple((start + direction*j) % n for j in range(n))
        for k in range(1, n+1):
            out.update(tuple(perm[i] for i in I) for I in combinations(range(n), k))
    return out


def rank_mod(columns, rows, p):
    index = {w:i for i,w in enumerate(rows)}
    pivots={}
    for w in columns:
        col = {index[w[:j]+w[j+1:]]:(-1 if j%2 else 1)%p for j in range(len(w))}
        while col:
            k = min(col)
            if k not in pivots:
                scalar=pow(col[k],-1,p)
                pivots[k]={i:(v*scalar)%p for i,v in col.items()}
                break
            scalar=col[k]
            for i,v in pivots[k].items():
                a=(col.get(i,0)-scalar*v)%p
                if a:col[i]=a
                else:col.pop(i,None)
    return len(pivots)


def homology(words,n,p=101):
    C=[sorted(w for w in words if len(w)==k) for k in range(1,n+1)]
    r=[0]+[rank_mod(C[k],C[k-1],p) for k in range(1,n)]+[0]
    b=[len(C[k])-r[k]-r[k+1] for k in range(n)]
    b[0]-=1
    return tuple(b)


def gap_sizes(n,T):
    starts=sorted(T)
    return [((starts[(i+1)%len(starts)]-starts[i])%n or n) for i in range(len(starts))]


def expected_rank(n,T):
    if len(T)==1:return comb(n-1,2)-1
    gaps=gap_sizes(n,T)
    return comb(n-1,2)+sum(a*b for i,a in enumerate(gaps) for b in gaps[i+1:])-2


def main():
    for n in range(3,8):
        plus=words_for_rotations(n,range(n),+1)
        tests=0
        for t in range(1,n+1):
            for T in combinations(range(n),t):
                minus=words_for_rotations(n,T,-1)
                intersection=plus&minus
                assert max(map(len,intersection))<=2
                edge_count=sum(len(w)==2 for w in minus)
                gaps=gap_sizes(n,T)
                assert edge_count==comb(n,2)+sum(a*b for i,a in enumerate(gaps) for b in gaps[i+1:])
                k=expected_rank(n,T)
                assert k>=0
                h=homology(plus|minus,n,101)
                assert h==(0,0,k)+ (0,)*(n-3),(n,T,k,h)
                tests+=1
        print(f'n={n} subsets={tests} modular_homology_passed',flush=True)
    print('PARTIAL_REVERSE_ROTATION_COMPLEX_VERIFICATION_PASS')

if __name__=='__main__':main()
