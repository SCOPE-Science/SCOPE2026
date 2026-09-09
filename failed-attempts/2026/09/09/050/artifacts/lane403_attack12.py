"""Lane-403 attack v12 (fixed): constructive lift lemma, exact, fast.

Lemma (Lift): M|N, K=N/M, tau a single M-cycle. Atoms (b,j), b in Z_M,
j in Z_K. psi(b,j) = (tau(b), j + 1_{b==b0}) for fixed b0. Then psi is a
single N-cycle lifting tau.
Justification for testing one tau per (M,N): all single M-cycles are
S_M-conjugate; block-relabel pi lifts to atom-permutation conjugating the
lifts, preserving single-cycle property. So verify canonical tau=(0 1..M-1)
for ALL b0, plus (for M<=6) all taus exhaustively, plus random taus for
larger M. Levels: (M,N) in {(2,6),(3,6),(2,30),(3,30),(5,30),(6,30),
(10,30),(15,30),(2,8),(4,8),(4,16),(8,32)}.
Corollary: pure-odometer N-pattern (single N-cycle) is S_N-conjugate to psi,
so some g sends odometer pattern to a pattern with M-quotient tau.
"""
import json, os, random, itertools

ART = os.path.dirname(os.path.abspath(__file__))
random.seed(312)
res = {}

def single(p):
    n = len(p)
    seen = [False] * n
    x, c = 0, 0
    while not seen[x]:
        seen[x] = True
        x = p[x]
        c += 1
    return c == n

def build_lift(tau, K, b0=0):
    M = len(tau)
    N = M * K
    psi = [0] * N
    for b in range(M):
        for j in range(K):
            psi[b * K + j] = tau[b] * K + (j + (1 if b == b0 else 0)) % K
    return psi

def lifts_tau(psi, tau, K):
    M = len(tau)
    return all((psi[b * K + j] // K) == tau[b]
               for b in range(M) for j in range(K))

out = {}
pairs = [(2, 6), (3, 6), (2, 30), (3, 30), (5, 30), (6, 30),
         (10, 30), (15, 30), (2, 8), (4, 8), (4, 16), (8, 32)]
for (M, N) in pairs:
    K = N // M
    tau0 = [(b + 1) % M for b in range(M)]
    # canonical tau, all b0
    good_b0 = [b0 for b0 in range(M)
               if single(build_lift(tau0, K, b0))
               and lifts_tau(build_lift(tau0, K, b0), tau0, K)]
    entry = {"K": K, "canonical_tau_all_b0_lift": len(good_b0) == M,
             "good_b0_count": len(good_b0)}
    if M <= 6:
        taus = [list(t) for t in itertools.permutations(range(M))
                if single(list(t))]
        ok = 0
        for tau in taus:
            if any(single(build_lift(tau, K, b0))
                   and lifts_tau(build_lift(tau, K, b0), tau, K)
                   for b0 in range(M)):
                ok += 1
        entry["exhaustive_taus"] = len(taus)
        entry["exhaustive_ok"] = ok
        entry["exhaustive_full"] = (ok == len(taus))
    else:
        ok = 0
        NT = 12
        for _ in range(NT):
            perm = list(range(M))
            random.shuffle(perm)
            tau = [0] * M
            for i in range(M):
                tau[perm[i]] = perm[(i + 1) % M]
            if any(single(build_lift(tau, K, b0))
                   and lifts_tau(build_lift(tau, K, b0), tau, K)
                   for b0 in range(M)):
                ok += 1
        entry["sampled_taus"] = NT
        entry["sampled_ok"] = ok
    out[f"{M}|{N}"] = entry

res["lift_lemma"] = out
res["all_ok"] = all(
    v["canonical_tau_all_b0_lift"] and
    (v.get("exhaustive_full", True)) and
    (v.get("sampled_ok", 1) == v.get("sampled_taus", 1))
    for v in out.values())
res["lemma_statement"] = ("For every single M-cycle tau with M|N, the "
    "twisted product lift psi(b,j)=(tau(b), j+1_{b==b0}) is a single N-cycle "
    "with M-quotient tau. Hence (S_N-transitivity on N-cycles) some "
    "conjugator g sends the pure-odometer N-pattern to a pattern inducing "
    "tau on the M-quotient: the odometer H-orbit meets every cyclic-factor "
    "basic open at divisor levels.")

with open(os.path.join(ART, "finite_level_log12.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
