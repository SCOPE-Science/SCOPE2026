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

PASS

The membership cells for the m variables partition the underlying atom set. Every feasible nonempty support is realized by assigning at least one atom to each type and the remaining atoms arbitrarily among those types. Operations preserve the property that the output is a union of cells determined solely by the support: the endpoint test checks only whether the chosen subset of types is empty or the whole support. Conversely the term δ₀(Y)=¬Y∧circ(Y) detects emptiness, so testing each cell defines exact-support selectors that realize any choice of output union on each feasible support. Constants for empty joins/meets are definable since m≥1. Independent choices of 2^r outputs at each r-element support give the displayed count and examples. The same inductively defined type semantics on every allowed support proves inclusion of the at-most-m-variable identity theories as k increases; exact support tests of size k+1 separate successive theories while k<2^m, and beyond that no new support can appear. This proves the ideal boundary statements even for k=1 and m=1. Independent concrete term-table closure on full input/atom coordinates (not assuming support collapse) used the additivity of ∃X, which tests nonemptiness, to refine Boolean blocks; it verified the exponents 4,16,28,32,32 for m=2 and k=1..5 among other cases. Replay: /workspace/branches/independent_replays/replay2.py and replay2.out. The finite checks do not replace the general proof.

## originality

FAIL

The exact form and threshold are mechanically recovered by classical discriminator interpolation on the simple monadic Boolean algebras, not merely analogous to a known atom visibility theorem. The necessary binary subalgebras are ordinary Boolean partitions, and the endpoint/quantifier condition immediately reduces them to products and graphs of partial isomorphisms; the published interpolation lemma then gives exactly the choices in the frozen normal form. Counting the feasible factors and observing first appearance of the full support gives the count and cutoff. No verbatim prior printed finite-k formula or priority is asserted.

## value

FAIL

The logical operation motivates the question, but the occupied-cell interpolation and sharp identity bound are routine consequences of the standard term equivalent simple monadic expansion and classical finite interpolation. The explicit count packages those consequences usefully for exposition; it does not add an independent unknown exact invariant, structural obstruction, or strengthening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
