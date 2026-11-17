---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For S⊆∏[n_i], to realize S\{x} but not x requires x to be a strictly largest coordinate among S in some i; conversely the coordinate maxima of any desired T⊆S then exclude every y outside T by its private maximum. Each coordinate has either one private maximum label or none; for prescribed j labels the count of m-coordinate tuples avoiding them is n_i^m−j∑_{v=1}^{n_i}(v−1)^{m−1}. Inclusion-exclusion divided by m! gives s_m, with no repeated successful points. At m≥2 each nontrivial coordinate supports at most one label and independent two-level witnesses give VCdim max(1,r). For q_m-alphabet samples each coordinate emits label a with probability p_m=A_m(q_m)/q_m^m≤1/m; Bonferroni with d_mp_m=log m+c+o(1), d_mp_m²→0 proves exp(−exp(−c)), and collision probability is o(1). Handles m=1, n_i=1, zero trace, and arbitrary changing alphabets.

## originality

PASS

Exact principal-downset shattering profiles and the varying-alphabet coupon threshold were not found as a theorem or automatic corollary in the checked higher-arity VC, convex geometry, categorical-subcube or general box literature; formalism and generic coupon convergence are credited. Best-of-knowledge originality, with a significant terminology-priority risk.

## value

PASS

Principal order ideals of finite products of chains are a canonical finite geometric range space; an all-coefficient count, not merely VCdim, measures its complete shattering complex. The sampling theorem supplies a natural sharp, model-relevant dimension transition between Boolean and large alphabets. Arbitrary grid dimensions and alphabet lengths prevent an artificial finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
