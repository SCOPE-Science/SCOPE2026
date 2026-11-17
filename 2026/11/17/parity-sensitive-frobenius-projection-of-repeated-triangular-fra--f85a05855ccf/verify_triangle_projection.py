"""Exact certificates for the Frobenius projection of disjoint half-triangles.

Run with Python 3; NumPy and SciPy are optional for the independent QP check.
The exact checks use only the standard library.
"""
from fractions import Fraction as F
from itertools import combinations


def target(r):
    n = 3 * r
    return [[F(0) if i // 3 != j // 3 or i == j else F(1, 2)
             for j in range(n)] for i in range(n)]


def projection(r):
    if r % 2 == 0:
        a = c = F(1, 3 * (3*r - 2))
    else:
        a, c = F(1, 3*r), F(1, 9*r)
    b = F(1, 3)
    n = 3 * r
    return [[a if i == j else (b if i//3 == j//3 else c)
             for j in range(n)] for i in range(n)]


def distance_sq(r):
    return (F(r, 6) + (F(r, 3*(3*r-2)) if r % 2 == 0
                        else F(r+2, 9*r)))


def involutions(n):
    """Enumerate involutions as tuple pairs, including singleton loops."""
    def rec(rest, pairs, fixed):
        if not rest:
            yield pairs, fixed
            return
        i = rest[0]
        yield from rec(rest[1:], pairs, fixed + (i,))
        for j in rest[1:]:
            yield from rec(tuple(x for x in rest[1:] if x != j),
                           pairs + ((i,j),), fixed)
    yield from rec(tuple(range(n)), (), ())


def dot(U,V):
    return sum((x*y for row_u,row_v in zip(U,V)
                for x,y in zip(row_u,row_v)), F(0))


def exact_check(r, exhaustive=False):
    n = 3*r
    A, Y = target(r), projection(r)
    assert all(sum(row) == 1 for row in Y)
    assert all(Y[i][j] == Y[j][i] for i in range(n) for j in range(n))
    assert all(Y[i][j] >= 0 for i in range(n) for j in range(n))
    R = [[A[i][j]-Y[i][j] for j in range(n)] for i in range(n)]
    assert dot(R,R) == distance_sq(r)
    contact = dot(R,Y)
    a, b, c = Y[0][0], Y[0][1], (Y[0][3] if r>=2 else F(0))
    # The next test is exact and dominates every possible involution.
    for internal in range(r+1):
        for cross in range((n-2*internal)//2+1):
            fixed = n-2*(internal+cross)
            score = -a*fixed + 2*(F(1,2)-b)*internal - 2*c*cross
            assert score <= contact, (r,internal,cross,score,contact)
    # Check the explicit mixture's three entry classes independently.
    if r % 2 == 0:
        p = F(1,3*r-2)
        q = (1-p)/F(r-1)
    else:
        p = F(1,r)
        q = (F(1)-p)/F(r-1) if r>1 else F(0)
    assert a == p/3 and b == F(1,3)
    if r>1: assert c == q/9
    count = equal = 0
    if exhaustive:
        for pairs, fixed_points in involutions(n):
            internal = sum(i//3 == j//3 for i,j in pairs)
            cross = len(pairs)-internal
            score = -a*len(fixed_points) + 2*(F(1,2)-b)*internal - 2*c*cross
            assert score <= contact
            count += 1
            equal += score == contact
        assert equal > 0
    return count,equal


def independent_qp(r):
    import numpy as np
    from scipy.optimize import minimize, LinearConstraint, Bounds
    n=3*r; A=np.array(target(r),float); Y=np.array(projection(r),float)
    ij=[(i,j) for i in range(n) for j in range(i,n)]
    m=len(ij)
    weights=np.array([1 if i==j else 2 for i,j in ij],float)
    target_v=np.array([A[i,j] for i,j in ij])
    initial=np.array([Y[i,j] for i,j in ij])
    rows=np.zeros((n,m))
    for t,(i,j) in enumerate(ij):
        rows[i,t]=1; rows[j,t]=1
    bloss=[]; upper=[]
    for k in range(3,n+1,2):
        for S in combinations(range(n),k):
            s=set(S)
            bloss.append([int(i!=j and i in s and j in s) for i,j in ij])
            upper.append((k-1)/2)
    con=[LinearConstraint(rows,np.ones(n),np.ones(n))]
    if bloss:
        con.append(LinearConstraint(np.asarray(bloss,float),-np.inf,np.asarray(upper,float)))
    fun=lambda z:np.dot(weights,(z-target_v)**2)
    jac=lambda z:2*weights*(z-target_v)
    result=minimize(fun,initial+1e-5*np.random.default_rng(r).normal(size=m),
                    jac=jac,bounds=Bounds(np.zeros(m),np.inf),constraints=con,
                    method='SLSQP',options={'ftol':1e-11,'maxiter':500})
    assert result.success, result.message
    assert abs(result.fun-float(distance_sq(r))) < 2e-7, (r,result.fun)
    assert np.max(np.abs(result.x-initial)) < 2e-5
    return result.fun,float(np.max(np.abs(result.x-initial)))


if __name__ == '__main__':
    total=0
    for r in range(1,26):
        count,equal=exact_check(r,exhaustive=(r<=4))
        total+=count
        print('r=%02d n=%02d squared=%s tested_involutions=%d tight=%d' %
              (r,3*r,str(distance_sq(r)),count,equal))
    qp=[]
    for r in (1,2,3):
        val,err=independent_qp(r)
        qp.append((r,round(val,10),err))
    print('TRIANGLE_INVOLUTION_PROJECTION_PASS exact_r=1..25 exhaustive_involutions=%d qp=%s' % (total,qp))
