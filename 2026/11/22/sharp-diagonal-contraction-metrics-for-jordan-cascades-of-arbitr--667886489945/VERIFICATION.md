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

Run `python3 verify.py` using only the Python standard library. Successful execution prints `CASCADE_DIAGONAL_METRIC_DIAGNOSTIC_OK 3288`.

The checker recomputes the proposed diagonal metrics and normalized path edges in five dimensions, verifies the exact threshold and stronger-budget values, evaluates the weighted adjacency Perron eigenvalues via a positive power iteration, compares those values to the closed form, and tests many feasible randomized alternative metrics. It checks the exactly representable five-stage boundary \(P=\operatorname{diag}(1,2,8,32,64)\) and \(q=1/2\).

Computational comparisons are finite diagnostics, not a complete enumeration of all diagonal matrices and not an infinite/all-dimensional certificate. The universal theorem follows from the explicit Rayleigh–AM–GM inequality, its rigid equality case and the energy criterion proved in the accompanying mathematical text. No external or independent audit has been performed.
