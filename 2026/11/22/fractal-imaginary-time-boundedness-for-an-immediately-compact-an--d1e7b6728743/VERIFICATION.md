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

The triangular blocks are individually entire semigroups. For |arg z|≤θ<π/2 the off-diagonal is bounded by n^γ/(e n! cos θ), while both diagonals are at most one in modulus. This gives strong continuity by density at zero; truncations converge in norm locally on the open right half-plane and at every positive real time, proving holomorphy and immediate compactness. The generator is the diagonal block operator on its maximal graph domain, with finite supports a core by truncation. Away from its listed eigenvalues its block inverses have diagonal entries O(1/(n!)²) and upper-right entries O(n^γ/(n!)³), excluding additional spectrum. For Re z<0 the first diagonal diverges; on the imaginary axis the supremum of the off-diagonal moduli is finite exactly under the factorial-distance criterion, by the two-sided sine bound. The right half-plane is the interior of the boundedness set and no extension through an axis point can agree with the blocks on an open neighborhood. For γ>1 the integer error in the nearest-integer recurrence eventually vanishes; the remaining signed error must vanish since it would otherwise grow by factorial factors. For γ≤1 use the canonical factorial expansion with a tail strictly less than the maximal tail (take terminating digits at ambiguous endpoints). In a fixed bound class, digit counts are O_C(1+n^(1−γ)); covers at size 1/N! give the stated upper bounds. For γ<1, restricting digits to 0 through floor(j^(1−γ)/4) keeps the points in the group; equal-weight cylinder mass is exp(−(1−γ)N log N+O(N)). An interval between the two successive factorial scales has positive-mass intersection with at most two level-N cylinders, giving a Frostman bound for each s<1−γ. Binary factorial digits give uncountably many points at γ=1. Multiplication by n! modulo 1 preserves Lebesgue measure, so the fixed bound classes are null; the subgroup property, rational density and exact group of translations follow directly. Bounded analyticity is sectorial (proper subsectors), not a uniform bound on the full half-plane. Finite diagnostics were inspected but not run; the proof, not those diagnostics, establishes the infinite statements.

## originality

PASS

The supported distinct contribution is the immediately compact bounded analytic semigroup realization of the exact factorial boundary group, including tunable positive Hausdorff dimension and no holomorphy across the imaginary axis. The individual digit-count techniques and general semigroup periodicity are not new. No equivalent or dominating operator result was found in the inspected statements; this is not a historical priority certification.

## value

PASS

The example separates boundedness at individual imaginary times from any analytic extension there even under immediate compactness and strictly negative real generator spectrum. The exact dense proper subgroup and continuously tunable dimension give a quantitative structural witness, not just isolated bounded times or a parameter substitution in the compared periodic examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
