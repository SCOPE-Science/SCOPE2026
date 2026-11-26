---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

FAIL

The main coefficient formula is correct after straightforward proof and wording corrections, but the frozen Finding explicitly calls B positive. In fact B/A=−ρN′(ρ)/N(ρ)+(ρ²+6ρ⁴)/p<0: the first ratio exceeds 3/2 since ρ>1/2, and the second is less than 7/6 since 0<ρ<1. Independent evaluation in /workspace/check_frozen_math.py gives B≈−1.1581858701 and recovers the stated positive leading coefficient 0.0898863185. The subgroup count gives a rotation contribution −(1/2)log P and a reflection contribution N/P. The even edge reflection at n=2 should be treated directly (its unique fixed word is 00), not as a path of m−2=−1 vertices using the empty-path convention; n=1 also directly fixes just 0. These counts agree with the formulas. At the positive pole of the exponent the square-root prefactor and exp(A/w+B) have the stated expansion. On |z|=ρr with r=1−δ and δ=√(A/n), the frozen uniform lower bound proportional to θ²/δ³ is not valid across a fixed positive-side neighborhood. The exact loss of real part for 1/(1−r exp(iθ)) is r(1+r)(1−cos θ)/[δ(δ²+2r(1−cos θ))], which is sufficient: outside the inner δ^(3/2)log(1/δ) arc it is at least a constant times log²(1/δ), and becomes order 1/δ away from the radius. On the inner scale θ=δ^(3/2)s, the order-δ^(1/2) terms are odd imaginary and integrate to zero; the order-δ integrated relative error is O(n^(−1/2)). The Gaussian width times the square-root prefactor gives 1/(2√(πpn)); r^(−n) produces exp(A/2), and the negative singularity is suppressed by the gap A−A_minus on this circle. Thus neither the wording error nor the nonuniform estimate disproves the boxed asymptotic. Frozen code and verification notes were inspected, not run.

## originality

FAIL

The exact zeta is a direct instance of the published flip matrix formula, and once it is specialized the all-n leading law with its constant and error is obtained by standard exponential-pole coefficient transfer and a comparison of two explicit positive residues. This is a failure of distinctness by implication, not evidence that an earlier paper printed the identical golden-mean formula or that any inaccessible source establishes priority.

## value

FAIL

The golden-mean flip and its Lind coefficients are natural objects, and separating coefficient growth from orbit growth is sensible. Here the exact zeta is already available by matrix substitution and the precise coefficient constant, all-n scope and relative error follow from the standard exponential-pole model once the two residues are compared. The frozen record does not supply a surviving nonmechanical invariant or useful new method beyond that routine specialization. Correcting B's sign wording or the contour proof estimate would not change this value decision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
