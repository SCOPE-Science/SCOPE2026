"""Exact finite matrix checks underlying the Rule 110 cyclic indegree theorem.

Run: python3 verify_certificate.py
Uses only the Python standard library. All integer calculations are exact.
"""

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def power(A, n):
    r=eye(len(A))
    for _ in range(n):
        r=mul(r,A)
    return r

def make_matrices():
    m=[[[0]*4 for _ in range(4)] for _ in range(2)]
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                out=(110>>(4*a+2*b+c))&1
                m[out][2*a+b][2*b+c]=1
    return m

M0,M1=make_matrices()
assert M0==[[1,0,0,0],[0,0,0,0],[1,0,0,0],[0,0,0,1]]
assert M1==[[0,1,0,0],[0,0,1,1],[0,1,0,0],[0,0,1,0]]

# State after zero is either 00 or 11.
H=[eye(2),[[0,0],[1,0]],[[1,1],[0,0]]]
for k in range(3,121):
    H.append(add(H[k-2],H[k-3]))
for k in range(1,61):
    X=power(M1,k)
    direct=[[X[0][2],X[0][3]],[X[3][2],X[3][3]]]
    assert H[k]==direct, (k,H[k],direct)
assert all(H[k+3]==add(H[k+1],H[k]) for k in range(118))

# Finite bases, together with the bivariate recurrence for the difference
# D(a,b), imply entrywise H[a]H[b] <= H[a+b+1] for a,b>=1
# except the pair (1,2). The recurrence in each argument is
# D(a+3,b)=D(a+1,b)+D(a,b), and symmetrically for b.
base=( [(a,b) for a in (4,5,6) for b in (0,1,2)]
      +[(a,b) for a in (2,3) for b in (1,2,3)]
      +[(1,b) for b in (1,3,4,5)] )
assert len(base)==19
for a,b in base:
    D=sub(H[a+b+1],mul(H[a],H[b]))
    assert min(min(row) for row in D)>=0, (a,b,D)
D12=sub(H[4],mul(H[1],H[2]))
assert D12==[[1,1],[0,-1]]
# Extra numerical checks are not used as an infinite proof.
for a in range(1,53):
    for b in range(1,53):
        D=sub(H[a+b+1],mul(H[a],H[b]))
        assert min(min(row) for row in D)>=0 or (a,b)==(1,2), (a,b,D)

P=[3,0,2]
for k in range(3,122):
    P.append(P[k-2]+P[k-3])
for k in range(1,60):
    assert tr(power(M1,k))==P[k]
for k in range(1,110):
    assert tr(H[k])<=P[k+1]
    if k!=3: assert tr(H[k])<P[k+1]

# Check arbitrary output matrices and zero-run factorization independently.
def from_matrices(bits):
    T=eye(4)
    for bit in bits:
        T=mul(T, M1 if bit else M0)
    return tr(T)

def from_zero_runs(bits):
    z=[i for i,b in enumerate(bits) if b==0]
    if not z: return P[len(bits)]
    T=eye(2)
    for i,a in enumerate(z):
        b=z[(i+1)%len(z)]
        gap=(b-a-1)%len(bits)
        if len(z)==1: gap=len(bits)-1
        T=mul(T,H[gap])
    return tr(T)
for n in range(1,12):
    for code in range(1<<n):
        bits=[(code>>i)&1 for i in range(n)]
        assert from_matrices(bits)==from_zero_runs(bits), (n,code)
        if n>=5:
            d=from_zero_runs(bits)
            assert (d==P[n])==(code==(1<<n)-1), (n,code,d,P[n])

print('CERTIFICATE_OK: matrices, 19 finite bases, recurrences, zero-run reduction, Perrin bound')
