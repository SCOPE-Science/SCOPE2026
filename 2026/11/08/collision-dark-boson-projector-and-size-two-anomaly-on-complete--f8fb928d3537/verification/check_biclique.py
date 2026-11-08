"""Exact finite cross-check of two-boson collision-dark projector on K_{a,b}."""
from itertools import combinations_with_replacement, combinations
from sympy import zeros, eye, ones, Rational, Matrix

def bp(a,b):
    n=a+b; edges=list(combinations(range(n),2)); ind={p:i for i,p in enumerate(edges)}; m=len(edges)
    A=zeros(n,n)
    for u in range(a):
        for v in range(a,n): A[u,v]=A[v,u]=1
    # A symmetric-matrix state X evolves under A*X+X*A, with coordinate basis X[i,j]=X[j,i]=1.
    states=list(combinations_with_replacement(range(n),2)); si={p:i for i,p in enumerate(states)}
    L=zeros(len(states),len(states)); R=zeros(len(states),m)
    for j,(u,v) in enumerate(edges):
        X=zeros(n,n); X[u,v]=X[v,u]=1
        Y=A*X+X*A
        for p,(i,k) in enumerate(states): R[p,j]=Y[i,k]
    # Cross-centered projector.
    Pa=zeros(m,m)
    for (i,j),e in ind.items():
        for (k,l),f in ind.items():
            if i<a and j>=a and k<a and l>=a:
                Pa[e,f]=(int(i==k)-Rational(1,a))*(int(j==l)-Rational(1,b))
    # Same-part pair zero-incidence projector.
    for lo,sz in [(0,a),(a,b)]:
        part=[(u,v) for u,v in edges if lo<=u<v<lo+sz]
        if sz>=3:
            C=zeros(sz,len(part))
            for p,(u,v) in enumerate(part): C[u-lo,p]=C[v-lo,p]=1
            Cproj=eye(len(part))-C.T*(C*C.T).inv()*C
            for ii,e in enumerate(part):
                for jj,f in enumerate(part): Pa[ind[e],ind[f]]+=Cproj[ii,jj]
    # mixed opposite-uniform intra-part dark vector
    vv=zeros(m,1)
    for p in edges:
        u,v=p
        if v<a: vv[ind[p]]=Rational(1,a-1)
        elif u>=a: vv[ind[p]]=-Rational(1,b-1)
    Pa+=vv*vv.T/(vv.T*vv)[0]
    return A,edges,R,Pa

def expected_dim(a,b):
    N=a+b
    return (N-1)*(N-4)//2 + (a==2)+(b==2)

for a,b in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)]:
    A,edges,R,P=bp(a,b); m=len(edges)
    assert P.T==P
    assert P*P==P
    assert R*P==zeros(R.rows,P.cols)
    dim=int(P.trace())
    assert dim==expected_dim(a,b),(a,b,dim)
    # Exact kernel of the two-boson Hamiltonian restricted to collision-free input subspace.
    rank=R.rank()
    assert m-rank==dim,(a,b,m,rank,dim)
    # Capture diagonal for cross part and within part.
    ci=edges.index((0,a)); cross=1-P[ci,ci]
    assert cross==Rational(1,a)+Rational(1,b)-Rational(1,a*b)
    ai=edges.index((0,1)); aa=1-P[ai,ai]
    mix=Rational(2*(b-1),(a-1)*(2*a*b-a-b))
    eq_aa=(Rational(2,a-1)-mix if a>=3 else 1-mix)
    assert aa==eq_aa
    if b>=2:
        bi=edges.index((a,a+1)); bb=1-P[bi,bi]
        mix_b=Rational(2*(a-1),(b-1)*(2*a*b-a-b))
        eq_bb=(Rational(2,b-1)-mix_b if b>=3 else 1-mix_b)
        assert bb==eq_bb
    print(f'K_{{{a},{b}}}: dim={dim}, capture AB={cross}, capture AA={aa}, trace={P.trace()}')
print('BICLIQUE_EXACT_OK')
