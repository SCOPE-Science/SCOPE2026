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

Run `python check_exact.py` (requires SymPy, NumPy and SciPy). The symbolic section checks the complete \(3\times3\) integrated-density Lyapunov equation entry by entry, the time formula, and unit capture probability. The independent finite matrix section constructs the full \(2n\)-vertex graph for each integer \(2\le n\le12\), verifies the invariant bright subspace and dark/bright projections, and solves the reduced continuous Lyapunov equation for three sets of physical parameters. The executable passed both suites. The analytic certificate is an all-parameter identity; finite experiments are consistency checks only.
