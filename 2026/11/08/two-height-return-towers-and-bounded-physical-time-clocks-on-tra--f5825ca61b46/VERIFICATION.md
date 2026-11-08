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

The theorem is a quantified analytic statement for every integer \(n\ge1\), every \(L,\eta>0\), every base point \(x\in[0,L+\eta)\), and every integer horizon \(k\ge1\). Its principal proof is in `RESULT.md`; the computational checks are supplemental, finite, and exact rational. No external symbolic-algebra package or downloaded source code is required.

Run the standalone verifier from the extracted package with `python checker.py`. The verified execution completed with:

```
PASS exact cases 54 exact return samples 3456 rational orbit periods 700 two-atom moment checks 180
```

The code's first test compares **direct iterations** of the full original four-interval exchange to both return-time branches and the cumulative-time identity, using exact fractions. The next checks least periods by iterating the original map from rational points until return. The final tests integrate the two-atom clock law over uniform rational grids and check its means and variances exactly. The integration grids are selected so the rational phase discontinuities are resolved exactly; this does not claim exhaustive verification for all real parameters.

Critical mathematical checks: the nonzero outside-index walk is addition by \(2n-1\) modulo \(4n\), which is a full cycle because the two numbers are coprime; the first-return map is rotation by \(L\) modulo \(A=L+\eta\); the number of wraps after \(k\) rotations is exactly \(\lfloor(x+kL)/A\rfloor\); and the full original-map period is the sum of \(u\) short excursions and \(v\) long ones for \(L/\eta=u/v\) reduced. The finite tests do not certify these universal implications; they are proved directly in the theorem.

Limits: polygonal endpoints are branch-ambiguous in the planar map, so geometric interpretations are stated for regular cap points; the half-open interval-exchange formulas themselves are exact. Uniqueness of invariant measures on the full ambient planar phase space is neither required nor claimed. The comparison to published work is a self-review and does not constitute independent publication-priority certification.
