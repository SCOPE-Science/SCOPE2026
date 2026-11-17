---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Beta monomial moments integrate to m!/(k+t)_{m+1}; reciprocal series yields exact m=1 quadratic and m=2 cubic numerator polynomials. At m=1 coefficient/discriminant signs show exactly one negative zero inside |s|<1 iff t<1/√2. At m=2 negative real root and conjugate pair follow from negative cubic discriminant; Vieta modulus bounds put conjugate pair outside; P2(-1)=2(2t+1)(2t²+2t−3) gives threshold (√7−1)/2. t=1 constant numerators and boundary s=-1 excluded. Independent exact Taylor coefficient and boundary checks agree. All t>0 domain from proof, finite checks not substitute for it.

## originality

FAIL

FAIL: full earlier published same-weight, same scalar zero counting theorem already establishes complete N_m(t) for m=0,1,2,3 with exact tau_1,tau_2 and negative-root geometry. This claim is direct restriction m∈{1,2}, not an independent result.

## value

FAIL

FAIL: although the exact weighted Bergman kernel zero-loss thresholds are natural and mathematically worthwhile, this submitted theorem duplicates the established exact table with no separate new invariant, boundary, or implication. Recomputing the same two cases does not supply additional research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
