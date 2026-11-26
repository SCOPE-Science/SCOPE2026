from itertools import product, combinations
from collections import Counter, deque

def addv(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))

def dot(a,b,p):
    return sum(x*y for x,y in zip(a,b))%p

class Extra:
    def __init__(self,p,n):
        self.p=p; self.n=n
        V=list(product(range(p),repeat=n))
        self.zero=(0,)*n
        self.elts=[(x,y,z) for x in V for y in V for z in range(p)]
        self.e=(self.zero,self.zero,0)

    def mul(self,a,b):
        x,y,z=a; X,Y,Z=b
        return (addv(x,X,self.p),addv(y,Y,self.p),
                (z+Z+dot(x,Y,self.p))%self.p)

    def inv(self,a):
        x,y,z=a
        X=tuple((-u)%self.p for u in x)
        Y=tuple((-u)%self.p for u in y)
        Z=(-z+dot(x,y,self.p))%self.p
        b=(X,Y,Z)
        assert self.mul(a,b)==self.e and self.mul(b,a)==self.e
        return b

    def commutes(self,a,b):
        return self.mul(a,b)==self.mul(b,a)

    def center(self,a):
        x,y,z=a
        return x==self.zero and y==self.zero

    def closure(self,gens):
        S={self.e}
        Q=deque([self.e])
        gs=list(gens)+[self.inv(g) for g in gens]
        while Q:
            a=Q.popleft()
            for g in gs:
                b=self.mul(a,g)
                if b not in S:
                    S.add(b); Q.append(b)
        return S

def symp(v,w,p,n):
    x=v[:n]; y=v[n:]
    X=w[:n]; Y=w[n:]
    return (dot(x,Y,p)-dot(X,y,p))%p

def normalize(v,p):
    j=next(i for i,x in enumerate(v) if x%p)
    inv=pow(v[j],-1,p)
    return tuple((inv*x)%p for x in v)

def projective_points(p,n):
    pts={}
    for v in product(range(p),repeat=2*n):
        if not any(v):
            continue
        pts[normalize(v,p)]=None
    return list(pts)

def base_graph(p,n):
    P=projective_points(p,n)
    N=len(P)
    A=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if symp(P[i],P[j],p,n):
                A[i][j]=A[j][i]=1
    return P,A

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(k))
             for j in range(m)] for i in range(n)]

# Rank-one boundary: every noncommuting pair generates.
for p in (2,3):
    G=Extra(p,1)
    V=[g for g in G.elts if not G.center(g)]
    for a,b in combinations(V,2):
        if not G.commutes(a,b):
            assert len(G.closure([a,b]))==len(G.elts)
    print({"boundary_p":p,"order":len(G.elts),"xi_edges":0})

# Base strongly regular checks.
for p,n in ((2,2),(3,2)):
    P,A=base_graph(p,n)
    v=(p**(2*n)-1)//(p-1)
    k=p**(2*n-1)
    mu=p**(2*n-2)*(p-1)
    assert len(P)==v
    assert all(sum(row)==k for row in A)

    for i,j in combinations(range(v),2):
        common=sum(A[i][r] and A[j][r] for r in range(v))
        assert common==mu

    A2=matmul(A,A)
    for i in range(v):
        for j in range(v):
            target=(k if i==j else mu)
            assert A2[i][j]==target

    fplus=(v-1-p**n)//2
    fminus=(v-1+p**n)//2
    s=p*(p-1)
    N=v*s
    D=s*k
    R=s*p**(n-1)
    z=v*(s-1)
    assert 1+fplus+fminus+z==N
    assert D+fplus*R-fminus*R==0
    assert D*D+(fplus+fminus)*R*R==N*D
    print({"p":p,"n":n,"base_v":v,"base_k":k,
           "lambda_mu":mu,"blowup_vertices":N,"degree":D})

# Full group check for the order-32 extraspecial plus type.
G=Extra(2,2)
V=[g for g in G.elts if not G.center(g)]
assert len(V)==30
for a,b in combinations(V,2):
    # d(G)=4 here; direct closure check confirms no pair generates.
    assert len(G.closure([a,b]))<len(G.elts)

degrees=[]
for a in V:
    degrees.append(sum(not G.commutes(a,b) for b in V if b!=a))
assert Counter(degrees)==Counter({16:30})

# Compare adjacency to the projective blow-up.
def quotient_vec(g):
    x,y,z=g
    return x+y

for a,b in combinations(V,2):
    lhs=not G.commutes(a,b)
    va=normalize(quotient_vec(a),2)
    vb=normalize(quotient_vec(b),2)
    rhs=(va!=vb and symp(va,vb,2,2)!=0)
    assert lhs==rhs

print("VERIFY_OK")
