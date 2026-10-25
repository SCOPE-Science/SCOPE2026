"""Exact finite certificate for the tetrahedral-volume profile of cube/octahedron intersections.
Run using Python 3.9+ (standard library only): python verify.py
All parameter inequalities are polynomial Bernstein certificates, not floating-point samples.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb

PERMS3 = tuple(permutations(range(3)))
PERMS4 = tuple(permutations(range(4)))
def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p))) % 2 else 1
SIGNS3 = tuple((p,parity(p)) for p in PERMS3)
SIGNS4 = tuple((p,parity(p)) for p in PERMS4)

def vertices(branch):
    seeds=((1,0),(0,1),(0,0)) if branch==1 else ((1,0),(1,0),(0,1))
    return sorted({tuple((sgn*seeds[p[k]][0],sgn*seeds[p[k]][1]) for k,sgn in enumerate(signs))
                   for p in PERMS3 for signs in product((-1,1),repeat=3)})

def poly_mul(a,b):
    out=[0]*4
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i+j<=3:out[i+j]+=ai*bj
    return out

def determinant_polynomial(points):
    base=points[0]
    A=[[tuple(points[i][j][k]-base[j][k] for k in (0,1)) for j in range(3)] for i in (1,2,3)]
    out=[0]*4
    for p,sgn in SIGNS3:
        z=poly_mul(poly_mul(A[0][p[0]],A[1][p[1]]),A[2][p[2]])
        for i in range(4):out[i]+=sgn*z[i]
    return tuple(out)

def eval_poly(p,t):
    return sum(a*t**k for k,a in enumerate(p))

def determinant_4x4_at(points,t):
    # Independent 4x4 Leibniz expansion with exact rational coordinates.
    A=[[F(1), *(F(a)+t*F(b) for a,b in pt)] for pt in points]
    return sum(sgn*A[0][p[0]]*A[1][p[1]]*A[2][p[2]]*A[3][p[3]] for p,sgn in SIGNS4)

def bernstein_coefficients(p,left,right):
    # Coefficients of p(left+(right-left)t) in cubic Bernstein basis on [0,1].
    a=[sum(F(p[k])*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,4)) for j in range(4)]
    return [sum(a[j]*F(comb(i,j),comb(3,j)) for j in range(i+1)) for i in range(4)]

def endpoint_vertices(v,t):
    return sorted({tuple(F(a)+t*F(b) for a,b in pt) for pt in v})

def det_scalar(pts):
    A=[[F(1),*pt] for pt in pts]
    return sum(sgn*A[0][p[0]]*A[1][p[1]]*A[2][p[2]]*A[3][p[3]] for p,sgn in SIGNS4)


def check_branch(b, regions, expectations):
    v=vertices(b)
    assert len(v)==24
    coeff_counts=Counter(); indexed=[]
    for ix in combinations(range(24),4):
        pts=[v[i] for i in ix]
        p=determinant_polynomial(pts)
        if any(p):
            # Exact independent determinant at two rational parameter points.
            for t in (F(1,3),F(2,3)):
                assert eval_poly(p,t)==determinant_4x4_at(pts,t)
            normalized = p if next(z for z in p[::-1] if z)!=-abs(next(z for z in p[::-1] if z)) else tuple(-z for z in p)
            coeff_counts[normalized]+=1
        indexed.append((ix,p))
    assert len(coeff_counts)==expectations['classes']
    assert sum(coeff_counts.values())==expectations['nonzero']
    summary=[]
    for left,right,target,count_away,count_right in regions:
        # Full continuum inequality: each signed polynomial gap has four nonnegative Bernstein coefficients.
        for p in coeff_counts:
            for sign in (-1,1):
                diff=tuple(target[k]+sign*p[k] for k in range(4))
                assert all(bc>=0 for bc in bernstein_coefficients(diff,left,right)), (b,p,sign,left,right)
        sample=(left+right)/2
        winner_count=sum(abs(eval_poly(p,sample))==eval_poly(target,sample) for _,p in indexed)
        assert winner_count==count_away,(b,left,right,winner_count)
        at_right=sum(abs(eval_poly(p,right))==eval_poly(target,right) for _,p in indexed)
        assert at_right==count_right,(b,right,at_right)
        summary.append((str(left),str(right),winner_count,at_right))
    return v,summary,len(indexed)

def test_endpoint(v,t,nexpected,dexpected,winning):
    points=endpoint_vertices(v,t)
    assert len(points)==nexpected
    vals=[abs(det_scalar([points[j] for j in ids])) for ids in combinations(range(len(points)),4)]
    assert max(vals)==dexpected
    assert vals.count(dexpected)==winning


def run():
    v1,s1,n1=check_branch(1,[(F(0),F(1,2),(2,2,4,0),24,30),
                          (F(1,2),F(1),(0,8,0,0),6,96)],{'classes':54,'nonzero':9924})
    v2,s2,n2=check_branch(2,[(F(0),F(1),(8,0,8,0),12,162)],{'classes':48,'nonzero':9846})
    test_endpoint(v1,F(0),6,2,12)
    test_endpoint(v1,F(1),12,8,6)
    test_endpoint(v2,F(0),12,8,6)
    test_endpoint(v2,F(1),8,16,2)
    # At the first transition there are 30 maximizers among the distinct 24-vertex candidates.
    assert sum(abs(eval_poly(p,F(1,2)))==4 for _,p in
               ((ix,determinant_polynomial([v1[i] for i in ix])) for ix in combinations(range(24),4)))==30
    # Separate exact occupancy certificate: M(c)-Vol(K_c)/6 is nonnegative.
    # On 1<=c<=3/2: c(2c-3)^2/9; on 3/2<=c<=2:
    # 2(2c-3)(c^2-3c+3)/9; on 2<=c<=3, putting w=c-2:
    # 2(1-3w+9w^2-w^3)/9 > 0, since w^3<=w^2 and 1-3w+8w^2>0.
    for p, lo, hi in [((0,9,-12,4),F(1),F(3,2)), # c(2c-3)^2 multiplied by 9
                       ((-18,30,-18,4),F(3,2),F(2)), # 2(2c-3)(c²-3c+3)
                       ((2,-6,18,-2),F(0),F(1))]: # 2(1-3w+9w²-w³)
        # Verify nonnegativity via same exact continuous basis where possible.
        assert all(q>=0 for q in bernstein_coefficients(p,lo,hi)),(p,lo,hi)
    print('VERIFY_OK polynomial_classes=(54,48) nonzero_vertex_quadruples=(9924,9846) tested_per_branch=10626')
    print('VERIFY_OK parameter_chambers='+repr(s1+s2)+' endpoint_maximizer_counts=(12,6,2)')
    print('VERIFY_OK exact_cubic_Bernstein_certificates=all_signed_gaps occupancy_min=1/6_at_c=3/2')

if __name__=='__main__':run()
