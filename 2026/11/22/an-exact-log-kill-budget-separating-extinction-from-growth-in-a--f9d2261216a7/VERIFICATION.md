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

Run `python3 verify.py` with Python 3.9 or later in the same directory. The program uses only the standard library. It checks the exact rational stage generator identity, both spectral projectors, its two-stage exponential, the determinant and trace identities of the rational targeted intervention, the exact strictly positive characteristic-polynomial value at unity, and the exact sign comparisons for the critical budget polynomial. A 70-digit decimal calculation brackets the smaller critical root; 6,000 additional reproducible sampled comparisons test the universal optimizer formula as a diagnostic.

The exact finite identities provide a reproducible certificate for the displayed model and policy witness. The 6,000 finite parameter tests cannot verify the universal optimizer for all real generators, and numerical approximation cannot establish the asymptotic extinction statement. Those claims are established by the mathematical argument in `RESULT.md` and the separately credited resistance-fixation theorem for the specified eco-evolutionary system. Neutral thresholds, stochastic survival, and independent validation are not assessed here.
