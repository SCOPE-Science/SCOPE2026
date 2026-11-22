"""Exact reproducibility checks for two-contact random pair averaging."""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matrix_for_edge(n, e):
    a = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    u, v = e
    for i, j in ((u,u),(v,v)): a[i][j] -= F(1,2)
    for i, j in ((u,v),(v,u)): a[i][j] += F(1,2)
    return a


def tr(x): return sum(x[i][i] for i in range(len(x)))


def q_value(edges, p):
    z = sum(t*t for t in p)
    for a,b in combinations(range(len(edges)), 2):
        if set(edges[a]) & set(edges[b]): z += F(1,2)*p[a]*p[b]
    return z


def expected_exact(n, edges, p):
    mats = [matrix_for_edge(n, edge) for edge in edges]
    # Covariance I - J/n, and orthogonal projections, hence tr(P_a P_b)-1.
    return sum(p[a]*p[b]*(tr(matmul(mats[a], mats[b]))-1)
               for a in range(len(edges)) for b in range(len(edges)))


def solve(a, b):
    n = len(b)
    z = [list(map(F,row)) + [F(b[i])] for i,row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if z[i][k])
        z[k],z[pivot]=z[pivot],z[k]
        d = z[k][k];z[k]=[t/d for t in z[k]]
        for i in range(n):
            if i!=k:
                d=z[i][k]
                z[i]=[z[i][j]-d*z[k][j] for j in range(n+1)]
    return [row[-1] for row in z]


def path_q(m):
    b=[[F(int(i==j))+F(int(abs(i-j)==1),4) for j in range(m)] for i in range(m)]
    return solve(b, [1]*m)


def path_formula(m):
    r = -2+sqrt(3)
    return [(2/3)*(1-r**i)*(1-r**(m+1-i))/(1+r**(m+1)) for i in range(1,m+1)]


def main():
    checks=0
    for n in range(2,8):
        pairs=list(combinations(range(n),2))
        # Complete graph, path, cycle, star, selected subgraphs.
        types=[pairs, [(i,i+1) for i in range(n-1)], [(0,j) for j in range(1,n)]]
        if n>2: types.append([(i,(i+1)%n) for i in range(n)])
        for edges in types:
            m=len(edges)
            p=[F(i+1, m*(m+1)//2) for i in range(m)]
            assert sum(p)==1
            assert expected_exact(n,edges,p)==n-3+q_value(edges,p)
            checks+=1
    for m in range(1,31):
        q=path_q(m)
        assert all(v>0 for v in q)
        assert all(4*q[i]+(q[i-1] if i else 0)+(q[i+1] if i+1<m else 0)==4 for i in range(m))
        checks+=2
        f=path_formula(m)
        assert max(abs(float(v)-f[i]) for i,v in enumerate(q))<1.e-10
        checks+=1
        ps=[z/sum(q) for z in q]
        assert sum(ps)==1
        edges=[(i,i+1) for i in range(m)]
        assert q_value(edges,ps)==1/sum(q)
        checks+=2
        if m<=7:
            for i in range(m):
                assert q_value(edges,[F(int(j==i)) for j in range(m)])>=q_value(edges,ps)
                checks+=1
    q=path_q(3)
    assert q==[F(6,7),F(4,7),F(6,7)]; checks+=1
    ps=[F(3,8),F(1,4),F(3,8)]
    assert q_value([(0,1),(1,2),(2,3)],ps)==F(7,16); checks+=1
    assert F(4,9)-F(7,16)==F(1,144); checks+=1
    rho=2-sqrt(3)
    for m in [50,100,200]:
        # Test the boundary asymptotic independently of the exact solver.
        f=path_formula(m); sp=sum(f)
        assert abs(m*f[0]/sp-(1+rho)) < .03
        assert abs(m*f[1]/sp-(1-rho**2)) < .03
        checks+=2
    # Separate spectral-gap benchmark on a path: parabolic optimal probabilities.
    for n in range(2,31):
        c=F(6,n*(n*n-1))
        p=[c*i*(n-i) for i in range(1,n)]
        assert sum(p)==1 and all(v>0 for v in p)
        checks+=1
        x=[F(2*i-n-1,2) for i in range(1,n+1)]
        eigen=F(12,n*(n*n-1))
        y=[(p[i-1]*(x[i]-x[i-1]) if i else F(0))+
           (p[i]*(x[i]-x[i+1]) if i<n-1 else F(0)) for i in range(n)]
        assert y==[eigen*xi for xi in x]
        checks+=1
        assert sum(xi*xi for xi in x)==F(n*(n*n-1),12)
        checks+=1
    print('PASS:',checks,'exact assertions for two-contact trace, path optimum and spectral-gap benchmark')

if __name__=='__main__':main()
