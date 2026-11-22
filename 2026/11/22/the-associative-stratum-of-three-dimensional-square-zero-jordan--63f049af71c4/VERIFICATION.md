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

# Reproduction and limits

Run `python3 verify.py` from the extracted package using Python 3 and no third-party libraries. Expected output lines:

```
EXHAUSTIVE_OK q=2 tables=512 associative=8 Veronese=8 mismatch=0
EXHAUSTIVE_OK q=4 tables=262144 associative=64 Veronese=64 mismatch=0
```

For each nine-coordinate product, the checker evaluates the six repeated-index associativity conditions and the one independent all-distinct condition on basis triples, then independently evaluates matrix symmetry and its nine rank-one minors. Addition in the binary extension-field representation is coefficientwise XOR. Every table is tested exactly once.

This checks finite cases only. The universal implication from associativity to the rank-one symmetric form is established by the seven-element independence argument and the annihilator/alternating-form reduction in `RESULT.md`. The converse is algebraic over arbitrary fields of characteristic two. The projective Hilbert-series calculation uses the standard second-Veronese coordinate ring. No nonreduced associativity scheme or independent mathematical audit was assessed.
