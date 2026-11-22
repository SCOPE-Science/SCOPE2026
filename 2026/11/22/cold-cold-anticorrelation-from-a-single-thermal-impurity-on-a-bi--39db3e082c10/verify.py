"""Exact stationary second-moment verification for KMP redistribution on a biclique.
Requires Python 3 and sympy; run: python verify.py
"""
from itertools import combinations_with_replacement
import sympy as sp


def formulas(n, g):
    r = (n**3*(2*n-1) + n**2*(8*n-3)*g + n*(6*n+1)*g**2
         - 4*(n-1)*g**3 - 4*g**4)
    db = 4*(n+g)**2*(n+2*g)**2*(2*n*n+(8*n-1)*g+6*g*g)
    s = (128*g**6 +(476*n-88)*g**5 + (740*n*n-164*n)*g**4
         +(638*n**3-131*n*n+2*n)*g**3
         +(332*n**4-85*n**3+10*n*n)*g*g
         +(98*n**5-39*n**4+6*n**3)*g + 12*n**6-6*n**5)
    dp = (4*(n+g)**2*(n+2*g)*(4*g+3*n)
          *(2*n*n+(8*n-1)*g+6*g*g)
          *(2*n*n+(11*n-2)*g+12*g*g))
    return r/db, s/dp


def direct_moments(n, g, cold, delta):
    """No orbit reduction: independently build all exact first/second moment equations."""
    N = 2*n
    neighbours = [[j for j in range(N) if (i < n) != (j < n)] for i in range(N)]
    bath = [cold+delta]+[cold]*(N-1)
    first = sp.zeros(N)
    source = sp.zeros(N, 1)
    for i in range(N):
        first[i,i] = g+sp.Rational(len(neighbours[i]),2)
        for j in neighbours[i]:first[i,j] -= sp.Rational(1,2)
        source[i] = g*bath[i]
    mean = first.inv()*source
    pairs = list(combinations_with_replacement(range(N),2))
    where = {ij:k for k,ij in enumerate(pairs)}
    mat = sp.zeros(len(pairs))
    rhs = sp.zeros(len(pairs),1)
    def add(row,i,j,coeff):mat[row,where[tuple(sorted((i,j)))]] += coeff
    for row,(i,j) in enumerate(pairs):
        if i==j:
            add(row,i,i,g)
            rhs[row] += 2*g*bath[i]**2
            for k in neighbours[i]:
                add(row,i,i,sp.Rational(2,3))
                add(row,i,k,-sp.Rational(2,3))
                add(row,k,k,-sp.Rational(1,3))
        else:
            add(row,i,j,2*g)
            rhs[row] += g*(bath[i]*mean[j]+bath[j]*mean[i])
            for k in neighbours[i]:
                if k==j:
                    add(row,i,i,-sp.Rational(1,6))
                    add(row,j,j,-sp.Rational(1,6))
                    add(row,i,j,sp.Rational(4,6))
                else:
                    add(row,i,j,sp.Rational(1,2))
                    add(row,k,j,-sp.Rational(1,2))
            for k in neighbours[j]:
                if k!=i:
                    add(row,i,j,sp.Rational(1,2))
                    add(row,i,k,-sp.Rational(1,2))
    m2 = mat.inv()*rhs
    return (lambda i,j: sp.factor(m2[where[tuple(sorted((i,j)))]]-mean[i]*mean[j])), (mean, mat, rhs, m2)


if __name__=='__main__':
    case_count = 0
    for n in [2,3,4]:
        for rate in [sp.Rational(1,2),sp.Rational(2),sp.Rational(5),sp.Rational(12)]:
            cov, _ = direct_moments(n,rate,sp.Rational(2),sp.Rational(3))
            b,p = formulas(sp.Integer(n),rate)
            assert sp.factor(cov(n,n+1) - 9*b)==0, (n,rate,'BB')
            assert sp.factor(cov(1,n)-9*p)==0, (n,rate,'PQ')
            if n>=3:
                assert sp.factor(cov(1,2) - sp.Rational(n,n+2*rate)*cov(1,n))==0
            case_count += 1
    x=sp.symbols('x',positive=True)
    n=sp.symbols('n',positive=True)
    # Coefficients of the quartic have exactly one sign variation for integers n>=2.
    r=n**3*(2*n-1)+n*n*(8*n-3)*x+n*(6*n+1)*x*x-4*(n-1)*x**3-4*x**4
    assert sp.factor(sp.limit(r.subs(x,x*n)/n**4,n,sp.oo)) == -2*(x+1)**2*(2*x*x-2*x-1)
    print('BIPARTITE_KMP_EXACT_MOMENTS_PASSED cases=',case_count)
