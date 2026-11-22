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

# Verification of the four-site diagonal-loading theorem

Run `python CHECKER.py` from the extracted files with installed SymPy, NumPy and SciPy. The script checks the characteristic-polynomial splitting into reflection parity sectors, determinant and derivative algebra (exact symbolic identities), 6,000 randomly selected feasible nonnegative allocations, 60 independently optimized budget-parameter scenarios, seven scalar activation-bracket cases and two reference controls. The analytical proof, not the finite tests, establishes the all-positive-parameter theorem.

The mathematically decisive steps are strict eigenvalue symmetrization (the positive minimum eigenvector), exact formulas for both extremal eigenvalues, monotone sign crossing in \(t\), and monotone uniqueness of the boundary root \(q_c\). The verifier does not establish literature priority or extend the theorem to larger paths, unequal gains prices, or heterogeneous edge weights.

Independent mathematical audit has not been performed.
