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

The fixed coordinate unitary gives A_{a,d}=r M_{exp(−dy)} V_a, d=δ, with boundedness exactly d≥0. The adjoint multiplier is r exp(−dy/a) composed with V_a* in the corresponding order, and the polar modulus is r M_{exp(−dy/a)}. This gives d→dq under the transform and W_c^*A_{a,d}W_c=A_{a,d/c}. For fixed 0<η≤1 and d>0, q crosses one at a=1. Dominated convergence applies to both multipliers on the operator and adjoint sides, but essential suprema give exact nonzero distances to the limits. Maximizing |exp(−qz)−exp(−z)| at z=log(q)/(q−1) gives the successive gap. Conjugating again to logarithmic translations gives weighted shifts whose two tails tend to one and zero. An interior eigen-recurrence decays at both tails in the stated operator or adjoint orientation; normalized measurable fields of solutions multiplied by arbitrary square-integrable scalar functions give infinite multiplicity. At radius r the product of weights on the one-tail has positive limit, eliminating eigenvectors for both recurrences; truncated plane waves on that tail give approximate null vectors for the shifted operator, with the weight error uniform across a bounded fundamental interval. At zero both operators are injective and the weight approaching zero rules out closed range. The zero-damping Fourier multiplier and a=1 multiplication cases have the stated boundary behavior. The commutator multiplier a^{-1}(exp(−2dy/a)−exp(−2dy)) gives the sign and claimed maximum directly.

## originality

PASS

Pass the explicit unitary-orbit dynamics and paired quantitative behavior, not priority for one-step weight formulas, the affine-index family, or the disk and interior eigenvalue facts. In particular, the latter facts already occur under an exact Laplace/half-plane equivalence in Schröderus. The compared literature does not establish the positive-damping Aluthge orbit as one fixed unitary class exhibiting both opposite strong-star limits and exact persistent successive separation in this family.

## value

PASS

This family gives a quantitative witness that an Aluthge orbit can retain its full unitary equivalence class and nonnormality at every finite step yet converge strongly-star to a normal operator. The two directions of dilation give opposite limiting mechanisms under the same parameter law, and the uniform exact norm separations make the topology distinction testable, beyond recovering the formerly known static spectra or one-step transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
