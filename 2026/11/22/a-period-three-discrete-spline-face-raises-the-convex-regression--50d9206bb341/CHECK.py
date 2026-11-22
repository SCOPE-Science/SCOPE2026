"""Supplementary exact-rational and floating-point tests for a discrete spline-face sensitivity bound.
Requires Python 3 standard library only. Finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def spline_matrix(cells):
    B = [[F(0) for _ in range(cells + 1)] for _ in range(3 * cells + 1)]
    for k in range(cells):
        for t in range(3):
            B[3*k+t][k] = F(3-t,3)
            B[3*k+t][k+1] = F(t,3)
    B[3*cells][cells] = F(1)
    return B


def inverse(A):
    n=len(A)
    M=[[A[i][j] for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        idx=next(i for i in range(k,n) if M[i][k])
        M[k],M[idx]=M[idx],M[k]
        pivot=M[k][k]
        M[k]=[a/pivot for a in M[k]]
        for i in range(n):
            if i != k:
                t=M[i][k]
                if t: M[i]=[a-t*b for a,b in zip(M[i],M[k])]
    return [row[n:] for row in M]


def dot(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A): return [list(x) for x in zip(*A)]


def check():
    count=0
    for m in range(2,10):
        B=spline_matrix(m)
        G=dot(transpose(B),B)
        for i in range(m+1):
            for j in range(m+1):
                desired=F(14,9) if i==j and i in (0,m) else F(19,9) if i==j else F(4,9) if abs(i-j)==1 else F(0)
                assert G[i][j]==desired
                count+=1
        H=dot(dot(B,inverse(G)),transpose(B))
        assert dot(H,H)==H
        count+=1
        assert H==transpose(H)
        count+=1
        # Knot-row entries of H equal inverse Gram coefficients interpolated through B.
        k=m//2
        pos=3*k
        for j in range(3*m+1):
            predicted=sum((inverse_column*B[j][a] for a,inverse_column in enumerate(inverse(G)[k])),F(0))
            assert H[pos][j]==predicted
            count+=1
        # Convex-combination structure controls every between-knot row by knot rows.
        rownorms=[sum(map(abs,row),F(0)) for row in H]
        for j in range(3*m+1):
            lower=(j//3)*3
            upper=min(lower+3,3*m)
            if lower<upper:
                assert rownorms[j] <= max(rownorms[lower],rownorms[upper])
                count+=1
        assert max(rownorms)==max(rownorms[::3])
        count+=1
        # Monotonic lower bound: finite face kernel row does not exceed coarse safe bound.
        assert rownorms[pos] < F(2)
        count+=1
    # Numerical long-chain check uses exact tridiagonal solve (Thomas algorithm), not eigen packages.
    def knot_row(m,k):
        diag=[14.0]+[19.0]*(m-1)+[14.0]
        off=4.0
        d=[0.0]*(m+1); d[k]=9.0
        c=[0.0]*m
        c[0]=off/diag[0]
        d[0]/=diag[0]
        for j in range(1,m+1):
            denom=diag[j]-off*c[j-1]
            if j<m: c[j]=off/denom
            d[j]=(d[j]-off*d[j-1])/denom
        g=[0.0]*(m+1)
        g[m]=d[m]
        for j in range(m-1,-1,-1): g[j]=d[j]-c[j]*g[j+1]
        total=sum(abs(x) for x in g)
        for j in range(m):
            total += abs((2*g[j]+g[j+1])/3)+abs((g[j]+2*g[j+1])/3)
        return total
    target=(9+2*sqrt(33))/11
    assert isclose(target, (3/sqrt(33))*(1+2/(1+(3*sqrt(33)-19)/8)),rel_tol=1e-14)
    count+=1
    vals=[]
    for m in [8,16,32,64,128]:
        s=knot_row(m,m//2)
        vals.append((m,s))
        assert 1.0 < s < target+1e-10
        count+=1
    assert abs(vals[-1][1]-target)<2e-10
    count+=1
    # Strict improvement over earlier alternating-curvature lower bound.
    assert target > 1+1/sqrt(2)
    count+=1
    print('Exact rational and numerical assertions passed:',count)
    print('Infinite period-three constant:',f'{target:.15f}')
    print('Finite centered-knot row samples:',vals)

if __name__=='__main__': check()
