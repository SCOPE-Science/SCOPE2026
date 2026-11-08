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

Run `python3 verify.py` in this directory with Python 3 (standard library only). Actual replay:

```
VERIFY_OK tree-root-threshold-tests 45 rational-inverse-graphs 223 exact-elimination-identities 45
```

The program checks all integer pairs \(3\le p\le11\), \(2\le q<p\), verifies the two-type root returns at the exact formula to floating-point tolerance, the strict gain over the degree-only bound, and the first negative finite ball for a step 2% above the boundary. It also tests 223 admissible small bipartite graphs by exact rational inversion of \(I+sL\) for a conservative rational step below the claimed threshold; 45 elimination identities use exact rational arithmetic.

The proof in `RESULT.md`, not these finite checks, establishes the universal quantifiers and sharpness for arbitrarily large finite balls. Approximate floating-point checks do not certify a symbolic identity on an infinite parameter domain. No independent audit or external certification was carried out.
