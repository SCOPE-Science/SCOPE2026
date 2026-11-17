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

For the selfadjoint Schur mask, Haagerup order majorization reduces the norm to the least t with a Hermitian P of diagonal <=t and P±M positive. The displayed P has P−M=vww* with v=2(ab−1)/(2ab+a+b); its P+M zero-sum eigenvalues are 2, and the 2×2 constant-block determinant is exactly zero with positive diagonal. For arbitrary feasible P, part-permutation averaging and the two 2×2 PSD compressions force 2√(ab)≤√((p+1)(r+1))+√((p−1)(r−1)). Diagonal constraints p≤1+a(t−1), r≤1+b(t−1) imply t−1≥v for t<2. This independently reconstructs both bounds for all positive sizes. Symmetric limit checks agree. Independent finite PSD eigenchecks at (2,2),(2,3),(3,7),(5,9) are diagnostic, not the infinite proof.

## originality

PASS

Best-of-knowledge original full claim after comparing equivalent formulations, dominating results, exact tables and known theorem implications. Relevant inaccessible primary literature remains named as residual risk; no search absence is treated as a proof of novelty.

## value

PASS

The natural graph Schur idempotent is a matrix norm projection; sharp unbalanced two-part constants quantify symmetry breaking beyond transitive balanced cases. Exact all-size formula and distinct asymptotic regimes are reusable operator-space invariants, not a relabeled known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
