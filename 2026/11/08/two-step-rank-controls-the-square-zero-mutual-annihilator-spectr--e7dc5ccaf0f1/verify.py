"""Independent small-field enumeration for the fixed-matrix square-zero annihilator theorem.
Run with Python 3: python verify.py. No third-party packages required.
"""
from collections import Counter
from itertools import product
from math import prod


def add(a,b,q):
    return (a ^ b) if q == 4 else (a+b)%q

def neg(a,q):
    return a if q==4 else (-a)%q

def mul(a,b,q):
    if q != 4:
        return (a*b)%q
    c=0
    for i in range(2):
        if (b>>i)&1:
            c ^= a<<i
    for i in (2,):
        if (c>>i)&1:
            c ^= 0b111 << (i-2)
    return c

def inv(a,q):
    assert a
    for b in range(1,q):
        if mul(a,b,q)==1:
            return b
    raise AssertionError('non-field')

def mm(A,B,n,q):
    return tuple(sum([0]) if False else
        fold_sum([mul(A[i*n+k],B[k*n+j],q) for k in range(n)],q)
        for i in range(n) for j in range(n))

def fold_sum(vals,q):
    c=0
    for v in vals:
        c=add(c,v,q)
    return c

def rank(A,n,q):
    M=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if M[i][j]),None)
        if pivot is None:
            continue
        M[r],M[pivot]=M[pivot],M[r]
        z=inv(M[r][j],q)
        M[r]=[mul(z,v,q) for v in M[r]]
        for i in range(n):
            if i != r and M[i][j]:
                c=M[i][j]
                M[i]=[add(a,neg(mul(c,b,q),q),q) for a,b in zip(M[i],M[r])]
        r+=1
    return r

def rank_rect(vectors,q):
    if not vectors:return 0
    N=len(vectors[0]);M=[list(v) for v in vectors];m=len(M);r=0
    for j in range(N):
        i=next((i for i in range(r,m) if M[i][j]),None)
        if i is None:continue
        M[i],M[r]=M[r],M[i]
        z=inv(M[r][j],q)
        M[r]=[mul(z,v,q) for v in M[r]]
        for k in range(m):
            if k!=r and M[k][j]:
                c=M[k][j]
                M[k]=[add(x,neg(mul(c,y,q),q),q) for x,y in zip(M[k],M[r])]
        r+=1
    return r

def gb(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-j)-1 for j in range(k))
    den=prod(q**(k-j)-1 for j in range(k))
    return num//den

def gl(k,q):
    return prod(q**k-q**j for j in range(k))

def theorem(n,q,r,r2):
    delta=r-r2;k=n-r
    out=Counter()
    for b in range(n//2+1):
        for t in range(min(b,delta)+1):
            v=gl(b,q)*gb(delta,t,q)*gb(k-delta,b-t,q)*q**((delta-t)*(b-t))*gb(k-b+t,b,q)
            if v:out[(b,t)]=v
    return out

def one(A,n,q,squarezero):
    r=rank(A,n,q)
    r2=rank(mm(A,A,n,q),n,q)
    nvec=tuple(tuple(A[i*n+j] for i in range(n)) for j in range(n))
    counts=Counter();zero=(0,)*(n*n)
    for B,b,Bvec in squarezero:
        if mm(A,B,n,q)!=zero or mm(B,A,n,q)!=zero:
            continue
        t=rank_rect(nvec,q)+b-rank_rect(nvec+Bvec,q)
        counts[(b,t)]+=1
    pred=theorem(n,q,r,r2)
    assert counts==pred,(n,q,A,counts,pred)
    bound=(n-r2)//2
    assert max(b for b,t in counts)==bound
    return (r,r2,dict(sorted(counts.items())))

def checks(n,q,As):
    squares=[];zero=(0,)*(n*n)
    for v in product(range(q),repeat=n*n):
        if mm(v,v,n,q)==zero:
            rv=rank(v,n,q)
            cols=tuple(tuple(v[i*n+j] for i in range(n)) for j in range(n))
            squares.append((v,rv,cols))
    for A in As:
        assert len(A)==n*n
        print('n={} q={} A={} stats={}'.format(n,q,A,one(A,n,q,squares)))
    # Four matrices of distinct types: actual enumeration does not assume their canonical forms.
    print('square-zero pool n={} q={} count={}'.format(n,q,len(squares)))

def I(n,blocks):
    rows=[[0]*n for i in range(n)]
    p=0
    for kind,size in blocks:
        if kind=='I':
            for i in range(p,p+size):rows[i][i]=1
        if kind=='J':
            for i in range(p,p+size-1):rows[i][i+1]=1
        p+=size
    assert p==n
    return tuple(x for row in rows for x in row)

if __name__=='__main__':
    checks(2,4,[I(2,[('I',1),('0',1)]),I(2,[('J',2)]),I(2,[('0',2)])])
    checks(3,3,[I(3,[('I',2),('0',1)]),I(3,[('J',3)]),I(3,[('J',2),('0',1)]),I(3,[('I',1),('0',2)])])
    checks(4,2,[I(4,[('I',2),('0',2)]),I(4,[('J',2),('J',2)]),I(4,[('J',3),('0',1)]),I(4,[('J',2),('I',1),('0',1)]),I(4,[('I',4)])])
    print('VERIFY_OK')
