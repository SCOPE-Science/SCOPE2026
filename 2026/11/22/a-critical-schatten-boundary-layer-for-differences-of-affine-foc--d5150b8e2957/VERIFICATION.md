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

# Verification notes

Analytical checks: the coefficient formula was derived from the binomial theorem in the normalized Fock basis. The step-shift trace-norm estimate uses a convergent binomial series; the operator estimate uses the exact maximum of \(y^{k/2}e^{-\delta y}\). The remainder bounds and Schatten interpolation verify the moving asymptotic scale, and the Riemann-sum argument verifies the complete counting law. The Hilbert–Schmidt identity was independently obtained by summing squared subdiagonal weights.

Reproducible finite checks: run `python3 checker.py` after installing NumPy. It passes 33 test groups, comparing exact Hilbert–Schmidt formulas, direct coefficient sums, leading-shift asymptotics and first-order matrix approximations; both worst Hilbert–Schmidt relative discrepancies are below \(1.2\times10^{-14}\). Finite checks cannot establish the infinite-dimensional asymptotic or literature novelty.

Scientific limits: no assertions for simultaneously moving centers, different slopes, non-Gaussian Fock spaces or \(p<1\). Independent audit has not been performed.
