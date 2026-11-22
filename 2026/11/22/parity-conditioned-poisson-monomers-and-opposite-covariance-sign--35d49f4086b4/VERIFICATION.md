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

The standalone `verify_tripartite.py` depends only on Python 3 standard-library modules. Running `python3 verify_tripartite.py` on the exact packaged source produced `TRIPARTITE_CHECKS_PASSED 344785`.

* `exact_counts(n)` reconstructs the labelled three-shore count from the displayed finite factorial formula. `brute_counts(n)` independently enumerates all matchings by a lowest-unprocessed-vertex recursive decomposition. Their histograms agree exactly for each \(1\le n\le5\).
* For each \(2\le n\le16\) and activity parameter \(c\in\{0.2,1,2,5\}\), the code normalizes the finite law, calculates total variation including limiting probability outside finite support, and checks the claimed explicit upper bound.
* For \(c=2\), direct probability sums at even \(n=80\) and odd \(n=81\) produce opposite distinct-shore covariance signs, as predicted.

These checks corroborate arithmetic and finite formulas; no finite program independently proves infinitely many instances. The mathematical proof establishes all-size TV bounds, convergence of polynomial moments, and strictly opposite asymptotic covariance limits. The theorem is for fixed \(c>0\), equal activities, and exactly balanced three-part complete graphs; no finite-\(n\) universal sign assertion or independently validated historical priority is claimed.
