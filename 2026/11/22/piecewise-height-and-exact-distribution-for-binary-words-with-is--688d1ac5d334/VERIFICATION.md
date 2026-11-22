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

# Verification of the mathematical statement

The proof is contained in RESULT.md. Its key nonstandard input is the insertion characterization of piecewise height in Proposition 3.1 of arXiv:2311.15431v1, together with Lemma 4.1 for appending a repeated symbol. The crucial side-distance step explicitly shows that a positive-gap prefix ending in \(i\) isolated ones has side distance exactly \(i\) against appending zero, and the mirror identity holds for the suffix. Inserting zero anywhere in the \(i\)-th gap gives the necessary lower bound \(t+a_i+1\). Required and forbidden all-marker subsequences prove the matching upper bound.

Run `python3 verify.py`, using only the Python standard library. A completed replay produced: `PASS: 3240 dynamic-height cases, 324 direct-subsequence cases, 261 coefficient cases`. The test computes finite word heights in two different ways, evaluates complete subsequence sets in small cases, and compares finite generating coefficients with the inclusion-exclusion formula. The finite tests cannot establish the general formula, the limit law, originality or independent validity. The formulas and supporting source statements must be evaluated mathematically as in RESULT.md.

Self-review only. No independent audit or external validation has been performed.
