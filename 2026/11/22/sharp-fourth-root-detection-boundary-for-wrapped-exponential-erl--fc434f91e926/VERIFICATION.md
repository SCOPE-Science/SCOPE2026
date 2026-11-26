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

Wrapping preserves integer Fourier moments; the exponential and Erlang moments at r are θ/(θ−ir) and its square. With A=1+θ² one obtains u=θ²/A−2qθ²/A² and v=θ/A+qθ(θ²−1)/A². Substitution gives D=|m−1/2|²−1/4=q²θ²/A² and v+√D=θ(1−u). Since q≥0 and u<1, the positive branch gives the claimed inverse; the (θ,q) Jacobian is 2qθ²/A³ and vanishes at the null. Under the null the gradient g=(2u−1,2v) has norm 1 and g·(u,v)=u. The second raw moment of g·(cos T,sin T) is (1+Re[(g₁−ig₂)² θ/(θ−2i)])/2. Subtracting u² gives the stated positive V(θ). The bounded vector triangular-array CLT and quadratic Taylor remainder give centered variance V(θ₀) for θ_n→θ₀>0 and q_n→0; the plug-in converges to θ₀ and the scaled population D at q_n=c n^(−1/4) gives exactly the claimed mean shift. At fixed q>0 the population D is positive and v/(1−u)>0, so the test is consistent. For the lower bound, differentiation of the unwrapped exponential then wrapping gives k_θ−h_θ=−θ∂_θh_θ. With θ in a compact positive-rate neighborhood, Taylor error against h_{θ(1−q)} is uniformly O(q²), and its density floor is strictly positive. The squared Hellinger distance is O(q⁴), tensorizes at most linearly in n and implies TV→0 below the fourth-root scale. The nearby null sequence stays in the neighborhood, so uniform near-rate size control, not merely pointwise size, suffices for the impossibility bound. No all-rate uniform calibration or local-efficiency claim is established. The supplied checker.py was read, not executed; it tests moments, inversion and variance on finite grids, not the limiting-testing theorem.

## originality

PASS

Best-of-knowledge pass for the combined explicit first-moment inversion and calibrated composite-null test, with its local normal drift and matching near-rate total-variation lower bound. Both published Lindley names describe the same interior family, whose mixture representation and Fourier moments are already known. The inversion is short algebra from those moments, and no originality is awarded to the bare fourth-root rate as a generic phenomenon. The distinct supported content is the model-specific inferential theorem; the inspected primary passages give moment formulas and compare fits, not this test or lower bound.

## value

PASS

A fitting model already in use has a singular null when its rate is unknown. The result turns that singularity into a usable first-moment test with explicit local power and a matching impossibility scale for any test with local uniform size control. These are concrete inferential consequences beyond deriving another moment formula, without asserting optimal power, finite-sample size control or robustness to an unknown angular origin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
