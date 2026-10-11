---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The mathematical deductions are correct. A topology on a finite set has only finitely many distinct opens, so every arbitrary intersection of opens is a finite intersection and the topology is Alexandrov. For an Alexandrov space its opens are exactly the up-sets of the specialization preorder, and the original intuitionistic preorder is contained in that specialization preorder because every open was assumed upward closed. In the finite quotient poset, the union of maximal specialization classes is open and meets every principal open; conversely every dense open must contain each maximal class, so this union is the unique least dense open. On a chain, the available up-sets are nested tails, so any subfamily containing the empty set and whole set is a topology, giving exactly 2^(n-1) choices and the stated multiplicities by fixing the least selected nonempty tail.

## originality

FAIL

The final claim is a direct assembly of standard finite-topology facts with Sedlár's published dense-open characterization of coherent justification. The finite-space specialization theorem already identifies every finite topology with the Alexandrov topology of its specialization preorder. Once that theorem is invoked, the least dense open as the maximal specialization classes is an elementary finite-poset observation, and the chain census is the immediate count of subfamilies of a nested set of tails. Under implication-based originality, the absence of the exact combined sentence in the evidence-logic paper does not make these textbook consequences original.

## value

FAIL

The finite collapse, maximal-class dense core and chain census are mathematically correct and may be pedagogically useful, but after the published semantic criterion and standard finite-space theorem they are routine textbook deductions. The chain multiplicity calculation is a direct count of a nested family and does not isolate a new structural gap under the stated value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
