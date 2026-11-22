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

The proof checks compatibility of arbitrary families of indexed subsequence embeddings and then constructs a conflicting two-embedding witness at the first permissible overlap span. This proves moment inequalities for arbitrary finite lengths; finite testing is not substituted for the proof.

Run `python3 verification.py` with the standard Python library; its recorded output is `verification_output.txt`. Exact-integer host enumerations and `fractions.Fraction` check full empirical distributions, direct pair-compatibility second moments, both extremal formulas, and the first separation for thousands of coarsening comparisons. The demonstration \(0123\) versus \(0120\) over a four-letter alphabet was verified through length seven. The tests do not exhaust arbitrary lengths, alphabets or patterns.

Self-review: passed. Independent audit: not yet performed.
