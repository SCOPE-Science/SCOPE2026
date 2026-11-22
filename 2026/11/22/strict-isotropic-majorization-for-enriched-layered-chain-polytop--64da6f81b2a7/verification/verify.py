"""Independent finite tests for exact enriched-chain isotropic shape profile.
Requires scipy and numpy for optional convex-hull triangulations.
All claimed volumes/covariances from triangulations use exact Fraction determinants.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, prod
from itertools import product

@lru_cache(None)
def det(matrix):
    n=len(matrix)
    if n==1: return matrix[0][0]
    return sum((-1)**j * matrix[0][j]*det(tuple(tuple(row[k] for k in range(n) if k!=j) for row in matrix[1:])) for j in range(n))

def compositions(n,r):
    if r==1:
        yield (n,)
    else:
        for k in range(1,n-r+2):
            for tail in compositions(n-k,r-1):
                yield (k,)+tail

def normalized_shape(m):
    return prod(F(((k+1)*(k+2))**k, factorial(k)**2) for k in m)

def predicted(m):
    n=sum(m)
    v=F(2**n*prod(factorial(k) for k in m),factorial(n))
    sigma=[]
    for k in m: sigma.extend([F((k+1)*(k+2),3*(n+1)*(n+2))]*k)
    return v,sigma

def test_convexity():
    for m in range(3,801):
        assert (m+1)**2 * ((m-1)*(m+2))**m > m*m*(m*(m+1))**m

def test_extremizers():
    checks=0
    for n in range(2,19):
        for r in range(2,min(n,6)+1):
            q,z=divmod(n,r)
            balanced=tuple(sorted([q+1]*z+[q]*(r-z)))
            extreme=tuple(sorted([n-r+1]+[1]*(r-1)))
            low=normalized_shape(balanced); high=normalized_shape(extreme)
            for comp in compositions(n,r):
                val=normalized_shape(comp)
                assert low <= val <= high, (n,r,comp)
                if val==low: assert tuple(sorted(comp))==balanced
                if val==high: assert tuple(sorted(comp))==extreme
                checks+=1
    return checks

def test_hulls():
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
    except ImportError:
        print('HULL_TESTS_SKIPPED: missing scipy and/or numpy')
        return 0
    tested=0
    cases=[(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(1,1,1),(2,1,1),(1,2,1),(1,1,2),(1,1,1,1)]
    for m in cases:
        n=sum(m)
        vertices=[]; off=0
        for k in m:
            for signs in product((-1,1),repeat=k):
                row=[0]*n;row[off:off+k]=signs; vertices.append(row)
            off+=k
        facets=ConvexHull(np.array(vertices,dtype=float)).simplices
        totvol=F(0)
        sum1=[F(0)]*n
        sum2=[[F(0)]*n for _ in range(n)]
        for inds in facets:
            mat=tuple(tuple(int(vertices[i][j]) for j in range(n)) for i in inds)
            vol=F(abs(det(mat)),factorial(n))
            if not vol: continue  # Qhull can emit degenerate coplanar tetrahedra for nonsimplicial faces
            totvol+=vol
            s=[sum(int(vertices[i][j]) for i in inds) for j in range(n)]
            for j in range(n):
                sum1[j]+=vol*F(s[j],n+1)
                for k in range(n):
                    sum2[j][k]+=vol*F(s[j]*s[k]+sum(int(vertices[i][j])*int(vertices[i][k]) for i in inds),(n+1)*(n+2))
        expected_v, expected_diag=predicted(m)
        assert totvol==expected_v,(m,totvol,expected_v)
        assert all(v==0 for v in sum1),(m,sum1)
        for j in range(n):
            for k in range(n):
                assert sum2[j][k]/totvol==(expected_diag[j] if j==k else 0),(m,j,k,sum2[j][k]/totvol)
        tested+=1
    return tested

if __name__=='__main__':
    test_convexity()
    n_profiles=test_extremizers()
    n_hulls=test_hulls()
    print('ENRICHED_CHAIN_BALANCING_PASS', 'second_differences=798', 'integer_profiles='+str(n_profiles),'exact_rational_hulls='+str(n_hulls))
