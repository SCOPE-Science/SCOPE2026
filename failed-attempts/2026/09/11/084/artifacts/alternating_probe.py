"""Alternating C-sequence probe with nontrivial osc parity split.

The earlier probes' majority-parity rule degenerated (all-even) because the toy
walks were too short to oscillate. Here C-sequences alternate in parity along
each limit ladder, producing genuine even/odd osc splits; then the witness-class
hereditary failure and overlap structure are tested.
"""
import sys


def build(N):
    C = {}
    for a in range(N):
        if a == 0:
            C[a] = []
        elif a % 2 == 1:
            C[a] = [a - 1]
        else:
            # alternate parity: take every other rung plus top
            C[a] = sorted(set(list(range(1, a, 2)) + [a - 1]))

    def rho2(a, b):
        if a >= b:
            return 0
        cur = b
        steps = 0
        while cur != a:
            if cur <= a:
                break
            cand = [x for x in C[cur] if x >= a]
            nxt = min(cand) if cand else a
            if nxt >= cur:
                steps += 1
                break
            cur = nxt
            steps += 1
            if steps > 500:
                break
        return steps

    def osc(a, b):
        n = 0
        prev = None
        for xi in range(a):
            s = 1 if rho2(xi, a) <= rho2(xi, b) else -1
            if prev is not None and s != prev:
                n += 1
            prev = s
        return n

    return rho2, osc


def main():
    N = 14
    rho2, osc = build(N)
    nodes = {}
    src = {}
    for beta in range(N):
        f = tuple(rho2(a, beta) for a in range(beta + 1))
        for xi in range(beta + 1):
            k = (xi, f[:xi])
            nodes[k] = True
            src.setdefault(k, []).append(beta)
    A0 = {k for k in nodes for b in src[k] if k[0] < b and osc(k[0], b) % 2 == 0}
    A1 = {k for k in nodes for b in src[k] if k[0] < b and osc(k[0], b) % 2 == 1}

    def nonhered(A):
        n = 0
        for (xi, t) in A:
            for j in range(xi):
                if (j, t[:j]) not in A:
                    n += 1
                    break
        return n

    def clo(S):
        cl = set()
        for (xi, t) in S:
            for j in range(xi + 1):
                cl.add((j, t[:j]))
        return cl

    print('nodes=%d A0=%d A1=%d inter=%d nonher0=%d nonher1=%d' % (
        len(nodes), len(A0), len(A1), len(A0 & A1), nonhered(A0), nonhered(A1)))
    c0, c1 = clo(A0), clo(A1)
    print('|clo0|=%d |clo1|=%d equal=%s' % (len(c0), len(c1), c0 == c1))
    # branch-parity rule under this family
    ev = []
    od = []
    for beta in range(N):
        e = sum(1 for xi in range(beta) if osc(xi, beta) % 2 == 0)
        (ev if e >= beta - e else od).append(beta)
    print('even-branches=%s odd-branches=%s' % (ev, od))
    # pairwise osc parity histogram
    import collections
    h = collections.Counter(osc(a, b) % 2 for a in range(N) for b in range(a + 1, N))
    print('pair-parity histogram (even,odd)=' + str((h[0], h[1])))
    # osc value table for small betas
    print('osc table rows a<b:')
    for a in range(6):
        print(' a=%d' % a, {b: osc(a, b) for b in range(a + 1, 10)})


if __name__ == '__main__':
    sys.exit(main())
