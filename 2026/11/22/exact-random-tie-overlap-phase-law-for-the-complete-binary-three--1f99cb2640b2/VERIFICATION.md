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

# Reproducible finite verification

From the directory containing the extracted embedded files, execute:

```
python3 verify_literal.py
python3 verify_paths.py
```

Both require only the Python 3 standard library and arbitrary-precision `fractions.Fraction`. The first computes the complete distribution by literal-string recursion, asserts noncontainment at every reachable state, checks the de Bruijn optimality witness, and reports 1,309 memoized states. The second performs a separate forward probability propagation on component paths, checking the seven overlap-signature probabilities and the five output-length probabilities, visiting path-state layer sizes 1,14,78,220,332,288,224,192. Both assert exact normalization and mean; they do not sample. Recorded outputs are `verify_literal.out` and `verify_paths.out` and were reproduced by replay of the embedded source code. The endpoint-overlap reduction in the second checker uses the established lemma cited in RESULT.md; this does not independently prove that external lemma, but the literal-string checker does not depend on it.

The exact string-state recurrence is exhaustive for this fixed eight-input finite problem. It is not evidence for any extension to larger alphabets or higher-order reads. Independent scientific validation has not been performed.
