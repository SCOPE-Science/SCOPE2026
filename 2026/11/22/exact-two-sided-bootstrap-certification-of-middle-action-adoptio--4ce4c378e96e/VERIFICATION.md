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

The weak seed exposure inequalities keep the social input within the closed middle-bin boundaries, and strict positive inertia preserves the open upper boundary from a middle-bin initial opinion. Once seed actions are fixed, the outsider map is order preserving. The two extremal runs are monotone and stay in [−1,a₂] or [a₂,1]; each consequently has only two possible actions. In the lower run, strict eligibility gives an input bounded above the lower threshold by a fixed positive margin, hence finite crossing. In the upper run the converse-sign strict margin gives finite crossing below the upper threshold. For either terminal closure, its complement is invariant on the nonadopting side from the corresponding extremal initialization: exposure is only weakly on the noncrossing side and relaxation preserves the requisite strict lower or weak upper side. This handles equality without letting an asymptotic approach count as adoption. Sandwiching yields a common finite time independent of the starting profile and separate extremal obstructions prove necessity. The combined closure lies in each directional closure by monotonicity of weights. The exact example has seed exposure 1/2 at each outsider and reversed directional thresholds 1/4 and 3/4, giving eligibility in opposite orders and a stalled combined rule. A one-agent seed is impossible because W_ii=0 and the other agents can all begin at −1 with the seed at its lower bin boundary, so at most one outsider is possible with n≤3 and then the two tests reduce to the combined test. Independently replayed the witness with heterogeneous rational inertias (consensus at step 8 on both extreme runs) and a separate two-sided equality obstruction via `cd /workspace && python -B -c 'import independent_checks as c; c.bootstrap()'`. The frozen source checker was inspected, not executed; its trajectory tests are not the all-network proof.

## originality

PASS

The pass is for the explicit static, inertia-independent characterization by two strict weight closures in the three-action model, and the sharp smallest strict-gap network in that model. Neither the extremal-trajectory characterization as such, the weak seed condition, nor the existence of a multiaction four-agent gap in general should be credited as distinct from the inspected literature and indexed claims.

## value

PASS

The static guarantee can be computed using weights and thresholds without evaluating any very long relaxation clock, and certifies the exact universal adopters, not just a sufficient subset. It separates directional routes that represent distinct worst-case initializations and proves their interaction matters already at the smallest possible three-action network. This is not a claim about strategic equilibrium realizability, arbitrary alphabet sizes, or the minimal size of networks capable of consensus at all.

The dated certificate retains the supplied scientific assessment, sources and limitations.
