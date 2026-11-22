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

# Reproducibility and evidence limits

Run `python check.py` from the directory containing `RESULT.md` and `check.py`. Python 3 with `sympy` and `scipy` is required. The standalone script checks symbolic uniformity, the Hessian's symmetric-ray second derivative, the exact degenerate-boundary constant and its strict separation, two polar Gaussian moments at seven parameter values, and direct exact finite multinomial enumeration at three positive profiles and two sample sizes. The packaged test completed successfully with 26 assertions.

The mathematical theorem for arbitrary fixed probability vectors and every sample-size limit is justified by the analytical Gaussian limit and symmetry argument in `RESULT.md`, not by finite computations. The script does not search the mathematical literature or supply independent verification of a novelty claim.

The complete text of the main motivating 2026 cyclic-variance preprint, its open-chain companion, and the 2019 multinomial order-statistics paper were materially inspected. The original 2011 Corrado paper was not accessible, leaving a historical-priority limitation. An independent audit has not been performed.
