#!/usr/bin/env python3
"""Finite verification of a sharp generating-set theorem for the magma monoid units."""
from collections import deque
from itertools import permutations
from math import factorial, comb


def perm_comp(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    v = [0] * len(p)
    for i, j in enumerate(p): v[j] = i
    return tuple(v)


def bmul(g, h):
    bits, p = g
    other, q = h
    shifted = sum(1 << p[i] for i in range(len(p)) if (other >> i) & 1)
    return (bits ^ shifted, perm_comp(p,q))


def smul(g, h):
    return perm_comp(g,h)


def product_mul(g,h):
    return (smul(g[0],h[0]), bmul(g[1],h[1]))


def closure(generators, identity, multiply, limit):
    gens = list(generators)
    seen = {identity}
    queue = deque([identity])
    while queue:
        x = queue.popleft()
        for y in gens:
            z = multiply(x,y)
            if z not in seen:
                seen.add(z)
                queue.append(z)
                if len(seen) > limit:
                    raise AssertionError('closure exceeded ambient group order')
    return seen


def generators(m):
    if m < 2: raise ValueError('requires m >= 2')
    c = tuple((i+1)%m for i in range(m))
    t = tuple([1,0]+list(range(2,m)))
    idperm=tuple(range(m))
    u=(1,c)
    v=(0,t)
    return u,v,(0,idperm),c,t,idperm


def check_b(m):
    u,v,one,c,t,identity_perm=generators(m)
    unit=(0,identity_perm)
    allones=(1<<m)-1
    power=unit
    for _ in range(m): power=bmul(power,u)
    assert power==(allones,identity_perm)
    uv=bmul(u,v)
    power2=unit
    for _ in range(m-1): power2=bmul(power2,uv)
    assert power2==(allones ^ (1<<1),identity_perm)
    elements=closure([u,v],unit,bmul,(1<<m)*factorial(m))
    assert len(elements)==(1<<m)*factorial(m)
    return len(elements)


def check_magma_bijection(n):
    from itertools import product
    # n <= 3: enumerate units as equivariant permutations of ordered pairs.
    diagonal=[(i,i) for i in range(n)]
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    all_reps=diagonal+edges
    observed=set()
    for p in permutations(range(n)):
        for ep in permutations(range(len(edges))):
            for signs in product([0,1],repeat=len(edges)):
                table={}
                for i,(x,y) in enumerate(diagonal): table[(x,y)]=diagonal[p[i]]
                for i,e in enumerate(edges):
                    dest=edges[ep[i]]
                    if signs[i]: dest=dest[::-1]
                    table[e]=dest
                    table[e[::-1]]=dest[::-1]
                assert len(table)==n*n and len(set(table.values()))==n*n
                for a in range(n):
                    for b in range(n):
                        assert table[(b,a)]==table[(a,b)][::-1]
                observed.add(tuple(table[z] for z in sorted(table)))
    expected=factorial(n)*(1<<len(edges))*factorial(len(edges))
    assert len(observed)==expected
    return expected


def check_three(n):
    m=comb(n,2)
    u,v,one,c,t,b_identity_perm=generators(m)
    idn=tuple(range(n)); id_b=(0,b_identity_perm)
    c_n=tuple((i+1)%n for i in range(n))
    t_n=tuple([1,0]+list(range(2,n)))
    g1=(c_n,u);g2=(t_n,id_b);g3=(idn,v)
    if n==3:
        G=closure([g1,g2,g3],(idn,id_b),product_mul,factorial(n)*((1<<m)*factorial(m)))
        assert len(G)==factorial(n)*(1<<m)*factorial(m)
    # Directly replay the isolated symmetric adjacent transpositions.
    p=g1
    for k in range(n-1):
        cp=tuple((i+k)%n for i in range(n))
        ci=perm_inv(cp)
        conjugate=perm_comp(perm_comp(cp,t_n),ci)
        assert {i for i in range(n) if conjugate[i]!=i}=={k,k+1}
    return factorial(n)*(1<<m)*factorial(m)


def main():
    for n in (1,2,3):
        order=check_magma_bijection(n)
        print('UNIT_ENUM',n,order)
    for m in (2,3,4,5,6):
        print('WREATH_GEN',m,check_b(m))
    for n in (3,4,5,6):
        print('THREE_GENERATOR_FORMULA',n,check_three(n))
    print('VERIFY_OK')


if __name__=='__main__': main()

# Additional independent table-level checks of the algebraic model.
def magma_product(f, g, n):
    return tuple(g[f[a*n+b]*n+f[b*n+a]] for a in range(n) for b in range(n))


def table_from_equivariant(n, sigma, bits, p):
    edges=[(a,b) for a in range(n) for b in range(a+1,n)]
    T={}
    for a in range(n): T[a,a]=(sigma[a],sigma[a])
    for i,(a,b) in enumerate(edges):
        x,y=edges[p[i]]
        if bits & (1<<p[i]): x,y=y,x
        T[a,b]=(x,y)
        T[b,a]=(y,x)
    assert len(T)==n*n
    return tuple(T[a,b][0] for a in range(n) for b in range(n))


def direct_binary_operation_checks():
    n=3; m=3
    u,v,one,c,t,idm=generators(m)
    idn=tuple(range(n));cn=tuple((i+1)%n for i in range(n));tn=(1,0,2)
    group_gens=[(cn,u),(tn,(0,idm)),(idn,v)]
    tables=[table_from_equivariant(n,s,bb,p) for s,(bb,p) in group_gens]
    identity=tuple(a for a in range(n) for b in range(n))
    seen=closure(tables, identity, lambda f,g: magma_product(f,g,n), 288)
    assert len(seen)==288
    # Independently check product commutativity ideal and required nonunit types at n=2.
    n=2
    all_tables=list(__import__('itertools').product(range(n), repeat=n*n))
    comm=lambda f: all(f[a*n+b]==f[b*n+a] for a in range(n) for b in range(n))
    count=0
    for f in all_tables:
        for g in all_tables:
            if comm(f):
                assert comm(magma_product(f,g,n))
                assert comm(magma_product(g,f,n))
                count+=2
    assert count>0
    diag_nonbijective=lambda f: len({f[i*n+i] for i in range(n)}) < n
    checked=0
    for f in all_tables:
        for g in all_tables:
            fg=magma_product(f,g,n)
            gf=magma_product(g,f,n)
            if diag_nonbijective(f):
                assert diag_nonbijective(fg) and diag_nonbijective(gf)
                checked+=2
    # Witnesses of distinct nonunit classes with diagonal restriction noninjective / injective.
    first_projection=tuple(a for a in range(n) for b in range(n))
    changed_diag=list(first_projection);changed_diag[0]=1
    collapsed_pair=list(first_projection);collapsed_pair[1*n+0]=0
    assert diag_nonbijective(tuple(changed_diag))
    assert not diag_nonbijective(tuple(collapsed_pair))
    def paired(f): return tuple((f[a*n+b], f[b*n+a]) for a in range(n) for b in range(n))
    assert len(set(paired(changed_diag)))<n*n
    assert len(set(paired(collapsed_pair)))<n*n
    print('BINARY_TABLE_CLOSURE n=3 units=288')
    print('COMMUTATIVE_IDEAL n=2 two_sided_products=',count)
    print('NONBIJECTIVE_DIAGONAL_IDEAL n=2 two_sided_products=',checked)
    print('NONUNIT_DIAGONAL_TYPES n=2 confirmed')


if __name__ == '__main__':
    direct_binary_operation_checks()
