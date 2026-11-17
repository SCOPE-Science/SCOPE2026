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

# Reproducibility and scope of verification

The `CHECK.py` script uses Python 3 with `sympy` and `mpmath`. Execute `python CHECK.py` to confirm the algebraic Hamiltonian identities, the independent vertical-section versus elliptic area integrals, and the exact action–period derivative formula at representative parameters. Its printed success line is `CUBIC_AREA_PARETO_IDENTITIES_OK`. The proof of the limit distribution and sharp mean is analytic in `RESULT.md` and does not follow from finite samples. All times and periods refer to the displayed polynomial vector field without time rescaling. Only self-review has been performed; no external independent audit is reported.
