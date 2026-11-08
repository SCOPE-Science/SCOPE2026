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

# Reproducible checks

The analytic proof appears in `RESULT.md`. The supplied `verify.py` uses symbolic exact determinants and covariance identities; exact rational enumeration of all delay histories through ten updates; exact root-bracketing signs; the weighted operator norms and strong-law logarithmic exponent. `verification_output.txt` records an actual successful run, and `requirements.txt` states the third-party dependency. Execute `python verify.py` after installing SymPy. Those experiments do not constitute a proof of the real-parameter stability theorem; the source text provides that proof.

No independent mathematical audit or external certification has been performed.
