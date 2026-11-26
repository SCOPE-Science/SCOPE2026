---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Mixed sets dominate immediately except for at most two vertices; when the two singletons have distinct indices, an observed vertex with a third index can force a missing vertex and then the other is forced. For a one-shore set of size at least two, the opposite shore is observed and each of its vertices sees either r or r−1 of the r omitted vertices. This stalls at r≥3, starts a force at r=2, and succeeds at r≤1. A one-shore singleton succeeds on Cr_3=C_6 but stalls for n≥4, and the empty set fails. Counting the disjoint mixed and one-shore classes gives the polynomial and hence the reported total and minimum layers. A separately written bit-mask replay exhausted all 87,360 subsets for 3≤n≤8, checking classification, coefficients, totals and minimum layers; the proof, not the replay, gives all n.

## originality

FAIL

A distinct indexed generalized crown-graph result covers the complete frozen classification and polynomial at k=1 without new graph-specific work. The overlapping record is dated the same day; this establishes mathematical coverage and defeats the claim of a distinct contribution, but does not settle historical priority. The later ordinary-crown result overlaps on n≥4 and is corroboration, not priority evidence. Inaccessibility of the 2019 paper is not a failure reason.

## value

FAIL

The complete enumerator of a natural graph family is potentially useful, but the frozen contribution is mechanically obtained from the indexed generalized enumerator by setting k=1. The total and minimum counts simply evaluate or extract coefficients of that same polynomial, with no surviving distinct mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
