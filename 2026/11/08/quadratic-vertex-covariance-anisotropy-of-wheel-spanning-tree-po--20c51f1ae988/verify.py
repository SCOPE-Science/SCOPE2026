"""Standalone exact checks and Fourier replays for wheel spanning-tree covariance.
Requires Python 3.9+ standard library only. No external datasets.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, cos, pi, sqrt
import cmath


def inverse_rational(A):
    n=len(A)
    x=[[F(A[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if x[i][k])
        x[k],x[p]=x[p],x[k]
        v=x[k][k]
        x[k]=[z/v for z in x[k]]
        for i in range(n):
            if i!=k:
                v=x[i][k]
                if v:
                    x[i]=[x[i][j]-v*x[k][j] for j in range(2*n)]
    return [v[n:] for v in x]


def exact_kernel_cov(m):
    # Edge order: hub spokes (0,i+1), then rim edges (i+1, (i+1)%m+1)
    E=[[F(0) for e in range(2*m)] for i in range(m)]
    for i in range(m):
        E[i][i]=F(1)
        E[i][m+i]=F(1)
        E[(i+1)%m][m+i]=F(-1)
    L=[[sum(E[i][e]*E[j][e] for e in range(2*m)) for j in range(m)] for i in range(m)]
    G=inverse_rational(L)
    GE=[[sum(G[i][k]*E[k][j] for k in range(m)) for j in range(2*m)] for i in range(m)]
    K=[[sum(E[k][i]*GE[k][j] for k in range(m)) for j in range(2*m)] for i in range(2*m)]
    return [[(K[i][i] if i==j else F(0))-K[i][j]*K[i][j] for j in range(2*m)] for i in range(2*m)]


def enumerated_cov(m):
    edges=[(m,i) for i in range(m)]+[(i,(i+1)%m) for i in range(m)]
    count=0; num=[0]*(2*m); pair=[[0]*(2*m) for _ in range(2*m)]
    for inds in combinations(range(2*m),m):
        parent=list(range(m+1))
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        good=True
        for e in inds:
            a,b=edges[e];a=find(a);b=find(b)
            if a==b:
                good=False;break
            parent[a]=b
        if not good:continue
        count+=1
        for e in inds:num[e]+=1
        for e in inds:
            for f in inds:pair[e][f]+=1
    C=[[F(pair[i][j],count)-F(num[i]*num[j],count*count) for j in range(2*m)] for i in range(2*m)]
    return C,count


def wheel_cov(m):
    a=(3-sqrt(5))/2
    gamma=lambda d:(a**(d%m)+a**(m-d%m))/(sqrt(5)*(1-a**m))
    g=[gamma(d) for d in range(m)]
    # Compute via cyclic Green formula, independent of enumerated covariance
    K=[[0.]*(2*m) for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            K[i][j]=g[(i-j)%m]
            K[i][m+j]=g[(i-j)%m]-g[(i-j-1)%m]
            K[m+i][j]=g[(i-j)%m]-g[(i-j+1)%m]
            K[m+i][m+j]=(2*g[(i-j)%m]-g[(i-j-1)%m]-g[(i-j+1)%m])
    C=[[(-K[i][j]**2+(K[i][i] if i==j else 0.)) for j in range(2*m)] for i in range(2*m)]
    return C


def blocks(m):
    C=wheel_cov(m)
    result=[]
    for j in range(m):
        z=cmath.exp(2j*pi*j/m)
        B=[[sum(C[a*m][b*m+d]*z**d for d in range(m)) for b in range(2)] for a in range(2)]
        # eigenvalues of Hermitian 2x2
        assert abs(B[0][0].imag)<1e-7 and abs(B[1][1].imag)<1e-7
        assert abs(B[0][1]-B[1][0].conjugate())<1e-7
        x,y=B[0][0].real,B[1][1].real
        delta=sqrt((x-y)**2+4*abs(B[0][1])**2)
        result.append(((x+y-delta)/2,(x+y+delta)/2))
    return result


def limit_branches(theta):
    t=cos(theta/2)
    scale=2/sqrt(5)
    return (scale*(3-2*t*t-t)/(9-4*t*t),scale*(3-2*t*t+t)/(9-4*t*t))

if __name__=='__main__':
    total=0;matrices=0
    for m in range(3,8):
        A=exact_kernel_cov(m)
        B,count=enumerated_cov(m)
        assert A==B,(m,'exact mismatch')
        assert all(sum(row)==0 for row in A)
        assert all(sum(A[i][i] for i in range(2*m))>0 for _ in [0])
        total+=count;matrices+=1
    checks=0; formula_checks=0
    for m in range(3,33):
        E=blocks(m)
        a=(3-sqrt(5))/2
        g=[(a**d+a**(m-d))/(sqrt(5)*(1-a**m)) for d in range(m)]
        h=[2*g[d]-g[(d-1)%m]-g[(d+1)%m] for d in range(m)]
        q=[g[d]-g[(d+1)%m] for d in range(m)]
        for j in range(m):
            z=cmath.exp(2j*pi*j/m)
            x=(g[0]-sum(g[d]**2*z**d for d in range(m))).real
            y=(h[0]-sum(h[d]**2*z**d for d in range(m))).real
            off=-sum(q[d]**2*z**d for d in range(m))
            D=sqrt((x-y)**2+4*abs(off)**2)
            prediction=((x+y-D)/2,(x+y+D)/2)
            assert max(abs(prediction[k]-E[j][k]) for k in range(2))<1e-9
            formula_checks+=1
        assert abs(E[0][0])<1e-8
        for j in range(1,m):
            assert E[j][0]>1e-10
            assert abs(E[j][0]-E[m-j][0])<1e-7
            assert abs(E[j][1]-E[m-j][1])<1e-7
            checks+=1
    goal=4/(5*pi*pi)
    previous=None
    for m in (40,60,80,100,160,240,320):
        E=blocks(m)
        positive=[v for pair in E for v in pair if v>1e-8]
        k=max(positive)/min(positive)
        scaled=k/m**2
        assert abs(scaled-goal)<0.004,(m,scaled,goal)
        assert E[0][1]==max(positive)
        assert abs(E[1][0]-min(positive))<1e-9
        assert max(abs(E[j][i]-limit_branches(2*pi*min(j,m-j)/m)[i]) for j in range(m) for i in range(2))<0.00001
        previous=(m,scaled)
    print('WHEEL_SPANNING_TREE_INERTIA_CHECKS_PASSED', 'exact_trees=',total, 'exact_matrices=',matrices, 'Fourier_blocks=',checks,'closed_formula_blocks=',formula_checks,'scaled_kappa_at_320=',round(previous[1],10),'limit=',round(goal,10))
