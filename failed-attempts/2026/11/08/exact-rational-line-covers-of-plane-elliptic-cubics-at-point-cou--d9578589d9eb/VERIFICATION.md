---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

A line meets a smooth plane cubic in at most three distinct rational points. A cover with N/3 lines forces a partition of E(F_q) into zero-sum triples using rational flex O and chord-and-tangent law. The group sum is the unique nonidentity involution if one exists, ruling out equality exactly then. Cichacz’s zero-sum triple partition theorem provides the N/3 optimum otherwise. In the unique-involution case, a surjection G→Z/3 and the Goddyn–Halasz near transversal of H=ker χ yield N/3−1 disjoint collinear triples, then two rational lines cover the remaining three points, giving N/3+1. The explicit cyclic construction and small-field exact enumeration in the actual verify.py corroborate; the two published group existence theorems are essential infinite inputs, not checked merely by finite code. Finite fields of all characteristics allowed; rational flex and 3|N required.

## originality

FAIL

FAIL: an October 18, 2026 published SCOPE theorem states verbatim the same all-finite-field exact covering formula, including the unique nonzero rational 2-torsion excess-one case and the no-excess alternative. Its proof uses the same order-three quotient, near-transversal construction, and group-sum obstruction; its cyclic example matches the submitted one. Rewording the criterion from |G[2]|=2 to unique nonzero involution does not change the theorem. Cichacz and Goddyn–Halasz were already attributed in the prior result.

## value

FAIL

FAIL: the exact line-cover obstruction is independently worthwhile in the earlier result, but this submission reproduces it without a new parameter regime, stronger classification, sharper bound, or distinct independent consequence. Reassembling the same group-theoretic ingredients is a known-table/theorem recomputation, not an independently useful new fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
