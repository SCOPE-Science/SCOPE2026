"""Exact finite census for edge-detuned Petersen Laplacian control.
Run with Python 3 standard library: python3 checker.py.
The parameter-universal inference is proved in RESULT.md, not inferred from sampling.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter

N = 10
EDGES = sorted({tuple(sorted((i,(i+1)%5))) for i in range(5)} |
               {(i,5+i) for i in range(5)} |
               {tuple(sorted((5+i,5+(i+2)%5))) for i in range(5)})
assert len(EDGES)==15 and (0,1) in EDGES

def lap(t):
    M = [[Q(0) for _ in range(N)] for _ in range(N)]
    for i,j in EDGES:
        w = Q(t) if (i,j)==(0,1) else Q(1)
        M[i][i]+=w; M[j][j]+=w;M[i][j]-=w;M[j][i]-=w
    return M

def rank(A):
    if not A:return 0
    B = [[Q(x) for x in row] for row in A]
    nr=len(B); nc=len(B[0]);r=0
    for c in range(nc):
        pivot=next((i for i in range(r,nr) if B[i][c]),None)
        if pivot is None:continue
        B[r],B[pivot]=B[pivot],B[r]
        v=B[r][c]
        B[r]=[x/v for x in B[r]]
        for i in range(r+1,nr):
            if B[i][c]:
                a=B[i][c];B[i]=[B[i][j]-a*B[r][j] for j in range(nc)]
        r+=1
        if r==nr:break
    return r

def nullspace(A):
    B=[[Q(x) for x in row] for row in A]
    nr=len(B);nc=len(B[0]); piv=[]; r=0
    for c in range(nc):
        i=next((i for i in range(r,nr) if B[i][c]),None)
        if i is None:continue
        B[r],B[i]=B[i],B[r]
        v=B[r][c];B[r]=[x/v for x in B[r]]
        for j in range(nr):
            if j!=r and B[j][c]:
                a=B[j][c];B[j]=[B[j][k]-a*B[r][k] for k in range(nc)]
        piv.append(c);r+=1
    free=[c for c in range(nc) if c not in piv]
    V=[]
    for f in free:
        v=[Q(0)]*nc;v[f]=Q(1)
        for i,c in enumerate(piv):v[c]=-B[i][f]
        V.append(v)
    return V

def rows(B,S):
    return [[v[i] for v in B] for i in S]

L=lap(1)
P2=[[sum(L[i][k]*(5*(k==j)-L[k][j]) for k in range(N))/6 for j in range(N)] for i in range(N)]
P5=[[sum(L[i][k]*(L[k][j]-2*(k==j)) for k in range(N))/15 for j in range(N)] for i in range(N)]
b=[Q(1),Q(-1)]+[Q(0)]*8
u=[sum(P2[i][j]*b[j] for j in range(N)) for i in range(N)]
v=[sum(P5[i][j]*b[j] for j in range(N)) for i in range(N)]
assert sum(x*x for x in u)==Q(2,3)
assert sum(x*x for x in v)==Q(4,3)
assert [i for i in range(N) if u[i] or v[i]]==[0,1,2,4,5,6]
assert all(u[i]+v[i]==b[i] for i in range(N))

E2=nullspace([[L[i][j]-2*(i==j) for j in range(N)] for i in range(N)])
E5=nullspace([[L[i][j]-5*(i==j) for j in range(N)] for i in range(N)])
U2=nullspace([[L[i][j]-2*(i==j) for j in range(N)] for i in range(N)]+[b])
U5=nullspace([[L[i][j]-5*(i==j) for j in range(N)] for i in range(N)]+[b])
assert [len(V) for V in (E2,E5,U2,U5)]==[5,4,4,3]

C_det=Counter();C_orig=Counter();K=Counter();matrix_cert=Counter();
for m in range(N+1):
    for S in combinations(range(N),m):
        d2=rank(rows(U2,S));d5=rank(rows(U5,S))
        e2=rank(rows(E2,S));e5=rank(rows(E5,S))
        d_uv=rank(rows([u,v],S))
        if d2==4:assert d5==3
        good=(d2==4 and d5==3 and d_uv>=1)
        old=(e2==5 and e5==4)
        C_det[m]+=int(good);C_orig[m]+=int(old)
        if d2==4 and d_uv==1:
            U=[u[i] for i in S];V=[v[i] for i in S]
            assert any(U)
            k=next(V[i]/U[i] for i in range(len(S)) if U[i])
            assert all(V[i]==k*U[i] for i in range(len(S)))
            assert k in (Q(-1),Q(2))
            K[(m,str(k))]+=1
        if m==4:matrix_cert[(d2,d5,d_uv)]+=1

assert [C_det[k] for k in range(11)]==[0,0,0,0,104,210,203,120,45,10,1]
assert [C_orig[k] for k in range(11)]==[0,0,0,0,0,162,195,120,45,10,1]
assert matrix_cert[(4,3,0)]==1
assert sum(v for (a,b,c),v in matrix_cert.items() if a==4)==105

# Independent finite check: Kalman rank mod a prime, at several detunings.
PRIME=1000003

def mod_rank(A,p=PRIME):
    if not A:return 0
    B=[row[:] for row in A]; nr=len(B);nc=len(B[0]);r=0
    for c in range(nc):
        i=next((i for i in range(r,nr) if B[i][c]%p),None)
        if i is None:continue
        B[r],B[i]=B[i],B[r]
        z=pow(B[r][c]%p,-1,p)
        for j in range(c,nc):B[r][j]=(B[r][j]*z)%p
        for i in range(r+1,nr):
            if B[i][c]:
                z=B[i][c]
                for j in range(c,nc):B[i][j]=(B[i][j]-z*B[r][j])%p
        r+=1
        if r==nr:break
    return r

def kalman_mod(L,S,p=PRIME):
    B=[[int(i==j) for j in S] for i in range(N)]
    Z=[row[:] for row in B]
    for k in range(1,N):
        B=[[sum(L[i][h]*B[h][j] for h in range(N))%p for j in range(len(S))] for i in range(N)]
        for i in range(N):Z[i].extend(B[i])
    return mod_rank(Z,p)

for t in (Q(1),Q(1,2),Q(2),Q(3)):
    Lt=lap(t); Lmod=[[int(a.numerator*pow(a.denominator,-1,PRIME)%PRIME) for a in row] for row in Lt]
    m=5 if t==1 else 4
    num=0
    for S in combinations(range(N),m):
        actual=kalman_mod(Lmod,S)==N
        expected=(rank(rows(E2,S))==5 and rank(rows(E5,S))==4) if t==1 else (rank(rows(U2,S))==4 and bool(set(S)&{0,1,2,4,5,6}))
        assert actual==expected,(t,S,actual,expected)
        num+=1
    print(f'Kalman modular truth table at t={t}: {num} sets OK')

print('Detuned controllable-set counts:', dict(sorted(C_det.items())))
print('Unweighted controllable-set counts:',dict(sorted(C_orig.items())))
print('Minimum-set rank patterns:',dict(sorted(matrix_cert.items())))
print('Rank-one restriction patterns:',dict(sorted(K.items())))
print('VERIFY_OK')
