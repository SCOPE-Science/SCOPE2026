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

# Reproduction and limits

Execute `python verify.py` with Python 3.9 or later. It checks the principal-angle block exactly using rational Pythagorean cosine-sine pairs and rational relaxations, without floating-point algebra or nonstandard packages. The expected output is `PASS: 5064 exact rational checks across 24 principal-angle instances.`

For a full proof, use the principal-angle decomposition and the determinant/diagonal conditions derived in `RESULT.md`. The tests range over finitely many rational parameters and do not certify the universal quantifiers. The older spectral-radius optimization used in the comparison is a published theorem, not independently certified here. Scientific correctness, originality and value were reviewed together; independent audit has not occurred.
