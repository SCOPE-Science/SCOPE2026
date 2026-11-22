---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Correctness PASS contingent on the actual independently established integral homotopy premise for the ordinary NON-PURE boundary tetrahedron. Its 24 Hasse incidence vertices give exactly f=(24,216,896,1692,1248,256), total 4332 nonempty acyclic matchings; independent enumerator rebuilt the 14-node directed Hasse graph, reversed disjoint chosen edges and checked all acyclic faces. The published B≈∨21 S³∨24 S⁴ implies rational homology ranks (21,24) and whole boundary ranks d5=256,d4=968,d3=703. Packaged tetra_boundary_char.py was read in full: it builds oriented differentials and signed invariant chain sums for the ten S4×C2 conjugacy classes and their powers, computes fixed-boundary ranks at primes 1009,10007; prime orders are coprime to 1,2,3,4,6 and whole ranks equal known rational ranks, so averaging direct-summand localizations ensure fixed ranks over Q. Cyclotomic inversion yields degree-3 natural (21,-3,1,0,-1) and ghost (9,1,-3,0,-1), degree-4 natural (24,-2,0,0,-2) and ghost (0,-2,0,0,2); independently computed complete signed Lefschetz differences and Specht ghost ± multiplicities (15,6), (12,12). Quotient rational invariants follow by transfer and character averaging. This run did not execute the full invariant-boundary rank checker; its exact finite algorithm and existing full output were materially inspected, and independent face/Lefschetz/character arithmetic verified, not misdescribed as a new full modular-rank reproduction.

## originality

PASS

Originality PASS best-of-knowledge. Scoville (2026) proves the ordinary non-pure boundary homotopy wedge but not graded rational S4×C2 action. Lin–Scoville computes the Morse-complex automorphism/ghost action on vertices but not its graded homology. Existing published characters treat the full tetrahedron, PURE boundary Morse matching complex, or GENERALIZED matchings without acyclicity; their chain complexes have different ranks. The published F/B relative Q[S4]^4 constrains only the virtual character chi4−chi3, not either graded character or ghost extension. Thus none of those statements implies the twenty rational character values and quotient distinctions.

## value

PASS

Value PASS. Determining the complete graded rational representation of a natural but nonpure discrete-Morse matching complex, including the incidence-complement ghost action, is a meaningful exact topological classification: it resolves a genuine ambiguity left by known wedge ranks, relative virtual character, and group automorphism classification. Distinguishing full/rotation quotient rational homology is a substantive structural consequence not inferable from nonequivariant Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
