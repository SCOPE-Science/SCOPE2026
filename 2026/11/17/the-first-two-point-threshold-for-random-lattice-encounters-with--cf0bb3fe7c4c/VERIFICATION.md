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

The analytic argument does not rely on a finite search or on simulation. It reduces the random rotation/translation model to covariogram overlaps, uses a local curvature expansion of the difference body and a lens-area integral, then evaluates the universal angular integral. The exact disk formula provides an independent non-generic boundary case.

Execute `python check_lattice.py` with SciPy installed (`pip install -r requirements.txt` if necessary). The checker independently integrates the ellipse-overlap formula for three anisotropic ellipses and two disks, compares shrinking-threshold ratios to the asserted asymptotic constants, tests the conditional angular second moment against \(1/6\), normalizes the limiting beta density, and verifies the absence of integer-lattice unit triangles in a representative finite neighborhood (this last finite check is illustrative; the proof uses bipartiteness of the full infinite grid).

The package checker was executed successfully and printed `RIGID_MOTION_LATTICE_TWO_POINT_ONSET_OK`. The optional `nonsymmetric_test.py` separately approximates a strictly convex asymmetric shape with support function \(h(\theta)=1+0.09\cos(2\theta)+0.03\cos(3\theta)\), numerically integrates overlap areas for shrinking gaps, and prints `ASYMMETRIC_CURVATURE_LENS_CHECK_OK`. Its polygon resolution and tested gaps are finite. Numerical quadrature is only corroboration. The \(o(\varepsilon^2)\) claim for general smooth convex bodies is established analytically; it is not experimentally certified in all bodies. Rigorous global priority search is not exhaustive, and independent mathematical audit has not been performed.
