"""Dependency-free checks for modular idempotents of prime-order dihedral quandle algebras.

Usage: python3 verify.py
Finite enumerations support, but do not replace, the all-primes proof.
"""
from itertools import product
from math import gcd, lcm


def order_mod(a, p):
    x = a % p
    for h in range(1, p):
        if x == 1:
            return h
        x = x * a % p
    raise AssertionError("not a unit")


def predicted_dim(p):
    return (p - 1) // lcm(2, order_mod(2, p))


def rank_mod(matrix, p):
    mat = [list(row) for row in matrix]
    if not mat:
        return 0
    rows, cols = len(mat), len(mat[0]); rank = 0
    for col in range(cols):
        piv = next((i for i in range(rank, rows) if mat[i][col] % p), None)
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        mat[rank] = [(x * inv) % p for x in mat[rank]]
        for i in range(rows):
            if i != rank and mat[i][col] % p:
                a = mat[i][col]
                mat[i] = [(x - a*y) % p for x,y in zip(mat[i], mat[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def action_rank(p):
    # The basis t^i-1, i=1,...,p-1, is an independent basis of J.
    # sigma_a sends t^i-1 to t^(a*i)-1.
    mat = [[0] * (p-1) for _ in range(p-1)]
    for i in range(1, p):
        mat[(-i) % p-1][i-1] += 1
        mat[(2*i) % p-1][i-1] += 1
        mat[i-1][i-1] -= 1
    return (p-1)-rank_mod(mat,p)


def ordinary_mul(a,b,p):
    out=[0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: out[(i+j)%p]=(out[(i+j)%p]+x*y)%p
    return out


def star(a,b,p):
    out=[0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: out[(2*j-i)%p]=(out[(2*j-i)%p]+x*y)%p
    return out


def zadd(a,b,p):
    return [(x+y)%p for x,y in zip(a,b)]


def zscale(x,a,p):
    return [a*y%p for y in x]


def exp_j(z,p):
    one=[1]+[0]*(p-1)
    result=one[:]; powz=one[:]; fact=1
    for m in range(1,p):
        powz=ordinary_mul(powz,z,p)
        fact=fact*m%p
        result=zadd(result,zscale(powz,pow(fact,-1,p),p),p)
    return result


def eigenvector(p,r):
    v=[0]*p
    for i in range(1,p):
        coefficient=pow(i,-r,p)
        v[i]=(v[i]+coefficient)%p
        v[0]=(v[0]-coefficient)%p
    return v


def symbolic_examples():
    for p in [3,5,7,11,13,17,19,23,29,31,41]:
        d=predicted_dim(p)
        assert action_rank(p)==d,(p,action_rank(p),d)
        ell=lcm(2,order_mod(2,p))
        roots=list(range(1,p,ell))
        assert len(roots)==d
        for r in roots:
            v=eigenvector(p,r)
            assert sum(v)%p==0 and any(v)
            assert star(exp_j(v,p),exp_j(v,p),p)==exp_j(v,p)
        if p==17:
            v=[eigenvector(p,r) for r in roots]
            assert len(v)==2
            found=set()
            for a in range(p):
                for b in range(p):
                    z=zadd(zscale(v[0],a,p),zscale(v[1],b,p),p)
                    u=tuple(exp_j(z,p))
                    assert star(u,u,p)==list(u)
                    assert sum(u)%p==1
                    found.add(u)
            assert len(found)==p**d==289
            basis={tuple(int(i==j) for i in range(p)) for j in range(p)}
            assert len(found-basis)==272
            # Verify induced core-quandle law on a linearly independent pair.
            for a,b,c,dv in [(1,2,3,4),(0,1,1,0),(16,4,7,9)]:
                x=zadd(zscale(v[0],a,p),zscale(v[1],b,p),p)
                y=zadd(zscale(v[0],c,p),zscale(v[1],dv,p),p)
                zz=zadd(zscale(x,-1,p),zscale(y,2,p),p)
                assert star(exp_j(x,p),exp_j(y,p),p)==exp_j(zz,p)
            print('p=17: 289 nonzero idempotents, 272 nonbasis, core-quandle law verified')
        print('prime',p,'linear kernel dimension',d)


def field_ops(p,ext):
    # F_9 = F_3[w]/(w^2+1), encoded a+3*b*w.
    if ext==1:
        return range(p), lambda x,y:(x+y)%p, lambda x,y:(x*y)%p
    assert p==3 and ext==2
    def add(x,y): return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
    def mul(x,y):
        a,b=x%3,x//3; c,d=y%3,y//3
        return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
    return range(9),add,mul


def check_direct(p,ext):
    field,add,mul=field_ops(p,ext)
    q=len(field)
    found=[]
    for a in product(field, repeat=p):
        sq=[0]*p
        for i,ai in enumerate(a):
            if ai:
                for j,aj in enumerate(a):
                    if aj:
                        k=(2*j-i)%p
                        sq[k]=add(sq[k],mul(ai,aj))
        if tuple(sq)==a:
            found.append(a)
    assert len(found)==q**predicted_dim(p)+1,(p,q,len(found))
    zero=(0,)*p
    assert zero in found
    print('direct enumeration',f'F_{q}[R_{p}]',len(found),'idempotents')


if __name__=='__main__':
    symbolic_examples()
    for p,ext in [(3,1),(3,2),(5,1)]:
        check_direct(p,ext)
    print('VERIFY_OK_MODULAR_QUANDLE')
