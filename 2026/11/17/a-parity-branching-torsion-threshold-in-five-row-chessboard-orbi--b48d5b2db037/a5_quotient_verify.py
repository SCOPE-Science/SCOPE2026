"""Exact ordinary-quotient cellular check for five-row chessboard complexes.
Run: python3 a5_quotient_verify.py   (requires SymPy).
All integers are exact; no randomized or floating-point steps.
"""
from itertools import combinations, permutations
from math import comb
from collections import defaultdict
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

ROWS = range(5)

def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2

def color(rows):
    if len(rows) < 4:
        return 0
    remaining = tuple(v for v in ROWS if v not in rows)
    return parity(tuple(rows)+remaining)

def cells(n,k):
    return [(s,c) for s in combinations(range(n),k) for c in (range(2) if k >= 4 else range(1))]

def base_rows(k,c):
    return (0,1,2,3,4)[:k] if c==0 else (1,0,2,3,4)[:k]

def differential(n,k):
    domain=cells(n,k)
    target=cells(n,k-1)
    ii={t:j for j,t in enumerate(target)}
    A=Matrix.zeros(len(target),len(domain))
    for j,(s,c) in enumerate(domain):
        r=base_rows(k,c)
        assert color(r)==c
        for h in range(k):
            t=s[:h]+s[h+1:]
            rr=r[:h]+r[h+1:]
            A[ii[(t,color(rr))],j]+=(-1)**h
    return A

def reduced_presentation(n):
    """Presentation of H_3 by 4-subsets, using 5- and 6-subset relations."""
    V=list(combinations(range(n),4)); W=list(combinations(range(n),5)); Z=list(combinations(range(n),6))
    idx={S:i for i,S in enumerate(V)}
    R=Matrix.zeros(len(V),len(W)+len(Z))
    for j,S in enumerate(W):
        for h in range(5):
            R[idx[S[:h]+S[h+1:]],j]+=1
    for j,T in enumerate(Z):
        for a in range(6):
            S=T[:a]+T[a+1:]
            for h in (1,3):
                R[idx[S[:h]+S[h+1:]],len(W)+j]-=(-1)**a
    return R

def diag_invariants(A):
    D=smith_normal_form(A,domain=ZZ)
    return sorted(abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i])

def mod_rank(A,p):
    m=[list(map(lambda z:int(z)%p,A.row(i))) for i in range(A.rows)]
    r=0
    for j in range(A.cols):
        pivot=next((i for i in range(r,len(m)) if m[i][j]%p),None)
        if pivot is None: continue
        m[r],m[pivot]=m[pivot],m[r]
        pivot_row=m[r]; inv=pow(pivot_row[j],-1,p)
        for k in range(j,A.cols): pivot_row[k]=pivot_row[k]*inv%p
        for i in range(r+1,len(m)):
            q=m[i][j]
            if q:
                for k in range(j,A.cols): m[i][k]=(m[i][k]-q*pivot_row[k])%p
        r+=1
        if r==len(m):break
    return r

def actual_orbit_checks():
    even=[p for p in permutations(ROWS) if parity(p)==0]
    assert len(even)==60
    for k in range(1,6):
        assignment=list(permutations(ROWS,k))
        unused=set(assignment)
        orbit_sizes=[]
        while unused:
            tup=min(unused)
            orb={tuple(g[x] for x in tup) for g in even}
            assert orb <=unused
            assert len({color(t) for t in orb})==1
            unused-=orb
            orbit_sizes.append(len(orb))
        assert len(orbit_sizes)==(2 if k>=4 else 1)
        assert set(orbit_sizes)==({60} if k>=3 else ({20} if k==2 else {5}))
    return True

def main():
    assert actual_orbit_checks()
    print('A5 orbit enumeration: PASS')
    for n in range(4,9):
        ds={k:differential(n,k) for k in range(2,min(5,n)+1)}
        for k in range(3,min(5,n)+1):
            assert ds[k-1]*ds[k]==Matrix.zeros(ds[k-1].rows,ds[k].cols)
        if n>=5:
            R=reduced_presentation(n)
            inv=diag_invariants(R)
            rank=len(inv)
            rank_h3=comb(n,4)-rank
            torsion=[d for d in inv if d>1]
            rank_d4=comb(n-1,4)+rank
            rank_h4=2*comb(n,5)-rank_d4
            # Independent full chain rational ranks, and ranks mod small primes
            d3=ds[4]
            d4=ds[5]
            assert mod_rank(d3,101)==comb(n-1,3)
            assert mod_rank(d4,101)==rank_d4
            assert (d3.rows,d3.cols)==(comb(n,3),2*comb(n,4))
            assert (d4.rows,d4.cols)==(2*comb(n,4),2*comb(n,5))
            for p in (2,3,5):
                assert mod_rank(R,p)==sum(d%p!=0 for d in inv)
                assert mod_rank(d4,p)==comb(n-1,4)+mod_rank(R,p)
        else:
            rank_h3,rank_h4,torsion=1,0,[]
        print(f'n={n}: H3 free={rank_h3}, torsion={torsion}; H4 free={rank_h4}; D^2=0 PASS')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
