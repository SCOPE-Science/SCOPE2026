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

# Computational reproducibility and limits

Execute `python verification/verify.py` with Python 3 and no third-party packages. The verifier enumerates all distinct subsequence strings, forms their set intersection, constructs insertion-maximal elements directly, and compares them with the exact symbolic prediction. In equal-power cases it also tests equality of the complete common-subsequence language with the union of the two proposed downward closures.

The packaged source was run and returned `PASS 1144 cases; 92735 common subsequence strings checked`. The test includes all nonempty strings of lengths at most three over each of two separate two-letter alphabets when the expanded inputs have length at most thirteen, plus five more repeated-letter block pairs with power exponents one and two. These are finite checks only: the full all-length and all-power conclusion rests on the proof in `RESULT.md`. Alphabet overlap is deliberately not allowed in the theorem; `RESULT.md` gives a direct counterexample to extending the language identity without this hypothesis.

No independent audit has yet been performed.
