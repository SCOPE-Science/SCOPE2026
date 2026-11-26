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

For deterministic input Av the independent centered entry noise has isotropic quadratic expectation nσ_w²μ_β²‖Av‖²/D; the mean cross term vanishes. Each modal coefficient is strictly convex in λ, giving the maximum over attained endpoints. Subtraction gives the strictly increasing H crossing; H(c)<(κ+1)c (the reported positive quadratic), hence the active f₁ branch is strictly increasing after the crossing. The derivative on the left has sign Qκ(t)−κc and Qκ is strictly increasing, giving the unique min{m,x}. At crossing the difference's sign is Pκ(x); the thresholds (1+√10)/3<√3 order the quadratic and linear coefficient sign changes, so Descartes counts one positive root, with opposite endpoint signs verifying existence. When x<m there are unequal one-sided derivatives of opposite signs. At κ=2,c=7/12, exact crossing t=2 has both errors 55/108 and risk at t=0 equal to 7/3; shifted-target ratio squared is 28/27 and is already feasible at t=3 (175/192). Independent replay: python3 /workspace/branches/independent_checks.py 2 verifies eight exact cases using nonsymmetric centered two-point errors, two independent copies, an interior eigenvalue and mixed directions, plus the rational example. This is diagnostic; all-phase coverage is analytic. Frozen verify.py inspected, not executed.

## originality

PASS

The supported distinction is the stationary/crossing minimax law for true unshifted correction, not the write model, the shifted-target feasibility bound, or diagonal damping in general.

## value

PASS

The shift is a natural design variable in a known programming model. A sharp condition for choosing one of two optimizer mechanisms and a nontrivial example separating implementability from actual accuracy are useful even for a diagonal single-application benchmark. The result does not imply iterative convergence, hardware advantage or an orientation-independent SPD law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
