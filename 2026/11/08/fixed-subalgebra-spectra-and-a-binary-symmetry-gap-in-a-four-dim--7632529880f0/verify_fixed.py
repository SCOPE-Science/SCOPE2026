"""Exhaustive fixed-space enumeration for automorphisms of F_q[x,y]/(x^2,y^2).

The group formula is independently checked by field arithmetic for q=2,4,8.
"""
from itertools import product


def gf_mul(a,b,q):
    if q==2:return a&b
    irr={4:0b111,8:0b1011}[q]
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&q:a^=irr
    return out


def gf_inv(a,q):
    assert a!=0
    for b in range(1,q):
        if gf_mul(a,b,q)==1:return b
    raise AssertionError('No inverse')


def rank(A,q):
    M=[row[:] for row in A]
    n=len(M);m=len(M[0]);r=0
    for c in range(m):
        k=next((i for i in range(r,n) if M[i][c]),None)
        if k is None:continue
        M[k],M[r]=M[r],M[k]
        inv=gf_inv(M[r][c],q)
        M[r]=[gf_mul(x,inv,q) for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]:
                factor=M[i][c]
                M[i]=[x^gf_mul(factor,y,q) for x,y in zip(M[i],M[r])]
        r+=1
        if r==n:break
    return r


def predicted(q):
    gl=(q*q-1)*(q*q-q)
    total=gl*q*q
    c1=q**3*(q+1)*(q-2)**2
    c3=(q*q-1)*(q+1)
    c4=1
    c2=total-c1-c3-c4
    return {1:c1,2:c2,3:c3,4:c4}


def check_end(q):
    hist={1:0,2:0,3:0,4:0}
    for a,b,c,d,u,v in product(range(q),repeat=6):
        determinant=gf_mul(a,d,q)^gf_mul(b,c,q)
        M=[[a^1,b,0],[c,d^1,0],[u,v,determinant^1]]
        fixed_dimension=4-rank(M,q)
        hist[fixed_dimension]+=1
    c1=q**3*(q**3-2*q*q+2)
    c3=(q*q-1)*(q+1)
    assert hist=={1:c1,2:q**6-c1-c3-1,3:c3,4:1},(q,hist)
    print('End q',q,'exact spectrum',hist)


def check(q):
    hist={1:0,2:0,3:0,4:0}
    for a,b,c,d in product(range(q),repeat=4):
        determinant=gf_mul(a,d,q)^gf_mul(b,c,q)
        if determinant==0:continue
        for u,v in product(range(q),repeat=2):
            # On the basis 1,x,y,xy the matrix is diag(1,block3).
            M=[[a^1,b,0],[c,d^1,0],[u,v,determinant^1]]
            fixed_dimension=4-rank(M,q)
            hist[fixed_dimension]+=1
    assert hist==predicted(q), (q,hist,predicted(q))
    print('q',q,'exact spectrum',hist)


if __name__=='__main__':
    for q in (2,4,8):check(q);check_end(q)
    print('VERIFY_OK_FIXED')
