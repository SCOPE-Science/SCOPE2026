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
# Verification record

The analytic proof in `RESULT.md` establishes the finite-population moment formula for every even \(n\ge4\) and every integer \(2\le k\le n-2\), including endpoints. Exact symbolic algebra reduces the derived expression for \(\operatorname{Var}(R_k)\) to \(A_{n,k}+B_{n,k}J\) with zero residual and verifies the quoted upper expression. The inequalities and equality cases are justified analytically by \(0\le J\le n^2\), and the geometric realization uses an explicit continuous family of antipodally paired closed equilateral convex polygons.

The embedded file `chord_variance_verifier.py` runs with Python's standard library, `python chord_variance_verifier.py`, and reports `VERIFY_OK exact_subsets=16 geometry_equalities=2` after exhaustive rational evaluation of all subsets for its specified \(n\)-and-\(k\) instances. Its computations verify illustrative cases but do not certify the universal proof. The proof does not establish odd-edge optimal bounds, polygon congruence recovery, finite-sample statistical bounds or historical uniqueness of the claim. Independent audit has not been performed.
