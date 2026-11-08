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

# Reproducibility and verification

Run `python3 verify.py` with Python 3.8 or later. The script does not use third-party packages or external input.

Its successful observed output was:

```text
VERIFY_OK k=1..8 all_words= 262140 minimal_lyndon= 17 direct_subsequence_words= 2728 formula_witness_k=2..100 ternary_contrast=PASS
```

The `all_words` count includes every binary word of lengths \(2k\) and \(2k+1\) for \(1\le k\le8\). The `direct_subsequence_words` count cross-checks greedy arches against the definition by considering all binary target subsequences, for \(1\le k\le5\). For every \(k\le8\), exact lexicographic comparisons with every cyclic rotation check the complete set of minimal-length Lyndon candidates. The witnesses are tested at all integer \(k\) from \(2\) through \(100\). A separate ternary example verifies that the theorem is alphabet-specific.

These finite tests cannot prove the all-integer result or establish scientific novelty. The complete infinite proof is in `RESULT.md`. The mathematical review in `REVIEW.md` is not an independent audit.
