---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

An injective vertex filtration on C_n gives a nonconstant orientation sign word. A selected vertex-edge incidence forces both adjacent signs, producing a 3-color marked word with no adjacent opposite marks; any single-sign marked word must leave at least one edge with both endpoints unmarked. Conversely these conditions extend to an acyclic orientation and hence a filtration. The weighted cyclic compatibility matrix T(t) counts all allowed adjacency words, while U(t) counts each of the two disallowed monochromatic vertex covers; they are disjoint for n>=3. Eigenvalues at t=-1 yield the trigonometric Euler formula and least period 12. Independent integer-matrix evaluation yields F22(1)=263593441; exact evaluations for n=3..14 matched all twelve stated Euler residues. The formula is for faces and Euler only, not complete homology.

## originality

FAIL

The published full strong-cycle dihedral Euler-character theorem already establishes precisely the same three-symbol face criterion and writes the same general weighted transfer matrices T(t) and U(t) in the proof of its much stronger character statement. It obtains the identity trace at t=-1 as a special case. Consequently F_n(t)=tr T(t)^n-2tr U(t)^n is an immediate full-weight generating-function reading of its already-displayed combinatorial enumeration, and the Euler period and n=22 count require only substitutions. This is stronger substantive coverage despite the absence of the full polynomial in its title.

## value

FAIL

A full f-polynomial and 12-periodic Euler characteristic are natural, but the same generative three-state criterion and symbolic transfer matrices are already published as the core of a stronger equivariant theorem. Extracting coefficients and evaluating n=22 do not provide a further independently useful unknown mathematical invariant beyond direct matrix substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
