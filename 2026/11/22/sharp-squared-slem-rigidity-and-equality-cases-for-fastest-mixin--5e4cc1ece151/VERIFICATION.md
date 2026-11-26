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

For n≥3 the first cosine vector has unit norm, zero sum and P_*y=cy, with c>0. For z_j=(c+cos((2j−1)π/n)/c)/n, product-to-sum gives z_j+z_{j+1}=2y_jy_{j+1} and summation gives ∑z_j=c. Row stochasticity and symmetry yield yᵀPy−c=∑P_jj(y_j²−z_j). The summands have coefficients zero at the endpoints and strictly positive in the interior because cos((2j−1)π/n)<c there. Therefore s²−c²−||(P−P_*)y||²=(s²−||Py||²)+2c(yᵀPy−c) is a sum of nonnegative terms. Equality forces all interior holding probabilities to vanish, hence the alternating family. The product with y is the negative discrete derivative of the weighted deviations with u₀=u_n=0. To prove sufficiency, test the perturbation on normalized cosine modes: each edge difference for mode r is proportional to sin(irπ/n), and multiplying by the alternating sign and taking the discrete derivative gives −2t sin(rπ/n)v_(n−r), also at the endpoints because the sine differences at i=0,n vanish. Hence the (r,n−r) block squares to [cos²(rπ/n)+4t²sin²(rπ/n)] times the identity; the unpaired even-size mode has eigenvalue −2t and the constant stays fixed. For |2t|≤1 the first pair has maximal nonconstant modulus, including |2t|=1, proving the equality, sharp coefficient and exact formula. The positive edge differences show uniqueness of P_* from the squared bound; the centered indicator on the first i sites gives the stated prefactor for edge recovery. Taylor expansion at t=0 has strictly positive quadratic coefficient, so the inverse exponent 1/2 is optimal for each fixed n. None of these steps requires an irreducible or aperiodic chain.

## originality

PASS

Credit classical path optimality and the cosine certificate. From the Rayleigh inequality for this same test vector the squared norm inequality alone follows mechanically. The supported distinct result is the sharp all-feasible equality classification, its exact contraction factor along the entire equality family, and the resulting quantitative inverse estimate with explicit normalization and an attaining sharp exponent. No equivalent prior classification or sharp path inverse theorem was established by the available comparisons.

## value

PASS

The squared-deficit equality classification describes exactly which paths saturate the stability constraint, even away from the known optimum. The matching explicit perturbations and coordinate bounds quantify how far a near-optimal kernel can move on any edge and explain why the excess rate can only recover the kernel at square-root scale. This is additional information not supplied by the optimizer or by the mechanical inequality alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
