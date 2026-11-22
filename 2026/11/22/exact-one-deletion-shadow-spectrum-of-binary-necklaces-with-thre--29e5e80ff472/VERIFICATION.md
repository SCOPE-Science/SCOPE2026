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

# Reproducibility

Run `python verify.py` with Python 3 and its standard library. The script independently canonicalizes every output necklace after each literal symbol deletion; checks 981 cyclic gap orbits with at most 24 zeros; independently enumerates all binary words with exactly three ones at lengths 3 through 18; and checks every coefficient in six rational series through length 57.

Expected output: `VERIFY_OK gap_orbits=981 direct_length=3..18 rational_coefficients=3..57`.

The finite checks do not establish the all-length claim alone: the coordinate-decrement rotation lemma and cyclic orbit counts supply the universal proof. Historical independence or priority is not certified.
