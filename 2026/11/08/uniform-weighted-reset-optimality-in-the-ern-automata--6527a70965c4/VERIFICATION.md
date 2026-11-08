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

# Reproducibility and limits

The proof in `RESULT.md` uses an explicit inverse-subset transformation, first-introduction chain, and sharp equality cases to establish the all-size statement. The code `verify.py` implements unrelated forward subset transitions; it does not reuse the inverse proof or unproved lemmas. Running `python3 verify.py` prints `VERIFY_OK: 12 state sizes, 60 positive-cost searches, unique weighted optimum in each` after completing all tests.

The zero-one search checks the rotation-count minimum for twelve state counts. The weighted shortest-path routine separately checks five pairs of positive integer weights for each state count, and counts ties. These finite computations are not an infinite certification and do not address arbitrary real costs except through the symbolic proof.

**Verification state:** self-reviewed; independent audit not performed. No external validation or formal proof certification is claimed.
