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

# Reproduction and evidentiary limits

Run `python3 verify_alias.py` alongside `RESULT.md`. The Python 3 script has no third-party dependencies. It compares exact integral paired-sum multisets and exact rational off-diagonal transforms without numerical approximation, tests the two possible two-class matchings over an integer grid, verifies all nine candidate off-diagonal sums are distinct, and enumerates the six three-class matchings. The script's passing test count is evidence about its finite checks only.

The general theorem follows from the separately written finite-exponential uniqueness proof, the two-class squared-sums identity, and the algebraic forbidden-ratio argument in `RESULT.md`, not from finite iteration or a computer search. The population-probability observations are assumed exact for all positive efforts and are not asserted to be practically available from a finite dataset. The first source's June 18, 2024 public date is the publisher's explicit first-publication date. Literature comparison is evidence-limited; independent expert or external audit is not claimed.
