---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The stationary qubit Bloch coherence is z=r/[1-(1-r)e^{iθ}]; substitution into full-rank qubit SLD QFI gives the rational F. The t=r/(2-r), w=tan²(θ/2) derivative polynomial has one positive Descartes sign change after x=t/(1-t), giving a unique maximum, with nonresonant θ→0 scaling and θ=π endpoint. Direct RESULT.md and verify_qfi.py inspected.

## originality

FAIL

The published November 2 theorem analyzes precisely the same Bernoulli reset/phase-gate channel and unconditioned stationary single-qubit phase SLD QFI. Its sign-convention U=exp(+iθσ_z/2) is equivalent by θ↦−θ, leaving QFI invariant. Its p/(1-p) polynomial is the algebraic reparametrization of this record’s r/(2-r) quintic, with the same uniqueness for every nonresonant phase, θ=π optimizer 2/3 and maximum 1/64, and identical near-identity constants sqrt((1+sqrt3)/2) and 2sqrt3/9. All central conclusions are covered; the crossing of r*=2/3 at one intermediate θ is an immediate evaluation of the published derivative polynomial, not a surviving independent finding.

## value

PASS

Sharp stationary sensor reset optimization has a natural metrological meaning; however it is already established in the earlier theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
