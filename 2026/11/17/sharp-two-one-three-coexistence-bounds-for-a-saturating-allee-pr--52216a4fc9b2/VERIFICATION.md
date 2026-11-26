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

PASS applies to the corrected /workspace/repairs/5/RESULT.md, not the frozen proof. Frozen RESULT.md 45–49 prints a false general Jacobian identity: at (r1,k1,s,k0,h,A,lambda,b)=(10,1,1,1/10,1/2,1,7,1) and coexistence (x,y)=(1/2,1), det J is 17/32 but its printed right side is 221/512. The replacement adds the predator row to the prey row, using the exact sum balance s(Y−y), and obtains det J = sy(Y' q_y + q_x) = sy q_y(Y'−Z'); direct differentiation gives q_y=x(Ab−lambda)/B². Thus in the inhibitory regime the signs from the repeated-node divided differences of F=Y−Z (F'''<0) give positive, negative, positive determinants as claimed. Rechecked all three count arguments: the feasible intersection is one open interval with no interior pole; on the cooperative interval Z decreases and is convex, F' is positive to the prey maximum and strictly decreasing after it, hence at most two distinct roots. The neutral cancellation fixes one prey coordinate, and inhibitory F'''<0 rules out four roots by Rolle. Replayed /workspace/independent_exact_checks.py, coexistence(): exact cooperative signs and neutral x=5/16, the quartic and Jacobian identities for the inhibitory example, its three disjoint feasible sign brackets, fourth root beyond the pole, and direct rational interval trace/determinant/discriminant signs (+,+,+), (+,-,+), (-,+,-). The nonzero Jacobians give persistence with the signs and domain retained. The positive count bounds are sharp maxima, not fixed counts for every parameter choice. The companion frozen checker and output were inspected, not executed; they cover only the examples and do not verify the false general formula. The replacement is complete and retains their correct scoped usage.

## originality

PASS

The supported distinct claim is the sharp sign-dependent trichotomy within this exact rational response family, including the inhibitory three-state example and its robustness. The only exact indexed match identified is the assigned record itself. The original paper is clearly a high-relevance source for the model and partial equilibrium counts; its precise theorem scope could not be independently verified here, so the repaired text does not claim a checked improvement over a particular statement of Theorem 2.4.

## value

PASS

The sign is a natural boundary: it changes the sign of the per-capita predator derivative in predator density. A sharp feasible count across all allowed prey-threshold ratios, with exact witnesses and robust three-state local stability rather than just a quartic degree bound, distinguishes two structurally different regimes and the neutral degeneracy. This conclusion does not require an experimental interpretation of inhibition or any global phase-portrait claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
