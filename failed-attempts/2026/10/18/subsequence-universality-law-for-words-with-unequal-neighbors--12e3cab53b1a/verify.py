"""Exact coefficient and independent short-word checks for an alphabet without adjacent repeats."""
from collections import Counter
from itertools import product, combinations


def segments(q, N, initial_choices):
    arch = [0] * (N + 1)
    tail = [0] * (N + 1)
    tail[0] = 1
    active = {1: initial_choices}
    for n in range(1, N + 1):
        if n == 1:
            tail[n] = initial_choices
            continue
        nxt = {}
        for j, ways in active.items():
            if j - 1:
                nxt[j] = nxt.get(j, 0) + ways * (j - 1)
            if j + 1 == q:
                arch[n] += ways * (q - j)
            else:
                nxt[j + 1] = nxt.get(j + 1, 0) + ways * (q - j)
        active = nxt
        tail[n] = sum(active.values())
    return arch, tail


def convolution(a, b, N):
    out = [0] * (N + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[:N + 1 - i]):
                if bj:
                    out[i + j] += ai * bj
    return out


def theoretical(q, N):
    first_arch, first_tail = segments(q, N, q)
    later_arch, later_tail = segments(q, N, q - 1)
    out = [Counter() for _ in range(N + 1)]
    for n, a in enumerate(first_tail):
        if a:
            out[n][0] = a
    chain = first_arch
    for k in range(1, N // q + 1):
        ends = convolution(chain, later_tail, N)
        for n, v in enumerate(ends):
            if v:
                out[n][k] = v
        chain = convolution(chain, later_arch, N)
    return out


def arches(w, q):
    seen = set()
    count = 0
    for a in w:
        seen.add(a)
        if len(seen) == q:
            count += 1
            seen.clear()
    return count


def subseq_index(w, q):
    # Unlike the first-cover scanning proof, enumerate all subsequences.
    out = 0
    for k in range(1, len(w) // q + 1):
        seen = {tuple(w[i] for i in inds) for inds in combinations(range(len(w)), k)}
        if len(seen) != q ** k:
            break
        out = k
    return out


def brute(q, N):
    out = [Counter() for _ in range(N + 1)]
    out[0][0] = 1
    for n in range(1, N + 1):
        for first in range(q):
            for rest in product(range(q - 1), repeat=n - 1):
                w = [first]
                for step in rest:
                    options = [a for a in range(q) if a != w[-1]]
                    w.append(options[step])
                k = arches(w, q)
                if n <= (9 if q == 3 else 8):
                    assert k == subseq_index(w, q), (q,n,w)
                out[n][k] += 1
    return out


def main():
    for q, N in [(2, 10), (3, 12), (4, 9), (5, 7)]:
        tab = theoretical(q, N)
        tab2 = brute(q, N)
        assert tab == tab2, (q, tab, tab2)
        for n in range(N + 1):
            target = 1 if n == 0 else q * (q-1)**(n-1)
            assert sum(tab[n].values()) == target, (q, n, tab[n])
        print('q=', q, 'N=', N, 'all histogram coefficients match brute force')
    print('TERNARY n=3:',dict(sorted(theoretical(3, 10)[3].items())))
    print('TERNARY n=6:',dict(sorted(theoretical(3, 10)[6].items())))
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
