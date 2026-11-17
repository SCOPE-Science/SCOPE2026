---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For an even wheel C_{2m} with m≥2, hub vacancy forces the rim to be perfectly matched by one of exactly two alternating matchings. Conditional on matching-edge arrival times t_j, both endpoint spokes must arrive after t_j, and each interposed rim edge after min(t_j,t_{j+1}); integrating independent exponential densities yields P_{2m}=2∫exp[-3∑t_j-∑min(t_j,t_{j+1})]dt. The strictly positive, trace-class kernel K(t,s)=exp[-3(t+s)/2-min(t,s)] gives 2tr(K^m). Spectral simplicity and domination follow from positivity improving compactness; the bounded positive eigenfunction solves u´´+u´-λ^{-1}exp(-4t)u=0 with Robin boundary u´(0)=-u(0), which yields 2zI_{3/4}(z)=I_{-1/4}(z), λ=1/(4z²). Independent rational first-event recurrence at spoke/rim ratio one gives P4=1/6, P6=1/21, P8=19/1386, P10=41/10395, agreeing with the frozen proof, and λ≈0.287730645241419. Odd rims cannot perfectly match. Finite checks support only stated finite cases; infinite decay follows from operator proof.

## originality

FAIL

The published 2026-10-25 weighted-wheel theorem strictly dominates the same observable at every positive spoke rate. At rate ratio one, a=2, its recurrence P_{2m+2}=q_m/2, q_m=∑_{j=0}^{m-1}q_jq_{m-1-j}/(4m-1) and hypergeometric dominant root ρ₂=3.47547269134629 recover the entire submitted equal-rate probability and exponential λ*=1/ρ₂; 0F1 and modified Bessel I are equivalent special-function forms. Neither transfer-operator language nor the Bessel reparameterization introduces an independent theorem.

## value

FAIL

The event is naturally motivated and its exact asymptotic would be useful in isolation; however the earlier weighted-wheel theorem already supplies all its values and sharp asymptotics for this specialization. A transfer trace and equivalent Bessel normalization are alternate derivations, not a motivated new mathematical gap or distinct surviving invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
