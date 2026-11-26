---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The run-start map is z ↦ exp(-μU)(a+Bz), globally contracting by at most B and preserving [0,L]. Backward iteration gives the unique entrance law even for real initial positions; finite mean h+θ/(α−1) gives the equilibrium occupation normalization. The post-run Y belongs to [a,L], independently of the following rest. Changing variables in the age measure S(t)dt/m gives the factor 1/(μmx) and S(log(Y/x)/μ); integrating the same age measure from log(Y/x)/μ to infinity gives θ[1+log(Y/x)/(μθ)]^(1−α)/[(α−1)m]. Uniform boundedness of log(Y/L) gives both constants. The active trajectory has occupation density bounded by 1/[mμ(L−x)] at small x and contributes no boundary atom. Finite ages and interior entrance positions rule out mass at zero; substituting x=L exp(−s) in the inverse-moment integral gives an exponentially divergent integral. The exponential-rest comparison should be read as an algebraic law, not a divergence at every exponential rate. In-house quadrature of the age integral at both entrance endpoints for two parameter sets corroborated the normalization; replay: python -B /workspace/independent_checks.py 1. This finite check does not prove the limits.

## originality

PASS

Limited to the exact asymmetric deterministic-run/Lomax-rest invariant law and its density coefficient. The strongest prior record has essentially the same mechanism but its stated theorem assumes a common iid heavy-tailed holding law across both signs and gives an edge probability rather than the asserted density in this model. Its theorem does not subsume this parameter regime. No claim of a new confinement mechanism or absolute priority is supported.

## value

FAIL

The physical trap center is a support endpoint in this one-sided process. The affine change of coordinates identifies the dynamics with the earlier two-sign edge model; replacing the opposite heavy-tailed hold by fixed h makes the entrance gap uniformly positive and removes the main estimate in that proof. The new coefficient is then the ordinary age normalization 1/(h+E U) and exponential-flow Jacobian, the density is a direct change of variables in the prior occupation identity, and the inverse-moment and no-atom consequences are immediate. No further invariant or scope extending beyond this simpler case is established. This is a correct and useful illustrative calculation, not a sufficiently substantive independent mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
