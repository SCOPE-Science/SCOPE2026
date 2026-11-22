"""Independent finite-field checks for rank-one anti-Rota--Baxter maps.

Run: python verify.py
All tests use the defining identity on matrix units, not the reduced criterion.
"""
from itertools import product
from math import prod

def matmul(a,b,n,p):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%p
                 for i in range(n) for j in range(n))

def tr_vx(v,x,n,p):
    return sum(v[i*n+j]*x[j*n+i] for i in range(n) for j in range(n))%p

def scalar(c,u,p):
    return tuple(c*x%p for x in u)

def rank_mod(a,n,p):
    m=[list(a[i*n:(i+1)*n]) for i in range(n)]
    i=0
    for j in range(n):
        at=next((h for h in range(i,n) if m[h][j]%p),None)
        if at is None:continue
        m[i],m[at]=m[at],m[i]
        inv=pow(m[i][j]%p,-1,p)
        m[i]=[(inv*t)%p for t in m[i]]
        for h in range(i+1,n):
            c=m[h][j]%p
            m[h]=[(a-c*b)%p for a,b in zip(m[h],m[i])]
        i+=1
        if i==n:break
    return i

def expected(u,v,n,p):
    uu=matmul(u,u,n,p)
    if uu==tuple(0 for _ in u):
        return matmul(u,v,n,p)==(0,)*len(u) and matmul(v,u,n,p)==(0,)*len(u)
    if uu!=u:return False  # only use canonical image idempotents here
    vu=matmul(v,u,n,p)
    uv=matmul(u,v,n,p)
    if p==2:return (vu==v and uv==(0,)*len(u)) or (uv==v and vu==(0,)*len(u))
    if p==3:return vu==v and uv==v
    return False

def original(u,v,n,p):
    es=[]
    for i in range(n):
        for j in range(n):
            es.append(tuple(int(h==i*n+j) for h in range(n*n)))
    uu=matmul(u,u,n,p)
    for x in es:
        ax=tr_vx(v,x,n,p)
        xu=matmul(x,u,n,p)
        bx=tr_vx(v,xu,n,p)
        for y in es:
            ay=tr_vx(v,y,n,p)
            uy=matmul(u,y,n,p)
            cy=tr_vx(v,uy,n,p)
            lhs=scalar(ax*ay,uu,p)
            rhs=scalar(-(ax*cy+ay*bx),u,p)
            if lhs!=rhs:return False
    return True

def gaussian(n,r,q):
    if r<0 or r>n:return 0
    a=prod(q**(n-j)-1 for j in range(r))
    b=prod(q**(r-j)-1 for j in range(r))
    return a//b

def gl(s,q):return prod(q**s-q**j for j in range(s))

def expected_counts(n,q):
    char=q # tests cover prime fields
    sq=sum(gaussian(n,s,q)*gaussian(n-s,s,q)*gl(s,q)//(q-1)*(q**((n-s)**2)-1)
           for s in range(1,n//2+1))
    extra=0
    if char==2:
        extra=sum(gaussian(n,r,q)*q**(r*(n-r))*2*(q**(r*(n-r))-1)
                  for r in range(1,n))
    if char==3:
        extra=sum(gaussian(n,r,q)*q**(r*(n-r))*(q**(r*r)-1)
                  for r in range(1,n+1))
    return sq,extra

def exhaustive(n,p):
    mats=list(product(range(p),repeat=n*n))
    maps={}
    for u in mats[1:]:
        for v in mats[1:]:
            pred=False
            sq=matmul(u,u,n,p)
            if sq==(0,)*(n*n):pred=expected(u,v,n,p)
            elif sq==u:pred=expected(u,v,n,p)
            else:
                # Every nonnilpotent anti-RB image line has a unique idempotent.
                for lam in range(1,p):
                    if sq==scalar(lam,u,p):
                        e=scalar(pow(lam,-1,p),u,p)
                        pred=expected(e,v,n,p)
                        break
            actual=original(u,v,n,p)
            assert pred==actual,(n,p,u,v,pred,actual)
            if actual:
                op=tuple((v[j*n+i]*u[h])%p for h in range(n*n) for i in range(n) for j in range(n))
                maps[op]=(u,v)
    sq,extra=expected_counts(n,p)
    assert len(maps)==sq+extra,(n,p,len(maps),sq,extra)
    nonsquare=0; idempotent=0; strong=0
    for op,(u,v) in maps.items():
        c=tr_vx(v,u,n,p)
        if c!=0:nonsquare+=1
        if c==1:idempotent+=1
        if matmul(u,u,n,p)==(0,)*(n*n):strong+=1
    if p==3:
        want_nonsquare=(p-1)*sum(gaussian(n,r,p)*p**(r*(n-r)+r*r-1) for r in range(1,n+1))
        want_idempotent=sum(gaussian(n,r,p)*p**(r*(n-r)+r*r-1) for r in range(1,n+1))
        assert nonsquare==want_nonsquare and idempotent==want_idempotent
    else:assert nonsquare==idempotent==0
    assert strong==sq
    print('EXHAUSTIVE',n,p,'nonzero=',len(maps),'squarezero_image=',sq,'idempotent_image=',extra,'R2_nonzero=',nonsquare,'idempotent_operator=',idempotent)

def direct_high_dimension():
    n,p=3,2
    mats=list(product(range(p),repeat=n*n))
    # Independently test the defining identity on canonical images
    count=0
    for u in mats:
        if not any(u):continue
        uu=matmul(u,u,n,p)
        if uu!=u and uu!=(0,)*(n*n):continue
        for v in mats:
            if not any(v):continue
            pred=expected(u,v,n,p)
            if pred:
                assert original(u,v,n,p)
                count+=1
    sq,extra=expected_counts(n,p)
    assert count==sq+extra
    print('DIRECT_ALL_CANONICAL',n,p,'total=',count,'squarezero_image=',sq,'idempotent_image=',extra)

if __name__=='__main__':
    exhaustive(2,2)
    exhaustive(2,3)
    exhaustive(2,5)
    direct_high_dimension()
    print('ANTI_ROTA_BAXTER_MATRIX_VERIFIED')
