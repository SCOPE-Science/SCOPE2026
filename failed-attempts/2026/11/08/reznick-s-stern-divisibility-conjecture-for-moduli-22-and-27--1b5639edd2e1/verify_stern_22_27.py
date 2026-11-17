"""Exact finite certificate for a Stern-divisibility identity.

Run: python3 verify_stern_22_27.py
Python standard library only. The proof of sufficiency of the finite check
comes from Cayley-Hamilton, not from extrapolating a table.
"""
from hashlib import sha256
from math import gcd

MODULI = (22, 27)


def primitive_counts(d, steps):
    states = [(a, b) for a in range(d) for b in range(d)
              if gcd(gcd(a, b), d) == 1]
    index = {pair: j for j, pair in enumerate(states)}
    assert len(index) == len(states)
    next0 = [index[(a, (a + b) % d)] for a, b in states]
    next1 = [index[((a + b) % d, b)] for a, b in states]
    v = [0] * len(states)
    v[index[(0, 1)]] = 1
    zeros = [j for j, (a, _) in enumerate(states) if a == 0]
    values = []
    for r in range(steps):
        assert sum(v) == 1 << r
        values.append(sum(v[j] for j in zeros))
        nxt = [0] * len(states)
        for j, count in enumerate(v):
            if count:
                nxt[next0[j]] += count
                nxt[next1[j]] += count
        v = nxt
    return len(states), values


def full_grid_counts(d, steps):
    """Second implementation: all residue pairs, direct integer indexing."""
    v = [0] * (d * d)
    v[1] = 1   # pair (0, 1)
    out = []
    for r in range(steps):
        assert sum(v) == 1 << r
        out.append(sum(v[:d]))
        nxt = [0] * (d * d)
        for a in range(d):
            for b in range(d):
                count = v[a*d+b]
                if count:
                    nxt[a*d+(a+b) % d] += count
                    nxt[((a+b) % d)*d+b] += count
        v = nxt
    return out


def direct_counts(steps):
    """Third method: compute actual Stern terms by scalar recurrence."""
    limit = 1 << (steps - 1)
    s = [0] * (limit + 1)
    s[1] = 1
    for i in range(2, limit + 1):
        if i % 2:
            s[i] = s[i // 2] + s[i // 2 + 1]
        else:
            s[i] = s[i // 2]
    totals = [0, 0]
    out = [[], []]
    for n in range(limit):
        for j, d in enumerate(MODULI):
            totals[j] += (s[n] % d == 0)
        if (n+1) & n == 0:  # n+1 is a power of two
            for j in range(2):
                out[j].append(totals[j])
    return out


def main():
    sizes = []
    all_values = []
    for d in MODULI:
        size, values = primitive_counts(d, 1008)
        sizes.append(size)
        all_values.append(values)
        assert values == full_grid_counts(d, 1008), d
    assert sizes == [360, 648], sizes
    assert len(all_values[0]) == sum(sizes)
    assert all_values[0] == all_values[1], 'An unequal level contradicts the identity'
    direct = direct_counts(19)
    assert direct[0] == all_values[0][:19]
    assert direct[1] == all_values[1][:19]
    sig = sha256(('\n'.join(str(x) for x in all_values[0])+'\n').encode()).hexdigest()
    print('VERIFY_OK', 'states22=360', 'states27=648',
          'Cayley_Hamilton_bound=1008', 'exact_levels=0..1007',
          'independent_full_grid=PASS', 'direct_Stern_levels=0..18',
          'first10=' + str(all_values[0][:10]),
          'counts_sha256=' + sig)


if __name__ == '__main__':
    main()
