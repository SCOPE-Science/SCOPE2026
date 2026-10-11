#!/usr/bin/env python3
from itertools import product


def model(n):
    m = 2 * (n + 1)
    level = [i // 2 for i in range(m)]
    def le(a, b):
        return a == b or level[a] < level[b]
    return m, level, le


def enumerate_maps(n):
    m, level, le = model(n)
    pairs = list(product(range(m), repeat=2))
    out = []
    chosen = []
    def rec(src_level):
        if src_level == n + 1:
            f = []
            for p in chosen:
                f.extend(p)
            out.append(tuple(f))
            return
        for p in pairs:
            if all(le(v, w) for old in chosen for v in old for w in p):
                chosen.append(p)
                rec(src_level + 1)
                chosen.pop()
    rec(0)
    return out


def pointwise_le(f, g, le):
    return all(le(a, b) for a, b in zip(f, g))


def beat_reduce_image(image, le):
    S = set(image)
    while len(S) > 1:
        removed = False
        for x in sorted(S):
            up = [y for y in S if y != x and le(x, y)]
            least = [y for y in up if all(le(y, z) for z in up)] if up else []
            if least:
                S.remove(x)
                removed = True
                break
            dn = [y for y in S if y != x and le(y, x)]
            greatest = [y for y in dn if all(le(z, y) for z in dn)] if dn else []
            if greatest:
                S.remove(x)
                removed = True
                break
        if not removed:
            break
    return frozenset(S)


def check(n, expected_maps):
    maps = enumerate_maps(n)
    m, level, le = model(n)
    assert len(maps) == expected_maps
    autos = [f for f in maps if len(set(f)) == m]
    assert len(autos) == 2 ** (n + 1)
    # Every automorphism preserves each two-point level and independently swaps its pair.
    for f in autos:
        for i in range(n + 1):
            assert {level[f[2*i]], level[f[2*i+1]]} == {i}
            assert {f[2*i], f[2*i+1]} == {2*i, 2*i+1}
    # Proper images have a singleton occupied target level and beat-reduce to a point.
    cores = {}
    nonautos = [f for f in maps if len(set(f)) < m]
    for f in nonautos:
        image = frozenset(f)
        occ = [sum(level[x] == j for x in image) for j in range(n + 1)]
        assert any(c == 1 for c in occ if c)
        if image not in cores:
            cores[image] = beat_reduce_image(image, le)
        assert len(cores[image]) == 1
    # Directly confirm each automorphism is isolated in the finite function poset.
    for a in autos:
        for g in maps:
            if g != a:
                assert not pointwise_le(a, g, le)
                assert not pointwise_le(g, a, le)
    classes = 1 + len(autos)
    return len(maps), len(nonautos), len(autos), classes, len(cores)


def main():
    expected = {1: 36, 2: 446, 3: 6080}
    for n in (1, 2, 3):
        total, nonauto, auto, classes, images = check(n, expected[n])
        print(f"n={n} maps={total} nonhomeomorphisms={nonauto} homeomorphisms={auto} homotopy_classes={classes} proper_images={images}")
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
