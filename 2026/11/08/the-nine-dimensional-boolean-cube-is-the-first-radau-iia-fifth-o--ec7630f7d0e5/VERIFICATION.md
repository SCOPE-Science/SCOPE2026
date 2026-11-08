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

# Exact verification protocol

Run `python verify.py CERTIFICATE.json` using Python 3 with the standard library. The program derives all forty-four numerator coefficient vectors from the finite Walsh transform rather than loading them from the certificate, then compares every array with the saved independent-readable coefficient list. It checks 43 coefficientwise nonnegative numerators, two interval transformations of the exceptional numerator, and the exactly negative nine-cube adjacent-vertex witness by two separate rational formulas. Expected message: `VERIFY_OK 792 exact integer/rational coefficients and identities`.

The proof that these finite coefficient calculations imply positivity at **all** real positive timesteps is written in RESULT.md; the script is a deterministic algebraic certificate, not a timestep scan. Replaying it does not establish novelty or independent scientific validation. The claim does not address cubes in dimensions greater than nine, directional weights, internal stages, or other endpoint maps.
