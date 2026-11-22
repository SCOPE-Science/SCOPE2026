"""Finite exact checks for symmetric boundary-column polytopes of polygon triangulations.

This code tests finitely many instances; universal results use the mathematical proof.
"""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from math import isclose
import sympy as sp

@lru_cache(maxsize=None)
def triangulations(vertices):
    if len(vertices) < 3:
        return ((),)
    a,b=vertices[0],vertices[-1]
    out=[]
    for j in range(1,len(vertices)-1):
        left=triangulations(vertices[:j+1]); right=triangulations(vertices[j:])
        for L in left:
            for R in right:
                out.append(((a,vertices[j],b),)+L+R)
    return tuple(out)

def boundary_gram(triangles):
    boundaries=[]
    for i,j,k in triangles:
        boundaries.append({(i,j):1,(j,k):1,(i,k):-1})
    return sp.Matrix(len(triangles),len(triangles),lambda i,j: sum(v*boundaries[j].get(e,0) for e,v in boundaries[i].items()))

def adjacency(triangles):
    E=[]
    for T in triangles:
        a,b,c=T
        E.append({(a,b),(b,c),(a,c)})
    n=len(E)
    return sp.Matrix(n,n,lambda i,j: int(i!=j and len(E[i]&E[j])==1))

def path_phi(n):
    G=3*sp.eye(n)-sp.Matrix(n,n,lambda i,j:int(abs(i-j)==1))
    return (sp.ones(1,n)*G.inv()*sp.ones(n,1))[0]

def verify():
    gram_cases=0; face_cases=0; radius_cases=0; strict_cases=0
    for n in range(1,7):
        target=path_phi(n)
        ts=triangulations(tuple(range(n+2)))
        from math import comb
        assert len(ts)==sp.binomial(2*n,n)//(n+1)
        for triangles in ts:
            G=boundary_gram(triangles)
            A=adjacency(triangles)
            assert G==3*sp.eye(n)-A
            assert G.det()>0
            gram_cases+=1
            inverse=G.inv()
            allpos=(sp.ones(1,n)*inverse*sp.ones(n,1))[0]
            degrees=[sum(A[i,j] for j in range(n)) for i in range(n)]
            assert allpos>=target
            if max(degrees,default=0)>2:
                assert allpos>target
                strict_cases+=1
            else:
                assert allpos==target
            radius_cases+=1
            if n>=2:
                for signs in product([-1,1],repeat=n):
                    s=sp.Matrix(signs)
                    norm=(s.T*inverse*s)[0]
                    assert norm<=allpos
                    if abs(sum(signs))<n:
                        assert norm<allpos
                    face_cases+=1
    print('PASS exact constructed triangulations',gram_cases,'strict nonpath comparisons',strict_cases,'inradius comparisons',radius_cases,'facet-norm comparisons',face_cases)
    for n in range(1,12):
        lam=(sp.Integer(3)+sp.sqrt(5))/2
        formula=sp.simplify(n-2*sum(lam**j for j in range(1,n+1))/(1+lam**(n+1)))
        assert sp.simplify(formula-path_phi(n))==0
    print('PASS radical Green-sum formula n=1..11')
    p4=path_phi(4)
    s4=(sp.ones(1,4)*(3*sp.eye(4)-sp.Matrix([[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]])).inv()*sp.ones(4,1))[0]
    assert p4==sp.Rational(14,5) and s4==3
    print('PASS four-triangle witness: path',p4,'three-arm star',s4)

if __name__=='__main__':
    verify()
