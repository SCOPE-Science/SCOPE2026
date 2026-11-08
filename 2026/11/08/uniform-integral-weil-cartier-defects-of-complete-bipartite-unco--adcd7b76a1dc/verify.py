"""Standalone exact finite checks of complete-bipartite toric divisor data.

Requires Python 3 and SymPy. The infinite-family assertions require
and are supplied with a separate mathematical proof.
"""
from itertools import product
from math import factorial, comb
from sympy import Matrix, zeros, ones
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def data(a,b):
    d=a+b
    rays=[]
    for i in range(a):
        for j in range(b):
            for s in (-1,1):
                for t in (-1,1):
                    r=[0]*d; r[i]=s; r[a+j]=t; rays.append(tuple(r))
    vertices=[]
    for signs in product((-1,1),repeat=a):
        vertices.append(tuple(signs)+(0,)*b)
    for signs in product((-1,1),repeat=b):
        vertices.append((0,)*a+tuple(signs))
    faces=[[i for i,r in enumerate(rays) if sum(x*y for x,y in zip(r,v))==1]
           for v in vertices]
    return rays,vertices,faces


def support_rank(rays,faces,d):
    # Each cone contributes the integer-free rational linear dependencies
    # in the ray values of a globally piecewise-linear function.
    relations=[]
    for face in faces:
        raysmat=Matrix([rays[j] for j in face])
        for k in raysmat.T.nullspace():
            row=[0]*len(rays)
            for idx,r in enumerate(face): row[r]=k[idx]
            relations.append(row)
    return len(rays)-Matrix(relations).rank()


def invariants(a,b):
    rays,vertices,faces=data(a,b)
    d=a+b
    R=Matrix(rays)
    T=R.row_join(ones(len(rays),1))
    def diagonals(B):
        D=smith_normal_form(B,domain=ZZ)
        return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    dr,dt=diagonals(R),diagonals(T)
    rank=support_rank(rays,faces,d)
    assert len(rays)==4*a*b
    assert len(vertices)==2**a+2**b
    assert all(len(face)==2*a*b for face in faces)
    assert rank-d==1 # toric Picard rank
    assert dr==[1]*(d-1)+[2]
    assert dt==[1]*(d-1)+[2,2]
    return len(rays),len(vertices),rank,dr,dt


def integer_points(t,a,b):
    def boundary(s,n):
        return (2*s+1)**n-(2*s-1)**n if s else 1
    return sum(boundary(s,a)*(2*(t-s)+1)**b for s in range(t+1))

for a,b in [(1,2),(1,3),(1,4),(2,2),(2,3),(3,3)]:
    output=invariants(a,b)
    d=a+b
    vals=[integer_points(t,a,b) for t in range(d+1)]
    vol=sum((-1)**(d-i)*comb(d,i)*vals[i] for i in range(d+1))
    assert vol == 2**d*factorial(a)*factorial(b), (a,b,vol)
    print('CHECK_OK',a,b,'rays',output[0], 'vertices',output[1],
          'PL_rank',output[2], 'Cl_torsion',output[3],
          'ClPic_torsion',output[4], 'anticanonical_degree',vol)
print('COMPLETE_BIPARTITE_TORIC_LATTICES_OK')
