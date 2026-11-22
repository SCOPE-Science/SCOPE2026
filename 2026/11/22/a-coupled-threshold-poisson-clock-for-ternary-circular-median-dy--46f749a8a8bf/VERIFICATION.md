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

The bundled `verify_median.py` independently implements ternary synchronous cyclic median and two binary threshold updates. For all \(3\le n\le11\), every initial ternary word was checked against the derived entrance-time formula and final period, including all two-cycle basins. For \(3\le n\le7\), a separate finite de Bruijn transfer automaton checked the exact cumulative trace at the first two clock cutoffs. The complete program output is in `verification_output.txt`, ending `VERIFY_MEDIAN_OK`. The two finite Monte Carlo checks were seeded and compare observed cumulative percentages to the stated Poisson law without treating simulations as proof.

The all-length claim and Poisson/mean limit are established by the analytic binary-threshold, run-erosion, and local-dependence arguments of RESULT.md. Finite enumeration, finite trace checks and random sampling cannot prove an infinite-size statement.
