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

# Reproduction of arithmetic checks

Run `python3 verify.py` with Python 3. The script uses no external services and only standard-library `fractions`, `math` and `itertools`. The expected marker is `VERIFY_OK`.

The checked objects are the exact 2026 two-facility Global Pair and classical Proportional mechanisms with nearest-facility social cost. The script recomputes the conditional-cost influence polynomials and exact rational variance \(147113/504000\), the Proportional integrand quotient, eleven rational symmetric three-site population formulas, 231 additional rational profiles, and two independent midpoint numerical integrations with 300 mesh points. In the run producing this record, the program terminated with the `VERIFY_OK` marker and reported 242 finite cases.

Analytic verification of infinite assertions requires following the bounded-kernel V-statistic decomposition, empirical-process two-median envelope argument and iid CLT in RESULT.md. Neither the finite profile checks nor quadrature certify infinite convergence or literature novelty. Independent audit has not been performed.
