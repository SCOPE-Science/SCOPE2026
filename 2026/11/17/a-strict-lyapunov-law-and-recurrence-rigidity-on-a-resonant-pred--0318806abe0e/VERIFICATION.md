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

# Reproducible checks and limitations

Run `python checker.py` with Python 3 and SymPy. Executed successfully with final output:

```
PASS: all exact symbolic identities, spectrum, and rational witness.
```

The checker uses exact SymPy expressions and rational arithmetic. It verifies both polynomial update identities, the multiplicative transverse recurrence, Jacobian eigenvalue factorization on the equilibrium line, the defining resonance relations, a positive stationary witness, the one-step capture witness, and a factorization certifying strict decrease in the rational illustrative case. No floating-point samples are used as proof.

For the general parameter range, the correctness certificate is the explicit proof in `RESULT.md`: positive multipliers, weighted AM–GM with its strict equality condition, compactness, a monotone positive product, unimodality along the equilibrium segment, asymptotically vanishing increments and an exact local normal-multiplier contraction. These establish the assertions for infinitely many iterates without extrapolating from finite computation.

The global convergence assertion is conditional on every iterate staying strictly positive. The zero-product alternative only implies that the smaller coordinate tends to zero. The nonlinear normal-neutral endpoints and global behavior of non-positive iterates remain outside the claim. An inaccessible related full text and possible unindexed equivalent work remain originality risks. Independent validation has not been performed.
