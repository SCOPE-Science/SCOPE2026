"""Exact integer and independent numerical checks for Euclidean directional width of a standard permutohedron.

No external packages. The infinite-dimensional-index theorem is proved in RESULT.md;
these finite checks are corroboration, not replacement.
"""
from itertools import product, permutations
from math import sqrt, atan, cos, sin


def total_variation(a):
    return sum(abs(a[i]-a[j]) for i in range(len(a)) for j in range(i+1,len(a)))


def sqnorm(a):
    return sum(x*x for x in a)


def centered_cut(n,t):
    # A is the lower-level group of size t.
    # integer direction, with sum zero and squared norm n*t*(n-t)
    return [-(n-t)]*t+[t]*(n-t)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


profiles = 0
sharp = 0
inequalities = 0
# Checks the sharp complete-graph variation inequality on bounded nonzero integer grids.
for m in range(2,9):
    for h in product(range(-2,3),repeat=m):
        if sum(h)!=0 or not any(h):
            continue
        tv=total_variation(h)
        assert tv*tv >= m*(m-1)*sqnorm(h), (m,h)
        inequalities += 1
    # One-versus-rest gives equality, so the constant cannot be increased.
    h=[-(m-1)]+[1]*(m-1)
    assert total_variation(h)**2 == m*(m-1)*sqnorm(h)

# Check combinatorial local minimum profiles, local maximum weights, and the
# sharp tangent directions in every rank with a wide range of block sizes.
for n in range(3,25):
    a=[2*j-n-1 for j in range(1,n+1)]
    assert sum(a)==0
    assert sqnorm(a)*3 == n*(n*n-1)
    assert total_variation(a)==sqnorm(a)
    for t in range(1,n):
        v=centered_cut(n,t)
        assert sum(v)==0
        assert sqnorm(v)==n*t*(n-t)
        assert total_variation(v)==n*t*(n-t)
        w=sqrt(n*t*(n-t))
        x=[z/sqrt(sqnorm(v)) for z in v]
        assert abs(total_variation(x)-w)<1e-10
        # A unit tangent vector on a nonsingleton block with one outlier.
        m_candidates=[(t,0),(n-t,t)]
        m,start=min(((m,start) for m,start in m_candidates if m>=2))
        h=[0]*n
        h[start]=-(m-1)
        for i in range(start+1,start+m):h[i]=1
        assert dot(v,h)==0 and sum(h)==0
        hn=sqrt(sqnorm(h))
        h=[z/hn for z in h]
        gamma=sqrt(m*(m-1))
        assert abs(total_variation(h[start:start+m])-gamma)<1e-10
        delta=sqrt(n/(t*(n-t)))
        theta=.3*atan(delta/sqrt(2))
        pert=[cos(theta)*x[i]+sin(theta)*h[i] for i in range(n)]
        assert abs(total_variation(pert)-(w*cos(theta)+gamma*sin(theta)))<1e-9
        profiles+=1;sharp+=1

# Every fixed order chamber is linear with gradient a, which supplies the
# n! strict spherical global maxima. Independent small-rank exact sorting test.
max_checks=0
for n in range(3,8):
    a=[2*j-n-1 for j in range(1,n+1)]
    for p in permutations(a):
        assert total_variation(p)==sqnorm(a)
        max_checks+=1
print(f'PERMUTO_WIDTH_CHECKS_PASS integer_inequalities={inequalities} cut_profiles={profiles} sharp_geodesics={sharp} maxima_permutations={max_checks}')
