"""Exact edge-spin covariance for the octahedral ice model.
Standard Python 3 only. The check exhausts all 4096 edge orientations.
"""
from fractions import Fraction as Q

N=6
E=[(a,b) for a in range(N) for b in range(a+1,N) if a//2 != b//2]
M=len(E)
assert M==12

def expected():
    # Canonical cycle vector, directed A -> B -> C -> A.
    v=[1 if (a//2,b//2) in ((0,1),(1,2)) else -1 for a,b in E]
    assert v==[1,1,-1,-1,1,1,-1,-1,1,1,1,1]
    B=[[int(a==r)-int(b==r) for a,b in E] for r in range(N)]
    D=[[Q(0) for _ in range(N)] for _ in range(N)]
    H=[[Q(0) for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if a//2 == b//2:
                D[a][b]=Q(1 if a==b else -1,2)
                H[a][b]=Q(1,2)
    # Laplacian spectrum 0,4 (within-pair),6 (between pairs).
    Lplus=[[(D[a][b]/4)+(H[a][b]-Q(1,6))/6 for b in range(N)] for a in range(N)]
    P=[[Q(int(i==j)) - sum(Q(B[a][i])*Lplus[a][b]*B[b][j] for a in range(N) for b in range(N)) for j in range(M)] for i in range(M)]
    C=[[Q(32,19)*P[i][j]+Q(v[i]*v[j],57) for j in range(M)] for i in range(M)]
    return v,B,P,C
v,B,P,C=expected()
assert all(sum(B[a][i]*v[i] for i in range(M))==0 for a in range(N))
assert all(sum(P[i][k]*P[k][j] for k in range(M))==P[i][j] for i in range(M) for j in range(M))
count=0
moment=[[0]*M for _ in range(M)]
for bits in range(1<<M):
    spins=[1-2*((bits>>i)&1) for i in range(M)]
    if any(sum(B[r][i]*spins[i] for i in range(M))!=0 for r in range(N)):
        continue
    count+=1
    for i in range(M):
        for j in range(M):moment[i][j]+=spins[i]*spins[j]
assert count==38, count
assert all(Q(moment[i][j],count)==C[i][j] for i in range(M) for j in range(M))
assert sorted({C[i][j] for i in range(M) for j in range(M)}) == [Q(-7,19),Q(-5,19),Q(-1,19),Q(1,19),Q(3,19),Q(7,19),Q(1)]
print('DIRECT PASS: 4096 orientations, 38 balanced, 144 exact covariance identities, projectors and v.')
print('Eigenvalues: 0 x 5; 32/19 x 6; 36/19 x 1. Frame condition sqrt(9/8).')

# The only smaller connected simple 4-regular graph is K5. Its frame
# is tight, providing a sharp six-vertex onset of anisotropy.
E5=[(a,b) for a in range(5) for b in range(a+1,5)]
B5=[[int(a==r)-int(b==r) for a,b in E5] for r in range(5)]
T5=[[0]*len(E5) for _ in E5]
z5=0
for bits in range(1<<len(E5)):
    x=[1-2*((bits>>i)&1) for i in range(len(E5))]
    if any(sum(B5[r][i]*x[i] for i in range(len(E5)))!=0 for r in range(5)):
        continue
    z5+=1
    for i in range(len(E5)):
        for j in range(len(E5)):
            T5[i][j]+=x[i]*x[j]
assert z5==24
for i in range(len(E5)):
    for j in range(len(E5)):
        Pc=Q(int(i==j)) - Q(sum(B5[r][i]*B5[r][j] for r in range(5)),5)
        assert Q(T5[i][j],z5)==Q(5,3)*Pc
print('BASELINE PASS: K5, 24 balanced orientations, tight 6-dimensional cycle frame.')
