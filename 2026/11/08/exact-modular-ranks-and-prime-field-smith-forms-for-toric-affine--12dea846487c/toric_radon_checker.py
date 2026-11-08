"""Exact finite-field toric affine line transform checks.

Uses integer modular elimination, finite-field arithmetic and optional SymPy
Smith normal form. No randomized numerical tests are used for rank assertions.
"""
from itertools import product
from math import isqrt


def field(p, f, modpoly):
    q = p**f
    def digs(a):
        return [(a//p**i)%p for i in range(f)]
    def pack(v):
        return sum((v[i]%p)*p**i for i in range(f))
    dd = [digs(a) for a in range(q)]
    def add(a,b):
        return pack([(u+v)%p for u,v in zip(dd[a],dd[b])])
    def neg(a):
        return pack([(-u)%p for u in dd[a]])
    def mul(a,b):
        c=[0]*(2*f-1)
        for i,u in enumerate(dd[a]):
            for j,v in enumerate(dd[b]):c[i+j]=(c[i+j]+u*v)%p
        for k in range(2*f-2,f-1,-1):
            v=c[k]
            for j in range(f):c[k-f+j]=(c[k-f+j]-v*modpoly[j])%p
        return pack(c[:f])
    one=1
    assert all(add(a,neg(a))==0 for a in range(q))
    assert all(mul(a,one)==a for a in range(q))
    assert all(any(mul(a,b)==one for b in range(1,q)) for a in range(1,q))
    return q,add,mul,neg


def prime_field(p):return field(p,1,[0])


def incidence(p,f,poly):
    q,add,mul,neg=field(p,f,poly)
    pts=list(product(range(1,q),repeat=2))
    lines=pts[:]
    M=[[int(y==add(mul(a,x),b)) for x,y in pts] for a,b in lines]
    return q,M


def rank_mod(matrix,p):
    a=[[v%p for v in row] for row in matrix]
    nr=len(a); nc=len(a[0]); row=0
    for col in range(nc):
        k=next((i for i in range(row,nr) if a[i][col]),None)
        if k is None:continue
        a[row],a[k]=a[k],a[row]
        inv=pow(a[row][col],-1,p)
        for j in range(col,nc):a[row][j]=(a[row][j]*inv)%p
        for i in range(row+1,nr):
            z=a[i][col]
            if z:
                for j in range(col,nc):a[i][j]=(a[i][j]-z*a[row][j])%p
        row+=1
        if row==nr:break
    return row


def expected_squares(q):
    return sorted([1]*(3*(q-2))+[q]*((q-2)*(q-3))+[(q-2)**2])


def run():
    import numpy as np
    specs=[(3,1,[0]),(5,1,[0]),(7,1,[0]),(11,1,[0]),
           (2,2,[1,1]),(2,3,[1,1,0]),(3,2,[1,0])]
    for p,f,poly in specs:
        q,B=incidence(p,f,poly)
        formula=(p*(p+1)//2)**f-(3 if p==2 else 2)
        r=rank_mod(B,p)
        assert r==formula,(q,r,formula)
        # Compare squared singular values, multiplicities and normalization.
        s=np.linalg.svd(np.array(B,dtype=float),compute_uv=False)**2
        expect=expected_squares(q)
        assert np.allclose(sorted(s),expect,atol=1e-8,rtol=1e-9),(q,s,expect)
        if q in (3,4,5,7):
            # Integer polynomial reconstruction identity for H=B^T B.
            from sympy import Matrix, eye
            T=Matrix(B); H=T.T*T; n=len(B)
            s1=1+q+(q-2)**2
            s2=q+(q-2)**2+q*(q-2)**2
            s3=q*(q-2)**2
            assert H*(H*H-s1*H+s2*eye(n))==s3*eye(n)
        if f==1 and p<=7:
            from sympy import Matrix,ZZ
            from sympy.matrices.normalforms import smith_normal_form
            S=smith_normal_form(Matrix(B),domain=ZZ)
            diag=sorted(abs(int(S[i,i])) for i in range(len(B)))
            e=(p-2)*(p-3)//2
            predicted=sorted(([1]*(len(B)-e)+[p]*(e-1)+[p*(p-2)]) if e>0 else [1]*len(B))
            assert diag==predicted,(q,diag,predicted)
        print('PASS',q,'matrix_size',len(B),'char_rank',r,'singular_sq_levels',sorted(set(expect)))
    print('TORIC_RADON_SMITH_AND_JACOBI_PASS 7_fields=checked')

if __name__=='__main__':run()
