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

# Verification methods and limits

Use Python 3 with no external packages; execute the two standalone scripts from this directory:

```
python3 verify_five_general.py
python3 verify_suffix_general.py
```

The saved output of each exact invocation appears in the corresponding `.out` file. The first checker tabulates all literal, possibly overlapping substring occurrences, applies the defining condition that a unique factor has two repeated one-symbol deletions, and compares the **entire factor set** to the eight-template prediction for all \(6^5=7776\) positive five-run parameter tuples with each parameter at most six. The second uses lexicographic suffix ordering and neighboring longest-common-prefix lengths to find a shortest unique prefix at each position, then checks the other one-letter deletion for repetition. It verifies the factor sets for all \(7^5=16807\) tuples with each parameter at most seven, independently checks 180 additional longer random tuples, tests that none of the positive five-run words of length less than ten has eight MUSs, and displays the ten-symbol witness and all its factors.

These two algorithms use different data representations and independent tests of occurrence uniqueness. Repeated finite checks are supporting evidence only; they do not imply the infinite classification or a proof of the length cutoff. The all-parameter proof is the run-boundary case analysis in `RESULT.md`. No claim of independent audit, publication acceptance, or complete external priority search is made.
