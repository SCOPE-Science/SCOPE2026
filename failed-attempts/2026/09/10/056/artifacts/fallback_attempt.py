"""Bounded fallback attempts: uniform-Gamma 3-divisibility for Basilica cell.

F0 = {u_a, u_b, e0=1_[0], e1=1_[1]}; need p1,p2,p3 pairwise orthogonal
projections, ||[pi,x]||<0.01 on F0, tau(pi)=1/3+-0.01, ||p1+p2+p3-1||<0.01.

Attempt R1 (diagonal family, exhaustive + exact gap lemma):
  Lemma: d in C(X_k) a projection (0/1 diagonal in level-k Koopman picture),
  u a permutation unitary => ||[d,u]|| is 0 or >= 1.
  Proof: [d,u]_{i,sigma(i)} = (lambda_i - lambda_{sigma(i)}); entries in {-1,0,1};
  if any nonzero entry, operator norm >= max |entry| = 1. QED.
  Consequence: ||[d,u_a]||,||[d,u_b]||<0.01 forces EXACT invariance under a,b
  => (level-transitivity) d in {0,1} => tau(d) in {0,1} => trace 1/3+-0.01
  impossible. So NO diagonal projection at ANY level can serve as any pi.
  Script: exhausts all 2^(2^k) diagonal projections at k<=4, confirms gap.

Attempt R2 (trace arithmetic): tau(d)=m/2^k for diagonal level-k d;
  find minimal k with |m/2^k-1/3|<=0.01 (answer: k=6, 21/64). Combined with R1:
  even where trace is reachable, centrality forces triviality. No diagonal route.

Attempt R3 (coefficient lower bound for general ansatz): for p=SUM f_g u_g,
  [p,e1] has u_a-coefficient f_a*(e1-e1 circ a^{-1}}) with |e1-e1 circ a|=1
  everywhere (a swaps [0],[1]) => ||f_a||_inf <= ||[p,e1]|| < 0.01. Similarly
  f_{a^{-1}}, and every word moving level-1 cylinders is suppressed; only
  <b>-orbit coefficients survive F0-diagonal constraints, but [p,u_a]<0.01
  couples them to suppressed ones. Script certifies the swap identities.
"""
import itertools, math

# ---------- pinned action (same as verify.py) ----------
def apply_a(w):
    if not w: return ()
    x, rest = w[0], w[1:]
    return ((1,) + apply_b(rest)) if x == 0 else ((0,) + tuple(rest))
def apply_b(w):
    if not w: return ()
    x, rest = w[0], w[1:]
    return ((0,) + apply_a(rest)) if x == 0 else ((1,) + tuple(rest))

def level_words(n):
    return list(itertools.product([0, 1], repeat=n))

def perm_of(f, W):
    idx = {w: i for i, w in enumerate(W)}
    return [idx[f(w)] for w in W]

def commutator_norm_01_gap(diag, perm):
    """diag: tuple of 0/1; perm: list sigma with (u v)_i = v_{sigma(i)}-style.
    [d,u] has entries (l_i - l_{sigma(i)}); return (is_zero, max_abs_entry)."""
    diffs = [abs(diag[i] - diag[perm[i]]) for i in range(len(diag))]
    m = max(diffs)
    return (m == 0, m)

def attempt_R1(kmax=4):
    print("=== R1: diagonal-family gap census ===")
    ok = True
    for k in range(1, kmax + 1):
        W = level_words(k); n = len(W)
        pa = perm_of(apply_a, W); pb = perm_of(apply_b, W)
        total = 0; bad = 0; min_nonzero = None
        for bits in itertools.product([0, 1], repeat=n):
            if all(v == bits[0] for v in bits):
                continue  # trivial
            total += 1
            for perm in (pa, pb):
                zero, m = commutator_norm_01_gap(bits, perm)
                if not zero:
                    if m < 1:
                        bad += 1
                    min_nonzero = m if min_nonzero is None else min(min_nonzero, m)
        print(f"level {k}: {total} nontrivial diagonals, violations(m<1 nonzero)={bad}, "
              f"min nonzero entry={min_nonzero}")
        assert bad == 0, "gap lemma violated?!"
        # exact-invariance => triviality check: count a,b-invariant diagonals
        inv = 0
        for bits in itertools.product([0, 1], repeat=n):
            za, _ = commutator_norm_01_gap(bits, pa)
            zb, _ = commutator_norm_01_gap(bits, pb)
            if za and zb:
                inv += 1
        print(f"  exactly (a,b)-invariant diagonals: {inv} (expect 2: 0 and 1)")
        assert inv == 2, "nontrivial invariant clopen?!"
        ok = ok and (inv == 2)
    print("R1 RESULT: diagonal family admits NO approximant (gap 0-or->=1 forces triviality).")
    return ok

def attempt_R2():
    print("=== R2: trace arithmetic ===")
    best = {}
    for k in range(1, 10):
        sols = [(m, abs(m / 2**k - 1/3)) for m in range(2**k + 1)]
        m, d = min(sols, key=lambda t: t[1])
        best[k] = (m, d)
        print(f"level {k}: best m={m}, tau={m/2**k:.6f}, |.-1/3|={d:.6f} {'OK' if d <= 0.01 else '--'}")
    mink = min(k for k in best if best[k][1] <= 0.01)
    print(f"R2 RESULT: minimal diagonal level for trace tolerance = {mink}; "
          f"R1 kills centrality there anyway.")
    return mink

def attempt_R3():
    print("=== R3: coefficient suppression identities ===")
    # a swaps [0],[1]: check on level 2 (hence boundary)
    W = level_words(3)
    e1 = {w: w[0] for w in W}  # indicator of [1]
    # e1 - e1 circ a^{-1}: a swaps level-1 cylinders, so difference is +-1 everywhere.
    swap = all(e1[apply_a(w)] == 1 - e1[w] for w in W)
    print(f"a swaps [0]<->[1] pointwise: {swap}")
    assert swap
    # b preserves [0],[1] but swaps [00]<->[01]:
    pres = all((apply_b(w)[0] == w[0]) for w in W)
    e00 = {w: 1 if w[:2] == (0, 0) else 0 for w in W}
    swapb = all(e00[apply_b(w)] == (1 if w[:2] == (0, 1) else 0) for w in W)
    print(f"b preserves first letter: {pres}; b swaps [00]<->[01]: {swapb}")
    assert pres and swapb
    print("R3 RESULT: F0-diagonal commutators suppress f_a (and all words moving [0]/[1]) "
          "below 0.01; only <b>-supported coefficients survive, but [.,u_a]<0.01 couples "
          "them back. No finite ansatz closed; general construction not found in bound.")

def main():
    r1 = attempt_R1()
    r2 = attempt_R2()
    attempt_R3()
    print({"R1_diagonal_no_go": r1, "R2_min_trace_level": r2,
           "fallback_constructed": False,
           "verdict": "ATTEMPTED_AND_BLOCKED"})
    print("FALLBACK_VERIFY_DONE")

if __name__ == "__main__":
    main()
