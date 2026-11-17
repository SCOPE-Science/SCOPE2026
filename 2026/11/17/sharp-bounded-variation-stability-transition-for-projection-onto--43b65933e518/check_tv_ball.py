"""Exact finite-face and attaining-witness checks for path-variation constrained projection."""
from fractions import Fraction as F
from itertools import product


def inverse(A):
    n=len(A)
    X=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if X[i][j])
        X[j],X[p]=X[p],X[j]
        v=X[j][j]
        X[j]=[x/v for x in X[j]]
        for i in range(n):
            if i!=j:
                v=X[i][j]
                X[i]=[a-v*b for a,b in zip(X[i],X[j])]
    return [r[n:] for r in X]


def matmul(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]


def projection_edge_derivative(signs):
    m=len(signs)
    S=[i for i,s in enumerate(signs) if s]
    if not S:return [[F(i==j) for j in range(m)] for i in range(m)]
    Z=[i for i,s in enumerate(signs) if not s]
    C=[[F(i==j) for j in range(m)] for i in Z]+[[F(s) for s in signs]]
    Q=[[F(2 if i==j else (-1 if abs(i-j)==1 else 0)) for j in range(m)] for i in range(m)]
    QC=matmul(Q,list(map(list,zip(*C))))
    K=matmul(C,QC)
    correction=matmul(matmul(QC,inverse(K)),C)
    return [[F(i==j)-correction[i][j] for j in range(m)] for i in range(m)]


def variation(z):
    return sum((abs(z[i+1]-z[i]) for i in range(len(z)-1)),F(0))


def witness(n):
    radius=F(2*(n-1)-2)
    epsilon=F(1,2)
    x=[F(2*i) for i in range(n)]
    y=[v+(epsilon if i>=2 else F(0)) for i,v in enumerate(x)]
    def project_halfspace(a):
        t=(a[-1]-a[0]-radius)/2
        p=a[:]
        p[0]+=t
        p[-1]-=t
        assert all(p[i+1]>p[i] for i in range(n-1)),(n,p)
        assert variation(p)==radius
        # p is feasible and is the Euclidean projection onto the containing halfspace.
        return p
    px=project_halfspace(x)
    py=project_halfspace(y)
    ratio=variation([u-v for u,v in zip(py,px)])/variation([u-v for u,v in zip(y,x)])
    assert ratio==2,(n,ratio)
    return ratio


def main():
    for n in range(2,9):
        m=n-1
        best=F(1)
        count=0
        for s in product((-1,0,1),repeat=m):
            if s and s[0]==-1:
                pass
            if not any(s): continue
            B=projection_edge_derivative(s)
            L=max(sum((abs(B[i][j]) for i in range(m)),F(0)) for j in range(m))
            best=max(best,L)
            count+=1
            assert L<=2
        expected=F(1) if n<=3 else F(2)
        assert best==expected,(n,best,expected)
        print('ALL_FACE_DERIVATIVES_PASS', 'n='+str(n),'faces='+str(count),'sharp='+str(best))
    for n in range(4,40):
        witness(n)
    print('EXACT_FINITE_WITNESSES_PASS', 'n=4..39')
    print('ALL_PATH_TV_BALL_PROJECTION_CHECKS_PASS')

if __name__=='__main__':main()
