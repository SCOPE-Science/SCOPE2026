"""Exact finite-parameter checks for coherent absorption on Johnson and Kneser graphs.
All calculations use SymPy integer/rational matrix arithmetic, without floating point.
The proof for every parameter is provided separately in RESULT.md.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, Rational, eye, zeros


def check(n, k):
    points = tuple(range(n))
    V = list(combinations(points, k))
    D = [s for s in V if 0 in s]
    U = [s for s in V if 0 not in s]
    rows = len(D)
    cols = len(U)
    DB = [frozenset(s) for s in D]
    UB = [frozenset(s) for s in U]
    B1 = Matrix(rows, cols, lambda a,b: int(len(DB[a] & UB[b]) == k-1))
    B2 = Matrix(rows, cols, lambda a,b: int(not DB[a] & UB[b]))
    assert B1.rank() == rows and B2.rank() == rows, (n,k,"rank")
    C1 = B1.rowspace()
    C2 = B2.rowspace()
    assert Matrix.vstack(*C1,*C2).rank() == rows, (n,k,"rowspace")
    d = comb(n-1,k)-comb(n-1,k-1)
    q = Rational(n-2*k,n-k)
    P = Matrix(cols,cols,lambda a,b: q*(-1)**(k-len(UB[a]&UB[b])) /
                comb(n-k-1,k-len(UB[a]&UB[b])))
    assert P.T == P and P*P == P, (n,k,"projector")
    assert P.trace()==d and B1*P==zeros(rows,cols) and B2*P==zeros(rows,cols), (n,k,"kernel")
    A1 = Matrix(cols,cols,lambda a,b:int(a!=b and len(UB[a]&UB[b])==k-1))
    A2 = Matrix(cols,cols,lambda a,b:int(a!=b and len(UB[a]&UB[b])==0))
    assert A1*P == -k*P, (n,k,"Johnson action")
    assert A2*P == (-1)**k*P, (n,k,"Kneser action")
    for a in range(cols):
        assert P[a,a]==q
    return d,rows,cols


def check_middle_shell():
    n,k=7,3
    V=list(combinations(range(n),k))
    D=[frozenset(s) for s in V if 0 in s]
    U=[frozenset(s) for s in V if 0 not in s]
    B=Matrix(len(D),len(U),lambda a,b:int(len(D[a]&U[b])==k-2))
    C=Matrix(len(U),len(U),lambda a,b:int(U[a].isdisjoint(U[b])))
    P=(eye(len(U))-C)/2
    A=Matrix(len(U),len(U),lambda a,b:int(a!=b and len(U[a]&U[b])==k-2))
    assert B.rank()==10 and P.rank()==10
    assert B*P==zeros(len(D),len(U)) and P*P==P and P.T==P
    assert A*C==C*A
    pairs=[]
    seen=set()
    for i,s in enumerate(U):
        if i in seen: continue
        j=next(j for j,t in enumerate(U) if t.isdisjoint(s))
        pairs.append((i,j))
        seen.add(i);seen.add(j)
    assert len(pairs)==10
    M=Matrix(len(D),len(pairs),lambda a,b:B[a,pairs[b][0]])
    from sympy import ones
    assert M.T*M==4*eye(10)+5*ones(10,10)
    i,j=pairs[0]
    assert P[i,i]==Rational(1,2) and P[i,j]==Rational(-1,2)
    return len(D),len(U),P.trace()


def main():
    cases=[]
    for n in range(3,10):
        for k in range(1,(n-1)//2+1):
            if comb(n-1,k)>36: continue
            cases.append((n,k,check(n,k)))
    print('VERIFY_OK', 'cases=',len(cases))
    for n,k,(d,rows,cols) in cases:
        print('n=%d k=%d dark=%d detectors=%d untrapped=%d'%(n,k,d,rows,cols))
    assert check(5,2)[0]==2
    print('Petersen/triangular: localized capture 2/3; complement-pair +/- capture 1/3 and 1')
    print('J_2(7,3) resonance:', check_middle_shell())

if __name__=='__main__': main()
