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

Run `python3 artifacts/check_star_types.py` with Python 3.10 or later. The script has no third-party dependencies, and success prints `VERIFY_OK`.

It independently enumerates all \(4^{n+1}\) positive-distance vectors for the center and \(n\) leaves for each \(1\le n\le7\), checks the triangle inequalities for all old/new triples, and counts the complete histogram by the number of leaves at distance at most two. For every \(1\le n\le300\) it separately checks the polynomial coefficient formula, total count, the exact grade-two Turán identity, unimodality, and the claimed set of log-concavity violations using Python's arbitrary-precision integers.

Observed run output:

```
n=11: c0,c1,c2,c3,c4= [6145, 56342, 84535, 126885, 127050]
n=11: c2^2 - c1*c3= -2788445
Brute-force diagram checks: 1..7 leaves
Shape and exact identity checks: 1..300 leaves
VERIFY_OK
```

The finite checks do not certify the infinite-size theorem. The independent proof in RESULT.md establishes it using a classification of every Katětov vector and exact inequalities. Historical novelty and external mathematical validation remain unverified.
