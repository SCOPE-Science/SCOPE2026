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

# Verification record

Run with Python 3 (standard library only):

```text
python3 verify.py
```

The finite verifier independently constructs every shortest universal linear word from alphabet permutations, closes these under rotations and compares resulting marked words, necklaces and primitive necklaces to exact arithmetic formulas. It separately tests the inclusion–exclusion sum against a positive-composition formula, and directly tests the scattered-subsequence definition on all words in the small regimes identified below.

Observed output ending:

```text
VERIFY_OK orbit_cases=19 marked_word_memberships=138088 formula_identities=35 direct_subsequence_crosschecks=q2_k1to3_q3_k1to3_q4_k1to2 PASS
```

Orbital comparisons: all \(1\le k\le9\) for \(q=2\), \(1\le k\le5\) for \(q=3\), \(1\le k\le3\) for \(q=4\), and \(1\le k\le2\) for \(q=5\). Composition/inclusion–exclusion identities also tested at \(2\le q\le8\), \(1\le k\le5\). Direct scattered-subsequence comparisons use all length-\(qk\) words for \(q\le3,k\le3\), and \(q=4,k\le2\). These are explicitly bounded tests; the universal-quantifier result rests on the combinatorial proof. The verification is not independent scientific audit.
