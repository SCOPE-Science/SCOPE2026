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

The lower face is P_(n-1,t+1); an upper k-face is the orthogonal product of the regular k-permutahedron and P_(n-k,t), with intrinsic area factor k^(k-3/2) by the spanning-tree determinant (one for k=1). These descriptions follow by taking equality in the subset inequalities; at t=0 the rank n-1 product loses a dimension, so its area is zero. For the imported volume EGF, the rational t=(a-1)/b are dense and the finite vertex lists are continuous in t in Hausdorff distance; Euclidean volume is continuous and the EGF coefficients are polynomials in t. This supplies the real-t extension implicit in the frozen proof, including the given base volumes. The tree square-root singularity gives f_m rho^m=C_t m^(-3/4)(1+O_t(m^(-1/2))), rho=e^(-1). The relative coefficient ratio after extracting rho^k differs from one by O_t(k/n+n^(-1/2)) for k<=n/2. Multiplying by the tree kernel k^(-3/2) and the area kernel k^(-2) and summing this error costs respectively O_t(n^(-1/2)) and O_t(n^(-1/2)+log(n)/n); the contribution from k>n/2 follows by summing (m+1)^(-3/4) over m=n-k. Thus the denominator has the O_t(n^(-1/2)) precision needed for the O_t(1) mean remainder. Lower ranks give the harmonic numerator with the stated Stirling prefactor; k>n/2 is O_t(1) even after weighting by k. The masses normalize and the limiting mean is infinite. An independent bounded Stirling-tail summation agrees with alpha=0.6186032871609 and beta=0.6178166125895. Inspected VERIFICATION.md and verify_surface_rank.py without executing supplied code: the 12 hull tests compare aggregate surface areas and volumes in dimensions 2–4, not each rank or the limit.

## originality

PASS

The facet product structure, volume EGF, regular permutahedron area and the series alpha in a different body are prior ingredients. The supported distinct contribution is the full high-dimensional Euclidean boundary-area distribution for rank in the stated parking family, including parameter cancellation, tight normalization and its logarithmic prelimit mean with bounded error. In the closest inspected results, the same-body geometric formula is finite dimensional and the high-dimensional laws are for quantitatively different face weights and polytopes.

## value

PASS

The result distinguishes metric from combinatorial typicality in a natural family: only n lower facets carry a fixed positive area fraction, yet large upper ranks create a divergent expectation at a precise logarithmic rate. The universality with respect to fixed t, the law for every rank and the O_t(1)-accurate mean are more informative than a low-dimensional area calculation or a list of facet counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
