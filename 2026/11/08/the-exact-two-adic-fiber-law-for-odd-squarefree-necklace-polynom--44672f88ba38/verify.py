"""Independent finite-level checks for odd-squarefree necklace-polynomial fibers.
Run: python3 necklace_verify.py
No third-party dependencies.
"""
from collections import Counter
from math import gcd


def mobius(n):
    p = 2
    sign = 1
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            sign = -sign
        p += 1
    return -sign if n > 1 else sign


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def phi(n):
    return sum(gcd(j,n) == 1 for j in range(1,n+1))


def nu2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def necklace_mod(n,x,mod):
    # Division by n is multiplication by inverse because n is odd.
    return sum(mobius(n//d)*pow(x,d,mod) for d in divisors(n))*pow(n,-1,mod)%mod


def main():
    instances = [3,5,7,11,13,15,21,33,35,105,1155]
    fibers = 0
    locally_bijective = 0
    for n in instances:
        assert mobius(n) in (-1,1) and n%2 == 1
        e = 2 + nu2(phi(n))
        for k in range(1,12):
            q = 1 << k
            observed = Counter(necklace_mod(n,x,q) for x in range(q))
            h = min(k,e)
            for y in range(q):
                expected = (y % 2 == 0) + ((1 << (h-1)) if y % (1 << h) == 0 else 0)
                assert observed[y] == expected, (n,k,y,observed[y],expected)
                fibers += 1
        # Each even/odd local branch map is separately a 2-adic isometry.
        for t in range(1,8):
            mod = 1 << t
            even_values = {((necklace_mod(n,2*s,2*mod)//2)%mod) for s in range(mod)}
            assert len(even_values) == mod
            locally_bijective += 1
            for base in (1,-1):
                modulus = 1 << (e+t)
                transformed = []
                for s in range(mod):
                    val = necklace_mod(n,base+4*s,modulus)
                    assert val % (1 << e) == 0
                    transformed.append((val >> e) % mod)
                assert len(set(transformed)) == mod, (n,t,base)
                locally_bijective += 1
    nonsquarefree = [9,25,27,45,75,81,99,121,135]
    for n in nonsquarefree:
        assert mobius(n) == 0 and n % 2
        for x in range(32):
            assert necklace_mod(n, x, 8) == 0, (n, x)
    print(f'VERIFY_OK squarefree_lengths={len(instances)} residue_entries={fibers} local_branch_bijections={locally_bijective} nonsquarefree_lengths={len(nonsquarefree)} finite_level_fibers=PASS')


if __name__ == '__main__':
    main()
