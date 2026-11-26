"""Exact finite-group character-exponent checks of generalized-dihedral zero masks.

This verifies algebraic witnesses and mask enumeration in selected finite abelian
kernels. The unrestricted proof is symbolic and does not depend on these tests.
"""
from itertools import product
from math import gcd, lcm


def test_group(moduli):
    m = lcm(*moduli)
    elements = list(product(*(range(n) for n in moduli)))
    characters = list(product(*(range(n) for n in moduli)))
    tested = patterns = 0
    for t in characters:
        def exponent(a):
            return sum((m // n) * j * x for j, x, n in zip(t, a, moduli)) % m
        if all((2*x)%n == 0 for x,n in zip(t,moduli)):
            continue
        # Character is not self-conjugate; its squared image has order L.
        fiber_index = {a: (2*exponent(a)) % m for a in elements}
        image = sorted(set(fiber_index.values()))
        L = len(image)
        assert L >= 2
        assert all(sum(z == q for z in fiber_index.values()) == len(elements)//L
                   for q in image)
        observed = set()
        for alpha in image:
            for beta in image:
                ar = frozenset(a for a in elements if fiber_index[a] == alpha)
                br = frozenset(a for a in elements if fiber_index[a] == beta)
                observed.add((ar, br))
                # Projective coefficient ratio witnesses: B/A=-alpha,
                # D/C=-beta, C^2=alpha/beta. Choose C=chi(a-b).
                a = next(x for x in elements if fiber_index[x] == alpha)
                b = next(x for x in elements if fiber_index[x] == beta)
                c_exp = (exponent(a)-exponent(b)) % m
                assert (2*c_exp + beta - alpha) % m == 0
                # The other square root is -C and defines a distinct matrix.
                patterns += 1
        empty = frozenset()
        full = frozenset(elements)
        # Empty / full coset / one fiber in either coset.
        observed.add((empty,empty))
        observed.add((full,empty))
        observed.add((empty,full))
        for alpha in image:
            observed.add((frozenset(a for a in elements if fiber_index[a]==alpha),empty))
            observed.add((empty,frozenset(a for a in elements if fiber_index[a]==alpha)))
        assert len(observed) == L*L+2*L+3
        assert {2*len(elements)-len(a)-len(b) for a,b in observed} == {
            len(elements), 2*len(elements)-len(elements)//L,
            2*len(elements)-2*len(elements)//L, 2*len(elements)
        }
        tested += 1
    return tested,patterns


def gaussian_checks():
    # Exact Gaussian-integer coefficient calculations for character chi(r)=i^r.
    # Exhaustively classify small-coordinate rank-one coefficients on D_8.
    vals = [0,1,-1,2,-2,1j,-1j]
    permissible = set()
    for a,b in product(range(4),repeat=2):
        ra = frozenset(r for r in range(4) if (2*r-2*a)%4==0)
        rb = frozenset(r for r in range(4) if (2*r-2*b)%4==0)
        permissible.add((ra,rb))
    E=frozenset()
    F=frozenset(range(4))
    permissible.update([(E,E),(F,E),(E,F)])
    for a in range(4):
        fa=frozenset(r for r in range(4) if (2*r-2*a)%4==0)
        permissible.update([(fa,E),(E,fa)])
    count=0
    for u1,u2,v1,v2 in product(vals,repeat=4):
        if not (u1 or u2) or not (v1 or v2):
            continue
        A,B,C,D=u1*v1,u2*v2,u1*v2,u2*v1
        assert A*B == C*D
        rot=frozenset(k for k in range(4) if A*(1j**k)+B*(1j**(-k))==0)
        ref=frozenset(k for k in range(4) if C*(1j**k)+D*(1j**(-k))==0)
        assert (rot,ref) in permissible,(rot,ref)
        count+=1
    return count


if __name__ == '__main__':
    groups=[(3,),(4,),(5,),(6,),(8,),(9,),(12,),(3,3),(4,2),(3,5),(4,3),(2,2,3)]
    c=d=0
    for G in groups:
        a,b=test_group(G)
        c+=a;d+=b
        print('GROUP_OK',G,'irreps',a,'double_fibers',b)
    n=gaussian_checks()
    print('CHECK_OK characters',c,'pair_witnesses',d,'gaussian_rank_one_vectors',n)
