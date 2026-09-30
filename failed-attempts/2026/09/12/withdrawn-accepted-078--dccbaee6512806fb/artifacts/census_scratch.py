"""Census lower bound for F* (target-only scale assessment). Stdlib only."""
import json
import math
from itertools import product


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def f(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def u(self, a, b):
        ra, rb = self.f(a), self.f(b)
        if ra != rb:
            self.p[ra] = rb


def cf_value(a):
    h2, h1 = 0, 1
    k2, k1 = 1, 0
    for ai in a:
        h2, h1 = h1, ai * h1 + h2
        k2, k1 = k1, ai * k1 + k2
    return h1, k1


def proper_tangles(c):
    out = []

    def rec(remaining, seq):
        if remaining == 0:
            if len(seq) >= 1 and seq[-1] >= 2:
                p, q = cf_value([0] + seq)
                assert 0 < p < q and math.gcd(p, q) == 1, (seq, p, q)
                out.append(((p, q), tuple([0] + seq)))
            return
        for v in range(1, remaining + 1):
            seq.append(v)
            rec(remaining - v, seq)
            seq.pop()

    rec(c, [])
    return out


def pair_H():
    return {0: 1, 1: 0, 2: 3, 3: 2}


def pair_X():
    return {0: 2, 2: 0, 1: 3, 3: 1}


def rot_pair(P):
    r = {0: 1, 1: 2, 2: 3, 3: 0}
    return {r[a]: r[b] for a, b in P.items()}


def add_pairs(P, Q):
    uf = UF(8)
    for a, b in P.items():
        if a < b:
            uf.u(a, b)
    for a, b in Q.items():
        if a < b:
            uf.u(4 + a, 4 + b)
    uf.u(1, 4 + 0)
    uf.u(2, 4 + 3)
    outer = [0, 3, 5, 6]
    reps = {}
    for x in outer:
        reps.setdefault(uf.f(x), []).append(x)
    R = {}
    for grp in reps.values():
        assert len(grp) == 2, grp
        R[grp[0]] = grp[1]
        R[grp[1]] = grp[0]
    mp = {0: 0, 3: 3, 5: 1, 6: 2}
    return {mp[a]: mp[b] for a, b in R.items()}


def tangle_pairing(cf):
    assert len(cf) >= 1
    if len(cf) == 1:
        return pair_H() if cf[0] % 2 == 0 else pair_X()
    return add_pairs(
        pair_H() if cf[0] % 2 == 0 else pair_X(),
        rot_pair(tangle_pairing(cf[1:])),
    )


def pairing_key(P):
    return (min(0, P[0]), max(0, P[0]), min(1, P[1]), max(1, P[1]))


def pretzel_components(ms):
    n = len(ms)
    uf = UF(4 * n)

    def tl(i): return 4 * i

    def tr(i): return 4 * i + 1

    def bl(i): return 4 * i + 2

    def br(i): return 4 * i + 3

    for i, m in enumerate(ms):
        if m % 2 == 0:
            uf.u(tl(i), bl(i))
            uf.u(tr(i), br(i))
        else:
            uf.u(tl(i), br(i))
            uf.u(tr(i), bl(i))
        j = (i + 1) % n
        uf.u(tr(i), tl(j))
        uf.u(br(i), bl(j))
    return len({uf.f(x) for x in range(4 * n)})


def montesinos_components(pairings):
    n = 4
    uf = UF(4 * n)
    for i, P in enumerate(pairings):
        for a, b in P.items():
            if a < b:
                uf.u(4 * i + a, 4 * i + b)
    for i in range(n):
        j = (i + 1) % n
        uf.u(4 * i + 1, 4 * j + 0)
        uf.u(4 * i + 2, 4 * j + 3)
    return len({uf.f(x) for x in range(4 * n)})


def main():
    res = {"checks": {}, "crossings": {}}
    agree = True
    for m in range(2, 15):
        PB = tangle_pairing([0, m])
        PA = {0: 3, 3: 0, 1: 2, 2: 1} if m % 2 == 0 else pair_X()
        if PB != PA:
            agree = False
            res["checks"].setdefault("twist_mismatch", []).append(m)
    res["checks"]["strand_vs_recursive_twist_agree"] = agree

    tang = {}
    for c in range(2, 13):
        tang[c] = proper_tangles(c)
        assert len(tang[c]) == 2 ** (c - 2), (c, len(tang[c]))
    res["checks"]["proper_tangle_counts_match_2^{c-2}"] = True

    cls = {}
    ok = True
    for c in range(2, 13):
        for (p, q), cf in tang[c]:
            P = tangle_pairing(list(cf))
            cls.setdefault((p % 2, q % 2), set()).add(pairing_key(P))
    for v in cls.values():
        if len(v) != 1:
            ok = False
    res["checks"]["pairing_constant_on_parity_class"] = ok
    res["checks"]["parity_classes"] = {str(k): len(v) for k, v in cls.items()}

    pair_cache = {}
    for c in range(2, 13):
        for (p, q), cf in tang[c]:
            pair_cache[(p, q)] = tangle_pairing(list(cf))

    for C in (16, 17, 18):
        comp = []

        def rec_tw(rem, parts):
            if len(parts) == 4:
                if rem == 0:
                    comp.append(tuple(parts))
                return
            for v in range(2, rem - 2 * (3 - len(parts)) + 1):
                parts.append(v)
                rec_tw(rem - v, parts)
                parts.pop()

        rec_tw(C, [])
        twist_knots = sum(1 for ms in comp if pretzel_components(ms) == 1)
        mism = 0
        for ms in comp:
            PAIR = [pair_cache[(1, m)] for m in ms]
            if (pretzel_components(ms) == 1) != (montesinos_components(PAIR) == 1):
                mism += 1
        gen_tuples = gen_knots = 0

        def rec_gen(rem, parts):
            nonlocal gen_tuples, gen_knots
            if len(parts) == 4:
                if rem == 0:
                    lists = [tang[c] for c in parts]
                    for combo in product(*lists):
                        gen_tuples += 1
                        PAIR = [pair_cache[pq] for pq, cf in combo]
                        if montesinos_components(PAIR) == 1:
                            gen_knots += 1
                return
            for v in range(2, rem - 2 * (3 - len(parts)) + 1):
                if v > 12:
                    continue
                parts.append(v)
                rec_gen(rem - v, parts)
                parts.pop()

        rec_gen(C, [])
        res["crossings"][C] = {
            "twist_ordered_tuples": len(comp),
            "twist_knot_tuples": twist_knots,
            "twist_closure_crosscheck_mismatches": mism,
            "general_ordered_tuples": gen_tuples,
            "general_knot_tuples": gen_knots,
            "fiber8_lower_bound_twist": twist_knots / 8,
            "fiber8_lower_bound_general": gen_knots / 8,
        }
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
