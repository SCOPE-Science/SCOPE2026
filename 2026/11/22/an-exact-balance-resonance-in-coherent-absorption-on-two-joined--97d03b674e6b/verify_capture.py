"""Exact finite-case verification of sitewise quantum capture on clique barbells.
Run: python3 verify_capture.py. Only Python standard library is required.
This verifies finite instances, not the all-size determinant identity in the proof.
"""
from fractions import Fraction as F


def transpose(A):
    return [list(x) for x in zip(*A)]


def mul(A, B):
    BT = transpose(B)
    return [[sum(x*y for x, y in zip(row, col)) for col in BT] for row in A]


def inverse(A):
    n = len(A)
    M = [[F(x) for x in row] + [F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if M[i][j]), None)
        if pivot is None:
            raise ArithmeticError('singular Gram matrix')
        M[j],M[pivot]=M[pivot],M[j]
        v = M[j][j]
        M[j] = [x/v for x in M[j]]
        for i in range(n):
            if i != j:
                v=M[i][j]
                if v:
                    M[i]=[a-v*b for a,b in zip(M[i],M[j])]
    return [row[n:] for row in M]


def independent_columns(A):
    # exact elimination, preserving original columns
    m, n = len(A), len(A[0])
    B=[[F(a) for a in row] for row in A]
    pivot_columns=[]
    i=0
    for j in range(n):
        p=next((k for k in range(i,m) if B[k][j]),None)
        if p is None:
            continue
        B[i],B[p]=B[p],B[i]
        fac=B[i][j]
        B[i]=[x/fac for x in B[i]]
        for k in range(m):
            if k!=i:
                fac=B[k][j]
                if fac:
                    B[k]=[a-fac*b for a,b in zip(B[k],B[i])]
        pivot_columns.append(j)
        i += 1
        if i==m:
            break
    return pivot_columns


def laplacian(m,n,t):
    N=m+n
    L=[[F(0) for _ in range(N)] for _ in range(N)]
    def edge(a,b,w):
        L[a][a]+=w;L[b][b]+=w
        L[a][b]-=w;L[b][a]-=w
    for a in range(m):
        for b in range(a+1,m):
            edge(a,b,F(1))
    for a in range(m,N):
        for b in range(a+1,N):
            edge(a,b,F(1))
    edge(0,m,t)  # bridge endpoints; trap is vertex 1
    return L


def capture(m,n,t):
    L=laplacian(m,n,t);N=m+n
    C=[[F(int(i==1))] for i in range(N)]
    for _ in range(N-1):
        out = [sum(L[i][j]*C[j][-1] for j in range(N)) for i in range(N)]
        for i,v in enumerate(out):C[i].append(v)
    cols=independent_columns(C)
    R=[[row[j] for j in cols] for row in C]
    G=mul(transpose(R),R)
    P=mul(mul(R,inverse(G)),transpose(R))
    return len(cols),[P[i][i] for i in range(N)]


def expected(m,n):
    d=[F(0)]*(m+n)
    d[1]=F(1)
    if m!=n:
        for i in range(2,m):d[i]=F(1,m-2)
        d[0]=d[m]=F(1)
        for i in range(m+1,m+n):d[i]=F(1,n-1)
        return 5,d
    q=F(2)+F(1,m-2)+F(1,m-1)
    for i in range(2,m):d[i]=F(1,m-2)-F(1,(m-2)**2)/q
    d[0]=d[m]=F(1)-F(1)/q
    for i in range(m+1,m+n):d[i]=F(1,m-1)-F(1,(m-1)**2)/q
    return 4,d


def run():
    count=0
    for m in range(3,8):
        for n in range(3,8):
            for t in (F(1,3), F(1), F(2), F(7,2)):
                actual=capture(m,n,t)
                target=expected(m,n)
                assert actual==target, (m,n,t,actual,target)
                count+=1
    print(f'PASS: {count} independent exact-rational full-graph cases; ranks and all site capture probabilities agree.')
    for m,n in [(3,3),(3,4),(4,4),(4,5),(6,6),(6,7)]:
        r,p=capture(m,n,F(1))
        print('m,n =',m,n,'rank =',r,'bridge efficiencies =',p[0],p[m])

if __name__=='__main__':
    run()
