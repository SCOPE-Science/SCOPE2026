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
# Reproducibility and proof boundary

Run `python3 verify.py` in the directory containing the embedded verifier. The successful local execution returned `VERIFY_OK cases=1469 max_q2=2 q3_d3=12 trie_worlds=22`.

The code constructs every prefix-trie model used for finite tests, computes the reflexive and transitive closures independently, and tests that precisely the terminal leaf corresponding to each minimal word can satisfy its associated path conjunct. It exhausts all nonempty subsets of run-reduced words through selected small alphabets and depths, then checks a deterministic sample at depth three and all full-length layers in alphabets up to four. The tests neither enumerate arbitrary infinite frames nor constitute a proof of the theorem; the explicit general argument in RESULT.md does that.

The relevant empirical checks cover the special boundary cases \(q=1\), \(q=2\), \(q=3\), empty word inclusion, and maximal depth layers. Verification does not assert independent certification or global literature priority.
