from itertools import product

def canonical(v,p):
    for a in v:
        if a % p:
            inv=pow(a,-1,p)
            return tuple((inv*x)%p for x in v)
    raise ValueError

def points(p):
    return sorted({canonical(v,p) for v in product(range(p), repeat=3) if any(v)})

def dot(a,b,p):
    return sum(x*y for x,y in zip(a,b))%p

def mm(A,B):
    n=len(A); m=len(B); k=len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(m)) for j in range(k)] for i in range(n)]

def madd(A,B,sa=1,sb=1):
    return [[sa*x+sb*y for x,y in zip(r,s)] for r,s in zip(A,B)]

def eye(n,c=1):
    return [[c if i==j else 0 for j in range(n)] for i in range(n)]

def zero(n):
    return [[0]*n for _ in range(n)]

def check(p):
    P=points(p)
    H=points(p)  # a canonical nonzero linear functional represents a plane kernel
    N=p*p+p+1
    assert len(P)==len(H)==N

    M=[[1 if dot(v,f,p)==0 else 0 for f in H] for v in P]
    B=[[1-x for x in row] for row in M]
    J=[[1]*N for _ in range(N)]
    I=eye(N)

    MT=[list(x) for x in zip(*M)]
    BT=[list(x) for x in zip(*B)]
    MM=mm(M,MT)
    BB=mm(B,BT)
    assert MM==madd(I,J,sa=p,sb=1)
    assert BB==madd(I,J,sa=p,sb=p*(p-1))
    assert all(sum(r)==p*p for r in B)

    # Active adjacency: points first, planes second.
    n=2*N
    A=zero(n)
    for i in range(N):
        for j in range(N):
            A[i][N+j]=B[i][j]
            A[N+j][i]=B[i][j]
    for i in range(N):
        for j in range(N):
            if i!=j:
                A[N+i][N+j]=1

    point_deg=p*p
    plane_deg=(N-1)+p*p
    assert all(sum(A[i])==point_deg for i in range(N))
    assert all(sum(A[N+i])==plane_deg for i in range(N))

    # Proper subspaces: 0, points, planes.
    verts=[("z",None)]+[("p",i) for i in range(N)]+[("h",j) for j in range(N)]
    adj=[set() for _ in verts]
    # indices: zero=0, points 1..N, planes 1+N..2N
    for i in range(N):
        for j in range(N):
            if B[i][j]:
                a=1+i; b=1+N+j
                adj[a].add(b); adj[b].add(a)
    for i in range(N):
        for j in range(i+1,N):
            a=1+N+i; b=1+N+j
            adj[a].add(b); adj[b].add(a)

    def leq(u,w):
        tu,iu=verts[u]; tw,iw=verts[w]
        if tu=="z": return True
        if tw=="z": return u==w
        if tu=="p" and tw=="p": return iu==iw
        if tu=="h" and tw=="h": return iu==iw
        if tu=="p" and tw=="h": return M[iu][iw]==1
        return False

    for u in range(len(verts)):
        for w in range(len(verts)):
            assert (adj[u] <= adj[w]) == leq(u,w), (p,u,w)

    # Spectral annihilator:
    # f(A)=(A^2-(p^2+p)A-p^4 I)(A^2+A-pI).
    A2=mm(A,A)
    I2=eye(n)
    F1=[[A2[i][j]-(p*p+p)*A[i][j]-(p**4)*I2[i][j] for j in range(n)] for i in range(n)]
    F2=[[A2[i][j]+A[i][j]-p*I2[i][j] for j in range(n)] for i in range(n)]
    assert mm(F1,F2)==zero(n)

    # Multiplicity/moment checks for active graph.
    m=N-1
    # Root sums/products: first quadratic sum s1=p^2+p, product -p^4.
    # second quadratic sum s2=-1, product -p, repeated m times.
    assert (p*p+p) + m*(-1) == 0  # trace
    # sum squares of roots is s^2-2 product.
    trace2=(p*p+p)**2+2*p**4 + m*(1+2*p)
    degree_sum=N*point_deg+N*plane_deg
    assert trace2==degree_sum

    print({"p":p,"N":N,"vertices_full":2*N+1,
           "point_degree":point_deg,"plane_degree":plane_deg,
           "trace2":trace2})

for p in (2,3,5):
    check(p)
print("VERIFY_OK")
