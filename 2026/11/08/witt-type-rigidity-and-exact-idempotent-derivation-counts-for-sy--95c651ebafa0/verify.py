"""Finite-field checks for idempotent derivations of symmetric-bracket algebras.

Run: python verify.py.  No external dependencies.
"""
from itertools import product


def mm(X,Y,q):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))%q
             for j in range(len(Y[0]))] for i in range(len(X))]


def transpose(X):
    return [list(z) for z in zip(*X)]


def form(n):
    assert n%2==0
    m=n//2
    return [[int((i<m and j==i+m) or (j<m and i==j+m))
             for j in range(n)] for i in range(n)]


def idempotent_derivations_2(q,B):
    """Brute-force ALL linear derivations including all central rows over prime Fq."""
    n=2
    I=[[int(i==j) for j in range(n)] for i in range(n)]
    count=0
    ranks=set()
    for coeff in product(range(q),repeat=4):
        A=[list(coeff[:2]),list(coeff[2:])]
        AA=mm(A,A,q)
        if AA!=A: continue
        left=mm(transpose(A),B,q)
        right=mm(B,A,q)
        for c in range(q):
            if c*c%q!=c: continue
            if any((left[i][j]+right[i][j]-c*B[i][j])%q
                   for i in range(n) for j in range(n)):
                continue
            for phi in product(range(q),repeat=n):
                if any((sum(phi[k]*A[k][j] for k in range(n))
                        +c*phi[j]-phi[j])%q for j in range(n)):
                    continue
                # Independently check the derivation identity on all basis pairs,
                # and the identity D^2=D on each basis vector.
                D=[A[0]+[0], A[1]+[0], list(phi)+[c]]
                # D is given here as a row list for the block matrix
                # [A 0; phi c]; multiplication tests all entries.
                if mm(D,D,q)!=D:
                    raise AssertionError('D^2 != D')
                for i in range(2):
                    for j in range(2):
                        lhs=c*B[i][j]%q
                        rhs=(sum(A[k][i]*B[k][j] for k in range(2))+
                             sum(A[k][j]*B[i][k] for k in range(2)))%q
                        assert lhs==rhs
                count+=1
                ranks.add(0 if c==0 else 2)
    return count,ranks


def canonical_basis(u,v,q):
    # RREF of two independent vectors (rows), or None if dependent.
    a=[list(u),list(v)]
    n=len(u)
    pivotrow=0
    for col in range(n):
        choices=[i for i in range(pivotrow,2) if a[i][col]%q]
        if not choices: continue
        j=choices[0]
        a[pivotrow],a[j]=a[j],a[pivotrow]
        inv=pow(a[pivotrow][col],-1,q)
        a[pivotrow]=[(t*inv)%q for t in a[pivotrow]]
        for k in range(2):
            if k==pivotrow:continue
            scale=a[k][col]
            a[k]=[(a[k][h]-scale*a[pivotrow][h])%q for h in range(n)]
        pivotrow+=1
        if pivotrow==2:break
    return tuple(map(tuple,a)) if pivotrow==2 else None


def dot_B(u,v,B,q):
    return sum(u[i]*B[i][j]*v[j]
               for i in range(len(u)) for j in range(len(u)))%q


def isotropic_planes_4(q):
    B=form(4)
    vectors=list(product(range(q),repeat=4))
    planes=set()
    for u in vectors:
        if not any(u) or dot_B(u,u,B,q):continue
        for v in vectors:
            if dot_B(v,v,B,q) or dot_B(u,v,B,q):continue
            t=canonical_basis(u,v,q)
            if t is not None: planes.add(t)
    return planes


def complement(U,V,q):
    # Two RREF planes are complementary iff their 4-by-4 row matrix has rank4.
    a=[list(u) for u in U+V]
    rank=0
    for j in range(4):
        opts=[i for i in range(rank,4) if a[i][j]%q]
        if not opts:continue
        i=opts[0]; a[i],a[rank]=a[rank],a[i]
        t=pow(a[rank][j],-1,q)
        a[rank]=[(v*t)%q for v in a[rank]]
        for i in range(rank+1,4):
            t=a[i][j]
            a[i]=[(a[i][h]-t*a[rank][h])%q for h in range(4)]
        rank+=1
    return rank==4


def verify():
    for q in (3,5,7):
        B=form(2)
        count,ranks=idempotent_derivations_2(q,B)
        assert count==1+2*q, (q,count)
        assert ranks=={0,2}
        print('split dim2',q,count)
    for q in (3,7):
        B=[[1,0],[0,1]]
        count,ranks=idempotent_derivations_2(q,B)
        assert count==1 and ranks=={0},(q,count)
        print('anisotropic dim2',q,count)
    # The split 4-space has 2(q+1) maximal totally singular planes;
    # each plane has q transverse maximal totally singular complements.
    for q in (3,5):
        planes=isotropic_planes_4(q)
        assert len(planes)==2*(q+1),(q,len(planes))
        pairs=sum(complement(U,V,q) for U in planes for V in planes)
        assert pairs==2*(q+1)*q,(q,pairs)
        assert 1+pairs*q*q==1+2*q**3*(q+1)
        print('split dim4',q,'isotropic planes',len(planes),
              'complementary ordered pairs',pairs,
              'idempotent derivations',1+pairs*q*q)
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
