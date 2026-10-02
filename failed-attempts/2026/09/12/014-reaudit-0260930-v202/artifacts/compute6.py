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
    n=len(A); vals=[]
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
    return list(reversed([Aug[i][n+1] for i in range(n+1)]))

# Candidate E6-positive pairing on Q: identify q_i with simple roots, pairing matrix P with P_ii=2.
# Our G11 has -2 diagonal (negative-definite). Standard positive Cartan is C. So compare -G11 vs C.
C = [[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
G11=[[-C[i][j] for j in range(6)] for i in range(6)]
print("G11 == -C:", G11==[[-C[i][j] for j in range(6)] for i in range(6)])
# Roots: r0,r1 combinations. e6,e7 classes:
# [e6] = -(e0+2e1+2e2+3e3+2e4+e5), [e7] = (e0+e1+2e2+3e3+2e4+e5).
# Pairing matrix of full G restricted: verify -G11 positive E6 Cartan (det 3).
print("det(-G11)=", bdet([[-x for x in row] for row in G11]))
# The quotient Q with basis [e0..e5] has Gram G11 (negative E6). Reflections s_i on Q:
# s_i(q) = q - <q,e_i> e_i (since <e_i,e_i>=-2: q - 2<q,e_i>/<e_i,e_i> e_i = q + ... wait:
# standard: s_e(x) = x - 2<x,e>/<e,e> e = x + <x,e> e (as <e,e>=-2). Column: S[j][k] = delta + G11[j][i]*delta_{k,i}? No:
# s_i(e_k) = e_k + G11[i][k] e_i. So matrix S_i[j][k] = delta_{jk} + delta_{j,i} G11[i][k].
def sq_ref(i):
    S=eye(6)
    for k in range(6):
        S[i][k]+=G11[i][k]
    return S
Sq=[sq_ref(i) for i in range(6)]
cox=eye(6)
for i in [0,1,2,3,4,5]: cox=matmul(Sq[i],cox)
print("cox via Q-pairing:")
for r in cox: print(r)
print("charpoly:",[str(c) for c in charpoly_coeffs(cox)])
P=eye(6)
for k in range(1,25):
    P=matmul(P,cox)
    if meq(P,eye(6)):
        print("order:",k); break
# Compare with S from Cartan formula: S[j][k] = delta - C[i][k] delta_{j,i}.
def s_ref(i):
    S=eye(6)
    for k in range(6):
        S[i][k]-=C[i][k]
    return S
S2=[s_ref(i) for i in range(6)]
print("Sq==S2:",[meq(a,b) for a,b in zip(Sq,S2)])
cox2=eye(6)
for i in [0,1,2,3,4,5]: cox2=matmul(S2[i],cox2)
print("equal cox:",meq(cox,cox2))
# So the correct charpoly is x^6+x^5-x^3+x+1?? verify: coeffs x^6..x^0 = 1,1,0,-1,0,1,1.
# Factor: (x^2+1)(x^4+x^3-x+1)? check: (x^2+1)(x^4+x^3-x+1) = x^6+x^5-x^3+x^4+x^3-x+... let me not.
# Check roots are primitive 12th roots with exponents 1,4,5,7,8,11: minimal polys: Phi12=x^4-x^2+1 (exponents 1,5,7,11), Phi6=x^2-x+1? exponents for order 6: 1,5 -> but exponent 4,8 have order 3: Phi3=x^2+x+1. So E6 poly = Phi12*Phi3 = (x^4-x^2+1)(x^2+x+1) = x^6+x^5-x^3+x+1? expand: x^6+x^5+x^2... compute:
p12=[1,0,-1,0,1]; p3=[1,1,1]
res=[0]*7
for i,a in enumerate(p12):
    for j,b in enumerate(p3):
        res[i+j]+=a*b
print("Phi12*Phi3 =",res)  # highest-first x^6..x^0
