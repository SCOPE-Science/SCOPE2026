"""Finite checks for regular-fan support-sampling determinant and noise amplification.
Only standard-library arithmetic; the all-size and tail statements rely on proof, not this test.
"""
import math, random


def matrix(angles):
    n=len(angles)
    theta=2*math.pi/n
    A=[[0.0]*n for _ in range(n)]
    for i,alpha in enumerate(angles):
        A[i][i]=math.sin(theta-alpha)/math.sin(theta)
        A[i][(i+1)%n]=math.sin(alpha)/math.sin(theta)
    return A


def determinant(A):
    M=[r[:] for r in A]
    n=len(M); sign=1.; prod=1.
    for k in range(n):
        j=max(range(k,n),key=lambda j:abs(M[j][k]))
        if abs(M[j][k])<1e-14: return 0.
        if j!=k:
            M[j],M[k]=M[k],M[j];sign=-sign
        p=M[k][k];prod*=p
        for i in range(k+1,n):
            ratio=M[i][k]/p
            for j in range(k+1,n):M[i][j]-=ratio*M[k][j]
    return sign*prod


def predicted(angles):
    n=len(angles);theta=2*math.pi/n
    x=math.prod(math.sin(theta-a)/math.sin(theta) for a in angles)
    y=math.prod(math.sin(a)/math.sin(theta) for a in angles)
    return x+((-1)**(n-1))*y


def solve(A,b):
    n=len(A);M=[A[i][:]+[b[i]] for i in range(n)]
    for k in range(n):
        i=max(range(k,n),key=lambda i: abs(M[i][k]))
        if abs(M[i][k])<1e-15:raise ZeroDivisionError
        M[k],M[i]=M[i],M[k]
        pivot=M[k][k]
        for j in range(k,n+1):M[k][j]/=pivot
        for i in range(n):
            if i==k:continue
            c=M[i][k]
            for j in range(k,n+1):M[i][j]-=c*M[k][j]
    return [row[n] for row in M]


def norm2(v):return math.sqrt(sum(x*x for x in v))

if __name__=='__main__':
    rng=random.Random(20261117)
    tested=0
    for n in range(3,17):
        theta=2*math.pi/n
        for j in range(80):
            angles=[theta*(0.2+0.6*rng.random()) for _ in range(n)]
            A=matrix(angles)
            v=determinant(A);w=predicted(angles)
            assert abs(v-w)<1e-8*max(1.,abs(v),abs(w)),(n,j,v,w)
            tested+=1
        m=theta/2
        A=matrix([m]*n)
        if n%2==0:
            z=[(-1.)**i for i in range(n)]
            assert max(abs(sum(A[i][j]*z[j] for j in range(n))) for i in range(n))<1e-11
            d=0.13*theta
            A2=matrix([m+d,m-d]+[m]*(n-2))
            z=[1.]
            for i in range(n-1):z.append(-A2[i][i]*z[-1]/A2[i][i+1])
            assert max(abs(sum(A2[i][j]*z[j] for j in range(n))) for i in range(n))<1e-10
        else:
            assert abs(determinant(A))>1e-12
    ratios=[]
    n=8;theta=2*math.pi/n;m=theta/2
    for eps in (1e-3,5e-4,2.5e-4,1.25e-4):
        A=matrix([m]*(n-1)+[m+eps])
        x=solve(A,[1.]+[0.]*(n-1))
        ratios.append(eps*norm2(x))
    assert max(ratios)/min(ratios)<1.002,ratios
    print('POLYGON_SUPPORT_DESIGN_PASS random_determinant_cases=',tested,
          ' midpoint_and_balanced_cases=14', ' inverse_pole_ratios=',[round(v,7) for v in ratios])
