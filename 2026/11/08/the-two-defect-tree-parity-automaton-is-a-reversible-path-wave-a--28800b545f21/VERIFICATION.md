---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Pinned RESULT.md blob 887184132cc35d2dc3288f7b5518c81f57e1111c gives a rooted even-offspring Schur identity det(XI-A(H))=X^|H| and root Green function X^-1. Each of the m=d+1 spine vertices has odd offspine branch count; eliminating them over F_2[X,X^-1] gives H_m=(X²+1)I_m+X A(P_m). Tridiagonal determinant recurrence yields Q_m(X)², and unit off-diagonal coefficients make the nonzero-primary module cyclic and similar to the m-site reversible wave T_m. Fitting decomposition yields q^(2m) initially periodic states, exact period 2(m+1), fixed counts q^deg gcd(Q_m²,X^t+1), valuation formula and Möbius orbit counts. Inspected verify/matching_check.py blob 7301b97a2fba0ad5210ca02e229c5a63f902bd6e and dynamics_check.py blob becc64b3fe3c09844ac98d612bdf8c7a4a7fd64f; independently checked matching-polynomial identity for all 12 n=4 and 840 n=6 labeled two-defect trees. Infinite result derives from the branch-elimination algebra, not exhaustive small n.

## originality

PASS

Best-of-knowledge: the tree-to-path-wave conjugacy under exactly two even-degree defects and complete d-only periodic orbit census go beyond general tree determinant computation, single-even-offspring nilpotence, and one-dimensional CA methods.

## value

PASS

A structural invariant of every finite tree with precisely two even-degree vertices collapses complex branch geometry to an exact reversible path-wave dynamics with explicit period and all periodic orbit counts. The branch-independent conjugacy and Fitting decomposition are motivated natural classifications, not a trivial single-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
