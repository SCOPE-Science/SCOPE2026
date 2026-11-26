---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The reciprocal sample mean of X^{-1} converges to (k-1)θ. The bounded transform and its V-statistic representation give the claimed scale-independent population discrepancy. The transform integrand's sign follows from (1+t/(4h))²-(1+t/h)=t(t-8h)/(16h²), where h=k-1. Multiplication by exp(8ha) makes its integral strictly decreasing, with strictly negative derivative, because the signed integrand has a single crossing. At a→0+ the tail diverges positively (logarithmically at k=5/2); at large a the negative linear term of the transform difference at t=0 dominates. The root is simple and has the claimed sign orientation. For fixed a>0 the kernel and scale derivatives are uniformly bounded on a compact scale neighborhood; first projection plus Taylor expansion and the delta method for the reciprocal mean give the stated influence function, with diagonal and degenerate terms negligible at √n scale. The fitted-scale derivative equals (a/λ*)F'_k(a) at the root, so the 1/X singularity cannot be canceled by the bounded projection; it has finite second moment for k>2. This proves the positive, finite alternative variance and the strict power limit for positive finite thresholds (also for thresholds tending in probability to such a constant). Under a Lévy null, the population kernel mean is identically zero in the scale and its derivative vanishes; the continuous first projection tends to a strictly positive constant as x→∞ and has mean zero, so its variance is positive on the full-support null. Independent replay: python /workspace/independent_checks.py (levy routine), using Tricomi U for the Laplace integrals, gives a=0.0375490493204766893 and derivative −42.31764123508 at k=9/4. The decimal is a numerical check, not the uniqueness proof. Read the submitted verification notes and code without executing it.

## originality

PASS

The published signed statistic and Lévy-null calibration are not new. The supported distinction is the simple, unique population blind weight throughout the stated Gamma shape interval and the nondegenerate fitted-scale alternative law at that weight. The closest checked primary article neither states this nor implies it from its light-tailed alternative simulations, null limit, or supremum consistency result. No distinct covering catalog statement was identified in the bounded comparison.

## value

PASS

The blind weight is a rigorously identified failure mode of a published signed goodness-of-fit test at ordinary non-null, fully supported alternatives. It distinguishes cancellation from a true characterization zero and rules out asymptotic power one rather than just showing small power in finite simulations. This is useful for tuning and interpreting the signed test even though the demonstrated weights are not the standard published grid; it does not discredit those recommended weights or the supremum test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
