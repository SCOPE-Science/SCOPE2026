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

Run `python3 verification/verify.py` after installing the packages listed in `verification/requirements.txt`. Python 3, its standard library, and SymPy are the only dependencies. A captured successful execution is included at `verification/verification_output.txt`.

The verifier independently derives the displayed conditional-expectation coefficients from exact finite binomial and Poisson moments and rechecks those formulas over 96 rational parameter-count combinations; it computes the target covariance by two-dimensional integration; compares the explained-variance and critical-polynomial identities; evaluates the asymptotic constants; probes roots and monotonicity for seven sample intensities; and compares analytic explained variance with an independently generated Poisson jump-time simulation. Its `133` counted assertions combine exact symbolic identities, rational examples, finite numerical root checks and two simulation checks. The simulation uses a fixed seed and 300,000 independently generated paths.

**Proof versus testing:** All-intensity optimality, strict uniqueness and strict intensity monotonicity follow from the exact sign and derivative argument in `RESULT.md`; the code's finite set of intensities does not by itself certify those universal statements. The asymptotic risk comparison is an exact polynomial coefficient computation. Independent mathematical verification and comprehensive historical-priority review remain to be performed.
