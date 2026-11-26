---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The dichotomy and its fixed-space and quotient consequences are sound, but the last sentence of the Finding at RESULT.md line 20 asserts rank-one top reduced homology under the sole stated condition dim W_G>0. Take arcs 1→2, 2→1, 2→3. The SCCs are {1,2} and {3}, so dim W_G=1. The arc 2→3 is a cone apex; the complex is the path of two edges with this common vertex, and its reduced homology is zero. The determinant calculation at lines 48–52 proves the claim only in the no-cross-arc case. For the core equivalence I checked that a lower sink fiber forbids all tails in S and admits the order contraction F ⊆ F∪A(S) ⊇ A(S) also on H-fixed fibers; an order complex has no inversion within a chain. The component join is equivariant even for component permutations: choose an equivariant inverse and homotopies for one representative per component isomorphism type and transport them along isomorphisms. On fixed vectors the component-sum map onto the SCC permutation module is split surjective, giving the difference of orbit counts. This proof handles empty realizations. The bundled checker was inspected at checks/verify.py lines 58–89: it uses zero reduced Euler characteristic in the cross-arc case, and is not evidence for the unqualified rank-one sentence or the general homotopy type. No frozen code was executed.

## originality

FAIL

The 2026-11-17 signed-equivariant record proves the same dichotomy for a larger symmetry group on exactly the same complex and representation. Restrict to positive signs to obtain the frozen theorem's main result. Its hemisphere cover is relabeling-compatible; the incidence comparisons yield a natural equivalence up to equivariant homotopy. The alternative sink-poset proof and the orbit-count/determinant restatements do not establish a distinct result.

## value

FAIL

A genuine representation model for the whole complex is mathematically useful, but this record does not fill that gap: the established signed result gives more information. The alternate sink-fiber argument is a neat application of a standard criterion, but no new use of the sink map or materially stronger conclusion is established here. The ordinary orbit counts and sign formula are immediate linear algebra once the model is known. No correction of the homology hypothesis yields a distinct useful remainder at the scale claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
