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

# Reproducibility and proof limits

Run `python3 check.py` from the artifact directory. The standard-library-only program printed `PASS 5615 exact rational assertions` on a fresh execution. It exactly tests the four-yield moment and derivative identities, positive derivative sensitivity on 400 rational examples, the rational third-moment threshold witness, and exact derivative brackets of the robust optimizer. It is supplementary finite validation, not an exhaustive computational proof of quantified mathematics. The universal claims are proved analytically in `RESULT.md` by strict concavity, Lagrange interpolation/partial fractions, and a quartic polynomial identity. No claim about ecological field validation or independent external review is made.
