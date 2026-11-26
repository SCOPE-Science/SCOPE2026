---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact reproducibility

The cycle blocks of `CERTIFICATE.json` contain 26 rational entries: the representative at each cyclic distance for each \(C_n\), \(3\le n\le9\). A numerator is nonzero and has nonnegative coefficients in every block; denominators have nonnegative coefficients with positive constant terms. The seven blocks exhaust the necessary entries by symmetry and rotation. To reproduce them, construct each combinatorial Laplacian and compute \((I+2hL/3+h^2L^2/6)^{-1}(I-hL/3)\) over the rational-function field, then cancel each representative fraction with positive leading denominator coefficient.

The attached `VERIFY.py` performs this computation using SymPy and compares ascending coefficient arrays. Its full output count includes additional path certificates retained in the source package. The checker also verifies the fifth-order coefficient \(1/108\) and the distance-five witness \((L^5)_{0,5}=-2\) on \(C_{10}\). The exclusion for arbitrary \(n\ge10\) follows from the five-edge walk argument, not extrapolation from the boundary test.
