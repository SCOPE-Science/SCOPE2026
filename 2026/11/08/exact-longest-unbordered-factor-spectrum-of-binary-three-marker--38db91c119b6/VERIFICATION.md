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

# Verification

Run `python3 VERIFY.py` using Python 3 and its standard library, with `VERIFY.py` in the current directory. The program directly enumerates each of the \(\binom n3\) binary words with exactly three ones for \(3\le n\le30\) (31,465 words) and independently computes the unbordered-factor maximum by prefix-function arrays for every suffix. It checks all gap tuples achieving the sharp minimum for \(5\le n\le64\), including exclusions, and uses independent 24-chamber rational Dirichlet moment evaluation.

Expected output from an actual successful run:
```
DIRECT_PREFIX_FUNCTION_OK 31465
SHARP_MINIMUM_CLASSIFICATION_OK 64
EXACT_DIRICHLET_MOMENTS_OK 157/192 3929/5760 2483/184320
```

The finite checks do not establish the infinite statements. The structural border lemma, minimum classification, uniform-composition limit and chamber integration are proved in RESULT.md. A standalone source code program is provided, not a formal proof assistant certificate. Historical novelty is qualified by the material-inspection and access limits documented in REVIEW.md and AUDIT.json. Independent mathematical audit has not been performed.
