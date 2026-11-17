#!/usr/bin/env python3
"""Exact cyclotomic determinant and matrix-polynomial certificate for 75 Fermat quintic lines.
Uses only Python standard library. No finite-field approximation or floating arithmetic.
"""
from itertools import permutations, product
from collections import deque

PAIRS = (((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2)))
PERMS = []
for p in permutations(range(4)):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    PERMS.append((p,(-1)**inv))

# A vector entry is either zero (None), the constant 1, or -zeta^e
# where zeta is a primitive fifth root of unity.
def make_line(family,a,b):
    C=[[None]*2 for _ in range(4)]
    for col, ((i,j),exp) in enumerate(zip(PAIRS[family],(a,b))):
        C[i][col]=(-1,exp)
        C[j][col]=(1,0)
    return C

def intersects(L,M):
    # Expand determinant in Z[zeta]; a 5-component polynomial vanishes
    # modulo Phi_5(zeta)=1+zeta+...+zeta^4 iff all coefficients equal.
    columns=[(L[i][0],L[i][1],M[i][0],M[i][1]) for i in range(4)]
    det=[0]*5
    for p,sgn in PERMS:
        terms=[columns[i][p[i]] for i in range(4)]
        if any(c is None for c in terms):continue
        coef=sgn;exp=0
        for c,e in terms:
            coef*=c;exp+=e
        det[exp%5]+=coef
    return len(set(det))==1

def multiply(A,B):
    n=len(A)
    Bcols=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col)) for col in Bcols] for row in A]

def shift(A,z):
    return [[v+(z if i==j else 0) for j,v in enumerate(row)] for i,row in enumerate(A)]

LINES=[(f,a,b,make_line(f,a,b)) for f in range(3) for a,b in product(range(5),repeat=2)]
N=len(LINES)
assert N==75
A=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i):
        A[i][j]=A[j][i]=int(intersects(LINES[i][3],LINES[j][3]))
assert set(map(sum,A))=={18}
# Connectedness proves the regular eigenvalue has multiplicity one.
reach={0}; queue=deque([0])
while queue:
    i=queue.popleft()
    for j in range(N):
        if A[i][j] and j not in reach:
            reach.add(j);queue.append(j)
assert len(reach)==N
# Exact annihilating polynomial: (A-18I)(A-3I)(A+2I)(A+7I)=0
prod=multiply(multiply(multiply(shift(A,-18),shift(A,-3)),shift(A,2)),shift(A,7))
assert all(x==0 for row in prod for x in row)
assert sum(A[i][i] for i in range(N))==0
assert sum(A[i][j]*A[j][i] for i in range(N) for j in range(N))==1350
# The only possible eigenvalues are four distinct real roots of the
# annihilating polynomial. Connected 18-regular graph: m18=1.
# Solve: m3+m(-2)+m(-7)=74; 3m3-2m2-7m7=-18;
# 9m3+4m2+49m7=1026. All integer solutions => (38,24,12).
assert 38+24+12==74
assert 3*38-2*24-7*12==-18
assert 9*38+4*24+49*12==1026
# Smooth degree-five surface: each line has self-intersection 2-5=-3.
# Hence Gram=A-3I: eigenvalues 15^1,0^38,(-5)^24,(-10)^12.
print('VERIFY_FERMAT_QUINTIC_LINE_SPECTRUM_OK lines=75 degree=18 connected=1 eigen=18:1,3:38,-2:24,-7:12 Gram_rank=37')
