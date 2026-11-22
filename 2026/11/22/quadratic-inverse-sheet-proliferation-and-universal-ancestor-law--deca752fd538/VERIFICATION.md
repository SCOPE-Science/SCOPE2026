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

# Finite verification and proof limits

Run `python3 verify_inverse.py` with the standard Python library. A fixed-seed test enumerates 95 parameter configurations and directly substitutes 70,328 distinct computed inverse points into the published two-dimensional cosine equations, including 5 values of the small parameter and arbitrary positive/negative phase shifts. Four additional parameter values assess the normalized \(b^2 N_b\) scaling and compare the second-coordinate moments with quadrature of the limiting \(\mu\) density.

The analytic proof—not the finite program—establishes the uniform asymptotic, the Wasserstein bound, and the bound on singular inverses. The program uses double precision, checks sampled instances only, and is not an exhaustive computation or a substitute for independent mathematical verification. The model is the literal printed map with different placements of \(\pi\) in the two equations. No external independent audit has been performed.
