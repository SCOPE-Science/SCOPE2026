"""Independent exact-field verification of prescribed rank-one sandwich commutator fibers.
Run: python checker.py
Small finite fields are constructed directly, including GF(4).
"""
from collections import Counter
from itertools import product


def fops(q):
    if q in (2, 3, 5):
        return (lambda a,b:(a+b)%q, lambda a,b:(a-b)%q,lambda a,b:(a*b)%q)
    if q == 4:
        def mul(a,b):
            r=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&(b>>j)&1:r ^= 1<<(i+j)
            if r & 8:r ^= 0b1110  # x^3=(x+1)*x = x^2+x, mod x^2+x+1
            if r & 4:r ^= 0b111  # x^2=x+1
            return r
        return (lambda a,b:a^b, lambda a,b:a^b,mul)
    raise ValueError(q)


def rank(rows, q):
    add,sub,mul=fops(q)
    A=[list(r) for r in rows]
    n=len(A);m=len(A[0]);i=0
    for j in range(m):
        pivot=next((k for k in range(i,n) if A[k][j]!=0),None)
        if pivot is None:continue
        A[i],A[pivot]=A[pivot],A[i]
        inv=next(v for v in range(1,q) if mul(v,A[i][j])==1)
        A[i]=[mul(inv,x) for x in A[i]]
        for k in range(n):
            if k!=i and A[k][j]:
                v=A[k][j]
                A[k]=[sub(x,mul(v,y)) for x,y in zip(A[k],A[i])]
        i+=1
        if i==n:break
    return i


def proposed_fiber(Z,m,n,q):
    alpha,beta=m-1,n-1
    if Z[0]!=0:return 0
    h=q**(2*alpha*beta)
    r=rank([Z[i*n:(i+1)*n] for i in range(m)],q)
    first_row=any(Z[j] for j in range(n))
    first_col=any(Z[i*n] for i in range(m))
    if r==0:
        K=(q**(alpha+beta+1)+q**(alpha+beta+2)
           -(q+1)*(q**alpha+q**beta)+q+q**(2*alpha)+q**(2*beta))
        return h*K
    if r==1:
        if not first_row and not first_col:return h*(q*q-1)*(q**alpha+q**beta-q)
        if not first_row:return h*(q*q-1)*q**alpha
        if not first_col:return h*(q*q-1)*q**beta
        return 0
    if r==2:
        if not first_row and not first_col:return h*q*(q*q-1)*(q-1)  # GL_2(q) = (q^2-1)(q^2-q)
        if first_row and first_col:return h*q*(q*q-1) # SL_2(q)
    return 0


def check(m,n,q):
    add,sub,mul=fops(q)
    matrices=list(product(range(q),repeat=m*n))
    observed=Counter()
    for X in matrices:
        for Y in matrices:
            z=tuple(sub(mul(X[i*n],Y[j]),mul(Y[i*n],X[j])) for i in range(m) for j in range(n))
            observed[z]+=1
    predicted={Z:proposed_fiber(Z,m,n,q) for Z in matrices}
    assert sum(predicted.values())==q**(2*m*n)
    assert all(observed[Z]==c for Z,c in predicted.items()),(m,n,q,next((Z,c,observed[Z]) for Z,c in predicted.items() if observed[Z]!=c))
    hist=Counter((rank([Z[i*n:(i+1)*n] for i in range(m)],q),predicted[Z]) for Z in matrices if predicted[Z]);
    print('CHECK_OK',m,n,q,'nonempty_target_fibers',len([v for v in predicted.values() if v]),'distinct_nonempty_fiber_sizes',len(set(v for v in predicted.values() if v)), 'pair_total',sum(predicted.values()))

if __name__=='__main__':
    for params in [(2,2,2),(2,3,2),(3,2,2),(3,3,2),(2,4,2),(2,2,3),(2,3,3),(2,2,4)]:check(*params)
    print('SANDWICH_PRESCRIBED_COMMUTATOR_FIBERS_VERIFIED')
