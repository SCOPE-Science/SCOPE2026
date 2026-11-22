"""Independent finite checks for prime-representative subgroups of 2-power units.

Requires Python 3 only.  The finite checks do not replace the all-exponents proof.
"""
from collections import Counter


def prime_table(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(n ** .5) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b'\x00' * ((n - p * p) // p + 1)
    return sieve


def predicted(a, prime):
    if a == 1:
        return {(1,)}
    if a == 2:
        return {(1,), (1, 3)}
    if a == 3:
        return {(1,), (1, 3), (1, 5), (1, 7), (1, 3, 5, 7)}
    n = 1 << a
    groups = {(1,)}
    for p in (n - 1, n // 2 - 1, n // 2 + 1):
        if prime[p]:
            groups.add((1, p))
    quartic = (n // 4 - 1, n // 2 + 1, 3 * n // 4 - 1)
    if all(prime[p] for p in quartic):
        groups.add(tuple(sorted((1,) + quartic)))
    return groups


def generated(H, p, n, prime):
    """Generate H * <p> by multiplication, rejecting composite residues."""
    result = set(H)
    power, seen = 1, set()
    while power not in seen:
        seen.add(power)
        for h in H:
            z = h * power % n
            if z != 1 and not prime[z]:
                return None
            result.add(z)
        power = power * p % n
    return tuple(sorted(result))


def independent_search(a, prime):
    """Exhaust ALL prime-representative subgroups by closure under prime generators."""
    n = 1 << a
    found = {(1,)}
    frontier = [(1,)]
    ps = [p for p in range(2, n) if prime[p] and p % 2 == 1]
    while frontier:
        H = frontier.pop()
        for p in ps:
            if p in H:
                continue
            K = generated(H, p, n, prime)
            if K is not None and K not in found:
                found.add(K)
                frontier.append(K)
    return found


def main():
    max_a = 14
    prime = prime_table((1 << max_a) - 1)
    total = 0
    print('a | subgroups by order | order-four nontrivial representatives')
    for a in range(1, max_a + 1):
        expected = predicted(a, prime)
        found = independent_search(a, prime)
        assert found == expected, (a, expected - found, found - expected)
        dist = dict(sorted(Counter(map(len, found)).items()))
        quartics = [tuple(v for v in H if v != 1) for H in found if len(H) == 4]
        print(a, dist, quartics)
        assert max(map(len, found)) <= 4
        total += len(found)
    assert predicted(5, prime) == {(1,), (1, 17), (1, 31), (1, 7, 17, 23)}
    assert (1, 127, 257, 383) in predicted(9, prime)
    a = 17
    deep_prime = prime_table((1 << a) - 1)
    deep_expected = predicted(a, deep_prime)
    deep_found = independent_search(a, deep_prime)
    assert deep_found == deep_expected, (a, deep_expected - deep_found, deep_found - deep_expected)
    assert (1, 65537) in deep_found and (1, 131071) in deep_found
    print('a=17', dict(sorted(Counter(map(len, deep_found)).items())))
    print('PASS; a=1..14 and a=17,', total + len(deep_found), 'subgroup instances, all independently generated')


if __name__ == '__main__':
    main()
