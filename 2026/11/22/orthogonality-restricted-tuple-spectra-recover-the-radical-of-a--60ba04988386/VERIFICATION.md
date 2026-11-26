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

This verdict is for the corrected RESULT.md. The frozen line 20 incorrectly gives T₂=5 at d=0 for every q; already q=3 is a counterexample. With U=0 an orthogonal pair type is specified only by its linear kernel in F_q², giving 1+(q+1)+1=q+3. The repair corrects that statement without weakening the fixed-prime-power scope. For arbitrary U, equality of the quotient kernel H, the map H→U and the complement-basis pairing functionals gives a linear isometry over U; Witt extension in a finite symplectic envelope gives conjugacy. Conversely, any such map with isotropic image S and any functionals annihilating S are realized by the alternating space U⊕W₀, embedded in the ambient space over U. This works in characteristic two. Finite relation/pairing diagrams determine complete types, not just counts of tuples in a finite sample. Counting the H→S surjections and the q^((r−h)(d−t)) complement pairing choices gives the all-arity sum, with J_t counted by radical intersections and graphs of linear maps over the nondegenerate quotient. Quotient ranks 0, 1, 2 give the binary formula for d≥1; its coefficient of q^ρ is q^d−q^(d−1)>0. The q=2 examples give unary 8 and binary 62 and 56; the empty tuple contributes one.

## originality

PASS

The repaired claim's distinct part is the explicit all-arity orthogonality-restricted spectrum over an individually named base and sharp recovery of its radical from two scalar counts. It does not claim the empty-base kernel count, isotropic-frame formulas, or Witt extension as new. No inspected source states or evaluates the named-base restriction with the radical reconstruction; the verdict is bounded by the inspected evidence.

## value

PASS

The exact profile of a natural named stabilizer on orthogonal tuples identifies a finite geometric invariant that the unary profile completely misses at fixed dimension. The second count sharply recovers the radical and thereby every higher profile without reconstructing the marked basis; q=2 gives a concrete witness to sharpness. The useful contribution is this discrimination and all-arity count, not the empty-base arithmetic correction on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
