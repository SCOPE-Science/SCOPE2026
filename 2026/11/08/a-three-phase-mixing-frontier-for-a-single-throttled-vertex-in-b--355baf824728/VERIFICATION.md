---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. Convexity of ||P-J||_2 and automorphism averaging over U\{u0} and V reduce every arbitrary feasible symmetric chain's optimum to scalar a in [0,1/m], preserving fixed escape b and all row-holding constraints. Complete decomposition gives two quotient nonstationary roots t± of x²-Tx+D and internal eigenvalues alpha=1-ma (mult m-2) and beta=1-b/m-(m-1)a (mult m-1), all others accounted for. Loewner monotonicity in a makes positive envelope decrease and negative eigenvalue modulus increase. For b<=1/(m+1), a=1/m saturates; in the middle a1 cancels T and internal modes stay below sqrt(-D) by the stated exact nonnegative factorizations; for b>2/3 a2 uniquely crosses alpha and -t_- in (a1,b/m), with q(alpha)=a(m-1)(b-ma)>=0 establishing t_+ does not dominate. Independent sympy algebra verified q(alpha), high-crossing polynomial and roots for m=3,4,10 and b=2/3,4/5,1; source script verifies more finite rational cases. Boundaries b=0,1/(m+1),2/3,1 consistent; m=2 expressly excluded.

## originality

PASS

PASS on best knowledge, qualified. General fastest symmetric mixing as convex SDP and orbit averaging are due to Boyd and colleagues. Their unrestricted complete bipartite optimum at SLEM=1/3 is exactly the single b=2/3 point of this constrained frontier; it is not new. The published matching-edge capacity law prescribes m disjoint edges and has two affine regimes; it does not impose a single vertex's total escape rate, and the feasible slices differ, so neither is a reformulation or bound implying this three-phase b-frontier. Another result for two-mass complete bipartite stationary distributions changes invariant measure, not one distinguished-row constraint. No inspected older theorem covers the full constrained all-m,b optimizer, though alternative FMMC parametrizations may exist.

## value

PASS

PASS. Fixing the exit probability at one bottleneck vertex is a natural local mixing-control constraint. The all-size exact semidefinite optimum has three spectral activation regimes, sharp thresholds b=1/(m+1) and b=2/3, and explicit optimizer/robustness formula including the quadratic-root branch. This is more than restating the unrestricted uniform optimum or doing numerical SDP instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
