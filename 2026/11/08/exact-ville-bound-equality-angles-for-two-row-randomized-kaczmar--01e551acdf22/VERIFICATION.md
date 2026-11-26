---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With row 1 as the initial label, the null-line projection on a switch multiplies squared norm by q, and a repeat leaves it unchanged. The switch bits determine each row string uniquely by recursion, so are jointly iid fair and yield the binomial law and exact mean rⁿ. The mean-normalized process is a martingale; its logarithmic drift is log(√q/r)<0, so it tends to zero and any supremum at a threshold above one is attained on this probability-one event. For the first crossing, stopped values are bounded by λ/r, so bounded-time optional stopping and dominated convergence give E[Zτ;τ<∞]=1. Equality requires no overshoot. Write A=log(1/r)>0 and B=log(r/q)>0. The finite all-up prefix through its first crossing forces log λ=mA; the finite one-down-then-up prefix forces B/A integral. Both finite prefixes have positive probability (no infinite all-up event is used). Conversely integral B/A makes +A skip-free on the lattice, so no overshoot at any level mA. Since r>√q, B/A>1; B/A=d−1 is precisely q=r^d for d≥3. Strict convexity, f_d(1/2)>0, f_d(1)=0 and f′_d(1)>0 give one nonunit root in (1/2,1), hence admissible q. Lattice rounding gives the full ceiling formula; d=3 gives the stated golden-ratio value. This argument is infinite-horizon; the frozen verifier was inspected but not executed.

## originality

PASS

Credit the jointly binomial switch law and complete row-correlation and threshold equality classification for this normalized Kaczmarz family. Standard Ville sharpness and zero overshoot are not new; the skip-free staircase is the expected consequence once the specific walk has been derived and its arithmetic necessity established.

## value

PASS

This supplies a concrete nonsingular randomized solver that exactly attains a time-uniform error bound, with a complete exceptional set rather than just an example. It distinguishes lattice exactness from strictness at the natural mean rate and gives a useful benchmark for adaptive error certificates. It does not assert sharpness for the different generic operator-norm rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
