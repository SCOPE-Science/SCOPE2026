"""Finite-level verifier for pinned Basilica cell blocking obstacle.

Pinned presentation (standard Bartholdi-Virag / Grigorchuk-Zuk):
  X = {0,1}^N (binary-tree boundary, product topology), cylinders [w].
  B = <a,b> with recursions on words (x in {0,1}, w word):
    a(0w) = 1 b(w),  a(1w) = 0 w        i.e. a = sigma(b, 1)
    b(0w) = 0 a(w),  b(1w) = 1 w        i.e. b = (a, 1)
  sigma swaps first letter; 1 denotes trivial section.

Checks (all finite, replayable, stdlib only):
  1. a,b are permutations of level n for n<=N.
  2. b fixes every word with prefix 1 (finite shadow of Fix(b) ⊇ [1]).
  3. b != 1 (explicit witness 00 -> 01).
  4. Level-transitivity (single orbit) for n<=N => minimality shadow.
  5. Bernoulli mass of fixed cylinder [1] = 1/2.
"""
import itertools, collections, json, sys

def apply_a(w):
    # w: tuple of bits; recursive via pinned formulas
    if not w:
        return ()
    x, rest = w[0], w[1:]
    if x == 0:
        return (1,) + apply_b(rest)
    else:
        return (0,) + tuple(rest)

def apply_b(w):
    if not w:
        return ()
    x, rest = w[0], w[1:]
    if x == 0:
        return (0,) + apply_a(rest)
    else:
        return (1,) + tuple(rest)

def apply_word(gens, w):
    # gens: string like "abA" where A=a^{-1}? Instead compute a^{-1}, b^{-1} by brute inverse per level.
    # Here only need <a,b> semigroup actions for transitivity (group orbit via BFS with inverses).
    cur = w
    for g in gens:
        if g == 'a':
            cur = apply_a(cur)
        elif g == 'b':
            cur = apply_b(cur)
    return cur

def invert_perm(mapping):
    inv = {}
    for k, v in mapping.items():
        inv[v] = k
    return inv

def level_words(n):
    return list(itertools.product([0, 1], repeat=n))

def check_level(n):
    W = level_words(n)
    ma = {w: apply_a(w) for w in W}
    mb = {w: apply_b(w) for w in W}
    # bijectivity
    assert len(set(ma.values())) == len(W), f"a not bijective at level {n}"
    assert len(set(mb.values())) == len(W), f"b not bijective at level {n}"
    # b fixes prefix-1 words
    fixed = [w for w in W if w[0] == 1]
    for w in fixed:
        assert mb[w] == w, f"b does not fix {w}"
    # b == identity on first letter (b=(a,1) preserves first bit), so level 1
    # carries no nontriviality signal; nontriviality witness lives at level >= 2.
    if n >= 2:
        wit = (0, 0) + (0,) * (n - 2)
        bwit = mb[wit]
        assert bwit != wit, "b==1 at level n?!"
    else:
        wit, bwit = (0,), mb[(0,)]
        # at level 1 b is trivial; record honestly, do not assert nontriviality
    nontriv = (bwit != wit) if n >= 2 else None
    # level transitivity via BFS with a,b and inverses
    inva = invert_perm(ma)
    invb = invert_perm(mb)
    start = W[0]
    seen = {start}
    q = collections.deque([start])
    while q:
        u = q.popleft()
        for v in (ma[u], mb[u], inva[u], invb[u]):
            if v not in seen:
                seen.add(v)
                q.append(v)
    transitive = (len(seen) == len(W))
    return {
        "n": n,
        "level_size": len(W),
        "b_fixes_prefix1_count": len(fixed),
        "b_nontrivial_witness": {"in": wit, "out": bwit, "nontrivial_at_this_level": nontriv},
        "transitive": transitive,
        "orbit_size": len(seen),
    }

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    rows = [check_level(n) for n in range(1, N + 1)]
    for r in rows:
        print(r)
    # topological-freeness verdict: b != 1 but fixes 2^{n-1} words at each level
    # => Fix(b) contains cylinder [1], clopen, mu0([1])=1/2.
    verdict = {
        "pinned_a": "sigma(b,1): a(0w)=1b(w), a(1w)=0w",
        "pinned_b": "(a,1): b(0w)=0a(w), b(1w)=1w",
        "fix_contains_cylinder": "[1]",
        "mu0_fix_lower_bound": 0.5,
        "b_ne_1_witness": "b(00)=01 (hence b(00w')=01... for all extensions)",
        "all_levels_transitive": all(r["transitive"] for r in rows),
        "consequence": "action minimal (level-transitive) but NOT topologically free; "
                       "Archbold-Spielberg => C(X)rtimes_r B NOT simple (B amenable so full=reduced).",
    }
    print(json.dumps(verdict, indent=2))
    assert all(r["transitive"] for r in rows), "transitivity failed"
    # explicit b(00)=01 check at word level
    assert apply_b((0, 0)) == (0, 1), "witness identity failed"
    assert apply_b((1, 0, 1)) == (1, 0, 1), "prefix-1 fixing failed"
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
