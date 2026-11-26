---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Tracing one ancestor backwards at rate-one copying, with independent constant reset hazard r, gives k_r and the fixed-environment conditional mean. Reset before time s makes the future conditional mean term independent of the past spin field; the surviving ancestry gives exp(-rs)P_s, so conditional covariance is bounded by exp(-rs) and the average has conditional variance <=2/(rT). Tonelli and p_s*p_t(0)=p_(s+t)(0) give V_d/r^2 as the Laplace transform of t p_t(0). The walk has coordinate variance t/d, giving the stated local CLT prefactor; integrating the t^(1-d/2) tail gives the Gamma constants below four, the 4/pi^2 logarithm at four, and the finite squared Green norm above four. The maximum weight is k_r(0) by the symmetric semigroup Cauchy–Schwarz bound. Its size relative to sqrt(V_d) tends to zero exactly in the asserted Gaussian regimes; log of the product of cosines gives -u^2/2 plus error O(u^4 max_x k_r(x)^2/V_d), an independent check for the countable array. In d>=5 domination in l2 gives the stated common-field limit; Rademacher fourth cumulants add to -2 sum of fourth powers, with strict negative sign. At d=4, one can also show l4 summability without a spatial Green bound: ||p_t||_4 <= p_t(0)^(3/4), whose tail is O(t^-3/2), so Minkowski gives G_4 in l4. The exact fourth cumulant then gives -2/(4/pi^2)^2=-pi^4/8 multiplying the fourth-power Green sum. For d=1 differentiating the elementary integral of 1/(1+r-cos theta) gives the exact squared-resolvent variance. The supplied verifier and supporting files were inspected as evidence, not executed. An independent bounded check verifies the exact C3 coordinate generator against the resolvent and sign-averaged fourth moments at rates 1/2 and 3/2 (variances 3/8 and 1/2; fourth moments 9/32 and 19/54) and checks five line spectral integrals to within 6e-17 absolute error. These are consistency checks, not substitutes for the infinite proof.

## originality

PASS

The surviving assessed novelty is the distribution over original fields of the stationary local time-average, including the sharp critical fourth cumulant. The same reset mechanism, resolvent, d=1 kernel and d=4 singular integral boundary already appear in Grange. The variance scaling and Green summability threshold should not be positioned as stand-alone new results. No covering distributional statement or critical fourth-cumulant asymptotic was found in the inspected material.

## value

PASS

A local long-time observable conditioned on fixed reset memory need not exhibit the distribution of an annealed current spin. The theorem explains exactly when the accumulated disorder behaves Gaussian and when individual sites retain macroscopic normalized weights. The sharp signed slow logarithmic fourth-order correction at the borderline and explicit non-Gaussian series on the other side add information not supplied by known stationary pair correlations or the resolvent divergence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
