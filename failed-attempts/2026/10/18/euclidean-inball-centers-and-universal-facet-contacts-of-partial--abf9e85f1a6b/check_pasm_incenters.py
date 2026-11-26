"""Finite reproducibility checks for Euclidean inball formulas of partial ASM polytopes.
Scientific source: arXiv:2012.09901, Theorem 4.6. This is not an all-dimensions proof.
"""
from decimal import Decimal, getcontext
getcontext().prec=70
D=Decimal

def candidates(m,n):
    L=max(m,n);r=1/(D(L)+D(L).sqrt()); eps=r/(D(100)*L*L)
    c=[[r]*n for _ in range(m)]
    if m<n:
        for i in range(1,m):
            c[i][0]=r+eps
            for j in range(1,n):c[i][j]=r-2*eps
        expected={(0,j) for j in range(n)}
    elif m>n:
        for j in range(1,n):
            c[0][j]=r+eps
            for i in range(1,m):c[i][j]=r-2*eps
        expected={(i,0) for i in range(m)}
    else:
        for i in range(1,m):
            for j in range(1,n):c[i][j]=r-eps
        expected={(0,j) for j in range(n)}|{(i,0) for i in range(m)}
    return r,c,expected

def check(m,n):
    r,c,eq=candidates(m,n)
    active=[]
    tol=D("1e-55")
    for i in range(m):
        for j in range(n):
            S=sum(c[i][:j+1]); a=r*D(j+1).sqrt()
            assert S>=a-tol and S<=1-a+tol,('row',m,n,i,j,S,a)
            if abs(S-a)<tol:active.append(('row_lower',i,j))
            if abs(S-(1-a))<tol:active.append(('row_upper',i,j))
            T=sum(c[s][j] for s in range(i+1));b=r*D(i+1).sqrt()
            assert T>=b-tol and T<=1-b+tol,('col',m,n,i,j,T,b)
            if abs(T-b)<tol:active.append(('col_lower',i,j))
            if abs(T-(1-b))<tol:active.append(('col_upper',i,j))
    if m<n:
        # Every first-row entry is a sharp lower facet, and row 1's total is sharp.
        assert all(('col_lower',0,j) in active for j in range(n))
        assert ('row_upper',0,n-1) in active
        assert len(set(active))==n+2 # includes the duplicate row_lower at (0,0)
    elif m>n:
        assert all(('row_lower',i,0) in active for i in range(m))
        assert ('col_upper',m-1,0) in active
        assert len(set(active))==m+2
    else:
        assert all(('col_lower',0,j) in active for j in range(n))
        assert all(('row_lower',i,0) in active for i in range(m))
        assert ('row_upper',0,n-1) in active and ('col_upper',m-1,0) in active
        assert len(set(active))==2*n+2 # duplicated normal for x_11>=0
    return len(active)

if __name__=='__main__':
    count=0;active=0
    for m in range(2,41):
        for n in range(2,41):
            active+=check(m,n)
            count+=1
    print(f'PASS: {count} matrix shapes, {active} labeled active inequalities; high-precision row/column prefix bounds verified.')
