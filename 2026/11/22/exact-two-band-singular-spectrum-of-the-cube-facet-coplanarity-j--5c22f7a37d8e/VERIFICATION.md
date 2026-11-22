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
# Reproducibility and limits

**Statement checked.** The exact all-dimensional two-band singular spectrum of the complete positive-coordinate-facet coplanarity-minor Jacobian at the cube, on even radial vertex labels, under unnormalized counting-measure norms.

**Analytic proof.** The cofactor derivative isolates the radial-label column because the facet's fixed coordinate column duplicates the homogeneous column. Cauchy–Binet and Schur complementation transform the complete squared-minor sum into a facetwise affine-regression residual. Distinct even Fourier–Walsh characters restrict orthogonally to each positive facet. Degree two survives on exactly \(n-2\) facets and higher even degrees on all \(n\), yielding the stated exact energies and eigenvalues for every \(n\ge3\).

**Actual computational reproduction.** The attached `verify.py` uses only standard-library Python and exact integer Bareiss determinants. Executing `python3 verify.py` produced the attached `verification_output.txt`: 15 passing exact assertions: 12 squared-norm checks over complete positive-facet minors in dimensions three, four and five, and three cross-term checks in dimension four. These are finite sanity checks rather than infinite-dimensional proof.

**Boundary and provenance.** The result depends essentially on including every positive-facet minor with unit weight, and on the antipodal even-label space. The general nonlinear defect and the Mahler-product variation are not evaluated by this spectrum. The previously established Walsh diagonalization and qualitative kernel in arXiv:2606.14709v4 are acknowledged. No independent mathematical audit has occurred.
