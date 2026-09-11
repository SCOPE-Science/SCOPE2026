"""Finite-level reduction scaffold for lane-860 target.

Source: truncated Pi04 source S = {s in 2^{N^4} : forall a exists b forall c exists d s(a,b,c,d)=1}.
Levels t=0..T-1 map to global-tail index n=t; finite window checks
  m <= M(t), k <= K(t), l <= L(t).
Good (merging, 2-letter-essential) vs Bad (splitting, 3-letter-essential)
proper primitive morphisms. Checks:
  (a) finite-window dependence => continuity of level map,
  (b) positive instance (all-ones source): all levels good => telescoped
      product is 2-letter primitive => finite-level rank<=2 certificate,
  (c) negative instance (all-zeros source): all levels bad => no telescoping
      over windows up to bound B collapses to 2 letters (bounded obstruction
      check), but NO uniform rank>=3 certificate (ergodic-measure / dimension
      group invariant not computed) => negative direction gap.
  (d) upper-bound quantifier count: naive exists-sequence projection is
      Sigma11 (analytic), not Pi04, without a uniformization/countable-section
      theorem (obstacle O1).
"""
import itertools, json

# --- morphisms on alphabet {0,1,2} ---
TAU_MERGE = {"0": "001", "1": "011", "2": "001"}   # image in {0,1}
TAU_SPLIT = {"0": "0012", "1": "0112", "2": "0212"}  # image uses {0,1,2}

def image_letters(tau):
    return sorted(set("".join(tau.values())))

def is_proper(tau):
    starts = set(v[0] for v in tau.values())
    ends = set(v[-1] for v in tau.values())
    return len(starts) == 1 and len(ends) == 1

def incidence(tau, alpha="012"):
    M = [[0]*3 for _ in range(3)]
    for j, a in enumerate(alpha):
        for ch in tau[a]:
            M["012".index(ch)][j] += 1
    return M

def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def is_primitive_on_letters(tau, letters):
    sub = [c for c in "012" if c in letters]
    idx = {c: i for i, c in enumerate(sub)}
    m = len(sub)
    M = [[0]*m for _ in range(m)]
    for j, a in enumerate(sub):
        for ch in tau[a]:
            if ch not in idx:
                return False
            M[idx[ch]][j] += 1
    P = [row[:] for row in M]
    for _ in range(m*m + 1):
        if all(P[i][j] > 0 for i in range(m) for j in range(m)):
            return True
        P = [[sum(P[i][k]*M[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
    return False

def compose(f, g):
    """Return f o g: apply g then f. Dicts on alphabet."""
    h = {}
    for a in "012":
        h[a] = "".join(f[ch] for ch in g[a])
    return h

# --- finite-window reduction ---
def window(t):
    # slowly growing bounds; finite for each t
    Mt = min(t, 3)
    Kt = min(t, 3)
    Lt = 4
    return Mt, Kt, Lt

def level_is_good(s, t, box):
    """s: dict keyed (a,b,c,d)->0/1 within box; n=t global-tail index."""
    A, B, C, D = box
    n = t
    if n >= B:
        return None  # outside truncated box; in full construction reads true source
    Mt, Kt, Lt = window(t)
    for m in range(min(Mt + 1, A)):
        for k in range(min(Kt + 1, C)):
            if not any(s.get((m, n, k, l), 0) == 1 for l in range(min(Lt + 1, D))):
                return False
    return True

def run_demo():
    out = {}
    out["merge_image"] = image_letters(TAU_MERGE)
    out["split_image"] = image_letters(TAU_SPLIT)
    out["merge_proper"] = is_proper(TAU_MERGE)
    out["split_proper"] = is_proper(TAU_SPLIT)
    out["merge_incidence"] = incidence(TAU_MERGE)
    out["split_incidence"] = incidence(TAU_SPLIT)
    out["merge_primitive_2letter"] = is_primitive_on_letters(TAU_MERGE, {"0", "1"})
    out["split_primitive_3letter"] = is_primitive_on_letters(TAU_SPLIT, {"0", "1", "2"})

    A = B = C = 4
    D = 5
    T = 4
    box = (A, B, C, D)
    s_pos = {(a, b, c, d): 1 for a in range(A) for b in range(B) for c in range(C) for d in range(D)}
    s_neg = {(a, b, c, d): 0 for a in range(A) for b in range(B) for c in range(C) for d in range(D)}

    # continuity: record window sizes per level
    out["windows"] = {t: window(t) for t in range(T)}
    out["windows_finite"] = all(all(v < 10**9 for v in w) for w in out["windows"].values())

    pos_levels = [level_is_good(s_pos, t, box) for t in range(T)]
    neg_levels = [level_is_good(s_neg, t, box) for t in range(T)]
    out["positive_levels_all_good"] = all(v is True for v in pos_levels)
    out["negative_levels_all_bad"] = all(v is False for v in neg_levels)

    # telescoping certificate, positive: compose all-merge run
    h = {a: a for a in "012"}
    for _ in range(T):
        h = compose(TAU_MERGE, h)
    out["telescoped_pos_image"] = image_letters(h)
    out["telescoped_pos_proper"] = is_proper(h)
    out["telescoped_pos_primitive_2letter"] = is_primitive_on_letters(h, {"0", "1"})
    out["positive_rank2_finite_cert"] = (
        out["telescoped_pos_image"] == ["0", "1"]
        and out["telescoped_pos_primitive_2letter"]
    )

    # negative: bounded-telescoping collapse search up to width W
    # check whether any contiguous block product of splits collapses to <=2 letters
    neg_collapse_found = False
    W = T
    for i in range(T):
        h = {a: a for a in "012"}
        for j in range(i, min(T, i + W)):
            h = compose(TAU_SPLIT, h)
            if len(image_letters(h)) <= 2:
                neg_collapse_found = True
    out["negative_bounded_collapse_found"] = neg_collapse_found
    out["negative_rank3_certificate"] = False  # no ergodic/dim-group invariant computed
    out["negative_gap"] = (not neg_collapse_found) and (not out["negative_rank3_certificate"])

    # upper-bound quantifier accounting
    out["upper_bound_accounting"] = {
        "KR_predicate": "finite Boolean combo of open/closed => Delta02 uniformly",
        "forall_n_KR": "countable conjunction => Pi02 (closed part Pi01, open part Pi02)",
        "diameter_generating": "arithmetical Pi03 on code alone",
        "exists_sequence_over_NN": "projection of Pi03 along Baire space => Sigma11 (analytic) in general",
        "missing": "uniformization / Lusin-Novikov countable-section or Saint-Raymond rank bound to pull back to Pi04; NOT established",
    }
    return out

if __name__ == "__main__":
    out = run_demo()
    print(json.dumps(out, indent=1, default=str))
    with open("reduction_demo_log.json", "w") as f:
        json.dump(out, f, indent=1, default=str)
