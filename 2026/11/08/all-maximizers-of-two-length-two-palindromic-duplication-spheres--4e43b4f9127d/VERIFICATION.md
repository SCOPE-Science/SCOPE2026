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

# Reproducible verification

The theorem's infinite quantifiers follow from the canonical-history proof in `RESULT.md`. For independent finite consistency checks, run `python3 checker.py` using Python 3. No third-party packages or external data are needed.

The script enumerates all exact-two length-two palindromic duplication outputs for all words over \(q=2\) through \(n=10\), \(q=3\) through \(n=8\), and \(q=4\) through \(n=6\). This tests 17,337 words, the maximal sphere formula, and the complete set of maximizers.

A separate symbolic calculation gives each source position its own integer label and, for each \(2\le n\le27\), checks that every two-step history shares an index template with one canonical representative and that every distinct canonical pair has a comparison position carrying **adjacent original source indices**. This directly stress-tests the critical collision lemma without using actual symbol values.

No finite test by itself proves the result for all word lengths. The source-index comparison table and canonical completeness argument in `RESULT.md` supply the general proof.
