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

The main proof in `RESULT.md` is analytic. It uses the generalized-eigenvalue equality lines and the strict Birkhoff functional, then a uniform fourth-root Taylor expansion and a unique analytic critical branch. The parameter range for global strictness is every positive real weight unequal to one; the optimizer series holds only for sufficiently small positive weight.

Run `python -m pip install -r requirements.txt` and then `python verify.py`. The script performs symbolic quartic and characteristic-polynomial identities, verifies the nondegenerate maximizer, the exact displacement and cubic coefficients, and checks finite deterministically sampled Birkhoff pairs. The expected final line is `BIRKHOFF_RESTRICTED_SKEW_MEAN_CHECK_OK 3322`.

The symbolic algebra confirms specified computations. The finite sample checks do not prove claims for all real weights or the uniqueness assertion. Those claims are justified only by the explicit analytic argument. The nonperformance of independent audit should not be interpreted as independent validation.
