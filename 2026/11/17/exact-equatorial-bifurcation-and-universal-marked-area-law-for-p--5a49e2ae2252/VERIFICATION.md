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

# Verification and reproducibility

Run `python checks/pole_area_checker.py` with Python 3 from the root of the extracted package. The script uses no external packages and prints `PINNED_POLE_SPHERICAL_AREA_CHECKS_OK` if every check succeeds. It compares the solid-angle phase to the independently derived law-of-cosines/Girard spherical excess on an angular grid, tests all three branches of the cumulative distribution against numerical pushforward quadrature, verifies the exact duality, and checks the critical-law scaling and a nonuniform angular-density example.

The proof in `RESULT.md` establishes the theorem for an entire continuum of colatitudes and gap densities. Numerical grids do not certify an identity for all angles; the analytic inverse-map argument and dominated/conditional-density limit are the evidence for the infinite assertions. Weak convergence is not convergence in expectation, and no independent mathematical audit has been performed.
