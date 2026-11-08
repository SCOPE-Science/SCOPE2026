#!/usr/bin/env python3
"""Reproduce finite checks for maximal mutual visibility in near-crown graphs.

The finite-state check has infinite scope only when paired with the
threshold-invariance lemma in RESULT.md. The small graph check is empirical.
"""
from collections import Counter
from itertools import product
from math import comb


def visible_state(r, u, v):
    c, d, e, h = r
    n = sum(r)
    a, b = c + d, c + e
    left_selected = e + h + 1 - u
    right_selected = d + h + 1 - v
    left_ok = (left_selected <= 1 or v == 1 or b >= 3 or
               (1 <= b <= 2 and c >= 1))
    right_ok = (right_selected <= 1 or u == 1 or a >= 3 or
                (1 <= a <= 2 and c >= 1))
    matched_ok = (h == 0 or (a + u > 0 and b + v > 0 and
                  not (c == 1 and d == e == u == v == 0)))
    return left_ok and right_ok and matched_ok


def saturated_state(r, u, v):
    if not visible_state(r, u, v):
        return False
    c, d, e, h = r
    moves = []
    if u:
        moves.append((r, 0, v))
    if v:
        moves.append((r, u, 0))
    if c:
        moves.extend([((c-1, d, e+1, h), u, v),
                      ((c-1, d+1, e, h), u, v)])
    if d:
        moves.append(((c, d-1, e, h+1), u, v))
    if e:
        moves.append(((c, d, e-1, h+1), u, v))
    return not any(visible_state(*x) for x in moves)


def classified_state(r, u, v):
    c, d, e, h = r
    n = sum(r)
    if n < 4:
        return False
    # Exhaustive seven families, including symmetric options.
    return (
        (c, d, e, u, v) == (0, 0, 0, 1, 1) or
        (c, d, e, h, u, v) in ((0, 0, n, 0, 0, 0),
                               (0, n, 0, 0, 0, 0),
                               (0, 1, n-1, 0, 0, 1),
                               (0, n-1, 1, 0, 1, 0)) or
        (c, d, e, u, v) in ((0, 0, 3, 1, 0),
                             (0, 3, 0, 0, 1),
                             (1, 0, 0, 0, 1),
                             (1, 0, 0, 1, 0),
                             (1, 0, 1, 0, 0),
                             (1, 1, 0, 0, 0),
                             (0, 3, 3, 0, 0))
    )


def finite_reduction():
    cases = 0
    for r in product(range(5), repeat=4):
        if sum(r) < 4:
            continue
        for u, v in product((0, 1), repeat=2):
            assert saturated_state(r, u, v) == classified_state(r, u, v), (r,u,v)
            cases += 1
    assert cases == 2360
    return cases


def direct_check(n):
    N = 2*n + 2
    nbr = [0]*N
    for i in range(n+1):
        for j in range(n+1):
            if i == j and i > 0:
                continue
            a, b = i, n+1+j
            nbr[a] |= 1 << b
            nbr[b] |= 1 << a
    distance = [[99]*N for _ in range(N)]
    for s in range(N):
        distance[s][s] = 0
        visited = step = 1 << s
        depth = 0
        while step:
            nxt = 0
            for x in range(N):
                if (step >> x) & 1:
                    nxt |= nbr[x]
            nxt &= ~visited
            depth += 1
            for x in range(N):
                if (nxt >> x) & 1:
                    distance[s][x] = depth
            visited |= nxt
            step = nxt
    assert max(max(row) for row in distance) == 3

    def visible_direct(mask):
        chosen = [k for k in range(N) if mask & (1 << k)]
        for pos, a in enumerate(chosen):
            for b in chosen[pos+1:]:
                dst = distance[a][b]
                if dst == 1:
                    continue
                if dst == 2:
                    if not (nbr[a] & nbr[b] & ~mask):
                        return False
                elif dst == 3:
                    candidates = nbr[a] & ~mask
                    found = False
                    while candidates:
                        bit = candidates & -candidates
                        x = bit.bit_length()-1
                        candidates -= bit
                        if nbr[x] & nbr[b] & ~mask:
                            found = True
                            break
                    if not found:
                        return False
                else:
                    raise AssertionError('unexpected distance')
        return True

    def get_state(mask):
        c=d=e=h=0
        for i in range(1,n+1):
            aa = (mask >> i) & 1
            bb = (mask >> (n+1+i)) & 1
            if not aa and not bb:
                c+=1
            elif not aa:
                d+=1
            elif not bb:
                e+=1
            else:
                h+=1
        u = 1 - (mask & 1)
        v = 1 - ((mask >> (n+1)) & 1)
        return (c,d,e,h),u,v

    all_visible = set()
    for mask in range(1 << N):
        direct = visible_direct(mask)
        r,u,v = get_state(mask)
        assert direct == visible_state(r,u,v), (n,mask,r,u,v)
        if direct:
            all_visible.add(mask)
    maximal = Counter()
    for mask in all_visible:
        is_maximal = all((mask | (1 << x)) not in all_visible
                         for x in range(N) if not mask & (1 << x))
        r,u,v = get_state(mask)
        assert is_maximal == saturated_state(r,u,v), (n,mask)
        assert is_maximal == classified_state(r,u,v), (n,mask)
        if is_maximal:
            maximal[mask.bit_count()] += 1

    target = Counter()
    target[n+1] += 2*n
    target[n+2] += 2
    if n >= 6:
        target[2*n-4] += 20*comb(n,6)
    target[2*n-2] += 2*comb(n,3)
    target[2*n-1] += 2*n*n
    target[2*n] += 1
    assert maximal == target, (n,maximal,target)
    return len(all_visible),sum(maximal.values()),maximal


def main():
    cases = finite_reduction()
    total_masks = 0
    total_valid = 0
    total_maximal = 0
    for n in range(4,10):
        visible, maximal, spectrum = direct_check(n)
        total_masks += 1 << (2*n+2)
        total_valid += visible
        total_maximal += maximal
        print('order',n,'visibility',visible,'maximal_spectrum',dict(sorted(spectrum.items())))
    print('VERIFY_OK finite_state_types=%d graph_orders=4..9 examined_subsets=%d mutual_visibility_sets=%d maximal_sets=%d'%(cases,total_masks,total_valid,total_maximal))


if __name__ == '__main__':
    main()
