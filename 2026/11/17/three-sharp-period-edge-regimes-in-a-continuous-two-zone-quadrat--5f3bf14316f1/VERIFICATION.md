---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytic proof is in `RESULT.md`. It uses an exactly invertible logarithmic coordinate, conservation of a globally defined piecewise \(C^2\) potential, a critical-point census, and singular-integral asymptotics. Three coefficient regimes and every fixed lower-zone coefficient \(h\geq0\) are covered by the proof.

Run `python checker.py` with SymPy and mpmath. The executable tests the potential derivative, vanishing value at the switching interface, nondegenerate center curvature, saddle location/height/curvature, \(k=1\) exact identity, and energy derivative. It also performs three finite-precision quadratures checking that the three periodic test cases have positive least periods, including representative large-energy and near-critical cases. The observed result is `PASS: symbolic potential, stationary point, curvature, energy and critical identities; three positive periods and edge comparisons`.

The finite quadratures do not establish the full asymptotic statements. The infinite statements rely on the integral comparisons, Taylor expansions at the critical turning points, and global potential-graph reasoning presented in the written proof. The smooth and piecewise primary papers were compared for implication, with possible unpublished equivalents left as a limitation. Independent audit is not yet performed.
