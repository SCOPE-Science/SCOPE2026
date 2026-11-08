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

The standalone `verify.py` uses only Python 3 standard-library integers and rational fractions. It constructs each connected labeled regular graph on two through six vertices, plus cycles and complete/multipartite graphs of higher order. It calculates the matrix \(P=(I-h_2L)(I-h_1L)\) exactly and compares entrywise positivity against the two local inequalities from the theorem for 48 positive rational step pairs per tested graph. At the extremal parameters it checks exact equality to \((A^2-tA-dI)/(d(d-1-t))\), nonnegative entries and stochasticity. It also checks exact complete-graph projection, the strict obstruction above the finite threshold, and feasible subthreshold products with real positive roots.

Executed from the actual `verify.py` in this package by `python3 verify.py`:

```
VERIFICATION_OK: 173 labeled connected regular graphs, 8304 rational endpoint pairs; sharp boundary identities checked
```

The universal all-size claim is proved algebraically in `RESULT.md`; finite replay is not a substitute for that proof. No floating-point certification, external independent audit, irregular-graph extension, or accuracy estimate is asserted.
