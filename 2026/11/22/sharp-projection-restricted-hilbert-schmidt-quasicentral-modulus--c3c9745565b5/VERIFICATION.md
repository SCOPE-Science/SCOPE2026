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

For a finite projection P the two squared leakage norms sum to the squared unnormalized Hilbert–Schmidt commutator norm, and their signed difference is the compressed trace of T*T−TT*. For the shift model this compressed trace tends to p−q for every strong exhaustion, giving the required lower bound without assuming nestedness. Pairing a forward and backward copy gives the bilateral shift after adding one matrix unit. Dyadic arc-constant projections increase strongly to the identity; on each arc the compressed multiplier has modulus sinc(π/N), so both leakages have total squared norm 2N(1−sinc²(π/N))→0. Each unpaired copy contributes a single boundary matrix unit to the direct-sum nested sequence, attaining |p−q| in squared norm. For any strong exhaustion by self-adjoint contractions, multiplication of I−R_n against a Hilbert–Schmidt K tends to zero in Hilbert–Schmidt norm on both sides by finite-rank approximation; this proves invariance sequence by sequence. The diagonal ramp with N jumps of size 1/N has squared cost (p+q)/N, hence the ordinary positive-contraction modulus vanishes. The index q−p follows from kernel and cokernel dimensions and compact-perturbation invariance. This covers also the balanced and pure one-sign cases. The frozen diagnostic is supplementary; the review used the analytic identities, not a run of that script.

## originality

PASS

Credit the usual positive-contraction zero, Hilbert–Schmidt stability mechanism, and normal approximation as background. The supported distinction is the exact nonzero unnormalized projection-only energy governed by the index in the specified model, including nested attainment and arbitrary Hilbert–Schmidt perturbations. No distinct result supplying this sharp law was established in the bounded comparison; older related index results remain a priority risk.

## value

PASS

Forward/backward shifts are canonical index models, and the least commutator leakage for projection cutoffs is a natural approximation invariant. The law quantifies exactly how the two signs cancel and separates this projection cost from a zero cost under positive contractions. An exact dimension-free floor, not just existence or nonexistence of approximate commutation, is useful in testing what information projection approximations can retain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
