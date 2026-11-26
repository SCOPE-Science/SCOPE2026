"""Finite-field checks for involutions of free two-step nilpotent Lie algebras.
Run: python3 verify_involutions.py
Only prime fields are enumerated; the symbolic theorem applies to odd prime powers.
"""
from itertools import product
from math import comb


def multiply(a,b,p):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%p for j in range(len(b[0]))) for i in range(len(a)))


def add(a,b,p):
    return tuple(tuple((a[i][j]+b[i][j])%p for j in range(len(a[0]))) for i in range(len(a)))


def identity(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))


def rank(a,p):
    if not a:return 0
    b=[list(row) for row in a]
    m,n=len(b),len(b[0]); r=0
    for c in range(n):
        t=next((t for t in range(r,m) if b[t][c]%p),None)
        if t is None:continue
        b[r],b[t]=b[t],b[r]
        scale=pow(b[r][c],-1,p)
        b[r]=[x*scale%p for x in b[r]]
        for i in range(m):
            if i!=r and b[i][c]:
                fac=b[i][c]
                b[i]=[(b[i][j]-fac*b[r][j])%p for j in range(n)]
        r+=1
        if r==m:break
    return r


def matrices(d,p):
    for v in product(range(p),repeat=d*d):
        yield tuple(tuple(v[i*d+j] for j in range(d)) for i in range(d))


def wedge_matrix(g,p):
    d=len(g); pairs=[(i,j) for i in range(d) for j in range(i+1,d)]
    return tuple(tuple((g[r][i]*g[s][j]-g[s][i]*g[r][j])%p for i,j in pairs) for r,s in pairs)


def linear_solutions_dim(g,p):
    d=len(g); w=comb(d,2)
    q=wedge_matrix(g,p)
    basis=[]
    for i in range(w):
        for j in range(d):
            f=tuple(tuple(int(a==i and b==j) for b in range(d)) for a in range(w))
            fg=multiply(f,g,p)
            qf=multiply(q,f,p)
            basis.append(tuple((fg[a][b]+qf[a][b])%p for a in range(w) for b in range(d)))
    if not basis:return 0
    c=tuple(tuple(col[t] for col in basis) for t in range(d*w))
    return w*d-rank(c,p)


def gaussian(d,a,q):
    num=1;den=1
    for i in range(a):
        num*=q**(d-i)-1
        den*=q**(a-i)-1
    assert num%den==0
    return num//den


def theory(d,q):
    out={}
    for a in range(d+1):
        b=d-a
        k=a*a*b+b*(comb(a,2)+comb(b,2))
        count=gaussian(d,a,q)*q**(a*b+k)
        fixed=a+comb(a,2)+comb(b,2)
        out[a]=(count,fixed,k)
    return out


def matrix_automorphism(g,f,p):
    d=len(g);w=comb(d,2)
    Q=wedge_matrix(g,p)
    return tuple(tuple(g[i][j] for j in range(d))+tuple(0 for _ in range(w)) for i in range(d))+tuple(tuple(f[i][j] for j in range(d))+tuple(Q[i][j] for j in range(w)) for i in range(w))


def verify(d,p,full_f=False):
    I=identity(d); predictions=theory(d,p)
    by_a={a:0 for a in range(d+1)}
    counted={a:0 for a in range(d+1)}
    inv_g=0
    for g in matrices(d,p):
        if rank(g,p)!=d or multiply(g,g,p)!=I: continue
        inv_g+=1
        a=rank(add(g,I,p),p)
        b=d-a
        k=a*a*b+b*(comb(a,2)+comb(b,2))
        assert linear_solutions_dim(g,p)==k, ('kernel',d,p,g,k)
        by_a[a]+=p**k
        counted[a]+=1
        if full_f:
            w=comb(d,2);found=0
            for z in product(range(p),repeat=w*d):
                f=tuple(tuple(z[i*d+j] for j in range(d)) for i in range(w))
                T=matrix_automorphism(g,f,p)
                if multiply(T,T,p)==identity(d+w):
                    found+=1
                    fixed=(d+w)-rank(add(T,tuple(tuple(-int(i==j) for j in range(d+w)) for i in range(d+w)),p),p)
                    assert fixed==predictions[a][1]
            assert found==p**k
    assert all(by_a[a]==predictions[a][0] for a in predictions), (d,p,by_a,predictions)
    assert sum(by_a.values())==sum(x[0] for x in predictions.values())
    print('d=',d,'p=',p,'involutive_quotients=',inv_g,'involutions=',sum(by_a.values()),'counts=',by_a,'OK')

if __name__=='__main__':
    verify(2,3,True)
    verify(2,5,True)
    verify(3,3,False)
    print('FREE_TWO_STEP_INVOLUTIONS_OK')

def size_gl(r,q):
    z=1
    for i in range(r):
        z*=q**r-q**i
    return z


def even_theory(d,q):
    out={}
    w=comb(d,2)
    for r in range(d//2+1):
        s=d-2*r
        t2=2*comb(r,2)+r*s
        t1=r+comb(s,2)
        assert 2*t2+t1==w
        k=r*(2*t2+t1)+s*(t2+t1)
        class_size=gaussian(d,r,q)*gaussian(d-r,r,q)*size_gl(r,q)
        out[r]=(class_size*q**k,k,class_size)
    return out


def verify_even(d,p,full_f=False):
    assert p==2
    I=identity(d); predictions=even_theory(d,p)
    by_r={r:0 for r in predictions}
    counts={r:0 for r in predictions}
    for g in matrices(d,p):
        if rank(g,p)!=d or multiply(g,g,p)!=I:continue
        delta=add(g,I,p)
        r=rank(delta,p)
        k=predictions[r][1]
        assert linear_solutions_dim(g,p)==k, ('even kernel',d,p,g,k)
        by_r[r]+=p**k
        counts[r]+=1
        if full_f:
            w=comb(d,2); found=0
            for z in product(range(p),repeat=w*d):
                f=tuple(tuple(z[i*d+j] for j in range(d)) for i in range(w))
                T=matrix_automorphism(g,f,p)
                if multiply(T,T,p)==identity(d+w): found+=1
            assert found==p**k
    assert all(by_r[r]==predictions[r][0] and counts[r]==predictions[r][2] for r in by_r)
    print('d=',d,'p=',p,'square_one_automorphisms=',sum(by_r.values()),'counts=',by_r,'OK')

if __name__=='__main__':
    verify_even(2,2,True)
    verify_even(3,2,True)
    verify_even(4,2,False)
    print('FREE_TWO_STEP_ALL_CHARACTERISTICS_OK')
