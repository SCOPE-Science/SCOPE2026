---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Every real bounded-variation input pair has a pointwise secant-slope mask for positive-part activation, A_theta=I+diag(theta)(Q_r-I). The absolutely summable jump decomposition reduces total-variation gain to step columns. Their two side ramps yield E_r=2 sum over nonadjacent falling transitions at weights 1,...,r-1, maximal 2 floor(r^2/4) per wing, hence 1+4 floor(r^2/4)/(2r+1). The finite principal matrix of I-Q_r is strictly positive definite from its adjacent-edge energy and realizes any optimal sign pattern on support of Q_rH-H; nonnegative finite-variation attaining pairs follow after adding a constant. Check r=1 exactly 1, r=2 9/5; no quotient at constant differences. Independent rational binary-wing enumeration for r=1..6 agreed with predicted constants. The verifier source was inspected, not taken as a proof or uncritically as a PASS.

## originality

PASS

No searched stronger statement implies the exact two-input BV modulus of the two-radius centered uniform envelope. One-input full discrete maximal regularity and unrelated two-choice L2 bounds have different hypotheses and conclusions; historical equivalences not indexed remain possible.

## value

PASS

A structural exact, attained stability threshold at r=2 for an elementary two-choice smoothing envelope, with linear instability as window radius grows, is mathematically motivated by the distinction between output variation and pairwise sensitivity; proof supplies usable sharp constants and witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
