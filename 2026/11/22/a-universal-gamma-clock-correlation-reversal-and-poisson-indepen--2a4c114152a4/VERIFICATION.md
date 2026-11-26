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

For a fixed excursion time t, conditional Gaussianity of X given the transverse path makes the mixed square moment 2D_x E[L_t Y_t²]. With the occupation-normalized local time, the Markov transition from Y_s=0 contributes 2D_y(t−s) and the density at Y_s=0 is (4πD_y s)^(−1/2). Integrating gives 8D_x√D_y t^(3/2)/(3√π); the product of the single-coordinate second moments is 4D_x√D_y t^(3/2)/√π. Complete independent resets give a positional marginal averaged over the equilibrium age A, not over S or over time since initialization. With a_p=E[A^p], the ratio to be tested is 2a_(3/2)/(3a_(1/2)a_1)−1. The survival integral gives a_p=Γ(k+p+1)/[(p+1)Γ(k+1)λ^p], reducing the ratio to (1−k)/(5(k+1)); the open endpoint bounds and sign claims follow. Nonzero square covariance excludes independence for all k≠1. For k=1, the equilibrium age is exponential and the decaying stationary Fourier resolvent in y has form c_ξ exp(−√(λ/D_y)|y|), where the jump at zero yields c_ξ=λ/(D_xξ²+2√(λD_y)). Its inverse is the product of normalized Laplace densities. All moments used are finite for k>0. I inspected the supplied quadrature script, without executing it; the conclusion is analytic.

## originality

PASS

The exponential product resolvent, free-comb framework and renewal-age averaging are preexisting. The supported distinct result is the complete Gamma-shape mixed-square dependence law and the use of its strict signs to exclude independence at every nonexponential shape. No independent consulted statement contains that all-shape classification. The full free propagator plus generic renewal mixing can encode the answer before evaluation; they are not themselves an evaluated mixed-square or independence theorem for Gamma resetting.

## value

PASS

The Gamma family changes clock dispersion around a natural Poisson baseline. A scale-free fourth-order observable separates the negative dependence at a fixed comb excursion age from positive dependence induced by age mixing, with a sharp sign reversal at the only independent shape. This provides a two-coordinate diagnostic not available from signed-coordinate covariance or a backbone MSD alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
