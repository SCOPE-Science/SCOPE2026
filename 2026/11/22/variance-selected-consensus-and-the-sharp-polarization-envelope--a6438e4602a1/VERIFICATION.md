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

For positive initial mean, the velocity is locally Lipschitz in the characteristic position and the two moments on m≥m₀/2; q∈[0,1] gives inward boundary velocities. Local characteristic iteration gives the probability evolution, and monotonicity of m extends it globally. Independently, differentiating q+m² gives the single integral ∫2(x+m)V dμ=∫(q−x²)dμ=0. Writing V=v/[2(x+m)]−(x−m)/2 gives m′=vG/2 and v′=−2mvG, so m≥m₀ and G≥1/2, giving variance decay and convergence to the stated Dirac mass in W₂. Jensen and x²≤x give the exact extremizers at each interior mean. The all-zero initial law is separately stationary by convention, and the empirical law proof uses the full-sum degree normalization, not leave-one-out or stochastic fixation. The independent unequal-mass example in python3 /workspace/independent_checks.py (section 2) verifies the neutral moment identities with L²=102497/264600; the characteristic/moment argument establishes the universal claims.

## originality

PASS

Bounded pass for the arbitrary-law first integral, exact selector and fixed-mean rigidity, not for general convergence, the transport model, or the endpoint mixture value. The primary equation implies the new conservation law via a short extra model-specific cancellation, and the primary convergence theorem can then replace the convergence part of the proof. No inspected prior theorem supplies the arbitrary-law conservation or selector as a restriction; the primary two-atom invariant alone does not establish conservation for other laws.

## value

PASS

The invariant computes the previously unspecified limiting cooperation for arbitrary laws, including continuously supported ones, and shows exactly which heterogeneous laws can maximize or minimize it at fixed mean. This is an exact observable and structural equivalence of moment-matched initial distributions, not another numerical trajectory or a restatement of convergence. It is limited to the stipulated deterministic neutral model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
