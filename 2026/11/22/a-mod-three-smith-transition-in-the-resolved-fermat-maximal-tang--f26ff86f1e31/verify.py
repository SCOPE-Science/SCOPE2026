"""Exact integer sanity checks for the Fermat maximal-contact boundary theorem.

The written integral presentation proves every degree. These finite tests independently
rebuild the graph and compare its reduced Laplacian Smith form to the five-generator
presentation and the claimed complete invariant factors.
"""
from sympy import Matrix, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from math import prod


def graph_laplacian(d):
    n = 3 * d + 3
    L = zeros(n)
    def add(i,j):
        L[i,i] += 1
        L[j,j] += 1
        L[i,j] -= 1
        L[j,i] -= 1
    for a in range(3):
        for b in range(a+1,3):
            for i in range(d):
                for j in range(d):
                    add(a*d+i, b*d+j)
        for i in range(d):
            add(a*d+i,3*d+a)
    return L


def factors(M):
    D = smith_normal_form(M, domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.rows,D.cols))]


def core(d):
    m=2*d+1
    return Matrix([[m,0,0,0,0],
                   [0,m,0,0,0],
                   [0,0,m,0,0],
                   [-1,-d,-d,2*d*d,-d*d],
                   [-d,-1,-d,-d*d,2*d*d]])


def expected(d):
    m=2*d+1
    if m%3:
        return sorted([1]*5+[m]*(3*d-5)+[d*d*m,3*d*d*m])
    return sorted([1]*4+[3]+[m]*(3*d-5)+[d*d*m]*2)


if __name__=='__main__':
    for d in range(3,13):
        L=graph_laplacian(d)
        n=3*d+3
        assert (L*Matrix([1]*n))==zeros(n,1)
        assert sum(int(L[i,i]) for i in range(n))==2*(3*d*d+3*d)
        assert [int(L[i,i]) for i in range(3*d)]==[2*d+1]*(3*d)
        assert [int(L[i,i]) for i in range(3*d,n)]==[d]*3
        full=factors(L[:n-1,:n-1])
        small=factors(core(d))
        predicted=expected(d)
        assert full==predicted, (d,full,predicted)
        assert sorted([1]*3+[2*d+1]*(3*(d-2))+small)==full
        assert prod(full)==3*d**4*(2*d+1)**(3*d-3)
        print(f'd={d}: {len([z for z in full if z>1])} nontrivial factors; order verified')
    print('FERMAT_MAXIMAL_TANGENT_BOUNDARY_UNIFORM_INTEGRAL_GROUP_OK')
