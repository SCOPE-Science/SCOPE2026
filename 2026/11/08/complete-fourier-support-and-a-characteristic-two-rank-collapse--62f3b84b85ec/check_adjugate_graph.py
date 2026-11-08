"""Exact finite-field checks for the Fourier transform of the 3x3 adjugate graph.

Binary case: an exhaustive 512-by-512 Fourier coefficient certificate using
integer Walsh-Hadamard transforms. Ternary case: exact cyclotomic norms for
multiple noncanonical matrix frequencies, and direct polar-radical checks.
"""
import itertools
import random


def cofactor_vector(x, p):
    # Adjugate is the transpose of the signed cofactor matrix.
    out = [0] * 9
    for i in range(3):
        for j in range(3):
            rr = [r for r in range(3) if r != j]
            cc = [c for c in range(3) if c != i]
            out[3*i+j] = ((-1)**(i+j)*(x[3*rr[0]+cc[0]]*x[3*rr[1]+cc[1]]
                             - x[3*rr[0]+cc[1]]*x[3*rr[1]+cc[0]])) % p
    return out


def matrix_rank_3(x, p):
    A = [list(x[3*i:3*i+3]) for i in range(3)]
    r=0
    for c in range(3):
        j=next((i for i in range(r,3) if A[i][c]%p),None)
        if j is None: continue
        A[r],A[j]=A[j],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(z*inv)%p for z in A[r]]
        for i in range(3):
            if i!=r:
                z=A[i][c]
                A[i]=[(A[i][k]-z*A[r][k])%p for k in range(3)]
        r+=1
    return r


def det3(x,p):
    a,b,c,d,e,f,g,h,i=x
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%p


def walsh_in_place(a):
    length=1
    while length<len(a):
        for i in range(0,len(a),2*length):
            for j in range(i,i+length):
                u,v=a[j],a[j+length]
                a[j],a[j+length]=u+v,u-v
        length*=2


def parity(x): return x.bit_count()&1


def independent_binary_basis(generators):
    piv={}
    for x in generators:
        y=x
        for k in sorted(piv,reverse=True):
            if (y>>k)&1:y^=piv[k]
        if y:piv[y.bit_length()-1]=y
    return list(piv.values())


def run_binary():
    q=2; V=list(range(512)); cofs=[]; ranks=[]; dets=[]
    for v in V:
        x=[(v>>i)&1 for i in range(9)]
        c=cofactor_vector(x,2)
        cofs.append(sum(a<<i for i,a in enumerate(c)))
        ranks.append(matrix_rank_3(x,2))
        dets.append(det3(x,2))
    N=[ranks.count(k) for k in range(4)]
    assert N==[1,49,294,168],N
    support=0
    for B in V:
        br=ranks[B]
        H=[]
        for i in range(9):
            row=0
            for j in range(9):
                if i==j:continue
                # All squarefree cofactor terms: Q(e_i)=0.
                if parity(B&cofs[(1<<i)|(1<<j)]):row|=1<<j
            H.append(row)
        rad=[z for z in V if all(parity(z&row)==0 for row in H)]
        basis=independent_binary_basis(rad)
        expected_dim={0:9,1:5,2:3,3:1}[br]
        assert len(basis)==expected_dim,(B,br,len(basis))
        assert len(rad)==(1<<expected_dim)
        bt=sum(((B>>(3*j+i))&1)<<(3*i+j) for i in range(3) for j in range(3))
        for z in rad:
            qz=parity(B&cofs[z])
            assert (qz==0 if br<3 else qz==((z==bt)*dets[B])),(B,z,qz,br)
        if br==3:
            assert set(rad)=={0,bt}
        values=[1 if parity(B&c)==0 else -1 for c in cofs]
        walsh_in_place(values)
        count=0
        for A,v in enumerate(values):
            if br==0:
                predicate=A==0; magnitude=512
            elif br in (1,2):
                predicate=all(parity(A&z)==0 for z in basis)
                magnitude={1:128,2:64}[br]
            else:
                # tr(AB) = dot(A,B^T), det(B)^1 is the Frobenius square root.
                bt=sum(((B>>(3*j+i))&1)<<(3*i+j) for i in range(3) for j in range(3))
                predicate=parity(A&bt)==dets[B]
                magnitude=32
            assert (v!=0)==predicate,(B,A,br,v,predicate)
            assert abs(v)==(magnitude if predicate else 0),(B,A,br,v,magnitude)
            if predicate:count+=1
        expected_count={0:1,1:16,2:64,3:256}[br]
        assert count==expected_count,(B,br,count)
        support+=count
    target=1+49*16+294*64+168*256
    assert support==target==62609
    print('EXHAUSTIVE_F2_OK', 'ambient',2**18,'nonzero',support,'zero',2**18-support)


def row_rank(A,p):
    A=[list(row) for row in A]
    m=len(A);n=len(A[0]);r=0
    for j in range(n):
        t=next((i for i in range(r,m) if A[i][j]%p),None)
        if t is None:continue
        A[r],A[t]=A[t],A[r]
        v=pow(A[r][j],-1,p)
        A[r]=[(v*x)%p for x in A[r]]
        for i in range(m):
            if i!=r:
                v=A[i][j]
                A[i]=[(A[i][k]-v*A[r][k])%p for k in range(n)]
        r+=1
        if r==m:break
    return r


def check_ternary():
    p=3
    E=[];cofs=[]
    for xx in itertools.product(range(p),repeat=9):
        E.append(xx);cofs.append(cofactor_vector(xx,p))
    basis=[tuple(int(j==i) for j in range(9)) for i in range(9)]
    canonical={0:(0,)*9,1:(1,0,0,0,0,0,0,0,0),
               2:(1,0,0,0,1,0,0,0,0),3:(1,0,0,0,1,0,0,0,1)}
    rng=random.Random(923)
    bs=list(canonical.values())
    # Test noncanonical B in each rank stratum.
    for r in (1,2,3):
        while sum(matrix_rank_3(b,p)==r for b in bs)<4:
            B=tuple(rng.randrange(p) for _ in range(9))
            if matrix_rank_3(B,p)==r and B not in bs:bs.append(B)
    total=0
    for B in bs:
        br=matrix_rank_3(B,p)
        polar=[]
        for i in range(9):
            row=[]
            for j in range(9):
                xx=tuple((basis[i][k]+basis[j][k])%p for k in range(9))
                row.append(sum(B[k]*z for k,z in enumerate(cofactor_vector(xx,p)))%p)
            polar.append(row)
        polar_rank=row_rank(polar,p)
        assert polar_rank=={0:0,1:4,2:6,3:9}[br],(B,br,polar_rank)
        AS=[(0,)*9]
        for _ in range(16):AS.append(tuple(rng.randrange(p) for _ in range(9)))
        for A in AS:
            if br==0:nonzero=any(A)==False
            else:
                # A belongs to the row space of the polar map exactly when
                # augmenting the row vectors by A leaves rank unchanged.
                nonzero=row_rank(polar+[list(A)],p)==polar_rank
            counts=[0]*p
            for X,C in zip(E,cofs):
                phase=(sum(A[j]*X[j]+B[j]*C[j] for j in range(9)))%p
                counts[phase]+=1
            u=counts[0]-counts[2];v=counts[1]-counts[2]
            normsq=u*u-u*v+v*v
            expected_sq={0:3**18,1:3**14,2:3**12,3:3**9}[br] if nonzero else 0
            assert normsq==expected_sq,(B,A,br,normsq,expected_sq,counts)
            total+=1
    print('EXACT_F3_CYCLOTOMIC_OK','frequencies',total,'matrix_arity',3**9)


if __name__=='__main__':
    run_binary()
    check_ternary()
    print('ALL_ADJUGATE_FOURIER_TESTS_OK')
