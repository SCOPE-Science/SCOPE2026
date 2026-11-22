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

The exact projection formula was checked against direct numerical Gram-system solutions for regular kernel orbits of sizes 2 through 8 and several monomial degrees. The unique optimizing radius satisfies the derived polynomial for the standard Bergman case; separate numerical checks also support the large-degree Gamma constant and the residue correction. Running `python3 verify.py` reports 347 passing finite checks. The proof of every infinite-degree assertion is the positivity/variance and Abelian-series argument given in RESULT.md, rather than any finite test. The code needs only Python 3's standard library. The verification does not assess unrestricted node locations, historical novelty, or independent mathematical certification.
