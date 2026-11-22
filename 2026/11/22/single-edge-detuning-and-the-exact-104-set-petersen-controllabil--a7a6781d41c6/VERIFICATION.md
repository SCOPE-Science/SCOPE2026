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

# Reproducibility and checks

Run `python3 checker.py` using only the Python standard library. The program independently reconstructs the fifteen Petersen edges, weighted Laplacian, eigenspaces for eigenvalues two and five, projections of the modified-edge incidence vector, and all finite exact-rational rank tests. It reports the two all-subset count vectors, a complete count of four-row rank patterns, the rank-one proportionality patterns, and ends with `VERIFY_OK`. No external paper, local data file, or numerical package is needed to replay it.

The exact enumeration comprises all \(2^{10}=1024\) coordinate subsets and all \(\binom{10}{4}=210\) minimum-size candidates; it proves the finite rational matrix rank comparisons. A separate modular Kalman check examines all 252 five-input sets at the unit edge weight and all 210 four-input sets at each of \(t=1/2,2,3\). All comparisons succeeded. Only the analytic rank-one spectral argument in RESULT.md establishes parameter-universality for every real \(t>0\), and the modular checks alone are not relied upon to prove noncontrollability.

There has been no independent mathematical audit. The theorem does not quantify energy or finite-precision controllability, and publication priority beyond the inspected source set is provisional.
