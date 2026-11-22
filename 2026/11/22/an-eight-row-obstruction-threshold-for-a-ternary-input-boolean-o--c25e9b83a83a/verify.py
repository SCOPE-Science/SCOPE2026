#!/usr/bin/env python3
"""Finite certificate for chained-dependence splitting over three inputs and a Boolean output."""
from collections import Counter
from itertools import combinations_with_replacement, product
from random import Random

X = range(3)
Z = range(2)


def rows_for(patterns):
    return tuple((x, y, z) for y, p in enumerate(patterns)
                 for x in X for z in Z if p[x] & (1 << z))


def choices(k):
    return tuple(product(range(-1, k), repeat=3))


def local_mask(p, y, fs, removed=None):
    rows = [(x, z) for x in X for z in Z
            if p[x] & (1 << z) and (x, z) != removed]
    out = 0
    for i, f in enumerate(fs):
        remaining = {z for x, z in rows if f[x] != y}
        if len(remaining) <= 1:
            out |= 1 << i
    return out


def direct_split(rows):
    """Independent brute-force split, used only on bounded-size check samples."""
    n = len(rows)
    for red in range(1 << n):
        f, g = {}, {}
        good = True
        for i, (x, y, z) in enumerate(rows):
            if (red >> i) & 1:
                if x in f and f[x] != y:
                    good = False
                    break
                f[x] = y
            else:
                if y in g and g[y] != z:
                    good = False
                    break
                g[y] = z
        if good:
            return True
    return False


def mask_sat(patterns):
    fs = choices(len(patterns))
    mask = (1 << len(fs)) - 1
    for y, p in enumerate(patterns):
        mask &= local_mask(p, y, fs)
    return bool(mask)


def census(k, critical):
    fs = choices(k)
    allmask = (1 << len(fs)) - 1
    local = []
    for y in range(k):
        one = []
        for p in critical:
            rows = [(x, z) for x in X for z in Z if p[x] & (1 << z)]
            sat = local_mask(p, y, fs)
            deleted = tuple(local_mask(p, y, fs, (x, z)) for x, z in rows)
            one.append((sat, deleted, len(rows)))
        local.append(one)
    sizes = Counter()
    examples = {}
    examined = 0
    for ids in combinations_with_replacement(range(len(critical)), k):
        examined += 1
        masks = [local[y][i][0] for y, i in enumerate(ids)]
        full = allmask
        for m in masks:
            full &= m
            if not full:
                break
        if full:
            continue
        others = []
        for y in range(k):
            m = allmask
            for j, v in enumerate(masks):
                if j != y:
                    m &= v
            others.append(m)
        if not all(others):
            continue
        if any(not (others[y] & dm)
               for y, i in enumerate(ids) for dm in local[y][i][1]):
            continue
        size = sum(local[y][i][2] for y, i in enumerate(ids))
        sizes[size] += 1
        examples.setdefault(size, tuple(critical[i] for i in ids))
    return examined, sizes, examples


def main():
    # A state is the bit mask of the z-values at each (x,y) cell.
    # Each y of a minimal falsifier must contain both z-values.
    critical = tuple(p for p in product(range(4), repeat=3)
                     if any(t & 1 for t in p) and any(t & 2 for t in p))
    assert len(critical) == 49
    expected = {
        1: (49, {}),
        2: (1225, {4: 3, 6: 6, 7: 12}),
        3: (20825, {6: 36, 7: 12, 8: 102}),
        4: (270725, {8: 135}),
    }
    examples = {}
    checked = 0
    for k in range(1, 5):
        n, counts, witness = census(k, critical)
        checked += n
        assert n == expected[k][0], (k, n)
        assert dict(counts) == expected[k][1], (k, counts)
        examples.update(witness)
        print(f'y={k}: canonical={n}, minimal={sum(counts.values())}, size_counts={dict(sorted(counts.items()))}')
    assert checked == 292824
    assert set(examples) == {4, 6, 7, 8}
    for size, pats in sorted(examples.items()):
        rows = rows_for(pats)
        assert len(rows) == size
        assert not direct_split(rows)
        assert all(direct_split(rows[:i] + rows[i + 1:])
                   for i in range(len(rows)))
        print(f'witness_size={size}, rows={rows}')

    # Independent split enumeration on a deterministic random sample.
    rng = Random(4242026)
    all_states = tuple(product(range(4), repeat=3))
    done = 0
    while done < 400:
        k = rng.randint(1, 4)
        pats = tuple(rng.choice(all_states) for _ in range(k))
        rows = rows_for(pats)
        if len(rows) > 11:
            continue
        assert direct_split(rows) == mask_sat(pats), (pats, rows)
        done += 1
    print(f'VERIFY_OK canonical={checked} independent_split_crosschecks={done}')


if __name__ == '__main__':
    main()
