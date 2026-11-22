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

The exact two-choice success-at-position formula was checked against direct uniform-permutation enumeration for all valid early and late cutoffs with at most eight candidates. The harmonic-sum criterion was checked against conditional distribution functions over all tested cutoffs through sixty candidates. Running `python3 verify.py` prints the finite-case result and a separate large-horizon numerical comparison to the analytic density.

Analytical checks independently reconstruct the conditional position masses by disjoint record events, normalize using two harmonic sums and their squared-sum identity, reduce first-order stochastic order to the final likelihood ratio, and expand the harmonic sums uniformly for bounded threshold offsets. The arithmetic density invokes the explicitly cited optimal-rounding theorem and Kronecker–Weyl equidistribution. Enumeration and numerical agreement do not prove the asymptotic density. This package has not undergone independent mathematical assessment.
