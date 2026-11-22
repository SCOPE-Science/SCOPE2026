"""Exhaustive finite checks for the joint opposite-product fiber theorem.

Run with Python 3, no external packages. The theorem is over all finite
fields; the computation tests prime fields, with a separate algebraic proof
for arbitrary extension fields. All ordered factors are nonzero rank-one
square-zero matrices; all multiplication is literal matrix multiplication.
"""
from collections import Counter
from itertools import product


def matmul(a, b, n, q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def rank(a, n, q):
    rows = [list(a[i*n:(i+1)*n]) for i in range(n)]
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, n) if rows[i][j] % q), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        factor = pow(rows[r][j], -1, q)
        rows[r] = [(x * factor) % q for x in rows[r]]
        for i in range(n):
            if i == r:
                continue
            c = rows[i][j]
            rows[i] = [(x-c*y) % q for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == n:
            break
    return r


def orbit(n, q):
    vectors = [x for x in product(range(q), repeat=n) if any(x)]
    result=[]
    for u in vectors:
        if next(c for c in u if c)!=1:
            continue
        for v in vectors:
            if sum(a*b for a, b in zip(u, v)) % q:
                continue
            A=tuple(u[i]*v[j] % q for i in range(n) for j in range(n))
            assert not any(matmul(A, A, n, q))
            result.append(A)
    assert len(set(result))==len(result)
    return result


def predicted(n,q):
    N=(q**n-1)*(q**(n-1)-1)//(q-1)
    L=(q**(n-1)-1)//(q-1)
    K=q**(n-1)*(q**(n-2)-1)
    Z=N*((q**(n-1)-1)+(L-1)*(q**(n-2)-1))
    n_joint_noncentral=(q**n-1)*q**(n-1)*L*q**(n-2)
    return N,K,Z,n_joint_noncentral


def category(P,Q,n,q):
    z=(0,)*(n*n)
    if P==z and Q==z:
        return 'both_zero'
    if Q==z and P!=z:
        if rank(P,n,q)==1 and matmul(P,P,n,q)==z:
            return 'one_nonzero'
        return 'invalid'
    if P==z and Q!=z:
        if rank(Q,n,q)==1 and matmul(Q,Q,n,q)==z:
            return 'one_nonzero'
        return 'invalid'
    if rank(P,n,q)==rank(Q,n,q)==1:
        tP=sum(P[i*n+i] for i in range(n))%q
        tQ=sum(Q[i*n+i] for i in range(n))%q
        if tP==tQ and tP!=0 and matmul(P,Q,n,q)==z and matmul(Q,P,n,q)==z:
            return 'orthogonal_pair'
    return 'invalid'


def verify(n,q):
    elements=orbit(n,q)
    counts=Counter()
    # Two independent literal multiplications are performed for every pair.
    for A in elements:
        for B in elements:
            counts[(matmul(A,B,n,q),matmul(B,A,n,q))]+=1
    N,K,Z,H=predicted(n,q)
    assert len(elements)==N,(n,q,'orbit',len(elements),N)
    classes=Counter()
    for (P,Q),multiplicity in counts.items():
        c=category(P,Q,n,q)
        assert c!='invalid',(n,q,P,Q)
        expected={'both_zero':Z,'one_nonzero':K,'orthogonal_pair':q-1}[c]
        assert multiplicity==expected,(n,q,c,P,Q,multiplicity,expected)
        classes[c]+=1
    assert classes['both_zero']==1
    assert classes['one_nonzero']==(2*N if K else 0),classes
    assert classes['orthogonal_pair']==H,(n,q,classes,H)
    assert sum(counts.values())==N**2
    assert Z+2*N*K+H*(q-1)==N**2
    print('PASS',f'n={n}',f'q={q}',f'factor_count={N}',
          f'joint_targets={len(counts)}',f'zero_fiber={Z}',
          f'one_nonzero_fiber={K}',f'orthogonal_fiber={q-1}',
          f'orthogonal_targets={H}')


if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,5),(3,2),(3,3),(3,5),(4,2)]:
        verify(n,q)
