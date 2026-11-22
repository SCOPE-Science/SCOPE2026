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

# Verification procedure and limits

Execute `python check.py` with the dependencies in `requirements.txt` from the directory containing these files. The script uses an independent expansion-clock change of variables, direct centered density-profile integration and arbitrary-precision evaluation of the exact moment formula. It checks the beta constants and rapid-reset exponential-moment identities, then tests the optimal squared position and convexity for nine reset rates, the slow-rate edge coefficient and two rapid-reset optimized coefficients.

The analytic proof in `RESULT.md` establishes the strict convexity and the asymptotic equivalents; computed finite examples do not certify limits or novelty. In particular, the domain \(|x|\le x_0\) is necessary for the stated optimization, and all probability statements refer to the random reset age of the macroscopic Thomas–Fermi profile. A separate independent scientific audit has not been carried out.
