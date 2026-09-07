#!/usr/bin/env python3
"""Canonical 2-border demonstration (constructive proof companion).
Given any dephased BH(6,3) (exponent matrix), finds:
 (1) column perm fixing col 0 sorting row 1 to [0,0,1,1,2,2];
 (2) row perm fixing rows 0,1 sorting col 1 segment rows2..5 to [1,1,2,2].
Verifies perms preserve dephasing + BH property, and border holds.
Demo: applies random row/col perms to our solution, re-dephases, re-sorts.
Pure Python. Usage: python3 canonical_border.py
"""
import random

def counts_ok(a,b):
    c=[0,0,0]
    for x,y in zip(a,b):
        c[(x-y)%3]+=1
    return c==[2,2,2]

def is_bh(rows):
    n=len(rows)
    for i in range(n):
        for j in range(i+1,n):
            if not counts_ok(rows[i],rows[j]): return False
    for j in range(n):
        for k in range(j+1,n):
            if not counts_ok([rows[i][j] for i in range(n)],[rows[i][k] for i in range(n)]):
                return False
    return True

def dephase(rows):
    # multiply row i by -rows[i][0], then col j by -rows[0][j] (add mod 3)
    n=len(rows)
    R=[row[:] for row in rows]
    for i in range(n):
        s=(-R[i][0])%3
        R[i]=[(v+s)%3 for v in R[i]]
    for j in range(n):
        s=(-R[0][j])%3
        for i in range(n):
            R[i][j]=(R[i][j]+s)%3
    return R

def sort_border(rows):
    n=6
    assert rows[0]==[0]*6 and all(r[0]==0 for r in rows)
    # col perm fixing 0: sort cols 1..5 by row1 key
    tail=sorted(range(1,6), key=lambda j: rows[1][j])
    cp=[0]+tail
    R=[[rows[i][cp[j]] for j in range(6)] for i in range(6)]
    assert R[1]==[0,0,1,1,2,2], R[1]
    # row perm fixing 0,1: sort rows 2..5 by col1 key
    mid=sorted(range(2,6), key=lambda i: R[i][1])
    rp=[0,1]+mid
    R2=[[R[rp[i]][j] for j in range(6)] for i in range(6)]
    col2=[R2[i][1] for i in range(6)]
    assert col2==[0,0,1,1,2,2], col2
    return R2, cp, rp

SOL=[[0,0,0,0,0,0],[0,0,1,1,2,2],[0,1,0,2,1,2],[0,1,2,0,2,1],[0,2,1,2,0,1],[0,2,2,1,1,0]]

def main():
    random.seed(16)
    assert is_bh(SOL)
    print("original is BH(6,3): True; R2/C2 already sorted.")
    for t in range(5):
        rp=list(range(6)); cp=list(range(6))
        random.shuffle(rp); random.shuffle(cp)
        # random monomial phases: row phase per row + col phase per col (preserves BH)
        rph=[random.randrange(3) for _ in range(6)]
        cph=[random.randrange(3) for _ in range(6)]
        P=[[ (SOL[rp[i]][cp[j]]+rph[i]+cph[j])%3 for j in range(6)] for i in range(6)]
        D=dephase(P)
        assert D[0]==[0]*6 and all(r[0]==0 for r in D) and is_bh(D)
        S,pc,pr=sort_border(D)
        assert is_bh(S) and S[0]==[0]*6 and all(r[0]==0 for r in S)
        print(f"trial {t}: random perm+phases -> dephase -> sort_border OK; R2={S[1]} C2={[S[i][1] for i in range(6)]}")
    print("CANONICAL BORDER LEMMA DEMO: PASS (5/5)")

if __name__=="__main__":
    main()
