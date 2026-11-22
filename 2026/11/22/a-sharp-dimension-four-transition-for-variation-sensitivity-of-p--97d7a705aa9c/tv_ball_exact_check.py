"""Exact rational verification of the path-TV-ball projection face calculation.

No external dependencies. Run: python tv_ball_exact_check.py
"""
from fractions import Fraction as F
from itertools import product


def H(i,k,m):
    return F(min(i,k)*(m+1-max(i,k)),m+1)


def transpose(M):
    return [list(x) for x in zip(*M)]


def mm(A,B):
    T=transpose(B)
    return [[sum(x*y for x,y in zip(a,b)) for b in T] for a in A]


def ucol(J,k,m):
    r=len(J)
    v=[F(0)]*r
    if k < J[0]:
        v[0]=F(k,J[0])
    elif k > J[-1]:
        v[-1]=F(m+1-k,m+1-J[-1])
    elif k in J:
        v[J.index(k)]=F(1)
    else:
        a=next(i for i in range(r-1) if J[i]<k<J[i+1])
        v[a]=F(J[a+1]-k,J[a+1]-J[a])
        v[a+1]=F(k-J[a],J[a+1]-J[a])
    return v


def schur_laplacian(J,m):
    nodes=[0]+J+[m+1]
    r=len(J)
    gaps=[F(1,nodes[i+1]-nodes[i]) for i in range(r+1)]
    B=[[F(0)]*r for _ in range(r)]
    for a in range(r):
        B[a][a]=gaps[a]+gaps[a+1]
        if a+1<r:
            B[a][a+1]=B[a+1][a]=-gaps[a+1]
    return B


def test(m):
    total=0
    maximum=F(1)
    witness=None
    for signs in product((-1,0,1),repeat=m):
        J=[i+1 for i,s in enumerate(signs) if s]
        if not J: continue
        s=[F(signs[j-1]) for j in J]
        B=schur_laplacian(J,m)
        HJ=[[H(i,j,m) for j in J] for i in J]
        prod=mm(B,HJ)
        assert all(prod[a][b] == (a==b) for a in range(len(J)) for b in range(len(J)))
        v=[sum(B[a][b]*s[b] for b in range(len(J))) for a in range(len(J))]
        den=sum(s[a]*v[a] for a in range(len(J)))
        assert den>0 and sum(map(abs,v))==den
        for k in range(1,m+1):
            U=ucol(J,k,m)
            assert all(sum(B[a][b]*H(J[b],k,m) for b in range(len(J))) == U[a] for a in range(len(J)))
            assert all(t>=0 for t in U) and sum(U)<=1
            su=sum(s[a]*U[a] for a in range(len(J)))
            T=[U[a]-v[a]*su/den for a in range(len(J))]
            val=sum(map(abs,T))
            assert val<=2
            if val>maximum:
                maximum=val;witness=(signs,k)
        total+=1
    return total,maximum,witness


if __name__=='__main__':
    for n in range(2,9):
        count,c,w=test(n-1)
        expected=F(1) if n<=3 else F(2)
        assert c==expected, (n,c,expected)
        print(f'ALL_ACTIVE_FACE_RATIONAL_CHECK_PASS n={n} faces={count} sharp={c} witness={w}')
    for n in range(4,101):
        m=n-1
        # On the all-positive active face, the input edge vector is
        # (2,1,...,1,2) and the projection has every edge difference 1.
        # Perturbing an interior difference by 1/4 produces sharp ratio 2.
        delta=F(1,4)
        y=[F(1)]*m
        y[0]=y[-1]=F(2)
        z=[F(1)]*m
        z2=z.copy()
        k=m//2
        z2[k]+=delta
        z2[0]-=delta/2
        z2[-1]-=delta/2
        assert sum(z)==sum(z2)==m
        assert all(a>0 for a in z2)
        # KKT: y-z = G*ones; y+delta*e_k-z2 = (1+delta/2)*G*ones.
        y2=y.copy();y2[k]+=delta
        assert [y2[i]-z2[i] for i in range(m)]==[(1+delta/2) if i in (0,m-1) else 0 for i in range(m)]
        assert sum(abs(z2[i]-z[i]) for i in range(m))==2*delta
        assert sum(abs(y2[i]-y[i]) for i in range(m))==delta
    print('EXPLICIT_GLOBAL_SHARPNESS_WITNESSES_PASS n=4..100')
    print('ALL_PATH_TV_BALL_PROJECTION_CHECKS_PASS')
