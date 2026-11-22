"""Exact arithmetic verification of a cospectral pair's reversible-wave orbit counts.
Run: python verify_wave.py (requires only Python 3 standard library).
"""

def zeros(n):
    return [[0]*n for _ in range(n)]

def friendship(triangles=16):
    n=2*triangles+1; A=zeros(n)
    for i in range(triangles):
        a,b=2*i+1,2*i+2
        for u,v in [(0,a),(0,b),(a,b)]: A[u][v]=A[v][u]=1
    return A

def exceptional():
    # Blocks J_3-I_3, J_3,5, 0; J_5,3, 0, J_5-I_5; 0, J_5-I_5, 0.
    A=zeros(33)
    for u in range(3):
        for v in range(3):
            if u!=v:A[u][v]=1
        for v in range(3,8):A[u][v]=A[v][u]=1
    for i in range(5):
        for j in range(5):
            if i!=j: A[3+i][8+j]=A[8+j][3+i]=1
    for i in range(10):
        u,v=13+2*i,14+2*i; A[u][v]=A[v][u]=1
    return A

def eye(n):
    M=zeros(n)
    for i in range(n):M[i][i]=1
    return M

def mm(A,B):
    n=len(A);C=zeros(n)
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b:C[i][j]=(C[i][j]+a*b)%3
    return C

def power(A,k):
    n=len(A);P=eye(n)
    while k:
        if k&1:P=mm(P,A)
        A=mm(A,A);k>>=1
    return P

def rank(A):
    M=[[v%3 for v in row] for row in A]
    m=len(M); n=len(M[0]);r=0
    for j in range(n):
        p=next((i for i in range(r,m) if M[i][j]!=0),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r]
        if M[r][j]==2:M[r]=[(2*v)%3 for v in M[r]]
        for i in range(r+1,m):
            t=M[i][j]
            if t:M[i]=[(a-t*b)%3 for a,b in zip(M[i],M[r])]
        r+=1
        if r==m:break
    return r

def plus(A,b):
    M=[[int(v)%3 for v in row] for row in A]
    for i in range(len(M)):M[i][i]=(M[i][i]+b)%3
    return M

def companion(A):
    n=len(A);T=zeros(2*n)
    for i in range(n):
        for j in range(n):T[i][j]=A[i][j]%3
        T[i][n+i]=2;T[n+i][i]=1
    return T

def fix_exponent(k,kind):
    s=1
    while k%3==0:k//=3;s*=3
    even=k%2==0
    if kind=='F':return min(4,s)+16*min(2,s)+ (15*min(2,s) if even else 0)
    return min(6,s)+15*min(2,s)+ (15*min(2,s) if even else 0)

for name,A in [('F',friendship()),('H',exceptional())]:
    assert len(A)==33 and all(len(row)==33 for row in A)
    print(name,'adjacency nullity sequences:')
    for eigen in [-1,1]:
        B=plus(A,-eigen); M=eye(33);null=[]
        for j in range(1,5):
            M=mm(M,B);null.append(33-rank(M))
        print(' eigen',eigen,':',null)
    T=companion(A)
    assert power(T,18)==eye(66)
    assert power(T,9)!=eye(66) and power(T,6)!=eye(66)
    found=[]
    for k in (1,2,3,6,9,18):
        exponent=66-rank(plus(power(T,k),-1))
        expected=fix_exponent(k,name)
        print(' iterate',k,'nullity(T^k-I)=',exponent,'formula=',expected)
        assert exponent==expected
        found.append(exponent)
    assert found==([17,32,35,65,36,66] if name=='F' else [16,31,33,63,36,66])
print('PASS: all assertions')
