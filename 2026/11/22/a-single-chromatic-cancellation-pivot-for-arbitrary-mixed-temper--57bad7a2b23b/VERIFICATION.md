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

The proof in `RESULT.md` is analytic and covers every compactly supported probability distribution of positive stellar blackbody temperatures having both hotter and cooler support relative to the reference transit chord. Its critical step is the explicit strict positivity of the mixed derivative of the logarithm of the temperature derivative of the Planck occupation number. That identity proves the required strict determinant inequality; it is not deduced from numerical tests.

Run `python3 verify.py` using Python 3's standard library. The deterministic checker uses fixed-seed randomized mixtures and inverse-wavelength grids, and independently checks the three-component cancellation example, equal-mean strict positive contrast, and a fourth-moment-neutral example. On preparation, 17,515 supplementary assertions passed. It prints an approximately 0.530284339425-micrometre pivot for the concrete example. The Planck constant combination used for the illustrative length-to-frequency conversion is truncated to 14387.76877 micrometre-kelvin; this affects the last reported numerical digits only, not any theorem.

The checker does not certify all temperatures or all wavelengths, and the experiments are not a substitute for the proof. No observational data, radiation-transfer models, limb darkening, uncertainty quantification, calibration, or independent replication are claimed. No independent audit has been performed.
