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

# Reproduction of symbolic and numerical checks

With Python 3 and the dependencies listed in `artifacts/requirements.txt`, run `python artifacts/verify_sampling.py` from the directory containing the extracted package files. The expected console output is preserved in `artifacts/verification.txt`.

The verifier checks 62 conditions: symbolic identities for the three-variable star normalized inverse-Hessian Gram and the optimal probabilities; exact 3-by-3 block residual formulas for three rational SPD matrices; numerical agreement of weighted residual spectra and normalized Gram spectra; the two-dimensional symmetric-mode discriminant and factor identities; rational-parameter comparisons of optimum, uniform and volume omission; and three independent positive-Gram examples of the general Perron optimizer.

The assertions involving floating point use explicit tolerances. They do not establish the continuous-parameter theorem: uniqueness, strictness, and the near-singular limit are proved analytically in RESULT.md. No external or independent audit has been performed.
