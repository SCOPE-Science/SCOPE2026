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

# Verification record

The standard-library-only `verify.py` is included in this same package and was executed successfully. Its completed run reported:

`SIGNED_MULTIPARTITE_ANGLE_PASS exact_profiles=12 rank_sign_arrangements=880232 convexity_inequalities=378 majorization_pairs=535`

For each of twelve class profiles, the program independently traverses coordinate sign assignments and every distinct absolute-rank permutation. It tests each cross-part sum inequality and verifies exact rational agreement with the stated binomial-tail law. Separately it checks finite integer-domain strict convexity for 378 triples and majorization for 535 comparable pairs. Verification requires Python 3 and no nonstandard dependencies. The proof in `RESULT.md` is unrestricted; finite enumeration cannot establish all-dimensional correctness or historical priority. Independent mathematical audit has not been performed.
