"""Independent finite check for partial affine self-inverse maps over F_2.
Execute: python3 verify.py. Uses the standard library only.
"""
from collections import Counter
from itertools import product
from math import prod


def gaussian(n, k):
    if k < 0 or k > n:
        return 0
    return prod((2**(n-i)-1) for i in range(k)) // prod((2**(k-i)-1) for i in range(k)) if k else 1


def gl_order(r):
    return prod((2**r - 2**j) for j in range(r))


def formula(d, k):
    c = Counter()
    aff_subspaces = 2**(d-k)*gaussian(d,k)
    for r in range(k//2+1):
        num_N = gaussian(k,r)*gaussian(k-r,r)*gl_order(r)
        c[(2**k, 0)] += aff_subspaces*num_N*(2**(k-r)-2**r)
        c[(2**k,2**(k-r))] += aff_subspaces*num_N*(2**r)
    return c


def rank_gf2(columns):
    pivots={}
    for c in columns:
        while c:
            b = c.bit_length()-1
            if b not in pivots:
                pivots[b] = c
                break
            c ^= pivots[b]
    return len(pivots)


def direct_affine(k):
    size = 2**k
    observed = Counter()
    if k == 0:
        return Counter({(1,1):1})
    for cols in product(range(size),repeat=k):
        if rank_gf2(cols) < k:
            continue
        linear = [0]*size
        for x in range(1,size):
            bit = x&-x
            linear[x] = linear[x^bit] ^ cols[bit.bit_length()-1]
        for b in range(size):
            perm = [linear[x]^b for x in range(size)]
            if all(perm[perm[x]]==x for x in range(size)):
                fixed = sum(perm[x]==x for x in range(size))
                observed[(size, fixed)] += 1
    return observed


def direct_affine_subspace_counts(d):
    size=2**d
    linear={frozenset({0})}
    frontier={frozenset({0})}
    while frontier:
        nxt=set()
        for u in frontier:
            for x in range(size):
                if x not in u:
                    w=frozenset(set(u)|{v^x for v in u})
                    if w not in linear:
                        linear.add(w)
                        nxt.add(w)
        frontier=nxt
    counts=Counter()
    for u in linear:
        cosets={frozenset(v^x for v in u) for x in range(size)}
        counts[len(u).bit_length()-1]+=len(cosets)
    return counts


def check_asymptotic_identity():
    from math import isclose
    p=1.0;f=2.0
    for j in range(1,100):
        p*=1-2.0**(-j)
        f*=1+2.0**(-j)
    delta=p/f
    assert isclose(delta,0.06056210400129026,abs_tol=1e-14)
    for k in (16,17,18,19):
        cells=formula(k,k)
        free=cells[(2**k,0)]/sum(cells.values())
        target=0.5+(-1 if k%2==0 else 1)*delta
        assert abs(free-target)<0.0012,(k,free,target)
    d=20
    all_cells=Counter({(0,0):1})
    for k in range(d+1):
        all_cells.update(formula(d,k))
    total=sum(all_cells.values())
    free=sum(value for (_,fixed),value in all_cells.items() if fixed==0)
    assert abs(free/total-0.5)<0.001
    print(f'LIMIT_IDENTITIES_OK delta={delta:.12f} global_d20={free/total:.12f}')


def main():
    assert gaussian(4,2)==35
    total={}
    for k in range(5):
        direct=direct_affine(k)
        predicted=formula(k,k)
        assert direct==predicted, (k,direct,predicted)
        total[k] = sum(direct.values())
        print(f'AFFINE_INVOLUTION_EXHAUSTIVE_OK k={k} count={total[k]} spectrum={dict(sorted(direct.items()))}')
    for d in range(5):
        counted=direct_affine_subspace_counts(d)
        expected={k:2**(d-k)*gaussian(d,k) for k in range(d+1)}
        assert dict(counted)==expected,(d,counted,expected)
        print(f'AFFINE_SUBSPACES_OK d={d} counts={dict(sorted(counted.items()))}')
    # Actual partial self-inverse maps on the four-bit space: affine subspace
    # symmetry lets us test each domain independently, without re-enumerating
    # conjugate affine subspaces of the same dimension.
    for d in range(5):
        observed=Counter({(0,0):1})
        predicted=Counter({(0,0):1})
        for k in range(d+1):
            aff_subspaces = 2**(d-k)*gaussian(d,k)
            for cell,multiplicity in direct_affine(k).items():
                observed[cell] += aff_subspaces*multiplicity
            predicted.update(formula(d,k))
        assert observed==predicted, (d,observed,predicted)
        print(f'PARTIAL_SELF_INVERSE_OK d={d} total={sum(observed.values())} fixed_free={sum(v for (rank,fixed),v in observed.items() if fixed==0)}')
    check_asymptotic_identity()
    print('VERIFY_OK')

if __name__=='__main__':
    main()
