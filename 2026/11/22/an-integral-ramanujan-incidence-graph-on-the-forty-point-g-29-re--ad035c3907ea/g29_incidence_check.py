"""Exact, dependency-free certificate for the G29 point--Klein-line spectrum.

The 40 points and 30 lines are specified by coordinate rules in the
accompanying mathematical description. All arithmetic is over Gaussian
integers; spectral checks use only integer matrix operations.
"""
from itertools import combinations, product

ZERO = (0, 0)
ONE = (1, 0)
MINUS_ONE = (-1, 0)
I = (0, 1)
MINUS_I = (0, -1)
ROOTS = (ONE, I, MINUS_ONE, MINUS_I)

def mul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def sub(z, w):
    return (z[0]-w[0], z[1]-w[1])

points = []
for a,b in combinations(range(4), 2):
    for z in ROOTS:
        v = [ZERO]*4
        v[a] = ONE
        v[b] = z
        points.append(tuple(v))
for b,c,d in product(ROOTS, repeat=3):
    if mul(mul(b,c),d) == ONE:
        points.append((ONE,b,c,d))
assert len(points) == 40 and len(set(points)) == 40

lines = [('coordinate',ab) for ab in combinations(range(4),2)]
for ab,cd in (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))):
    for z in (ONE,I):
        for e,f in product((z,(-z[0],-z[1])),repeat=2):
            lines.append(('diagonal',ab,cd,e,f))
assert len(lines) == 30

def lies_on(p,L):
    if L[0]=='coordinate':
        a,b=L[1]
        return p[a]==ZERO and p[b]==ZERO
    _,ab,cd,e,f=L
    return sub(p[ab[0]],mul(e,p[ab[1]]))==ZERO and sub(p[cd[0]],mul(f,p[cd[1]]))==ZERO

B = [[int(lies_on(p,L)) for L in lines] for p in points]
assert all(sum(row)==3 for row in B)
assert all(sum(B[i][j] for i in range(40))==4 for j in range(30))
G = [[sum(B[i][k]*B[j][k] for k in range(30)) for j in range(40)] for i in range(40)]
assert all(G[i][i]==3 for i in range(40))
assert all(G[i][j] in (0,1) for i in range(40) for j in range(40) if i!=j)
A = [[G[i][j]-(3 if i==j else 0) for j in range(40)] for i in range(40)]
assert all(sum(row)==9 for row in A)
assert sum(A[i][j] for i in range(40) for j in range(i))==180

def mm(X,Y):
    n=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

# Since A is real symmetric, this annihilating identity confines its
# eigenvalues to the five displayed distinct integers.
Q=identity(40)
for root in (9,5,1,-1,-3):
    F=[[A[i][j]-(root if i==j else 0) for j in range(40)] for i in range(40)]
    Q=mm(Q,F)
assert all(Q[i][j]==0 for i in range(40) for j in range(40))

P=identity(40)
traces=[]
for k in range(5):
    traces.append(sum(P[i][i] for i in range(40)))
    P=mm(P,A)
assert traces == [40,0,360,960,10920],traces
roots=(9,5,1,-1,-3)
mult=(1,5,15,4,15)
assert all(sum(mult[j]*roots[j]**k for j in range(5))==traces[k] for k in range(5))
# The 5x5 Vandermonde matrix on distinct roots is invertible, so the
# multiplicities are uniquely determined by these traces.
# B B^t=A+3I has eigenvalues 12,8,4,2,0, hence rank(B)=25.
assert sum(m for r,m in zip(roots,mult) if r!=-3)==25
print('PASS: 40 points, 30 lines, 180 edges, 9-regular; exact eigenvalues and multiplicities')
print('adjacency spectrum: 9^1, 5^5, 1^15, (-1)^4, (-3)^15')
print('incidence rank: 25, rational left kernel: 15, right kernel: 5')
print('nontrivial spectral radius: 5 < 2*sqrt(8), hence Ramanujan')
