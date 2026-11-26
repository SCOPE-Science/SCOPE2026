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

The backward stochastic convolution conditional on Poisson times is a centered Gaussian with variance 2D times the integral of exp(-2 kappa t) a^(2N(-t,0]) for t>0. It lies strictly between zero and v_*, including for a=0. The common-noise coupling forgets the initial condition. Independent backward Poisson gaps yield the stationary pre-last-jump variance, independent of the exponential observation age. Thus delta=1-U=HB with H=1-a^2U' bounded below by 1-a^2 and B=e^(-2 kappa T) with CDF b^alpha. The endpoint CDF K z^alpha holds on 0<z<1-a^2. The normalized variance drift and jump generator on u^n yields the stated m_n; the convergent binomial expansion gives K, including K=1 at full resetting. In the mixture integral put q=x^2/(2v_*) and y=q delta; the endpoint density produces alpha K q^(-alpha) y^(alpha-1)e^(-y) at leading order. For delta>=delta_0>0 and q>1/2, the integrand after factoring e^(-q) increases with 1-delta and is bounded by its exponentially small value at delta_0. Integrating the resulting density asymptotic gives the stated two-sided survival by symmetry and the Gaussian Mills factor. Testing the same rescaled integral against bounded continuous functions and dividing by its mass proves the Gamma posterior for the density-defined conditional distribution. The zero-current invariant diffusion formula yields the stated polynomial tail at fixed positive weak-reset parameter; it says nothing about a joint limit or a=1. The uploaded checker was inspected but not executed; no simulation is needed for the exact endpoint or tail.

## originality

FAIL

Two distinct available records already state the same exact variance endpoint and Gaussian asymptotic, one with the identical series and the other with an equivalent product, and the latter states the same contrast with the fixed-parameter diffusion. These are statement-level matches under dimensional normalization, not a priority finding. The conditional Gamma assertion is not printed in the inspected findings, but the matched endpoint and Gaussian mixture proofs immediately give it by inserting a bounded test function in the very same dominated-convergence integral and normalizing. The included full-reset endpoint is also mechanically obtained with H=1. No separate repaired claim is submitted.

## value

FAIL

The Gaussian-versus-polynomial tail distinction is scientifically useful, but it is fully present in the matched exact-model work. The additional normalized Gamma limit in this package is the normalized endpoint kernel of that same available proof. Without a substantive additional localization result or application, that mechanical remainder does not supply a distinct valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
