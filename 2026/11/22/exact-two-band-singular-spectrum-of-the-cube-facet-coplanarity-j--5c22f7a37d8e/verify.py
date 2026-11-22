"""Standalone exact minor enumeration for the cube coplanarity singular spectrum.
Public reproduction code for n=3,4,5; analytic theorem covers every n>=3.
Requires only Python 3 standard library.
"""
from itertools import product, combinations
from math import comb

def determinant_integer(M):
    A=[list(map(int,row)) for row in M]
    z=len(A); assert all(len(r)==z for r in A)
    if z==1: return A[0][0]
    sign=1; old=1
    for k in range(z-1):
        if not A[k][k]:
            j=next((j for j in range(k+1,z) if A[j][k]),None)
            if j is None: return 0
            A[k],A[j]=A[j],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,z):
            for j in range(k+1,z):
                v=A[i][j]*piv-A[i][k]*A[k][j]
                assert v%old==0, 'Bareiss fraction failure'
                A[i][j]=v//old
            A[i][k]=0
        old=piv
    return sign*A[z-1][z-1]

def char(q,S):
    a=1
    for i in S: a*=q[i]
    return a

def square_minor_energy(n,S):
    """Exact sum of squared first-order facet-coplanarity determinants."""
    verts=list(product((-1,1), repeat=n))
    val=0; count=0
    for i in range(n):
        facet=[q for q in verts if q[i]==1]
        for I in combinations(facet,n+1):
            mat=[ [q[j] for j in range(n) if j!=i]+[char(q,S),1] for q in I]
            d=determinant_integer(mat)
            val+=d*d; count+=1
    return val,count

def predicted(n,k):
    return 0 if k==0 else (n-2 if k==2 else n)*2**(n*n-1)

def test():
    total=0
    for n in (3,4,5):
        expected_count=n*comb(2**(n-1),n+1)
        for k in range(0,n+1,2):
            # All spectral bands, with two unequal subsets where possible
            sets=[tuple(range(k))]
            if 0<k<n: sets.append(tuple(range(n-k,n)))
            for S in sets:
                val,cnt=square_minor_energy(n,S)
                expected=predicted(n,k)
                assert cnt==expected_count,(n,k,cnt,expected_count)
                assert val==expected,(n,k,S,val,expected)
                print(f'n={n}, S={S}, minors={cnt}, Q={val}, predicted={expected}: PASS')
                total+=1
    # Generic even linear combinations: verify bilinear orthogonality explicitly
    n=4; C=[(0,1),(0,2),(0,1,2,3)]
    Q={S:square_minor_energy(n,S)[0] for S in C}
    for k,S in enumerate(C):
        for T in C[k+1:]:
            a=0
            verts=list(product((-1,1),repeat=n))
            for i in range(n):
                facet=[q for q in verts if q[i]==1]
                for I in combinations(facet,n+1):
                    def minor(U):
                        return determinant_integer([[q[j] for j in range(n) if j!=i]+[char(q,U),1] for q in I])
                    a+=minor(S)*minor(T)
            assert a==0,(S,T,a)
            print(f'n=4, pair={S},{T}, cross inner product={a}: PASS')
            total+=1
    print(f'ALL {total} direct exact determinant checks PASS')

if __name__=='__main__': test()
