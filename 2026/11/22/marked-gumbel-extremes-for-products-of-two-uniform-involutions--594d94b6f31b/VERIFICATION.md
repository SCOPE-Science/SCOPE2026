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

The exact finite verifier is `verify_involutions.py` and requires Python 3 standard library only. Execute `python3 verify_involutions.py` to reproduce the 60,528 counted exact enumeration/component checks for all pairs of involutions on up to seven vertices. It checks the transposition-colour component classification, cycle structure of the composed permutation, exact one-path count formula and exact second factorial moments. The proof of the asymptotic marked Poisson and Gumbel claims is written in `RESULT.md`; the finite checks are not substitutes for that proof. The coefficient estimate is drawn from the published combinatorial analysis cited in the result.
