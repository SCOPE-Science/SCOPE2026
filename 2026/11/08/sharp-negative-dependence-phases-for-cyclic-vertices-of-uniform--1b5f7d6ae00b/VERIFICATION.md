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

# Reproducible verification

Run `python3 verify.py` with Python 3 and no third-party packages. The checker uses exact `fractions.Fraction` arithmetic for every finite rational comparison and also enumerates every function on at most six vertices to compare direct cyclic-vertex frequencies against the formulas. Its observed output was:

```
PASS 191 exact assertions; all 2<=n<=168 certified and n>=169 by analytic bound
n=4: pairwise covariance -177/16384; disjoint pair-events +23/4096
strict pairwise sign: negative n=2..5; positive n>=6
```

The universal \(n\ge169\) comparison is proved analytically in RESULT.md using a Gaussian-sum bound and exact rational radical inequalities; checking a finite range would not establish it. The checker independently confirms the required elementary rational inequalities. Every package path is relative and self-contained. No independent audit has yet been conducted.
