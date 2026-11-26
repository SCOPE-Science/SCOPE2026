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

The frozen recursion agrees with deterministic Algorithm 1 specialized to a ball indicator and a centered scalar-Hessian quadratic. Projection reduces to scalar clipping on the initial diameter. Starting on the sphere, a full flip occurs exactly at lambda*eta/S_k >= 2, including equality; every such update multiplies S_k by Q. Counting the qualifying nonnegative exponents gives M, including M=0 when r<1 and a final flip at any exact power r=Q^j. S becomes strictly above the saturation threshold after those flips, so no tail step increases the radius or needs projection. In the interior recursion, S_{k+1}^2-S_k^2=lambda^2*||x_k||^2; the squared radius drop is at least 2*eta*(2-theta_entry)/lambda times S_{k+1}-S_k. Telescoping bounds S above and keeps the tail contraction uniform and strictly below 1 (including finite termination). Taylor expansion gives 1/log Q=eta^2/(2R^2)+1+O(eta^-2); the integer rounding changes the count by at most 1. Independent replay: python3 /workspace/independent_checks.py 2, fifteen rational saturation tests immediately below, at, and above five exact threshold powers; these corroborate, not prove, the general result. The frozen checker and verification record were inspected, not executed.

## originality

PASS

Best of current knowledge: the method and general convergence/boundedness properties are prior. The supported distinction is the exact plateau count, its sharp diverging gain dependence, and the corresponding pathwise exit and geometric tail on the specified instance. No inspected stronger theorem gives the count as a corollary.

## value

PASS

On a canonical compact strongly convex test problem, the exact number of zero-improvement updates is a concrete startup obstruction: any fixed nontrivial objective target must wait, yet a fixed projected step solves the same instance in one update. The sharp gain coefficient and proof of later geometric convergence distinguish startup delay from instability. This is useful for interpreting parameter-dependent convergence bounds, not a general complexity lower bound for adaptive methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
