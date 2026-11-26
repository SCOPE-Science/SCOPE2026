"""Finite diagnostics for a countable Alexandrov realization of transitive frames.

The unbounded omega-accumulation identity has a separate symbolic proof;
finite counts below check the exact affine counting formula underlying it.
"""
from itertools import product


def frames(n):
    for bits in product((0, 1), repeat=n*n):
        r = {(i, j) for i in range(n) for j in range(n) if bits[i*n+j]}
        if all((i, k) in r for i, j in r for j2, k in r if j2 == j):
            yield r


def clusters(n, r):
    classes = []
    which = {}
    for x in range(n):
        found = next((z for z, c in enumerate(classes) if
                      (x, c[0]) in r and (c[0], x) in r), None)
        if found is None:
            found = len(classes)
            classes.append([])
        classes[found].append(x)
        which[x] = found
    return classes, which


def order_data(n, r):
    cc, wh = clusters(n, r)
    ref = [((c[0], c[0]) in r) for c in cc]
    higher = {(i, j) for i in range(len(cc)) for j in range(len(cc))
              if i != j and (cc[i][0], cc[j][0]) in r}
    def le(u, v):
        x, a = u
        y, b = v
        return u == v or (wh[x], wh[y]) in higher or (
            wh[x] == wh[y] and ref[wh[x]] and a < b)
    return cc, wh, ref, higher, le


def check_frame(n, r):
    cc, wh, ref, higher, le = order_data(n, r)
    points = list(product(range(n), range(3)))
    assert all(le(p, p) for p in points)
    assert all(not (le(p, q) and le(q, p)) or p == q
               for p in points for q in points)
    assert all(not (le(p, q) and le(q, s)) or le(p, s)
               for p in points for q in points for s in points)
    checks = 0
    for bs in product((0, 1), repeat=n):
        B = {i for i, b in enumerate(bs) if b}
        for x in range(n):
            i = 1
            for N in (3, 5):
                pts = product(range(n), range(N))
                observed = sum(le((x, i), (y, j)) and y in B for y, j in pts)
                expected = (int(x in B) +
                            int(ref[wh[x]]) * (N-i-1) * sum(y in B for y in cc[wh[x]]) +
                            N * sum(y in B for y in range(n) if (wh[x], wh[y]) in higher))
                assert observed == expected
                checks += 1
            unbounded = (any(y in B for y in cc[wh[x]]) and ref[wh[x]]) or any(
                y in B and (wh[x], wh[y]) in higher for y in range(n))
            kripke = any((x, y) in r for y in B)
            assert unbounded == kripke
            checks += 1
    if all((x,x) not in r for x in range(n)):
        assert not any(ref)
        # Each strict order step then changes the finite cluster upward.
        assert all(wh[x] != wh[y] for x in range(n) for y in range(n)
                   if le((x,0), (y,1)))
    return checks


def main():
    inspected = 0
    checks = 0
    for n in range(1, 5):
        for r in frames(n):
            checks += check_frame(n, r)
            inspected += 1
    print('ALL_CHECKS_OK', 'transitive_frames=', inspected,
          'counting_and_modal_checks=', checks)

if __name__ == '__main__':
    main()
