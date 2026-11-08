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

# Reproducibility and evidence limits

Run `python checker.py` from the directory containing the extracted files. It needs only Python's standard library and applies exact integer-scaled Thiele scores. The verified run checked every committee for every seat count at each \(3\le n\le16\) for the triple-window PAV model: \(131064\) committees, including the proposed counting formula. It also checked \(24064\) committee-rule cases from distinct strictly decreasing Thiele sequences and several cyclic block lengths for \(3\le n\le10\). The observed complete output was:

```
Triple-window PAV: PASS; 131064 committees for n=3..16
All-block generality, two distinct strictly decreasing rules: PASS; 24064 committee-rule evaluations
n=12 winner counts by committee size: [1, 12, 42, 40, 3, 72, 174, 72, 3, 40, 42, 12, 1]
```

The proof in `RESULT.md` supplies the infinite-parameter argument. The enumerations are not substitutes for it. The comparisons with related papers evaluate mathematical coverage, not independently certified publication priority. An independent scientific audit has not been performed.
