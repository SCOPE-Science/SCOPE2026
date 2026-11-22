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

# Verification of the local hexagon Hessian certificates

The exact checker `verify.py` reads `certificate.json` and reconstructs triangular monomial moments, pairwise-energy polynomials, gradient stationarity, the normalized Hessian, and all \(LDL^{\mathsf T}\) pivots for each of the nine powers \(k\in\{8,10,12,14,16,18,20,22,24\}\).

Command: `python3 verify.py certificate.json` (run normally, without `-O`). This uses only Python's standard library. Actual replay: PASS for all 9 exponents; 72 exact positive rational pivots; 576 exact matrix entry checks; all 9 stationarity tests; 9 exact factorization reconstructions.

Optional diagnostic: `python3 numeric_crosscheck.py` with NumPy. Actual independent Gauss–Legendre quadrature for \(k=8,16,24\) matched the baseline energy to relative error less than \(7\cdot10^{-14}\) and the selected second derivative to relative error less than \(2\cdot10^{-6}\). It is not a replacement for the exact certificate.

The proof assumes simple convex labeled hexagons sufficiently near the reference; fan triangles remain valid and Taylor smoothness holds there. The executable certificate does not quantify a neighborhood size, and neither the code nor this review establishes global optimality or independent mathematical validation.
