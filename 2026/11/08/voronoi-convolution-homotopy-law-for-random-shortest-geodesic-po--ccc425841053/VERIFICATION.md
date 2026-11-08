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

The identity \(W_m=S-R\) follows by lifting shortest geodesics and reducing the closing displacement to the Voronoi cell. The resulting complete lattice probability law is \(v f^{*m}\) sampled at lattice points; the exact covariance uses independence of the modular remainder and each of at least two independent increments.

Finite exact checks: the standalone checker evaluates cardinal B-spline samples with rational arithmetic for \(3\le m\le13\), verifies type-A and type-B Eulerian coefficient formulas and sums, and checks \(\mathbb E W^2=m/12\) for the one-dimensional winding law.

Independent numerical method: sample torus points in fundamental coordinates and choose shortest segments directly by comparing nearby lattice translates. The test includes square and regular hexagonal lattices, \(m\in\{3,4,5\}\), 690,000 sampled polygons, exact square null probabilities, the known hexagonal triangular probability, and full covariance matrix targets. The checker emits `GEODESIC_TORUS_HOMOLOGY_AND_BSPLINE_CHECKS_OK` on success.

Neither finite simulation nor exact computations for finitely many \(m\) prove the general law; analytic convolution, covariance, and Fourier arguments are given in the proof. No independent mathematical or priority audit has been performed.
