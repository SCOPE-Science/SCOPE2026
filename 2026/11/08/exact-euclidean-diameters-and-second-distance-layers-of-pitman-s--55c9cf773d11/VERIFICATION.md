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
# Verification notes

The self-contained standard-library script `pitman_stanley_diameter_checker.py` is bundled with this result. Run `python3 pitman_stanley_diameter_checker.py` in the containing directory. It enumerates the prefix-polytope vertices by every admissible active-set choice using `fractions.Fraction`, and independently computes all squared vertex-pair distances.

Actual execution passed 72 deterministically seeded positive rational increment vectors in dimensions 2–7. For each, the computed maximum squared distance equaled the claimed formula, and the unique maximizing unordered vertex pair matched the two singleton-support points. Exact canonical checks for dimensions 3–10 recovered the two largest distinct squared-distance levels and one-or-two realizing pairs. The successful output was `PITMAN_STANLEY_DIAMETER_TWO_TOP_LEVELS_CHECKS_PASSED 72 8`.

The mathematical proof independently establishes the assertions for arbitrary positive *real* increments and all integers in scope. Exact-rational finite enumeration cannot certify an all-dimensional theorem or establish historical novelty. Independent audit has not been performed.
