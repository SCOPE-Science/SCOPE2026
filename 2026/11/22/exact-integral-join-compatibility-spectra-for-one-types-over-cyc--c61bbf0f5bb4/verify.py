#!/usr/bin/env python3
"""Exact independent checker for cycle-base one-type join-compatibility matrices.
No external packages except SymPy, used for independent Smith reduction.
"""
import sys
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def masks(n):
    return [s for s in range(1 << n) if not any((s >> i) & 1 and (s >> ((i+1)%n)) & 1 for i in range(n))]

def zpath(t):
    p0,p1=1,0
    if t==0:return p0
    if t==1:return p1
    for i in range(2,t+1):p0,p1=p1,p1-p0
    return p1

def w_from_link(s,n):
    if s==0:
        # Cycle independence polynomial at -1.
        return [2,1,-1,-2,-1,1][n%6]
    points=[i for i in range(n) if s>>i&1]
    result=1
    for i,p in enumerate(points):
        d=(points[(i+1)%len(points)]-p)%n
        if len(points)==1:d=n
        if d==2 or d==3:continue
        result*=zpath(d-3)
    return result

def ws_direct(n,ff):
    return [sum((-1)**((g^f).bit_count()) for g in ff if g&f==f) for f in ff]

def predicted_rank(n):
    a=[3,0,2]
    for j in range(3,n+1):a.append(a[j-2]+2*a[j-3])
    return 1+a[n]-3*(n%3==0)

def run():
    total_entries=0;count_n=0
    for n in range(4,11):
        ff=masks(n)
        ws=[w_from_link(s,n) for s in ff]
        assert ws==ws_direct(n,ff),('link identity',n)
        assert all(abs(w)<=1 for w in ws[1:]),('nonempty link',n)
        nonzero=sum(w!=0 for w in ws)
        assert nonzero==predicted_rank(n),(n,nonzero,predicted_rank(n))
        assert sum(abs(w)==2 for w in ws)==(n%3==0)
        Z=Matrix(len(ff),len(ff),lambda i,j:int(ff[i]&ff[j]==ff[i]))
        assert abs(Z.det())==1
        D=Matrix.diag(*ws)
        # The union of positive old-neighborhood requirements is consistent exactly when its vertex set is independent.
        M=Matrix(len(ff),len(ff),lambda i,j:int((ff[i]|ff[j]) in ff))
        assert M==Z*D*Z.T
        diag=smith_normal_form(M,domain=ZZ).diagonal()
        nz=[abs(int(x)) for x in diag if x]
        expected=[1]*(nonzero-(n%3==0))+([2] if n%3==0 else [])
        assert nz==expected,(n,nz,expected)
        total_entries+=len(ff)**2;count_n+=1
        print(f'C{n}: types={len(ff)}, rational_rank={nonzero}, torsion2={int(n%3==0)}, equality_and_SNF=OK')
    for n in range(11,20):
        ff=masks(n)
        ws=[w_from_link(s,n) for s in ff]
        assert sum(w!=0 for w in ws)==predicted_rank(n)
        assert sum(abs(w)==2 for w in ws)==(n%3==0)
        print(f'C{n}: link_count={len(ff)}, rank={predicted_rank(n)}, link_distribution=OK')
    print(f'VERIFICATION_OK: {count_n} exact integer-matrix SNFs; {total_entries} feasibility entries; rank/link checks through C19')
if __name__=='__main__':run()
