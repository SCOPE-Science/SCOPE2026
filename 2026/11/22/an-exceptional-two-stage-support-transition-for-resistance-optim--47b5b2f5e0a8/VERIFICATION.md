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

## How to reproduce

Run `python3 verify_triangle.py` alongside the files, with Python 3, NumPy, and SymPy available. The verifier checks full weighted-Laplacian characteristic polynomials and inverse traces using exact rationals for sizes \(5\) through \(9\), exact inequalities governing phase boundaries through size \(62\), and direct full-edge first-order optimality conditions on multiple sizes and price regimes.

The exact finite calculations and numerical tests passed when the packaged script was run. They supplement the mathematical proof and do not certify the quantified infinite theorem independently. Its full proof is in `RESULT.md`. No external audit, specialist validation, or formal proof certificate is claimed.
