"""Exact facet and Ehrhart enumeration for five seven-dimensional 0/1 polytopes.

Source vertex columns: Kaibel--Pokutta, arXiv:2606.31640v2, Appendix A,
Table 3 (2026-06-30). Requires Python 3.11+, NumPy, Numba.
Run: python verify.py
"""
from itertools import combinations
from math import comb, gcd, factorial
import numpy as np
from numba import njit

VERTEX_COLUMNS = '''
0000000 0000000 0000000 0000000 0000000
1100000 1100000 1100000 1100000 1100000
1010000 1010000 1010000 1010000 0011000
0001100 0001100 0001100 0001100 1010100
1111100 1001010 1001010 1001010 0101100
1001010 0111010 0111010 0111010 0110010
0110110 1000110 0100110 0110110 1001110
1001001 0111001 1011001 1001001 0110001
0110101 1000101 1000101 0110101 1001101
1110011 1111101 0111101 1111101 1010011
0111011 1110011 1110011 1110011 1101011
1000111 0110111 0010111 1000111 0100111
0101111 0101111 0101111 0101111 0011111
0011111 0011111 1111111 0011111 1111111
'''
rows = [line.split() for line in VERTEX_COLUMNS.strip().splitlines()]
assert len(rows) == 14 and all(len(r) == 5 for r in rows)
vertices = np.array([[[int(c) for c in rows[i][j]] for i in range(14)]
                     for j in range(5)], dtype=np.int64)

@njit
def exact_det(M):
    """Fraction-free Gaussian elimination; integer result for integer square matrices."""
    a = M.copy()
    n = a.shape[0]
    sign = 1
    prev = 1
    for k in range(n-1):
        if a[k,k] == 0:
            p = -1
            for i in range(k+1,n):
                if a[i,k] != 0:
                    p=i; break
            if p == -1: return 0
            for j in range(n):
                a[k,j],a[p,j]=a[p,j],a[k,j]
            sign=-sign
        pivot=a[k,k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i,j]*pivot-a[i,k]*a[k,j]
                assert z % prev == 0
                a[i,j]=z//prev
        for i in range(k+1,n):a[i,k]=0
        prev=pivot
    return sign*a[n-1,n-1]

@njit
def normal_of_seven(v, ix):
    """Integer cofactors normal to a hyperplane spanned by 7 candidate vertices."""
    D=np.empty((6,7),dtype=np.int64)
    for i in range(6):
        for j in range(7):D[i,j]=v[ix[i+1],j]-v[ix[0],j]
    n=np.empty(7,dtype=np.int64)
    for excluded in range(7):
        M=np.empty((6,6),dtype=np.int64)
        for i in range(6):
            col=0
            for j in range(7):
                if j==excluded:continue
                M[i,col]=D[i,j];col+=1
        n[excluded]=(-1 if excluded%2 else 1)*exact_det(M)
    return n

@njit
def grid_count(t,halfspaces):
    """Count lattice points in tP inside [0,t]^7, testing all exact facets."""
    count=0
    for K in range((t+1)**7):
        j=K
        x=np.empty(7,dtype=np.int64)
        for a in range(7):
            x[a]=j%(t+1)
            j//=t+1
        valid=True
        for a in range(halfspaces.shape[0]):
            z=0
            for b in range(7):z+=halfspaces[a,b]*x[b]
            if z>t*halfspaces[a,7]:
                valid=False
                break
        if valid:count+=1
    return count


def facets_exact(v):
    found=[]
    facets=[]
    for face in combinations(range(14),7):
        n=normal_of_seven(v,np.array(face,dtype=np.int64))
        if np.all(n==0):continue
        b=sum(int(n[j])*int(v[face[0],j]) for j in range(7))
        vals=[sum(int(n[k])*int(v[i,k]) for k in range(7))-b for i in range(14)]
        if min(vals)<0<max(vals):continue
        zeros=tuple(i for i in range(14) if vals[i]==0)
        assert len(zeros)==7 and zeros==face, (face, zeros)
        if min(vals)==0: n=-n;b=-b
        gg=0
        for k in n:gg=gcd(gg,int(k))
        assert gg>0
        n=n//gg;b//=gg
        assert all(sum(int(n[k])*int(v[i,k]) for k in range(7))<=b for i in range(14))
        assert 2*b-sum(int(k) for k in n)>0 # c=(1/2,...,1/2) is strict interior
        facets.append(face)
        found.append([*map(int,n),int(b)])
    assert len(facets)==len(set(facets))
    return facets, np.array(found,dtype=np.int64)

EXPECTED_FACETS=(144,136,136,136,136)
EXPECTED_HSTAR=((1,6,31,132,201,92,1,0),
                (1,6,31,112,171,64,1,0),
                (1,6,31,112,171,64,1,0),
                (1,6,29,134,197,82,1,0),
                (1,6,33,148,231,94,1,0))
EXPECTED_VOLUMES=(464,386,386,450,514)


def run():
    for j,v in enumerate(vertices):
        assert len({tuple(x) for x in v}) == 14
        assert all(int(v[:,k].sum()) == 7 for k in range(7))
        A=np.array([list(map(int,x))+[1] for x in v[:8]],dtype=np.int64)
        det8=int(exact_det(A))
        assert det8!=0 # affine dimension is 7
        facets,hs=facets_exact(v)
        assert len(facets)==EXPECTED_FACETS[j]
        # Center-star triangulation, independent of Ehrhart enumeration.
        sum_scaled_determinants=0
        for face in facets:
            m=np.array([[2*int(v[i,k])-1 for k in range(7)] for i in face],dtype=np.int64)
            sum_scaled_determinants+=abs(int(exact_det(m)))
        assert sum_scaled_determinants % 128 == 0
        vol=sum_scaled_determinants//128
        assert vol==EXPECTED_VOLUMES[j]
        L=[int(grid_count(t,hs)) for t in range(8)]
        hstar=tuple(sum((-1)**(q-t)*comb(8,q-t)*L[t] for t in range(q+1))
                    for q in range(8))
        assert hstar==EXPECTED_HSTAR[j]
        assert sum(hstar)==vol
        print('V%d: affine_det8=%d facets=%d L(0..7)=%s hstar=%s normalized_volume=%d' %
              (j+1,det8,len(facets),L,hstar,vol),flush=True)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':run()
