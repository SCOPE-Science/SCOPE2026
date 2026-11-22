"""Independent finite checks of extremal nilpotence in parity/fence inverse monoids.

Run: python verify.py   (standard Python 3, no dependencies)
A finite exhaustive check is not a proof of the all-dimensions theorem.
"""
from itertools import combinations
from math import comb


def admissible(domain, image):
    # Test preservation of chain order, parity and both directions of fence order.
    if any((x - y) % 2 for x, y in zip(domain, image)):
        return False
    for i in range(len(domain)):
        for j in range(i+1, len(domain)):
            if (domain[j] - domain[i] == 1) != (image[j] - image[i] == 1):
                return False
    return True


def all_maps(n):
    yield ()  # empty partial injection
    for k in range(1, n+1):
        for domain in combinations(range(1, n+1), k):
            for image in combinations(range(1, n+1), k):
                if admissible(domain, image):
                    yield tuple(zip(domain, image))


def nil_index(f):
    d = dict(f)
    if not d:
        return 1
    longest = 1
    for x in d:
        y = x
        seen = {x}
        length = 1
        while y in d:
            y = d[y]
            if y in seen:
                return None  # has a nonempty cycle
            seen.add(y)
            length += 1
        longest = max(longest, length)
    return longest


def proposed(n):
    # Construct all maps as restrictions of translations by +2 or -2.
    assert n >= 3
    m = n // 2
    families = set()
    for sign in (-1, 1):
        active = set(range(1, n+1))
        target = {x for x in active if 1 <= x + 2*sign <= n}
        for parity in (1, 0):
            max_length = (n+1)//2 if parity else n//2
            if max_length != (n+1)//2:
                continue
            parity_points = [x for x in range(1, n+1) if x % 2 == parity]
            if sign == 1:
                obligatory = set(parity_points[:-1])
            else:
                obligatory = set(parity_points[1:])
            optional = sorted(target - obligatory)
            # At the maximum index, an optional source with a fixed point is prohibited;
            # restricting a translation never has fixed points, so there is no such issue.
            for count in range(len(optional)+1):
                for choice in combinations(optional, count):
                    domain = sorted(obligatory.union(choice))
                    candidate = tuple((x, x+2*sign) for x in domain)
                    if admissible(tuple(x for x,y in candidate), tuple(y for x,y in candidate)):
                        if nil_index(candidate) == (n+1)//2:
                            families.add(candidate)
    return families


def predicted_rank(n):
    m = n//2
    if n % 2:
        return {m+j: 2*comb(m-1,j) for j in range(m)}
    d = {m-1+j: 4*comb(m-1,j) for j in range(m)}
    d[2*m-2] -= 2
    return {k:v for k,v in d.items() if v != 0}


def main():
    expected_orders = {3:10,4:22,5:52,6:120,7:286,8:678,9:1628,10:3912}
    for n in range(3,11):
        entries = tuple(all_maps(n))
        assert len(entries)==expected_orders[n], (n,'size',len(entries))
        target = (n+1)//2
        observed = {f for f in entries if nil_index(f)==target}
        direct_ranks = {k:sum(len(f)==k for f in observed) for k in range(n+1)}
        direct_ranks = {k:v for k,v in direct_ranks.items() if v}
        assert direct_ranks == predicted_rank(n), (n, direct_ranks, predicted_rank(n))
        assert observed == proposed(n), (n,'normal forms disagree')
        assert all(nil_index(f) is None or nil_index(f) <= target for f in entries)
        print(f'n={n}: monoid={len(entries)}, maximal index={target}, extremizers={len(observed)}, ranks={direct_ranks}')
    print('FENCE_EXTREMAL_NILPOTENCE_VERIFIED n=3..10')

if __name__=='__main__':
    main()
