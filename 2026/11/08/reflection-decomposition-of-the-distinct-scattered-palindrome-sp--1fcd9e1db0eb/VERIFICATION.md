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

The complete finite-language enumeration in `verify.py` checks the exact sets of distinct nonempty palindromic scattered subsequences (not merely their sizes) against the two language decompositions for all half-words over alphabets of sizes 2, 3, and 4 through lengths 7, 6, and 5, respectively. It also checks every graded coefficient and total in both formulas. The observed result is `VERIFY_OK half_words=2713 hosts=11962 language_equalities_and_graded_counts`.

The noncomputational part of the proof is the reflection normalization of arbitrary embeddings, which establishes the exact language equivalences for all finite words and alphabets. Exhaustive finite checks are corroboration and cannot by themselves establish the infinite result. An independent scientific audit has not been conducted.
