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
# Verification and limits

Reproduce with `python VERIFY.py` (Python 3, NumPy and SciPy). It checks the two vertex-orbit counts for all factor orders from 2 through 5 using explicit strictly exposed score witnesses, 13,230 deterministic and random top-r grid truncation identities through factor order eight, normal-gap quadrature (including the symmetry \(\alpha_{p,q}+\alpha_{q,p}=1\)), and a seeded Monte Carlo comparison at factor orders \((2,3)\).

The script reports `LINEUP_ANGULAR_FINITE_PASS` when all checks succeed. The finite enumerations test the rank-classification ingredients; analytic proof of the all-dimension formula and asymptotic limits is in RESULT.md. Simulation does not certify Gaussian solid-angle values, and no finite test certifies a Poisson process limit or exhaustive originality.

Independent audit: not performed.
