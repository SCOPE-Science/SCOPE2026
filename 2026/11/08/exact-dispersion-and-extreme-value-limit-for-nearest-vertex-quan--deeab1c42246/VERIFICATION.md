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

# Verification of the nearest-vertex distortion theorem

Execute `python3 verify.py` from the package directory. Only Python's standard library is needed. Successful replay on the package files reported:

`VERIFY_OK ordered_simplex_exact_cases=15 exact_dim1=1 exact_dim2=1 sampled_points=210000 strict_positive_covariance_cases=15`

The exact check is structurally independent of the proof's inclusion-exclusion method. It orders the barycentric coordinates, reparametrizes the ordered chamber by a standard Dirichlet simplex, expands the cubic product and evaluates all monomials with exact rational factorial moments. It checks the full mixed moment identity for each integer \(2\le m\le16\), its strictly positive covariance, and two independently calculable low-dimensional cases.

The simulation comparisons use 70,000 uniformly sampled simplex points for each of three dimensions, with fixed seeds, to test the predicted mean and variance. Simulation and the finite exact checks are supplementary only. The analytic proof gives the results for every integer dimension and establishes the infinite-dimensional limiting law. The full finite-dimensional CDF and statistical estimation guarantees were not checked or claimed.
