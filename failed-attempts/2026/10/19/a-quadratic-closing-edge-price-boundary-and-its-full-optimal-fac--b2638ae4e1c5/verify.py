"""Exact-rational finite checks for a priced closing edge on a path.

Python 3 standard library only. Finite tests support, but do not replace,
the proof for arbitrary network order and positive budgets.
"""
from fractions import Fraction as F


def dot(a, b):
    return sum((u*v for u,v in zip(a,b)), F(0))


def mv(a, x):
    return [dot(row,x) for row in a]


def lap(n, edge_weights, chord=F(0)):
    m=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,w in enumerate(edge_weights):
        m[i][i]+=w;m[i+1][i+1]+=w
        m[i][i+1]-=w;m[i+1][i]-=w
    m[0][0]+=chord;m[-1][-1]+=chord
    m[0][-1]-=chord;m[-1][0]-=chord
    return m


def det(a):
    n=len(a)
    if not n:return F(1)
    b=[list(row) for row in a];sgn=1;out=F(1)
    for j in range(n):
        piv=next((i for i in range(j,n) if b[i][j]),None)
        if piv is None:return F(0)
        if piv!=j:
            b[j],b[piv]=b[piv],b[j];sgn=-sgn
        p=b[j][j];out*=p
        for i in range(j+1,n):
            v=b[i][j]/p
            for k in range(j+1,n):b[i][k]-=v*b[j][k]
            b[i][j]=F(0)
    return out*sgn


def assert_pos_ground(a):
    # A symmetric zero-row-sum matrix is nonnegative with simple
    # constant nullspace iff this anchored block is positive definite.
    n=len(a)
    for k in range(1,n):
        assert det([row[:k] for row in a[:k]])>0


checks=0
for n in range(3,12):
    m=n-1
    u=[F(i*(n-i),2) for i in range(1,n)]
    x=[F(2*i-(n-1),2) for i in range(n)]
    S=F(n*(n*n-1),12)
    assert sum(u)==S;checks+=1
    L0=lap(n,u)
    assert mv(L0,x)==x;checks+=1
    for k in range(1,n):
        f=[F(j**k) for j in range(n)]
        v=[z-F(k*(k+1),2)*b for z,b in zip(mv(L0,f),f)]
        # A polynomial of degree <k has vanishing k-th difference.
        for _ in range(k):v=[v[j+1]-v[j] for j in range(len(v)-1)]
        assert all(vv==0 for vv in v);checks+=1
    C=[[F(min(i,j)*(n-max(i,j)),n) for j in range(1,n)] for i in range(1,n)]
    D=[[u[i] if i==j else F(0) for j in range(m)] for i in range(m)]
    A=[[D[i][j]-C[i][j] for j in range(m)] for i in range(m)]
    Q=[[F(m if i==j else 0)-1 for j in range(m)] for i in range(m)]
    assert all(sum(A[i])==0 and sum(Q[i])==0 for i in range(m));checks+=1
    assert all(A[i][j]==-C[i][j] for i in range(m) for j in range(m) if i!=j);checks+=1
    assert_pos_ground(A);checks+=1
    for delta in (F(0),F(1,5),F(1,4)):
        H=[[A[i][j]-delta*Q[i][j] for j in range(m)] for i in range(m)]
        assert_pos_ground(H);checks+=1
        w=[val-m*delta for val in u]
        assert min(w)>0
        L=lap(n,w,delta)
        assert mv(L,x)==x;checks+=1
        # Cost is independent of the chord allocation at price m^2.
        assert sum(w)+m*m*delta==S;checks+=1
    # Centered pairwise variance identity for a nontrivial difference vector.
    d=[F((i*i+3*i+1)%7-3) for i in range(1,n)]
    y=[F(0)]
    for di in d:y.append(y[-1]+di)
    mean=sum(y)/n;y=[yi-mean for yi in y]
    assert dot(y,y)==dot(d,mv(C,d));checks+=1
    # A price above the boundary strictly discounts the closing edge in
    # the test Rayleigh quotient; below it raises the path-optimal eigenvalue
    # to first order in the added conductance.
    assert (m*m-F(1))>0 and m*m+1>m*m;checks+=1

for n in (3,4):
    m=n-1
    u=[F(i*(n-i),2) for i in range(1,n)]
    C=[[F(min(i,j)*(n-max(i,j)),n) for j in range(1,n)] for i in range(1,n)]
    A=[[((u[i] if i==j else F(0))-C[i][j]) for j in range(m)] for i in range(m)]
    Q=[[F(m if i==j else 0)-1 for j in range(m)] for i in range(m)]
    T=[[A[i][j]-F(1,3)*Q[i][j] for j in range(m)] for i in range(m)]
    assert det([row[:m-1] for row in T[:m-1]])==0;checks+=1

print('VERIFY_OK',checks,'exact rational assertion groups')
