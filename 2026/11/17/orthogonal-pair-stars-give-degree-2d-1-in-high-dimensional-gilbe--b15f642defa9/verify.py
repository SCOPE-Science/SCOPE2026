"""Finite checks of orthogonal-pair Gilbert-star subset inequalities.

The all-dimension result has an analytic proof; these computations are not a
substitute for its quantified inequalities or global network optimality.
"""
from itertools import combinations
from math import ceil, sqrt


def sufficient_even_k(p):
    assert 0.5 < p < 1.0
    q = 2*p - 1
    cutoff = max(1 / (2**(-q)-0.5), 4/(1-q))**(1/q)
    return max(4, 2*ceil(cutoff/2))


def worst_subset_sq(k, p, j):
    a2 = k**(2*p-2)
    return j*j*a2 + min(j,k-j)*(1-a2)


def check(k,p,eps=1e-9):
    assert k%2==0 and k>=4
    count=0
    for j in range(k+1):
        actual=worst_subset_sq(k,p,j)
        bound=j**(2*p)
        assert actual<=bound+eps*max(1,bound), (k,p,j,actual,bound)
        count+=1
    return count


def exact_subsets(k,p):
    m=k//2
    a=k**(p-1)
    b=sqrt(1-a*a)
    vectors=[]
    for i in range(m):
        for sgn in (-1,1):
            vec=[0.0]*(m+1)
            vec[0]=a
            vec[i+1]=sgn*b
            vectors.append(vec)
    count=0
    for j in range(k+1):
        worst=0
        for inds in combinations(range(k),j):
            summed=[sum(vectors[h][r] for h in inds) for r in range(m+1)]
            norm_sq=sum(v*v for v in summed)
            assert norm_sq<=j**(2*p)+1e-8,(k,p,j,inds,norm_sq,j**(2*p))
            worst=max(worst,norm_sq)
            count+=1
        assert abs(worst-worst_subset_sq(k,p,j))<=1e-7,(k,p,j,worst)
    assert count==2**k
    return count


def main():
    tests=0
    for p in (0.60,0.65,0.70,0.75,0.80,0.90,0.95,0.99):
        k=sufficient_even_k(p)
        assert k**(2*p-1)*(2**(-(2*p-1))-0.5)>=1-1e-9
        assert k**(2*p-1)*(1-(2*p-1))>=4-1e-9
        tests+=check(k,p)
        tests+=2
        # A nearby, larger even dimension must also meet the sufficient condition.
        tests+=check(k+2,p)
    # Independently enumerate actual ordered paired vectors when dimensions
    # are small enough for exhaustive subsets.
    for p in (0.9,0.95):
        for k in (6,8,10):
            tests+=exact_subsets(k,p)
    print('PASS: %d finite assertions/checks' % tests)


if __name__ == '__main__':
    main()
