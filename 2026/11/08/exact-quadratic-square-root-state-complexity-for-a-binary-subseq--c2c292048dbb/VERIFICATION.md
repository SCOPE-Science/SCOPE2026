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

# Reproducibility and limits

Run `python3 checker.py` using only the standard Python library. The standalone file implements the proposed four-type complete DFA and an independent reference method based on transition transformations of the \(b+3\)-state subsequence-matching DFA. It confirms the proposed minimal state count for each \(1\le b\le16\), checks 49,008 literal binary word-membership cases against direct scanning of each doubled word, and independently minimizes the transformation automaton for each \(1\le b\le8\). Expected terminal line:

```
PASS {'parameters': 16, 'direct_word_comparisons': 49008, 'independent_transform_monoid_minimizations': 8}
```

The checker tests only finitely many parameters and words. The proof's all-parameter acceptance criterion, reachability and Myhill–Nerode distinguishability are required for its infinite assertion. The review is a self-review; no independent mathematical audit was undertaken, and historical priority is not definitively certified.
