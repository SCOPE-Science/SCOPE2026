"""Exact algebra and matrix checks for RK4 positivity on strongly regular graphs.

Run: python3 verification.py (Python standard library only).
Finite graph checks complement, but do not replace, the general polynomial proof.
"""
from fractions import Fraction
from itertools import combinations

# Multivariate integer polynomials in k, lam, mu, represented by monomial dictionaries.
def const(x): return {(0, 0, 0): x} if x else {}
def var(j): return {tuple(int(i == j) for i in range(3)): 1}
def add(a, b):
    c = dict(a)
    for u, v in b.items():
        c[u] = c.get(u, 0) + v
        if c[u] == 0: del c[u]
    return c
def neg(a): return {u: -v for u, v in a.items()}
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    c = {}
    for u, x in a.items():
        for v, y in b.items():
            w = tuple(u[i] + v[i] for i in range(3))
            c[w] = c.get(w, 0) + x*y
            if c[w] == 0: del c[w]
    return c
def pow2(x): return mul(x, x)
def sc(x, c): return mul(x, const(c))
K, LA, MU = var(0), var(1), var(2)
p = sub(sub(K, LA), const(1))
q = sub(K, MU)
a = sub(sc(K, 2), LA)
b = mul(p, q)
s = add(sub(K, LA), MU)
C = add(add(sc(mul(K, s), 3), pow2(sub(K, s))), q)

# Independently derive all powers in the adjacency algebra L^j=u I+v A+w J.
u, v, w = K, const(-1), const(0)
polys = []
for j in range(1, 5):
    polys.append((add(u, w), add(v, w), w))
    u, v, w = (sub(mul(K, u), mul(sub(K, MU), v)),
               add(neg(u), mul(s, v)),
               neg(mul(MU, v)))
assert polys[0][1] == const(-1)
assert polys[1][1] == neg(a)
assert polys[1][2] == MU
assert polys[2][1] == neg(sub(pow2(a), b))
assert polys[2][2] == mul(MU, add(K, s))
assert polys[3][1] == neg(sub(mul(pow2(a), a), mul(b, add(sc(a, 2), MU))))
assert polys[3][2] == mul(MU, C)
# Certify strict negativity of the non-neighbor quadratic discriminant.
assert sub(sub(pow2(add(K, s)), sc(C, 3)),
           neg(add(add(sc(pow2(K), 2), mul(K, s)),
                   add(sc(pow2(s), 2), sc(q, 3))))) == {}
print('VERIFY: universal adjacency-algebra and discriminant identities passed')


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][z]*B[z][j] for z in range(n)) for j in range(n)]
            for i in range(n)]

def adjacency(n, edges):
    A = [[0]*n for _ in range(n)]
    for i, j in edges:
        assert i != j
        A[i][j] = A[j][i] = 1
    return A

def paley(p):
    residues = {x*x % p for x in range(1, p)}
    return adjacency(p, ((i, j) for i in range(p) for j in range(i+1, p)
                         if (i-j) % p in residues))

def petersen():
    V = list(combinations(range(5), 2))
    return adjacency(len(V), ((i,j) for i in range(len(V))
                              for j in range(i+1,len(V))
                              if not set(V[i]) & set(V[j])))

def triangular(t):
    V = list(combinations(range(t), 2))
    return adjacency(len(V), ((i,j) for i in range(len(V))
                              for j in range(i+1,len(V))
                              if set(V[i]) & set(V[j])))

def rook(t):
    return adjacency(t*t, ((i,j) for i in range(t*t) for j in range(i+1,t*t)
                           if i//t == j//t or i%t == j%t))

def complete_bipartite(t):
    return adjacency(2*t, ((i,j) for i in range(t) for j in range(t,2*t)))

def shrikhande():
    jumps={(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)}
    return adjacency(16, ((i,j) for i in range(16) for j in range(i+1,16)
                           if ((j//4-i//4)%4,(j%4-i%4)%4)
                           in {((x%4),(y%4)) for x,y in jumps}))

def params(A):
    n=len(A)
    k=sum(A[0]); assert 0<k<n-1
    assert all(sum(row)==k for row in A)
    A2=matmul(A,A)
    lam = next(A2[i][j] for i in range(n) for j in range(i+1,n) if A[i][j])
    mu = next(A2[i][j] for i in range(n) for j in range(i+1,n) if not A[i][j])
    assert 0<mu<=k and 0<=lam<=k-2
    for i in range(n):
        for j in range(n):
            assert A2[i][j] == (k if i==j else (lam if A[i][j] else mu))
    return k,lam,mu

def coeffs(k, lam, mu):
    a=2*k-lam
    b=(k-lam-1)*(k-mu)
    s=k-lam+mu
    c=3*k*s+(k-s)**2+k-mu
    return a,b,s,c

def f(h,k,lam,mu):
    a,b,_,_=coeffs(k,lam,mu)
    return 1-Fraction(a,2)*h+Fraction(a*a-b,6)*h*h - Fraction(a**3-b*(2*a+mu),24)*h*h*h

examples = [
    ('Petersen', petersen()), ('triangular5',triangular(5)),
    ('triangular6',triangular(6)), ('rook3',rook(3)), ('rook4',rook(4)),
    ('Shrikhande',shrikhande()), ('K3,3',complete_bipartite(3)),
    ('K4,4',complete_bipartite(4)),
] + [('Paley%d'%p,paley(p)) for p in (5,13,17,29)]

checked=0
for name,A in examples:
    k,lam,mu=params(A); n=len(A)
    a,b,s,c=coeffs(k,lam,mu)
    assert a>0 and b>=0 and 4*b<a*a and mu<a
    m3=a*a-b;m4=a**3-b*(2*a+mu)
    assert m3>0 and m4>0 and 9*a*m4>4*m3*m3
    L=[[k*int(i==j)-A[i][j] for j in range(n)] for i in range(n)]
    powers=[L]
    for _ in range(3): powers.append(matmul(powers[-1],L))
    # Exact rational node-entry comparison at multiple positive time steps.
    for h in (Fraction(1,10*k),Fraction(1,k),Fraction(2,k),Fraction(5,k)):
        for i in range(n):
            for j in range(n):
                t=Fraction(int(i==j))
                for r,denom in enumerate((1,2,6,24)):
                    t+=(-1)**(r+1)*h**(r+1)*Fraction(powers[r][i][j],denom)
                if i!=j and A[i][j]:
                    expected=h*f(h,k,lam,mu)
                elif i!=j:
                    expected=Fraction(mu,24)*h*h*(12-4*(k+s)*h+c*h*h)
                else:
                    expected=t
                    assert expected>0
                assert t==expected,(name,i,j,h,t,expected)
                checked+=1
        # Row sums exactly one for the RK4 update.
        for i in range(n):
            assert sum((Fraction(int(i==j))+
                        sum((-1)**(r+1)*h**(r+1)*Fraction(powers[r][i][j],denom)
                            for r,denom in enumerate((1,2,6,24)))
                        for j in range(n)),Fraction(0)) == 1
print('VERIFY: %d exact matrix-entry identities on %d strongly regular graphs passed' %(checked,len(examples)))
