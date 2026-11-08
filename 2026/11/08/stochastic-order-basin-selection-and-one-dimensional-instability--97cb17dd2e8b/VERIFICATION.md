---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limitations

The proof in `RESULT.md` establishes the general claim for every integer \(k\geq2\); it does not extrapolate the finite checks to an infinite theorem. Its decisive steps are the exact tail-coordinate transformation, nonnegative off-diagonal partial derivatives, strict comparison with uniform, explicit strict sub- and supersolutions, direct equilibrium classification, and a rank-one inertia argument.

Execute `python3 check.py` using the standard Python library. The script checks exact stationary and barrier identities for every integer \(2\leq k\leq16\) (30 signed barrier configurations), reconstructs their simplex masses, tests the precise directional inequalities, and integrates the two rational five-opinion examples by fourth-order Runge–Kutta. It prints a final PASS line only if every assertion holds. The original packaged script was run and passed before publication.

The time integrations are numerical cross-checks, not global convergence proofs. No formal proof assistant or independent scientific audit has been used. The verification does not establish generic nonsymmetric basin boundaries, finite-agent consensus probabilities, or a sharp convergence rate.
