---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Exact prepoint kernel gives n>=2 -> -r or 2n+r and n<=-2 -> +r or 2n-r; center 0 -> ±1, ±1 -> {0, ±2}. For r=1 the unique communicating class is {0,±1}∪{±(3·2^k−1)}, and direct incoming-flux balance yields 1/5 center masses plus 1/(5·2^{k+1}) outer masses. For r>=2 closed class is the ±r(2^{k+1}−1) ladders, masses 2^{-k-2}, and center transient. Four-step P1⁴(x,0)>=1/16 and five-step P_r⁵(x,{±r}) minorization imply uniform TV geometric mixing. Exact geometric tail shells give (3/5,6/5) or (r,2r) liminf/limsup and p-moment iff p<1. Conditional one-step absolute drift equals 1 at 0, 0 at ±1, r outside; summing with geometric mixing gives 3t/5+O_x(1) for r=1 and rt+O_x(1) for r>=2, exact for exterior starts. Infinite-state statements are established by renewal/Doeblin arguments, not finite simulations.

## originality

PASS

PASS, best of knowledge, with strong known subcase: separate published November 2 result supplies the *identical* full r=1 stationary law, log-periodic tail, moment cutoff, and Doeblin rate, so none of these alone is original. The present all-r theorem additionally proves the sharp recurrence/occupation switch at r=2, gives unique stationary law and uniform mixing for every r>=2, and determines finite-time absolute-moment slopes; those additions are not consequences of the r=1 special-case theorem or generic multiplicative-reset papers. The original Lima–Curado model supplies the transition, not the exact threshold classification.

## value

PASS

PASS: The sharp origin-recurrence boundary between first two positive integer rule parameters and coexistence of uniform total-variation ergodicity with unbounded first moments are mathematically motivated questions for a nonstandard position-feedback Markov chain. The all-r exact-support/return/moment classification distinguishes lattice from continuum analyses, independent of already-known r=1 subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
