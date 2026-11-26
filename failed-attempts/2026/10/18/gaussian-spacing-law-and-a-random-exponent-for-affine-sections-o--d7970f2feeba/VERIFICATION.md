---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At a generic cut, intersecting edges (and only those edges) give section vertices, so the count is K(m-K). For fixed direction the K=k offsets occupy the kth ordered gap. The marginal direction of the conditioned plane is weighted by its width, not uniform. The centered Gaussian vector factors into an independent Haar direction and radial norm; multiplying the normal's gaps and width by the independent norm gives the Gaussian expected-gap ratio. Tonelli and the count of iid samples below a fixed level give the finite integral and its normalization. To independently check the exponent, in the equivalent Gaussian construction the joint density of the Gaussian sample and threshold t is the iid sample density times 1{min Z<t<max Z}/E R_m. Put s=sqrt(2 log m); Gaussian extremes, with first-moment control from the union bound on max |Z_i|, give E R_m/s -> 2. The density of t/s is s[1-Phi(sx)^m-(1-Phi(sx))^m]/E R_m, converging pointwise away from ±1 to the uniform density on [-1,1] and hence in L1. Given t/s=x with |x|<1, K is Bin(m,Phi(sx)) conditioned on 0<K<m, an event of probability tending to one. The tail-side count has mean m^(1-x^2+o(1)) and concentrates relatively, while the other count has exponent 1 (both exponent 1 at x=0). This yields the log-vertex limit by integrating bounded test functions; it also checks the binomial argument without treating the minimum of the two realized counts as itself binomial. The explicit CDF and mean 5/3 follow from |Uniform[-1,1]| and boundedness of the exponents. The centroid-only contrast follows by squeezing the empirical sign fraction at the Gaussian sample mean between counts at fixed small opposite thresholds, so that K/m -> 1/2.

## originality

FAIL

Two distinct indexed Findings cover the same conditioned motion-invariant affine section, exact rank law, K(m-K) vertex count and limiting exponent. One gives the same formulas directly, and the other proves the same rank law with a stronger joint log-face limit. Replacing Uniform[-1,1] by its absolute value gives exactly the stated Uniform[0,1] convention. The reported CDF and expectation convergence follow directly from that limit and boundedness. This establishes duplicate scientific coverage, not priority, copying, or the order of work among the same-day labels.

## value

PASS

The invariant random affine cut of a regular simplex is a natural model, and its nondegenerate vertex-count exponent resolves a typical-size question not answered by possible-count bounds, first moments or central sampling. This is value of the theorem itself, not a case for a second dissemination of the equivalent result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
