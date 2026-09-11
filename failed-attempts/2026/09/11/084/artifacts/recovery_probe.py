"""Bounded recovery probe: rho2-walk even/odd truncation across C-sequence families.

Finite analogue (N ordinals) of the omega1 construction. Tests:
  (a) hereditariness of osc-parity witness classes A0/A1 (must be subtrees);
  (b) balance of parity classes;
  (c) level-size profiles of downward closures (necessary condition for embedding);
  (d) exact level-preserving parent-respecting embedding between small closures.
"""
import sys

def build(N, mode):
    C = {}
    for a in range(N):
        if a == 0:
            C[a] = []
        elif a % 2 == 1:
            C[a] = [a - 1]
        else:
            if mode == 'sparse':
                C[a] = sorted(set(list(range(0, a, 2)) + [a - 1]))
            elif mode == 'mod3':
                C[a] = sorted(set(list(range(0, a, 3)) + [a - 1]))
            elif mode == 'ladder':
                C[a] = [0, a - 1] if a > 1 else [a - 1]
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

def analyze(N, mode):
    rho2, osc = build(N, mode)
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
    c0, c1 = clo(A0), clo(A1)
    def levsizes(cl):
        d = {}
        for (xi, t) in cl:
            d[xi] = d.get(xi, 0) + 1
        return dict(sorted(d.items()))
    l0, l1 = levsizes(c0), levsizes(c1)
    dom01 = all(l0.get(l, 0) <= l1.get(l, 0) for l in l0)  # c0 fits in c1 per level
    dom10 = all(l1.get(l, 0) <= l0.get(l, 0) for l in l1)
    return {
        'mode': mode, 'N': N, 'nnodes': len(nodes),
        'A0': len(A0), 'A1': len(A1), 'inter': len(A0 & A1),
        'nonher0': nonhered(A0), 'nonher1': nonhered(A1),
        'c0': len(c0), 'c1': len(c1),
        'lev0': l0, 'lev1': l1,
        'levelwise_c0_fits_c1': dom01, 'levelwise_c1_fits_c0': dom10,
    }

def main():
    out = []
    for mode in ['sparse', 'mod3', 'ladder']:
        r = analyze(12, mode)
        out.append(r)
        print(('mode={mode} N={N} nodes={nnodes} A0={A0} A1={A1} inter={inter} '
               'nonher0={nonher0}/{A0} nonher1={nonher1}/{A1} '
               '|clo|={c0},{c1} fit01={levelwise_c0_fits_c1} fit10={levelwise_c1_fits_c0}').format(**r))
        print('   lev0=' + str(r['lev0']))
        print('   lev1=' + str(r['lev1']))
    with open('probe_results.txt', 'w') as fh:
        for r in out:
            fh.write(str(r) + '\n')

if __name__ == '__main__':
    sys.exit(main())
