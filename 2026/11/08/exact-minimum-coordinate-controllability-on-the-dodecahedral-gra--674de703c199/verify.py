#!/usr/bin/env python3
"""Exact finite certificate for minimum coordinate control on the dodecahedral graph.

Run: python3 verify_dodecahedron.py
Only Python's standard library is required. Vertex indexing is explained in RESULT.md.
"""
from itertools import combinations

N=20
EDGE_SET=set()
for i in range(10):
    for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        EDGE_SET.add(tuple(sorted((a,b))))
assert len(EDGE_SET)==30
A=[[0]*N for _ in range(N)]
for u,v in EDGE_SET:A[u][v]=A[v][u]=1

def dotmat(X,Y):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*Y)] for row in X]

def matvec(X,v):return [sum(x*y for x,y in zip(row,v)) for row in X]

def quotient(v):return v%5+5*(v>=10)

def representative(q):return q if q<5 else q+5

def rank_mod(mat,p):
    a=[[int(v)%p for v in row] for row in mat]
    m,n=len(a),len(a[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p)
        for i in range(r+1,m):
            if a[i][j]:
                z=a[i][j]*inv%p
                for k in range(j,n):a[i][k]=(a[i][k]-z*a[r][k])%p
        r+=1
        if r==m:break
    return r

# Five linearly independent adjacency-eigenvectors for eigenvalue 1.
B1=[]
for j in range(5):
    v=[]
    for k in range(N):
        idx=k%5
        if k<10:
            v.append(int(idx==j)-int((idx+2)%5==j)-int((idx+3)%5==j))
        else:v.append(int(idx==j))
    assert matvec(A,v)==v
    B1.append(v)
assert rank_mod([[v[i] for v in B1] for i in range(N)],11)==5

# The antipodal involution is a polynomial in A, hence scalar on every eigenspace.
I=[[int(i==j) for j in range(N)] for i in range(N)]
P=[I,A]
for _ in range(2,6):P.append(dotmat(P[-1],A))
for i in range(N):
    for j in range(N):
        lhs=P[5][i][j]-2*P[4][i][j]-7*P[3][i][j]+10*P[2][i][j]+10*P[1][i][j]-6*P[0][i][j]
        tau_j=j+5 if j<10 and j%10<5 else j-5 if j<10 else j+5 if j%10<5 else j-5
        assert lhs==6*int(i==tau_j)

rho=tuple((i+1)%10 if i<10 else 10+(i-10+1)%10 for i in range(N))
sigma=tuple((-i)%10 if i<10 else 10+(-(i-10))%10 for i in range(N))
g=(10,0,1,11,13,15,5,6,16,18,12,9,2,19,3,17,4,7,14,8)
generators=(rho,sigma,g)
for p in generators:
    assert len(set(p))==N
    assert {tuple(sorted((p[u],p[v]))) for u,v in EDGE_SET}==EDGE_SET

def closure(gens):
    id_=tuple(range(len(gens[0])));seen={id_};queue=[id_]
    for h in queue:
        for k in gens:
            z=tuple(h[k[i]] for i in range(len(h)))
            if z not in seen:seen.add(z);queue.append(z)
    return seen
G=closure(generators)
assert len(G)==120
Q={tuple(quotient(h[representative(i)]) for i in range(10)) for h in G}
assert len(Q)==60

# The quotient graph is GP(5,2), the Petersen graph.
E_Q=set()
for i in range(5):
    for u,v in ((i,(i+1)%5),(i,i+5),(i+5,5+(i+2)%5)):
        E_Q.add(tuple(sorted((u,v))))
assert len(E_Q)==15
assert E_Q=={tuple(sorted((quotient(u),quotient(v)))) for u,v in EDGE_SET}

def induced_type(S):
    deg={i:0 for i in S}
    for u,v in E_Q:
        if u in deg and v in deg:deg[u]+=1;deg[v]+=1
    signature=tuple(sorted(deg.values()))
    return {
        (2,2,2,2,2):'C5',
        (1,1,2,2,2):'P5',
        (0,1,1,2,2):'P4+K1',
        (1,1,1,2,3):'T-shaped tree',
        (0,0,1,1,2):'P3+2K1',
        (0,1,1,1,1):'2K2+K1'
    }[signature]

# Three exact obstruction vectors, each killed by the displayed five inputs.
OBSTRUCTIONS={
    (0,1,2,3,6):(1,[0,0,0,0,1,0,0,0,0,1,-1,0,0,-1,1,-1,0,0,-1,1]),
    (0,1,2,8,9):(1,[0,0,0,-1,-1,0,0,0,-1,-1,1,0,1,0,0,1,0,1,0,0]),
    (0,1,3,7,8):(0,[0,0,1,0,-1,0,0,-1,0,1,-1,-1,0,0,0,1,1,0,0,0])
}

def krylov_rank_mod(S,p):
    columns=[]
    for v in S:
        x=[int(i==v) for i in range(N)]
        for _ in range(N):
            columns.append(x)
            x=matvec(A,x)
    return rank_mod([[col[i] for col in columns] for i in range(N)],p)

all_subsets=set(combinations(range(10),5));orbits=[]
while all_subsets:
    rep=min(all_subsets)
    orbit={tuple(sorted(h[i] for i in rep)) for h in Q}
    assert orbit<=all_subsets
    all_subsets-=orbit
    S=[representative(i) for i in rep]
    kind=induced_type(rep)
    good=kind in ('C5','P5','P4+K1')
    if good:
        # A nonzero rank-20 minor modulo 11 proves rank 20 over Q.
        assert krylov_rank_mod(S,11)==20
    else:
        eigenvalue,witness=OBSTRUCTIONS[rep]
        assert any(witness) and matvec(A,witness)==[eigenvalue*x for x in witness]
        assert all(witness[i]==0 for i in S)
    orbits.append((rep,len(orbit),kind,good))

assert len(orbits)==8
assert [o[1] for o in orbits]==[6,60,60,30,6,30,30,30]
assert sum(sz for _,sz,_,good in orbits if good)==132
assert sum(sz for _,sz,_,good in orbits if not good)==120
assert sum(sz for _,sz,_,good in orbits if good)*2**5==4224

# Independent secondary check over all 252 quotient patterns via PBH in F_11.
def kernel_mod(mat,p):
    M=[[x%p for x in row] for row in mat];nrow=len(M);ncol=len(M[0]);r=0;piv=[]
    for j in range(ncol):
        h=next((i for i in range(r,nrow) if M[i][j]),None)
        if h is None:continue
        M[r],M[h]=M[h],M[r]
        inv=pow(M[r][j],-1,p)
        M[r]=[v*inv%p for v in M[r]]
        for i in range(nrow):
            if i!=r and M[i][j]:
                z=M[i][j]
                M[i]=[(u-z*v)%p for u,v in zip(M[i],M[r])]
        piv.append(j);r+=1
        if r==nrow:break
    free=[j for j in range(ncol) if j not in piv]
    vectors=[]
    for j in free:
        x=[0]*ncol;x[j]=1
        for i,k in enumerate(piv):x[k]=-M[i][j]%p
        vectors.append(x)
    return vectors
bases={e:kernel_mod([[A[i][j]-(e if i==j else 0) for j in range(N)] for i in range(N)],11) for e in (3,1,0,9,4,7)}
assert {e:len(b) for e,b in bases.items()}=={3:1,1:5,0:4,9:4,4:3,7:3}
count=0;counts={}
for T in combinations(range(10),5):
    S=[representative(i) for i in T]
    passes=all(rank_mod([[v[i] for v in basis] for i in S],11)==len(basis) for basis in bases.values())
    assert passes==(induced_type(T) in ('C5','P5','P4+K1'))
    count+=passes
    counts[induced_type(T)]=counts.get(induced_type(T),0)+1
assert count==132
assert counts=={'C5':12,'P5':60,'T-shaped tree':60,'P4+K1':60,'P3+2K1':30,'2K2+K1':30},counts
for rep,size,kind,good in orbits:print('ORBIT',rep,size,kind,'PASS' if good else 'FAIL')
print('PBH_FINITE_FIELD_ALL_252_OK','ORBIT_CERTIFIED_8','MINIMUM_LEADERS_5','OPTIMAL_SETS_4224')
