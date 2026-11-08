"""Reproducibility checks for the uniform-vertex matching-polytope covariance theorem."""
import itertools
import math
from fractions import Fraction


def matching_counts(n):
    return sum(math.comb(n,k)**2 * math.factorial(k) for k in range(n+1))


def exact_eigenvalues(n):
    counts=[matching_counts(j) for j in (n,n-1,n-2)]
    mu=Fraction(counts[1],counts[0]); eta=Fraction(counts[2],counts[0])
    return (mu - n*n*mu*mu + (n-1)**2*eta,
            mu-(n-1)*eta,mu+eta)


def enumerate_vertices(n):
    for k in range(n+1):
        for rows in itertools.combinations(range(n),k):
            for cols in itertools.permutations(range(n),k):
                v=[0]*(n*n)
                for i,j in zip(rows,cols):v[i*n+j]=1
                yield v


def direct_covariance(n):
    verts=list(enumerate_vertices(n)); t=len(verts); d=n*n
    assert t==matching_counts(n)
    means=[Fraction(sum(v[a] for v in verts),t) for a in range(d)]
    cov=[[Fraction(sum(v[a]*v[b] for v in verts),t)-means[a]*means[b]
          for b in range(d)] for a in range(d)]
    e00,er,ei=exact_eigenvalues(n)
    ones=[1]*d
    # Each matrix in the row, column, interaction spaces is an eigenvector.
    test=[(ones,e00)]
    for a in range(n-1):
        row=[(1 if i==a else -1 if i==n-1 else 0) for i in range(n) for j in range(n)]
        col=[(1 if j==a else -1 if j==n-1 else 0) for i in range(n) for j in range(n)]
        test.extend([(row,er),(col,er)])
    for i in range(n-1):
        for j in range(n-1):
            v=[0]*d;v[i*n+j]=1;v[i*n+n-1]=-1
            v[(n-1)*n+j]=-1;v[n*n-1]=1
            test.append((v,ei))
    assert len(test)==n*n
    for v,lam in test:
        got=[sum(cov[a][b]*v[b] for b in range(d)) for a in range(d)]
        assert got==[lam*u for u in v]
    assert 0<e00<er<ei
    return tuple(float(z) for z in (e00,er,ei))


def finite_laguerre_zeros():
    from scipy.special import roots_laguerre
    for n in range(2,16):
        xs,_=roots_laguerre(n)
        assert all(x>0 for x in xs)
        assert all(xs[i]<xs[i+1] for i in range(n-1))


def large_n_checks():
    import numpy as np
    from scipy.special import gammaln,logsumexp
    for n in (1000,5000,10000):
        d=np.arange(n+1)
        logs=gammaln(n+1)-gammaln(n-d+1)-2*gammaln(d+1)
        p=np.exp(logs-logsumexp(logs)); ed=float(np.dot(d,p))
        vd=float(np.dot((d-ed)**2,p)); ek=n-ed
        # Moments of K and edge indicators; stable formulas avoid cancellation.
        er=float(np.dot(d*(n-d),p))/(n*n*(n-1))
        e0=vd/(n*n)
        mu=ek/(n*n)
        eta=float(np.dot((n-d)*(n-d-1),p))/(n*n*(n-1)**2)
        ei=mu+eta
        assert abs(ed-math.sqrt(n)+.75)<.4/math.sqrt(n)
        assert abs(vd-.5*math.sqrt(n)+.5)<.4/math.sqrt(n)
        assert abs(n**1.5*e0-.5)<.12
        assert abs(n**1.5*er-1)<.12
        assert abs(n*ei-1)<.12
        assert abs(ei/e0/math.sqrt(n)-2)<.06
        assert 0<e0<er<ei
        print('n=',n, 'scaled:', tuple(round(x,6) for x in (n**1.5*e0,n**1.5*er,n*ei,ei/e0/math.sqrt(n))))


if __name__=='__main__':
    for n in range(2,5):
        print('n=',n,'finite exact:',direct_covariance(n))
    finite_laguerre_zeros()
    large_n_checks()
    print('PARTIAL_PERMUTATION_VERTEX_COVARIANCE_CHECKS_PASSED')
