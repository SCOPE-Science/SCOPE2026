"""Exact independent tests for symplectic Rota--Baxter classification.
No third-party packages. Run: python verify_rb_heisenberg.py
"""
from itertools import product
from math import prod


def omega(v, w, m, p):
    return sum(v[i]*w[m+i]-v[m+i]*w[i] for i in range(m)) % p


def matvec(A, v, p):
    return tuple(sum(row[j]*v[j] for j in range(len(v))) % p for row in A)


def criterion(A, c, m, p):
    n = 2*m
    for i in range(n):
        for j in range(n):
            v = tuple(int(k == i) for k in range(n))
            w = tuple(int(k == j) for k in range(n))
            av, aw = matvec(A, v, p), matvec(A, w, p)
            va = tuple((v[t]+av[t])%p for t in range(n))
            wa = tuple((w[t]+aw[t])%p for t in range(n))
            if ((1+c)*omega(av,aw,m,p)-c*omega(va,wa,m,p)) % p:
                return False
    return True


def maps_B(A, c, ell, m, p):
    inv2 = pow(2,-1,p)
    def B(g):
        v,z=g[:-1],g[-1]
        av=matvec(A,v,p)
        out=(c*z+sum(ell[i]*v[i] for i in range(2*m))-c*inv2*omega(av,v,m,p))%p
        return av+(out,)
    return B


def mul(g,h,m,p):
    n=2*m
    v,w=g[:n],h[:n]
    return tuple((v[i]+w[i])%p for i in range(n))+((g[-1]+h[-1]+pow(2,-1,p)*omega(v,w,m,p))%p,)


def inverse(g,p):
    return tuple(-x%p for x in g)


from functools import lru_cache

@lru_cache(maxsize=3)
def group_data(p,m):
    elems=list(product(range(p),repeat=2*m+1))
    index={g:i for i,g in enumerate(elems)}
    M=tuple(tuple(index[mul(g,h,m,p)] for h in elems) for g in elems)
    inv=tuple(index[inverse(g,p)] for g in elems)
    return elems,index,M,inv


def is_rb_bruteforce(A,c,ell,m,p):
    elems,index,M,inv=group_data(p,m)
    B=maps_B(A,c,ell,m,p)
    b=tuple(index[B(g)] for g in elems)
    for i,bi in enumerate(b):
        right0=M[i][bi]
        invi=inv[bi]
        for j,bj in enumerate(b):
            lhs=M[bi][bj]
            inner=M[M[right0][j]][invi]
            if lhs != b[inner]:
                return False
    return True


def num_isotropic(m,r,p):
    top=prod(p**(2*m-i)-p**i for i in range(r))
    bot=prod(p**r-p**i for i in range(r))
    return top//bot


def count_rank(m,r,p):
    return num_isotropic(m,r,p)*prod(p**(2*m)-p**i for i in range(r))


def run():
    # Complete 2x2 matrix census, checking the full group law for the zero
    # central character and a nonzero arbitrary linear correction.
    p,m=3,1
    yes=no=0
    by_c={c:0 for c in range(p)}
    for flat in product(range(p),repeat=4):
        A=(flat[:2],flat[2:])
        for c in range(p):
            predicted=criterion(A,c,m,p)
            for ell in product(range(p),repeat=2):
                actual=is_rb_bruteforce(A,c,ell,m,p)
                assert actual==predicted,(A,c,ell,actual,predicted)
                if predicted:
                    yes+=1
                    by_c[c]+=1
                else:
                    no+=1
    assert by_c[0]==p**2*sum(count_rank(m,r,p) for r in range(m+1))
    assert by_c[p-1]==by_c[0]
    print('H3 full 2x2/c/ell parameter census:',yes,'valid',no,'invalid; by c:',by_c)

    # Higher-dimensional independent direct multiplication tests.  Includes
    # the boundary strata c=0 and c=-1 and a nontrivial c=1 split map.
    p,m=3,2
    n=2*m
    test=[]
    seed_rows=[
        (0,0,0,0),(1,0,0,0),(0,1,0,0),
        (1,1,1,2),(2,1,2,1),(0,2,1,1),
        (1,0,2,0),(2,2,0,1),
    ]
    # Matrices with image in the standard Lagrangian span(e1,e2).
    for k in range(7):
        T=tuple(seed_rows[(k+i)%len(seed_rows)] if i<2 else (0,0,0,0) for i in range(4))
        for c in (0,p-1):
            if c==0: A=T
            else: A=tuple(tuple((T[i][j]-(i==j))%p for j in range(4)) for i in range(4))
            assert criterion(A,c,m,p)
            test.append((A,c))
    # Pairwise symplectic diagonal matrices for c=1.
    solutions=[]
    for a in range(p):
        for b in range(p):
            if ((1+1)*a*b - (1+a)*(1+b))%p==0:
                solutions.append((a,b))
    for (a,b),(d,e) in product(solutions,repeat=2):
        A=tuple(tuple((a,d,b,e)[i] if i==j else 0 for j in range(4)) for i in range(4))
        assert criterion(A,1,m,p)
        test.append((A,1))
        if len(test)>=21:break
    assert len(test)>=16
    for A,c in test:
        assert is_rb_bruteforce(A,c,(1,2,0,1),m,p),(A,c)
    print('H5 complete pairwise RB identity:',len(test),'valid matrices, 243^2 pairs each')
    for r in range(3):
        print('p=3, 2m=4: c=0 and c=-1, rank',r,'matrix count',count_rank(m,r,p),'RB map count',3**4*count_rank(m,r,p))
    # Characteristic five: a genuinely nonsingular similitude branch.
    p,m=5,2
    A=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
    c=2 # a=1 gives c=a^2/(1+2a) = 1/3 modulo 5
    assert criterion(A,c,m,p)
    from random import Random
    rng=Random(20261015)
    B=maps_B(A,c,(1,2,3,4),m,p)
    for _ in range(1000):
        g=tuple(rng.randrange(p) for _ in range(5))
        h=tuple(rng.randrange(p) for _ in range(5))
        bg=B(g)
        lhs=mul(bg,B(h),m,p)
        inner=mul(mul(mul(g,bg,m,p),h,m,p),inverse(bg,p),m,p)
        assert lhs==B(inner)
    print('H5 characteristic-five nonsingular scalar branch: 1000 deterministic group pairs')
    print('VERIFY_OK',yes+no,'full H3 map cases;',len(test),'exhaustive H5 pair tests; 1000 further checks')

if __name__=='__main__':
    run()
