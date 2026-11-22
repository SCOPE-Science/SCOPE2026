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

# Reproduction and scope

Execute `python3 artifacts/verify.py` in the artifact root. The script needs only standard-library Python. It computes exact rational moments of the actual convex hulls in two and three dimensions, independently of the conditional-tile proof, for seven weight profiles. Each computation compares the full covariance matrix with the proposed closed form and verifies exact consistency of the scalar inverse identity. A passing run concludes with `WEIGHTED_CACTUS_COVARIANCE_AND_INVERSE_PASS`.

The proof in RESULT.md establishes the formula and inverse for all connected simple cacti and all strictly positive real edge lengths. Small-dimensional convex-hull examples cannot establish this universal quantification. The inverse is an exact population identity; the script does not test stability under noise or cover noncactus graphs. No independent mathematical audit has been performed.
