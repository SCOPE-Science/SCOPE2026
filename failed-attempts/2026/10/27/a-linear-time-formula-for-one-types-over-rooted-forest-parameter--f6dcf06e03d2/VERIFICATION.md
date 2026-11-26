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

A legal profile consists of a downset L below the new point and an upset U above it with every member of L strictly below every member of U; this is necessary and sufficient for transitivity without new comparisons on the parameters. Fraïssé extension realizes every profile; homogeneity fixes its complete type over named parameters, and any finite number of mutually incomparable copies realize the same profile, so the type is nonalgebraic. One independent count splits profiles with an empty side, giving 2D−1 since ideals and filters are in bijection by complement. If both sides are nonempty, choosing u in U shows L is contained in the strict ancestor chain of u. Its greatest element v determines L uniquely as the principal ideal of v. Then U is any nonempty filter of the strict descendant forest of v (automatically a filter in P); its count is the number of ideals of that forest minus one, namely product of the child d-values minus one = d_v−2. The standard empty-or-containing-root split gives d_v and product over components gives D. Thus the sum is exactly 2D+sum d_v−2n−1. This includes the empty case D=1 and t=1. Substitution gives the chain, star and antichain expressions. One postorder pass multiplies once per child and per component and sums once per vertex; every counted integer has O(n) bits, so polynomial bit complexity follows, not linear bit complexity. This is an analytic replay for all sizes. The supplied direct-transitivity checker and its 874-encoding and 24-example recorded output were inspected, not executed.

## originality

FAIL

A distinct indexed theorem (23742e530543) gives an exact linear-arithmetic formula for the same named nonalgebraic types on arbitrarily oriented cover trees. Its outward-root specialization telescopes to the frozen formula itself, and adjoining one minimum transfers it to every forest without changing the arithmetic complexity or the surviving scalar recurrence. The explicit expression need not be printed in the prior source for this to be mechanical coverage. This determination is about mathematical implication, not priority inferred from catalogue dates.

## value

FAIL

The tractability of a natural type-count invariant on these forests is mathematically useful, and the frozen proof is concise. But the exact scalar expression and arithmetic complexity are already recoverable by elementary cancellation from the broader formula. This leaves an expository simplification, not a distinct exact invariant, stronger complexity bound, or other motivated scientific remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
