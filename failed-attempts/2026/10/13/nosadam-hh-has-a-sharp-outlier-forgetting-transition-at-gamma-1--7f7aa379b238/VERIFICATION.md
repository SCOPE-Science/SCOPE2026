---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Algorithm 1 gives B_t v_t=B_{t−1}v_{t−1}+b_t g_t², with B_0=0 and b_t=t^(−γ). Subtracting the all-baseline recurrence leaves zero for t<τ and exactly (H²−G²)τ^(−γ) in B_t(v_t−G²) for t≥τ. Integral comparison gives B_t∼t^(1−γ)/(1−γ) for 0≤γ<1 (at γ=0 it is exactly t), B_t∼log t for γ=1, and B_t→ζ(γ) for γ>1. These prove the constants, the positive permanent imprint, and the special γ=0.1 tail. Since G>0, taking the inverse-square-root ratio gives exactly the claimed rescaling, with limit 1 or strictly below 1 as stated. The calculation is for fixed τ and the prescribed one-coordinate input; it does not prove a trajectory statement, a momentum statement, or convergence of the full optimizer. The frozen verify.py was inspected but not executed; numerical guards are not required for these exact identities.

## originality

FAIL

The original NosAdam paper already gives the exact normalized influence of every past squared gradient and the nonnegative hyperharmonic exponent family. Replacing one input in that identity and applying elementary partial-sum asymptotics directly implies the whole finding, even though the finite-outlier formulas and rates are not expressed verbatim there.

## value

FAIL

The distinction between summable and nonsummable memory is a useful explanation for users of the algorithm. As a mathematical finding, however, this is only substitution into the published influence weight followed by the textbook p-series calculation. No new stability, trajectory, or other nontrivial consequence survives within the submitted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
