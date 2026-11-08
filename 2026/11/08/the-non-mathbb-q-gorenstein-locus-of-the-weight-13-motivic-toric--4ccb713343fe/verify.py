"""Exact integer/rational checks for the weight-13 motivic toric fourfold.

Run: python3 toric_weight13_verifier.py
Requires only the Python 3 standard library.
"""
from fractions import Fraction
from itertools import combinations, product
from functools import reduce
from math import gcd, lcm

WEIGHTS = (2, 3, 5, 7, 8)
WEIGHT = 13


def det(matrix):
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    a = [[Fraction(t) for t in row] for row in matrix]
    sign = 1
    out = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            sign *= -1
        v = a[j][j]
        out *= v
        for k in range(j+1, n):
            factor = a[k][j] / v
            for h in range(j+1, n):
                a[k][h] -= factor * a[j][h]
    return sign * out


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    nrow, ncol = len(a), len(a[0])
    i = 0
    for j in range(ncol):
        piv = next((k for k in range(i, nrow) if a[k][j]), None)
        if piv is None:
            continue
        a[i], a[piv] = a[piv], a[i]
        fact = a[i][j]
        a[i] = [x/fact for x in a[i]]
        for k in range(nrow):
            if k != i:
                fact = a[k][j]
                if fact:
                    a[k] = [x - fact*y for x,y in zip(a[k],a[i])]
        i += 1
        if i == nrow:
            break
    return i


def solve_unique(rows, rhs):
    assert len(rows) == len(rhs)
    n = len(rows[0]); assert rank(rows) == n
    a = [[Fraction(x) for x in row] + [Fraction(b)] for row,b in zip(rows,rhs)]
    k = 0
    for j in range(n):
        piv = next(i for i in range(k,len(a)) if a[i][j])
        a[k],a[piv] = a[piv],a[k]
        t=a[k][j];a[k]=[x/t for x in a[k]]
        for i in range(len(a)):
            if i != k:
                t=a[i][j]
                a[i]=[x-t*y for x,y in zip(a[i],a[k])]
        k+=1
    assert all(all(x==0 for x in row[:-1]) and row[-1]==0 for row in a[n:])
    return tuple(a[i][-1] for i in range(n))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def affine_dim(zs):
    if len(zs)<=1:return 0
    return rank([[x-y for x,y in zip(p,zs[0])] for p in zs[1:]])


def primitive_normal(rows):
    assert len(rows)==3 and all(len(row)==4 for row in rows)
    n=[(-1)**k * det([[r[j] for j in range(4) if j!=k] for r in rows]) for k in range(4)]
    if not any(n):return None
    assert all(x.denominator==1 for x in n)
    a=[int(x) for x in n]
    d=reduce(gcd,a)
    return tuple(x//d for x in a)


def main():
    p=sorted(tuple(x) for x in product(*(range(WEIGHT//w+1) for w in WEIGHTS))
             if sum(a*b for a,b in zip(x,WEIGHTS))==WEIGHT)
    assert len(p)==9 and len(set(p))==9
    assert p[0]==(0,0,1,0,1)
    # Explicit integral basis for the affine difference lattice of the nine exponent vectors.
    B=[(-3,-4,-5,-4),(2,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    z=[]
    for x in p:
        d=[a-b for a,b in zip(x,p[0])]
        assert (d[1]-d[2]-d[3])%2==0
        v=((d[1]-d[2]-d[3])//2,d[2],d[3],d[4])
        assert tuple(dot(row,v) for row in B)==tuple(d)
        z.append(v)
    # These four of the actual difference vectors form a unimodular basis.
    assert abs(det([z[i] for i in (1,2,3,6)]))==1
    assert affine_dim(z)==4

    facets={}
    for ids in combinations(range(len(z)),4):
        rows=[[z[i][j]-z[ids[0]][j] for j in range(4)] for i in ids[1:]]
        n=primitive_normal(rows)
        if n is None:continue
        c=dot(n,z[ids[0]])
        vals=[dot(n,x)-c for x in z]
        if all(v>=0 for v in vals):
            n=tuple(-t for t in n);c=-c;vals=[-v for v in vals]
        if any(v>0 for v in vals):continue
        support=tuple(i for i,v in enumerate(vals) if v==0)
        assert affine_dim([z[i] for i in support])==3
        facets[(n,c)]=support
    expected=[
     ((1,1,1,1),0,(0,1,2,3,4,5)),
     ((0,1,2,1),0,(0,1,2,6)),
     ((0,0,-1,0),0,(0,1,3,4,5,7,8)),
     ((-1,0,0,0),0,(0,1,6,7)),
     ((0,0,1,1),0,(0,2,3,6)),
     ((-1,-1,-1,0),0,(0,3,6,7,8)),
     ((0,0,0,-1),1,(1,2,4,5,6,7,8)),
     ((0,-1,0,0),1,(2,3,5,6,8)),
    ]
    assert len(facets)==8
    assert {(n,c,ids) for (n,c),ids in facets.items()}==set(expected)
    fac=list(facets)
    for idx in range(8):
        n,c,ids=expected[idx]
        assert fac[idx]==(n,c) and facets[fac[idx]]==ids
    assert tuple(fac[1][0][i]-2*fac[4][0][i]-fac[6][0][i]+fac[7][0][i] for i in range(4))==(0,0,0,0)
    assert 1-2-1+1==-1

    # Enumerate all nonempty proper faces from subsets of the eight supporting facets.
    faces={}
    for r in range(1,9):
        for subs in combinations(range(8),r):
            pts=tuple(i for i in range(9) if all(i in facets[fac[j]] for j in subs))
            if pts:faces[pts]=affine_dim([z[i] for i in pts])
    assert {d:sum(t==d for t in faces.values()) for d in range(4)}=={0:8,1:19,2:19,3:8}
    expected_bad={(2,),(6,),(2,6)}
    bad=set()
    good_point_models={}
    for face,dim in faces.items():
        ids=tuple(j for j in range(8) if all(v in facets[fac[j]] for v in face))
        rows=[fac[j][0] for j in ids]
        assert rank(rows)==4-dim
        if rank([list(row)+[1] for row in rows])>rank(rows):
            bad.add(face)
            continue
        if dim==0:
            sol=solve_unique(rows,[1]*len(rows))
            assert all(s.denominator==1 for s in sol)
            good_point_models[face[0]]=sol
    assert bad==expected_bad
    assert len(good_point_models)==6
    # Every other proper face is contained in a maximal cone whose K-support
    # vector is integral, hence is a Gorenstein orbit.
    for face in faces:
        if face in bad:continue
        assert any(v in face for v in good_point_models)
    assert tuple(sorted(i for i in range(9) if (i,) in faces))==(0,1,2,3,5,6,7,8)
    print('WEIGHT_13_TORIC_CHECKS_PASS')
    print('monomials',len(p),'dimension',affine_dim(z),'facets',len(facets),'vertices',8)
    print('face_vector',tuple(sum(t==d for t in faces.values()) for d in range(4)))
    print('non_Q_Gorenstein_faces',sorted(bad))
    print('Gorenstein_fixed_point_indices',sorted(good_point_models))

if __name__=='__main__':
    main()
