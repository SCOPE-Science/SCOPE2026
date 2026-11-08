"""Exact finite checks for the covariance of vertices of complete-graph matching polytopes.
This checker corroborates an independent all-dimensional combinatorial proof."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, sqrt


def involution_numbers(n):
    out = [1, 1]
    for j in range(2, n + 1):
        out.append(out[-1] + (j - 1)*out[-2])
    return out


def matching_edge_sets(n):
    """Every matching exactly once, by the first unused vertex recurrence."""
    def visit(unused, selected):
        if not unused:
            yield selected
            return
        i = unused[0]
        yield from visit(unused[1:], selected)
        for k, j in enumerate(unused[1:]):
            yield from visit(unused[1:k+1] + unused[k+2:], selected + ((i,j),))
    yield from visit(tuple(range(n)), ())


def expected_eigenvalues(n):
    t = involution_numbers(n)
    aa = Q(t[n-2],t[n])
    bb = Q(t[n-4],t[n]) if n>=4 else Q(0)
    m = comb(n,2)
    lam0 = aa+Q((n-2)*(n-3),2)*bb-m*aa*aa
    lam1 = aa-(n-3)*bb
    lam2 = aa+bb
    return lam0,lam1,lam2


def exact_cov(n):
    edges = list(combinations(range(n),2))
    ei = {e:i for i,e in enumerate(edges)}
    m = len(edges)
    first = [0]*m
    second = [[0]*m for _ in range(m)]
    total=0
    for matching in matching_edge_sets(n):
        total+=1
        inds=[ei[e] for e in matching]
        for i in inds:
            first[i]+=1
            for j in inds:
                second[i][j]+=1
    assert total==involution_numbers(n)[n]
    mean=[Q(x,total) for x in first]
    C=[[Q(second[i][j],total)-mean[i]*mean[j]
        for j in range(m)] for i in range(m)]
    return edges,C,total


def matvec(M,x):
    return [sum((M[i][j]*x[j] for j in range(len(x))),Q(0)) for i in range(len(x))]


def check():
    sum_matchings=0
    basis_vectors=0
    all_t=involution_numbers(150)
    for n in range(4,10):
        edges,C,total=exact_cov(n)
        sum_matchings+=total
        m=len(edges)
        l0,l1,l2=expected_eigenvalues(n)
        assert Q(0)<l0<l1<l2
        a=Q(all_t[n-2],all_t[n]);b=Q(all_t[n-4],all_t[n]);p=Q(all_t[n-1],all_t[n]);p2=Q(all_t[n-3],all_t[n-2])
        assert l0==(1-n*p*p)/Q(2*(n-1))
        assert l1==(1-p)*p2/Q(n-1)
        assert l1-l0==n*(1-p)*(p2-p)/Q(2*(n-1))
        for i,e in enumerate(edges):
            for j,f in enumerate(edges):
                target= (a-a*a) if i==j else (-a*a if set(e)&set(f) else b-a*a)
                assert C[i][j]==target
        vec=[Q(1)]*m
        assert matvec(C,vec)==[l0]*m
        # Standard representation: edge weights x_i+x_j with sum_i x_i=0.
        for vertex in range(1,n):
            x=[Q(0)]*n
            x[0]=Q(1);x[vertex]=Q(-1)
            v=[x[i]+x[j] for i,j in edges]
            assert matvec(C,v)==[l1*z for z in v]
            basis_vectors+=1
        # Every four-cycle contrast is orthogonal to all star-sums.
        for a0,b0,c0,d0 in combinations(range(n),4):
            vv={tuple(sorted(e)):Q(z) for e,z in
                 [((a0,b0),1),((c0,d0),1),((a0,c0),-1),((b0,d0),-1)]}
            v=[vv.get(e,Q(0)) for e in edges]
            assert matvec(C,v)==[l2*z for z in v]
            basis_vectors+=1
    for n in range(4,151):
        l0,l1,l2=expected_eigenvalues(n)
        assert Q(0)<l0<l1<l2
        p=Q(all_t[n-1],all_t[n]);p2=Q(all_t[n-3],all_t[n-2])
        assert p2>p
        if n>=16:
            r=all_t[n]/all_t[n-1]
            assert sqrt(n)<r<sqrt(n)+1
            assert abs(r-sqrt(n)-0.5)<10/sqrt(n)
    print('COMPLETE_MATCHING_COVARIANCE_CHECKS_PASSED',
          'exact_vertices=',sum_matchings,'basis_checks=',basis_vectors,
          'parameter_cases=',147)

if __name__=='__main__':
    check()
