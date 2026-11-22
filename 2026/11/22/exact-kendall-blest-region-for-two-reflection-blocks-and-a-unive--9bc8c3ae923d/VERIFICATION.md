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

Run `python3 verify.py` from the same directory as the proof. It requires Python 3 only; no external packages, internet resources, or randomness. In this package, the program exited with `PASS 62362 exact rational and polynomial assertions`.

The checker validates, by exact integer-polynomial arithmetic, the differentiation and positivity identities for the rational objective; it checks rational brackets containing the root of the governing cubic, exact formulas for a large finite collection of one- and two-block lengths and placements, sign and order comparisons, saturated-branch identities, the universal block lower-bound comparisons on rational families, and the general strict-splitting identity on rational families of several block counts.

The uniqueness of the cubic root, all-real two-sided optimization, complete vertical interval filling, endpoint classifications, strict inequalities for arbitrary finite block families, and all quantifiers in the theorem follow from the argument in `RESULT.md` and are **not** inferred from sampled values. The exact root is characterized algebraically rather than by a floating-point approximation. The result is self-reviewed only; independent audit and independent validation have not been performed. Source priority has residual uncertainty as stated in `REVIEW.md`.
