"""Phase-1g (TARGET widen): larger-field random existential census incl.
negated atoms (exists y F!=0), plus (3,3)/(5,2) nv=4. Reuses phase1f_census.Tab.
Stdlib only."""
import random
from phase1f_census import Tab, mons_vars, eval_row, growth_struct


def census_neq(p, l, nv=3, trials=3000, seed=771):
    T = Tab(p, l)
    q = T.q
    mons = mons_vars(nv, 2)
    sig = T.frob
    rng = random.Random(seed)
    seen = {}
    for _ in range(trials):
        coeff = [rng.randrange(p) for _ in mons]
        if all(c == 0 for c in coeff):
            continue
        A = set()
        for x in range(q):
            sx = sig[x]
            for y in range(q):
                vals = [x, y, sx][:nv] if nv <= 3 else [x, y, sx, sig[y]][:nv]
                if eval_row(T, vals, mons, coeff) != T.z:
                    A.add(x)
                    break
        seen.setdefault(frozenset(A), coeff)
    return T, seen


def census_eq(p, l, nv=4, trials=3000, seed=772):
    T = Tab(p, l)
    q = T.q
    mons = mons_vars(nv, 2)
    sig = T.frob
    rng = random.Random(seed)
    seen = {}
    for _ in range(trials):
        coeff = [rng.randrange(p) for _ in mons]
        if all(c == 0 for c in coeff):
            continue
        A = set()
        for x in range(q):
            sx = sig[x]
            for y in range(q):
                vals = [x, y, sx, sig[y]][:nv]
                if eval_row(T, vals, mons, coeff) == T.z:
                    A.add(x)
                    break
        seen.setdefault(frozenset(A), coeff)
    return T, seen


def audit(T, seen, tag, delta=0.2, eps=0.1, eta=0.25):
    q = T.q
    lo, hi = q ** delta, q ** (1 - delta)
    inwin = g = s = 0
    viol = []
    sizes = {}
    for A in seen:
        n = len(A)
        sizes[n] = sizes.get(n, 0) + 1
        if n == 0 or n == q:
            continue
        r = growth_struct(T, set(A), eps, eta)
        if lo <= n <= hi:
            inwin += 1
            g += r["grow"]
            s += r["struct"]
            if not r["grow"] and not r["struct"]:
                viol.append((sorted(A), r))
    print("%s q=%d distinct=%d inwin=%d grow=%d struct=%d VIOL=%d" %
          (tag, q, len(seen), inwin, g, s, len(viol)))
    print("   sizedist=%s" % sorted(sizes.items()))
    for A, r in viol[:8]:
        print("   VIOL A=%s n=%d sum=%d tw=%d best=%d(%s)" %
              (A, r["n"], r["sum"], r["tw"], r["best"], r["bestname"]))
    return len(viol)


def main():
    tot = 0
    T, seen = census_eq(5, 2, nv=4, trials=3000)
    tot += audit(T, seen, "EQ(5,2,nv4)")
    T, seen = census_eq(3, 3, nv=4, trials=2500)
    tot += audit(T, seen, "EQ(3,3,nv4)")
    T, seen = census_neq(5, 2, nv=3, trials=2000)
    tot += audit(T, seen, "NEQ(5,2,nv3)")
    T, seen = census_neq(3, 3, nv=3, trials=2000)
    tot += audit(T, seen, "NEQ(3,3,nv3)")
    print("TOTAL_VIOL=%d" % tot)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
