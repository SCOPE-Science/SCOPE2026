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
# Verification scope

The proof's checkable algebra is the degree-four endpoint identity for cosine coefficients. It is derived through integration by parts from exact polynomials, followed by analytic positivity inequalities. Its necessity uses Cesàro convergence of elementary trigonometric sequences and the maximal-gap property of roots of unity. These are infinite statements proved in RESULT.md, not extrapolated from data.

Run `python3 CHECK.py` using the Python 3 standard library to regenerate 6,240 finite coefficient comparisons for the two admissible grids and verify the degree-four forbidden-grid example. The checker separately expands the Bernstein polynomial from sampled values and evaluates its endpoint derivatives. It checks the predicted closed expressions independently of the analytical argument and is not an exhaustive search over all real node locations.

No independent mathematical audit has been performed. No external certification is claimed.
