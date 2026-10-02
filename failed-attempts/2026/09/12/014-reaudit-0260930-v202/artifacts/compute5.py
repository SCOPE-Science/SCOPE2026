from fractions import Fraction

def matmul(A,B):
    n,m,p=len(A),len(B),len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def eye(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def meq(A,B):
    return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def matpow(A,e):
    n=len(A); R=eye(n); B=[r[:] for r in A]
    while e:
        if e&1: R=matmul(R,B)
        B=matmul(B,B); e>>=1
    return R
def transp(A):
    return [list(r) for r in zip(*A)]

# Standard E6 root lattice: use Cartan C and simple reflections on root space with
# pairing <a_i, a_j> = C_ij. Simple reflection: s_i(x) = x - <x, a_i^v> a_i where
# for simply-laced, s_i matrix in simple-root basis: (s_i)_{j,k} = delta_{jk} - C_{ij} delta_{ik}?
# Column k = coordinates of s_i(a_k) = a_k - C_{ik} a_i. So S_i[j][k] = delta_{jk} - C[i][k]*delta_{j,i}.
C = [[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
def s_ref(i):
    S=eye(6)
    for k in range(6):
        for j in range(6):
            S[j][k]-= (C[i][k] if j==i else 0)
    return S
for i in range(6):
    S=s_ref(i)
    print(i,"invol:",meq(matmul(S,S),eye(6)))
# Coxeter element: product s0..s5. Try orderings.
import itertools
def order_of(A,lim=40):
    P=[r[:] for r in A]
    for k in range(1,lim+1):
        if meq(P,eye(len(A))): return k
        P=matmul(P,A)
    return None
def bdet(M):
    n=len(M); A=[[Fraction(x) for x in row] for row in M]; prev=Fraction(1)
    for k in range(n-1):
        piv=k
        while piv<n and A[piv][k]==0: piv+=1
        if piv==n: return Fraction(0)
        if piv!=k: A[k],A[piv]=A[piv],A[k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])/prev
            A[i][k]=Fraction(0)
        prev=A[k][k]
        if prev==0: return Fraction(0)
    return A[n-1][n-1]
def charpoly_coeffs(A):
    n=len(A)
    vals=[]
    for t in range(n+1):
        M=[[(t if i==j else 0)-A[i][j] for j in range(n)] for i in range(n)]
        vals.append(bdet(M))
    V=[[Fraction(i**j) for j in range(n+1)] for i in range(n+1)]
    Aug=[row[:]+[vals[i]] for i,row in enumerate(V)]
    for col in range(n+1):
        piv=col
        while Aug[piv][col]==0: piv+=1
        Aug[col],Aug[piv]=Aug[piv],Aug[col]
        d=Aug[col][col]
        Aug[col]=[v/d for v in Aug[col]]
        for i in range(n+1):
            if i!=col and Aug[i][col]!=0:
                t=Aug[i][col]
                Aug[i]=[a-t*b for a,b in zip(Aug[i],Aug[col])]
    sol=[Aug[i][n+1] for i in range(n+1)]  # x^0..x^n
    return list(reversed(sol))  # x^n..x^0
S=[s_ref(i) for i in range(6)]
cox=eye(6)
for i in [0,1,2,3,4,5]: cox=matmul(S[i],cox)
print("cox:")
for r in cox: print(r)
print("order:",order_of(cox))
print("charpoly:",[str(c) for c in charpoly_coeffs(cox)])
# standard Coxeter order for bipartite ordering
cox2=matmul(matmul(matmul(S[0],S[1]),S[5]),matmul(matmul(S[2],S[4]),S[3]))
print("bipartite order:",order_of(cox2))
print("bipartite charpoly:",[str(c) for c in charpoly_coeffs(cox2)])
