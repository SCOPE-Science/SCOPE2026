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

# Reproducible verification

Run `python CHECK.py` using Python 3 and `sympy==1.14.0` (see `requirements.txt`). This independently generates the rational knot-line partition for the order-four B-spline and converts both polynomial inequalities to degree-three Bernstein form on every triangle. It checks every coefficient is a nonnegative rational number and checks strict positivity at every vertex with positive \(v\). It verifies exact area conservation, and requires the 8-cell/10-triangle partition.

Expected result: `CHECK_OK cells=8 triangles=10 bernstein_coefficients=200 zero_coefficients=39 strict_vertex_tests=42`.

The finite script is an exact certificate of polynomial positivity across a continuum. Full proof still requires the explicit Zak imaginary-part identity and Poisson boundary argument in `RESULT.md`, and Proposition 4.3 from arXiv:2609.13116v1 for the midpoint-frequency line. No independent audit has been performed.
