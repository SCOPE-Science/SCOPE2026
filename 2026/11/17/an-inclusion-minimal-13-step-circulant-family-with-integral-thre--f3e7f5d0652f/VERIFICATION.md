---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For t>=109 the three sum bands [2,6], [t-46,t+14], [2t-94,2t+22] are disjoint; within each, equal pair sums and singleton pairs depend only on the ten offsets, so the same complete relation matrix applies for all t. Independent generation of all legal singleton-vs-pair and pair-vs-pair relations at t=109 gives thirteen 13-column rows. Independent exact Smith form has ten 1s and a 3 (rank11), cokernel Z^2⊕Z/3; all thirteen one-generator deletions regenerated from scratch have only unit nonzero Smith factors. Checked several separated parameters as corroboration; band-separation argument handles infinitely many. Read Tang–Yau step-word and insertion-homotopy constructions: integral chain contracting relation ∂h+h∂=z-1 leads to an integral quotient of the infinite translation complex; n>2(t+11) prevents two-step modular aliasing, so the relation cokernel represents regular GLMY H1. The key all-parameter statement is not deduced from finite samples.

## originality

PASS

Existing published work establishes the step-word reduction (Tang–Yau) and 2-primary torsion circulants, but does not exhibit the stable deletion-minimal 13-step odd-primary Z/3 family as an already known special case. Novelty is the explicit Z/3 exact lattice family and deletion-minimality, not the general theory of Cayley path homology.

## value

PASS

Produces an explicit infinite family of strongly connected vertex-transitive Cayley digraphs with stable odd-primary torsion, and proves its short-relation presentation is inclusion-minimal for torsion. This is a motivated new arithmetic phenomenon beyond previously exhibited order-two examples; the family is exact and reproducible, while global step-count minimality is expressly not asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
