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

The standalone `verify.py` uses Python's standard-library `fractions.Fraction` to reconstruct the entire graph Laplacian from the edge list and compute exact grounded inverse traces independently of the proof's Schur-complement formula. On replay it checked every nonempty selected vertex set for \(n=2,3,4,5\) (1,356 cases), including each exact objective and all budget-wise optimum configurations/counts. It also evaluated every admissible occupancy profile at every budget for \(2\le n\le60\), comparing 635,312 exact rational values with the stated theorem. The command and expected success line are:

```
python3 verify.py
PASS: 1356 exhaustive exact grounded-matrix calculations on n=2..5; 635312 exact occupancy comparisons on n=2..60.
```

The infinite family is established by the direct proof in `RESULT.md`. No finite sample proves uniqueness beyond its range, and no independent mathematical audit is asserted. Exact rational calculations have no floating-point tolerance issues.
