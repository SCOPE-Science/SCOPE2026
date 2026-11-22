"""Independent finite-field checks of simultaneous sandwich-idempotent commutant rank spectra.

Usage: python checker.py. Enumerates small prime-field cases directly from matrix multiplication.
The general formula is proved separately; finite tests do not certify all dimensions or fields.
"""
from itertools import product
from math import prod
from collections import Counter


def matmul(A,B,q):
    m = len(A); k = len(B); n = len(B[0])
    return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(k)) % q for j in range(n)) for i in range(m))


def matrix_rank(M,q):
    if not M: return 0
    rows = [list(row) for row in M]
    m=len(rows); n=len(rows[0]); k=0
    for j in range(n):
        i=next((i for i in range(k,m) if rows[i][j]%q),None)
        if i is None:continue
        rows[k],rows[i]=rows[i],rows[k]
        inv=pow(rows[k][j],-1,q)
        rows[k]=[(inv*x)%q for x in rows[k]]
        for t in range(m):
            if t!=k and rows[t][j]:
                c=rows[t][j]
                rows[t]=[(x-c*y)%q for x,y in zip(rows[t],rows[k])]
        k+=1
        if k==m:break
    return k


def matrices(m,n,q):
    for vals in product(range(q),repeat=m*n):
        yield tuple(tuple(vals[i*n:(i+1)*n]) for i in range(m))


def mul(A,B,C,q):return matmul(matmul(A,B,q),C,q)


def rank_poly(a,b,q):
    out=Counter({0:1})
    for j in range(1,min(a,b)+1):
        num=prod((q**a-q**i)*(q**b-q**i) for i in range(j))
        den=prod(q**j-q**i for i in range(j))
        assert num%den==0
        out[j]=num//den
    return out


def polyprod(A,B):
    out=Counter()
    for i,x in A.items():
        for j,y in B.items():out[i+j]+=x*y
    return out


def gl(r,q):return prod(q**r-q**i for i in range(r))


def expected_mult(m,n,r,q,t):
    tau=m+n-2*r
    labels=list(product((0,1),repeat=t))
    out=Counter()
    def rec(i,left,ds):
        if i==len(labels)-1:
            counts=ds+[left]
            D=r-counts[0]
            mult=gl(r,q)//prod(gl(d,q) for d in counts)
            mult*=q**(tau*D)
            if mult:
                out[tuple(counts)]+=mult
            return
        for d in range(left+1):rec(i+1,left-d,ds+[d])
    rec(0,r,[])
    return labels,out


def sig_profile(tup,r,q):
    t=len(tup)
    if r==0:return (0,)*(2**t)
    identity=tuple(tuple(int(i==j) for j in range(r)) for i in range(r))
    zero=tuple(tuple(0 for j in range(r)) for i in range(r))
    cores=[tuple(tuple(X[i][j] for j in range(r)) for i in range(r)) for X in tup]
    dims=[]
    for bits in product((0,1),repeat=t):
        P=identity
        for b,B in zip(bits,cores):
            F=B if b else tuple(tuple((identity[i][j]-B[i][j])%q for j in range(r)) for i in range(r))
            P=matmul(P,F,q)
        dims.append(matrix_rank(P,q))
    assert sum(dims)==r
    return tuple(dims)


def run_case(q,m,n,r,t):
    A=tuple(tuple(int(i==j and i<r) for j in range(m)) for i in range(n))
    mat=list(matrices(m,n,q))
    Ids=[X for X in mat if mul(X,A,X,q)==X]
    commuting={(i,j):mul(Ids[i],A,Ids[j],q)==mul(Ids[j],A,Ids[i],q) for i in range(len(Ids)) for j in range(len(Ids))}
    labels,expected=expected_mult(m,n,r,q,t)
    observed=Counter()
    observed_rank=Counter()
    for indices in product(range(len(Ids)),repeat=t):
        if any(not commuting[indices[i],indices[j]] for i in range(t) for j in range(i+1,t)):continue
        seq=[Ids[i] for i in indices]
        ds=sig_profile(seq,r,q)
        observed[ds]+=1
        D=r-ds[0]
        pred=rank_poly(m-D,n-D,q)
        for dim,d in zip(ds[1:],labels[1:]):
            pred=polyprod(pred,rank_poly(dim,dim,q))
        brute=Counter(matrix_rank(Y,q) for Y in mat if all(mul(X,A,Y,q)==mul(Y,A,X,q) for X in seq))
        if brute!=pred:
            raise AssertionError((q,m,n,r,t,ds,brute,pred))
        for rank,count in brute.items():observed_rank[(ds,rank)]+=count
    assert observed==expected,(q,m,n,r,t,observed,expected)
    print('PASS q,m,n,r,t=',q,m,n,r,t,'idempotents=',len(Ids),'commuting tuples=',sum(observed.values()),'centralizer-tuples=',sum(observed_rank.values()),'profiles=',len(observed))

if __name__=='__main__':
    for case in ((2,2,2,0,2),(2,2,2,1,2),(2,2,2,2,2),(2,2,2,1,3),(2,3,2,1,2),(2,2,3,1,2),(3,2,2,1,2),(2,3,3,2,2),(2,2,2,2,3),(3,2,2,2,2)):
        run_case(*case)
    print('VERIFY_OK')
