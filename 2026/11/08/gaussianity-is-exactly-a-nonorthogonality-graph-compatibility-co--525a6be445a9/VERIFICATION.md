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

A positive-probability block of spanning row projectors is strictly contracting: norm equality would fix a vector orthogonal to the spanning rows. Independent blocks give exponential L^r decay for their products and almost sure contraction, so the Gaussian pullback converges in every finite L^r and shared-drive coupling gives uniqueness even without assuming moments of a rival invariant law. For an initial law of only finite fourth moment, use the moment-coupling statement only through r=4. Stationary mean is zero by positive definiteness of Σp_i u_i u_i^T. A centered Gaussian stationarity mixture can agree with a single Gaussian only when all component covariances agree, by variance of the directional variances. The equation S_i=S is equivalent to Su_i=s_i u_i; hence equal eigenvalues on each nonorthogonality edge are necessary and the orthogonal component covariance is sufficient. The conditional covariance Γ of the pullback gives 3 Var(v^TΓv), and conditioning on the last row proves the bound. Incompatibility makes at least one S_i−S nonzero, so some direction's bound is already strictly positive, not necessarily every direction's. Independent exact replay: python /workspace/audit_checks/kaczmarz_conditional_variances.py. It solves the conditional scalar variance process in dimension two and reproduced all three reported rationals (covariance, fourth cumulant and lower bound); it checks that example only. The uploaded program was inspected, not executed.

## originality

PASS

The exact graph compatibility criterion with arbitrary positive iid sampling of fixed spanning rows, plus a computable directional fourth-cumulant witness, is distinct on the evidence compared. Neither Gaussian mixture rigidity nor orthogonality of eigenspaces is claimed as new.

## value

PASS

A necessary and sufficient graph test for invariant Gaussianity works for arbitrary spanning row families, including overdetermined ones, irrespective of the positive sampling law. The fourth-cumulant bound provides a quantitative observable diagnostic without fitting a stationary density, unlike a criterion based only on covariance convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
