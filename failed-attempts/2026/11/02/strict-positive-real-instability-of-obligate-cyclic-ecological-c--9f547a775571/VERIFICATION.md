---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At a feasible equilibrium Bx*=A with A_i=-a_i<0. Put X=diag(x*), let P have its ones in the unique successor columns, and write BX=-DP+R with D_ii=c_i x*_(i+1)>0. Every row sum of R is D_ii-a_i, so D^(-1)R is nonnegative with maximum row sum strictly below 1, also when some chords vanish. Factor BX=(-DP)(I-P^(-1)D^(-1)R). The second determinant is positive since interpolation from I to I-P^(-1)D^(-1)R stays invertible by the row norm bound, while det(-DP)=-prod_i D_ii by the permutation sign of one n-cycle. Therefore B is invertible, giving uniqueness among strictly positive solutions, and J=-XB gives det(-J)<0. The real monic characteristic polynomial is negative at zero and positive far to the right, so it has a positive real root; for this smooth flow a positive real part yields Lyapunov instability. In the witness x*=1 the per-capita rates cancel and J1=1. There is no implication about the absence of unstable equilibria, positive periodic trajectories, or global extinction. Replay: frozen RESULT.md lines 25–50; exact finite-check code inspected but not executed.

## originality

FAIL

Theorem 3.4 of Stable Coexistence in Ecologies and Games (arXiv:2609.09286v1, 8 September 2026) proves an odd-cycle result whose proof gives the same signed determinant calculation with k=1. Its determinant computation uses only feasibility, not stability. The displayed dominance and nonsingular M-matrix argument is unchanged for zero competitive or antagonistic entries, since negative intrinsic growth still makes dominance strict and the off-diagonal sign condition is nonpositive, not strictly negative. Uniqueness and the positive real eigenvalue follow immediately from the determinant sign. The n=3 subcase is already present in the algebra of Meng et al.; the column-scaling argument also applies without change at n=3. This is demonstrated mathematical coverage, not an inference from a title or a search miss.

## value

FAIL

An exact instability mode and its determinant criterion would be useful for ecological coexistence if new, but the existing determinant proof already supplies the full sign criterion. Replacing its M-matrix step with a dominance homotopy and restating immediate spectral and uniqueness consequences adds no distinct criterion. The uniform equilibrium witness is a direct row-sum example rather than a separate motivating result. No genuinely valuable uncovered remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
