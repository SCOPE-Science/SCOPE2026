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

The competitors' reset term in the first-moment equation is −λu, so with α=r+λ the mean at the next visit conditional on gap t and initial stock z is (rC/α)(1−exp(−αt))+z exp(−αt). To justify a chronological long-run rate despite dependent rewards, view each gap and its independent Poisson event segment as an iid block. With common blocks, the postvisit recursion contracts by at most 1−q per visit; a two-sided block construction gives a bounded stationary ergodic reward sequence, with summably small initial-state effects. The gap strong law divides the stationary reward mean by m. The resulting expression is strictly decreasing in E exp(−αT), so strict Jensen gives unique fixed-mean periodic optimality. For exponential gaps the transform is 1/(1+x), x=αm. The resulting ratio has strictly positive q derivative for x>0, so equality in the ceiling requires q=1. Then the derivative has the sign of 1+x+x²−exp(x); the single sign change of the second derivative of exp(x)−1−x−x² implies exactly one positive crossing, with the ratio tending to 1 at both endpoints. Thus the bound and 'if and only if' are exact and feasible, including λ=0. Independent bisection of exp(x)−1−x−x² on [1,3] reproduced x=1.793282132900761 and ratio 1.298425607525639. Frozen check code and reported output were inspected, not executed; their simulations and samples are not the proof.

## originality

PASS

Credit the established qualitative advantage of regular visits to a decelerating renewing resource. The supported distinct contribution is the sharp fixed-mean percentage over the full partial-harvest/independent-clearing model and its complete attainment criterion. No accessible independent result compared here gives or implies that full claim. Priority remains provisional, especially for the full depletion/no competitor case.

## value

PASS

The exact cap gives a calibrated timing-only benchmark at fixed visitation effort in a standard replenishment model. It identifies when the upper limit is attainable and proves that partial collection cannot amplify that maximum despite memory across visits. The dimensionless ceiling survives independent competition without purporting to quantify travel, population or spatial effects. This goes beyond the routine qualitative Jensen comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
