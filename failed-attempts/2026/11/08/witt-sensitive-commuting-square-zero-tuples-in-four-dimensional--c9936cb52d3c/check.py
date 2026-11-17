"""Direct finite prime-field checks for commuting square-zero orthogonal tuples.

This program is independent of the counting proof. It enumerates all skew-adjoint
4-by-4 matrices over selected prime fields and multiplies them literally.
"""
from itertools import product


def matmul(A, B, p):
    return tuple(sum(A[i*4+k]*B[k*4+j] for k in range(4)) % p
                 for i in range(4) for j in range(4))


def rank(A, p):
    rows = [list(A[i*4:(i+1)*4]) for i in range(4)]
    h = 0
    for j in range(4):
        piv = next((i for i in range(h,4) if rows[i][j]%p),None)
        if piv is None:
            continue
        rows[h],rows[piv] = rows[piv],rows[h]
        inv = pow(rows[h][j],-1,p)
        rows[h] = [(v*inv)%p for v in rows[h]]
        for i in range(4):
            if i != h:
                v = rows[i][j]
                if v:
                    rows[i] = [(rows[i][k]-v*rows[h][k])%p for k in range(4)]
        h += 1
    return h


def nonsquare(p):
    sq = {j*j%p for j in range(p)}
    return next(d for d in range(1,p) if d not in sq)


def form_inverse(p, split):
    if split:
        return (0,0,1,0, 0,0,0,1, 1,0,0,0, 0,1,0,0)
    d=nonsquare(p)
    return (0,1,0,0, 1,0,0,0, 0,0,1,0, 0,0,0,-pow(d,-1,p)%p)


def skew_symmetric(v,p):
    S=[0]*16
    pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    for x,(i,j) in zip(v,pairs):
        S[4*i+j]=x
        S[4*j+i]=-x%p
    return tuple(S)


def square_zero_set(p, split):
    Hinv=form_inverse(p,split)
    zero=(0,)*16
    sqzero=[]
    for v in product(range(p),repeat=6):
        X=matmul(Hinv,skew_symmetric(v,p),p)
        if matmul(X,X,p)==zero:
            assert X==zero or rank(X,p)==2
            sqzero.append(X)
    return sqzero


def predicted(q, r, split):
    if not split: return (1,1,0)
    zero=1+2*(q+1)*(q**r-1)
    mixed=(q+1)**2*((2*q-1)**r -2*q**r+1)
    return zero+mixed,zero,mixed


def check(q,split,r_max):
    mats=square_zero_set(q,split)
    exp=1+2*(q*q-1) if split else 1
    assert len(mats)==exp, (q,split,len(mats),exp)
    products={}
    for i,A in enumerate(mats):
        for j,B in enumerate(mats):
            AB=matmul(A,B,q)
            BA=matmul(B,A,q)
            if AB==BA:
                assert rank(AB,q) in (0,1)
                products[i,j]=(AB==(0,)*16)
    for r in range(2,r_max+1):
        total=zero=mixed=0
        for ids in product(range(len(mats)),repeat=r):
            if all((ids[i],ids[j]) in products for i in range(r) for j in range(i+1,r)):
                total+=1
                if all(products[ids[i],ids[j]] for i in range(r) for j in range(i+1,r)):
                    zero+=1
                else: mixed+=1
        assert (total,zero,mixed)==predicted(q,r,split), (q,split,r,total,zero,mixed,predicted(q,r,split))
        print(f'q={q} type={"split" if split else "nonsplit"} r={r}: total={total}, all-products-zero={zero}, nonzero-product={mixed}: PASS')


if __name__=='__main__':
    for q,maxr in [(3,4),(5,3),(7,2)]:
        for split in (False,True):
            check(q,split,maxr)
    print('ALL_ORTHOGONAL_COMMUTING_SQUARE_ZERO_TESTS_PASS')
