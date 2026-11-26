---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a=fR, b=gR and z=R(u), the tensor equality in the proof is equivalent to the original bilinear identity. If z is not in ku, the u and z coefficients vanish separately, forcing a=0,b=−λg or b=0,a=−λf. If z=cu, evaluation at y=u gives c(c+λ)=0. With z=0 the tensor a⊗b vanishes; with z=−λu at nonzero weight it is (a+λf)⊗(b+λg) that vanishes. Substitution proves sufficiency without any division by 2. The fixed row and column constraints give the stated dimensions, and for n≥3 no component is contained in another (in particular z can have a nonzero W part in F3 and F4). The only pairwise edges are 12, 24, 56, 36, so each connected triple is open and closed by the distinct value of g(z). For ranks, F1/F2 have an unrestricted m×m block; F3/F4 have one pivot and an h×m residual with h unused entries; F5 has two pivots, an h×h residual and 2n−3 unused entries; F6 has one pivot and an m×m residual. The four intersections remove exactly the blocks counted in the subtraction terms. Inclusion–exclusion works even when n=2 pieces are not maximal. Evaluation at full rank and summation give the invertible count and doubling; only nonzero-weight maps can be invertible. Independent replay: python3 /workspace/branches/independent_replay.py 3, using the actual bracket and image cardinalities rather than elimination; exhaustive in the listed F₂, F₃ and added F₄ small cases, e.g. n=2 over F₄ gives (1,6,0) at weight zero and (1,7,6) at every nonzero weight.

## originality

PASS

The supported contribution is the all-dimensional weighted operator and rank census, including reduced component incidence and the finite-field total and invertible counts. The split algebra and the small-dimensional classification credited in the record are not claimed as new; an earlier exact rank census on the same algebra concerns different operator equations. No verified source was found that already yields the weighted census.

## value

PASS

This is a natural split family from the structural theory of Leibniz algebras with one-dimensional derived ideal. A single calculation gives complete reduced incidence and labeled rank spectra in all dimensions, explaining why the nonzero fiber has two connected components and twice the rational points, and exactly when invertible maps occur. The ranks and component changes give reusable information about the parameter space beyond an existence construction or low-dimensional table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
