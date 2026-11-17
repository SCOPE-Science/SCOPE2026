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

The exact side-sector formula was checked using `regular_polygon_crossover_checker.py`, including probability-normalization identities, positive and negative directions on each side, several polygon orders, and \(n/m^3\) values in the transition window. It computes normalized ratios without underflow. The separate `regular_polygon_mc_checker.py` samples points independently on actual polygon sides, computes the maximum angular gap, and compares direct geometric failure frequencies with independently quadrature-integrated probabilities. Both ran successfully, with output markers `REGULAR_POLYGON_PARITY_CROSSOVER_OK` and `POLYGON_CONTAINMENT_INDEPENDENT_MC_OK`.

For a reproducible replay, install `requirements.txt` and execute both files with Python. Analytic proof uses exact geometry and a uniform Taylor bound, not simulation or approximate quadrature. Conditional weak convergence is established from a density expansion rather than Monte Carlo. Bibliographic checking did not access the complete 1982 coverage article; no claim of exhaustive historical priority is made.
