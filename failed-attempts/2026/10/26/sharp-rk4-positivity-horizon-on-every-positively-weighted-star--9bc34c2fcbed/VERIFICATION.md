---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For formal s, the hub Schur complement of I-sL is S=1-sA-s²∑w_i²/(1-sw_i). The coefficients of S⁻¹ through s³ are 1,A,A²+B,A³+2AB+C. Multiplying this series by -sw_i/(1-sw_i) or by s²w_iw_j/[(1-sw_i)(1-sw_j)] gives the claimed entries. The distinct-leaf quadratic is positive since 3W_ij>(A+w_i+w_j)²; the diagonal is positive by the fourth exponential Taylor bound and the spectral theorem. The spoke difference uses exactly the same positive leaf quadratic. Normalizing by A gives the stated derivative certificate (B/A²≤1), so the largest spoke has a single crossing, with exactly the stated ties. When m=1 there are no leaf-pair conditions. The polynomial in M=I-hL with nonnegative coefficients and a positive linear term gives strict spoke positivity at the Euler endpoint. Independent exact algebra passed with python3 /workspace/checks/rk4_algebra.py; the uploaded program was inspected, not executed.

## originality

FAIL

The earlier bidirected-star record proves the necessary-and-sufficient interval and supplies the formulas and strict signs that mechanically yield the heaviest-spoke refinement, indeed even for unequal inward and outward rates. The strict Euler comparison is an immediate nonnegative-power expansion for any such generator, not a distinct surviving result for this class.

## value

FAIL

Finding a controlling edge would be useful if it required a new fact. Here it replaces a prior minimum by a maximizer via one subtraction using the already positive leaf entry. The endpoint tie statement follows from the same subtraction; the Euler comparison is generic. No independently valuable uncovered remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
