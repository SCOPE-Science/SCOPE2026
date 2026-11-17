---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The 16 Q4 vertices with inclusive pairwise Hamming distances <=2 give 392 nonempty simplices and 196 orbit cells. Antipodes never share an edge, so the geometric involution has a regular orbit-CW structure. The eight even-parity vertices form the boundary of the four-dimensional cross-polytope; its antipodal quotient is RP^3. Independently reconstructed and validated the 76 exact relative face/coface pairs from matching.json, all 600 orbit Hasse incidences, acyclic reversed Hasse digraph, and exactly four critical dimension-3 orbit cells outside RP^3. Relative Forman reduction attaches four 3-cells to RP^3. Their S^2 attaching maps are null because pi_2(RP^3)=pi_2(S^3)=0, hence RP^3 wedge four S^3; the claimed integral homology and fundamental group follow. This finite exhaustive certificate proves only Q4 at scale two.

## originality

PASS

The result is a geometric orbit-space integral HOMOTOPY classification. Existing all-cube statements concern unquotiented Rips homotopy, B_n-representations or cohomological bounds; neither invariant rational homology nor equivariant character formally implies the RP^3 summand and integral orbit-space wedge splitting.

## value

PASS

This is a nontrivial integral geometric quotient classification of a natural central symmetry of the first dimension-four hypercube scale-two Rips complex. The projective subcomplex yields a previously unaccounted fundamental group and 2-torsion, and the explicit relative discrete-Morse splitting supplies information not retrievable from rational group characters. It is a motivated exact finite homotopy result, not a raw table or generic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
