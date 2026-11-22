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

# Verification of the fixed-circle Crofton theorem

Run the included `check.py` using Python 3 with SciPy installed. A completed execution printed `PASS 246 finite checks`, with dimension-three optimizer \(1.118904787310\), dimension-four optimizer \(1.324717957245\), limiting optimal radius divided by \(\sqrt d\) equal to \(0.734903908748\), and limiting optimal probability \(0.792442639800\). All 246 assertions returned success. Re-execution requires no external data or internet connection.

The checker directly integrates the projection-density orientation formula for dimensions 3 through 1000, compares it against the regularized-incomplete-beta formula, verifies that the three section probabilities sum to one, verifies positivity and the unique-root sign around the optimizer, and compares large-dimensional optima with the analytical Rayleigh constant. The dimension-three case is included solely as a published consistency control; the new theorem's claimed domain begins at dimension four.

The analytical proof is necessary: finitely many quadrature and numeric root checks cannot certify the homotopy argument in all dimensions, the unique optimizer for every integer dimension, or the high-dimensional convergence. The geometric proof uses a strong deformation retract and excludes tangent or transition hyperplanes of invariant measure zero. The optimizer proof relies on strict monotonicity of incomplete-beta terms; the limit proof relies on Gaussian-normal projection, uniform integrability, strict uniqueness and a compactness bound. All these assumptions and dependencies are stated in `RESULT.md`.

The scientific review is an internal mathematical consistency and overlap check, not an independent mathematical audit. No formal machine proof, historical-priority certification or external validation is claimed.
