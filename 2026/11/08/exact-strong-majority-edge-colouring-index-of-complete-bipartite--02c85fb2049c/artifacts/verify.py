#!/usr/bin/env python3
"""Standalone exact arithmetic checks for strong-majority edge colorings of bicliques."""
from itertools import product
from math import comb

def valid(rows, palette):
    m=len(rows);n=len(rows[0]);cap=(m+n-2)//2
    for i in range(m):
        for j in range(n):
            for c in range(palette):
                adj=sum(rows[i][t]==c for t in range(n) if t!=j)
                adj+=sum(rows[s][j]==c for s in range(m) if s!=i)
                if adj>cap:return False
    return True

WITNESSES={
 (4,4,3):('0202','1021','0101','2211'),
 (4,7,3):('0010212','1202011','0020121','2121200'),
 (3,4,4):('0220','1313','1223'),
 (4,5,4):('01202','32130','01121','33202'),
}

def unsat_three(m,n):
    """Exhaust columns modulo permutations, with sound incremental pruning."""
    cap=(m+n-2)//2
    patterns=list(product(range(3),repeat=n)); A=[]; columns=[[0]*3 for _ in range(n)];R=[]
    checked=[0]*m
    def rec(t):
        if t==m: return True
        for p in patterns:
            if any(p[j]<p[j-1] and all(A[i][j]==A[i][j-1] for i in range(t)) for j in range(1,n)):
                continue
            checked[t]+=1
            r=[p.count(c) for c in range(3)]
            for j,c in enumerate(p):columns[j][c]+=1
            feasible=True
            for i,row in enumerate(A+[p]):
                s=R[i] if i<t else r
                for j,col in enumerate(row):
                    for c in range(3):
                        if s[c]+columns[j][c]-2*(c==col)>cap:
                            feasible=False;break
                    if not feasible:break
                if not feasible:break
            if feasible:
                A.append(p);R.append(r)
                if rec(t+1):return True
                A.pop();R.pop()
            for j,c in enumerate(p):columns[j][c]-=1
        return False
    assert not rec(0)
    return checked

if __name__=='__main__':
    for (m,n,k),strings in WITNESSES.items():
        rows=[tuple(map(int,s)) for s in strings]
        assert len(rows)==m and all(len(r)==n for r in rows)
        assert valid(rows,k),(m,n,k)
        print('EXPLICIT_COLORING_OK',m,n,k)
    for m,n in [(3,4),(4,5)]:
        print('EXHAUSTIVE_THREE_COLOR_UNSAT_OK',m,n,unsat_three(m,n))
    failures=[]
    for m in range(3,17):
        for n in range(m,17):
            if m+n>16:continue
            if (m+2)//3+(n+2)//3>(m+n-2)//2:failures.append((m,n))
    assert failures==[(3,4),(4,4),(4,5),(4,7)],failures
    print('SMALL_PARAMETER_BOUNDARY_OK',failures)
    for m in range(2,8):
        for n in range(m,9):
            if m*n>16:continue
            actual=sum(valid([v[i*n:(i+1)*n] for i in range(m)],2) for v in product(range(2),repeat=m*n))
            predicted=(comb(n,n//2) if m==2 and n%2==0 else 0)
            if m==n==2:predicted*=2
            assert actual==predicted,(m,n,actual,predicted)
            print('TWO_COLOR_COUNT_OK',m,n,actual)
    print('VERIFY_OK')
