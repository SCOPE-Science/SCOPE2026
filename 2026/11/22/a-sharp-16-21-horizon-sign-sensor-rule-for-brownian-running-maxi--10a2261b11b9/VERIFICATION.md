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

# Reproducibility and evidence

Install the packages specified in `requirements.txt`, then execute `python verify.py`. This tests the Gaussian reflection-density normalization, exact covariance in nine sample cases against an independent numerical integral, the radical optimum and risk via symbolic simplification, and signs of the derivative on both sides of the unique critical time. The recorded output from this exact source file is included in `VERIFIER_OUTPUT.txt`.

The analytic proof in `RESULT.md` derives the continuum assertion and covers the endpoint time. The checks do not by themselves certify global uniqueness or rule out earlier literature. No independent mathematical audit has been performed. The optimality guarantee is limited to one predetermined zero-threshold sign and arbitrary decoders of that sign.
