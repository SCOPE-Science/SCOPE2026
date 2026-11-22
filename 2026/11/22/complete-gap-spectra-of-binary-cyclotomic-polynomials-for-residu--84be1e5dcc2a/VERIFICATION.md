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

# Reproducibility

Run `python3 CHECK.py` with Python 3.9 or later; no packages, network services or external files are required. The program builds coefficients of \((1-X)(1-X^{ab})/((1-X^a)(1-X^b))\) from the exact recurrence for the reciprocal denominator up to the degree \((a-1)(b-1)\); it neither imports the theorem's gap formulas as polynomial coefficients nor calls a computer-algebra cyclotomic routine. It independently compares support positions and row memberships for both residue cases.

The recorded execution passed all 810 pairs from odd \(a=5,7,\ldots,57\), quotient \(s=1,\ldots,15\), and the two signs, covering 8,050,320 coefficient positions and 4,140,180 nonzero support positions. Every histogram, coefficient alphabet constraint, endpoint and total gap-length sum matched the formulas.

The checker validates finite samples only. The infinite proof is the exact two-rectangle identity, the residue-wise row partition, and the row-boundary gap enumeration in `RESULT.md`. No independent mathematical assessment has been carried out.
