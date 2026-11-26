---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Under independent clocks, conditioning on the switching history gives a centered Gaussian. With r=2D, λ=2k and q=r/λ, excess variance increases at rate r in release and contracts by A=exp(−λC) in confinement. At release starts the stationary solution is the sum r∑_{j≥1} B_{i−j}∏_{ℓ=1}^j A_{i−ℓ}; the L^m norms of its summands are r b_m^(1/m) a_m^(j/m), a summable series for each integer m≥1. This justifies finite moments before using the fixed-point equation H_m=a_m T_m/(1−a_m). The fresh release length is independent of the starting variance, and conditioning on occupation in release gives age measure P(B>z) dz/b_1. Integrating the powers of U+rz gives (2), correctly normalized by b_1. Gaussian even-moment division and binomial centering recover F_m from the observed law; odd moments vanish. For known B, the coefficient of H_m in (2) is one, and T_m contains a positive j=0 term, so a_m=H_m/(H_m+T_m) is uniquely recovered. Hausdorff determinacy and injectivity of C↦exp(−λC) then identify C. For known C and b_1, (1) gives H_m before (2) recovers b_{m+1} at positive coefficient r^m/[(m+1)b_1]; identifying the law of B uses its stated moment determinacy. With B and coefficients held fixed, equality of the first K even spatial moments is equivalent to equality of the first K exponential moments of C. At K+3 positive distinct durations, perturb positive weights in a nonzero kernel annihilating mass, mean and those K moments. For arbitrary calibrated coefficients the same construction uses c_j=j log(2)/λ. For the lower bound substitute z=exp(−λc): a combination of the K+2 functions is a polynomial of degree ≤K plus a multiple of log z. If that multiple is nonzero, derivative K+1 never vanishes, giving at most K+1 distinct zeros by Rolle; otherwise the polynomial bound applies. Thus the evaluation matrix on any K+2 distinct points is nonsingular, and signed differences on that many or fewer points cannot match all measurements. An independent exact-rational replay at K=1 with B=1 and r=λ=q=1 gave a_1=15/64 for both clocks, a_2=13/160 and 217/2560, common E[X²|release]=177/98 and fourth moments 24449/2401 and 390461/38269. Replay the numbers by summing a_m=∑p_j 2^(−mj) for p=(9/40,7/20,1/8,3/10) or (11/40,3/20,3/8,1/5), using H_1=a_1/(1−a_1), H_2=a_2(1+2H_1)/(1−a_2), F_1=H_1+1/2, F_2=H_2+H_1+1/3. The frozen checkers were inspected, not run. The 369 in RESULT.md excludes the final eight grid checks; the script counter and VERIFICATION.md say 377. The simulation's asserted tolerance is 0.025, not a certificate of the prose's reported error below 0.003. Neither reporting point is used in the all-order proof. No noisy inversion or identification of both unknown clocks is established.

## originality

PASS

Credit is limited to the one-clock inverse problem in this alternating model and the precise finite-data obstruction, especially the sharp K+3 union-of-support cutoff under a matched confinement mean. The forward variance mixture and recursions, ordinary compact moment determinacy, and unconstrained moment perturbation are not themselves the contribution. A very close reset-OU result shares the broad identification and aliasing pattern but has a different forward operator and does not cover the sharp finite-support claim here.

## value

PASS

This distinguishes what can actually be identified with one temporally calibrated clock from what cannot be identified by any fixed finite list of even moments, even with a second mean constraint. The exact minimal combined support K+3 is a scientifically interpretable sharp data limit, useful when comparing finite plausible duration laws. The result is an identifiability statement rather than an unsupported claim of experimental stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
