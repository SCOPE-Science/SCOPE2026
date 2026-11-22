---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The well-defined index-27 numerical assertion is valid and is already proved in prior literature: rank-three independence K has 234 triangles and 66-dimensional boundary image, so H_2(K)=Z^168; 234 quadrangle 4-arc boundaries have Smith invariants 1^165,3^3 and quotient (Z/3)^3. Inspected assigned verify.py regenerates the 13 GF(3) projective points, 234 facets and arcs, a unimodular 66-column integral section, mod-2 rank168, mod-3 rank165, a specified exact maximal minor -27 and a full Smith-form check. HOWEVER its RESULT.md additionally states these 234 are "exactly the support-minimal nonzero integral 2-cycles". In the standard inclusion-minimal support meaning this is FALSE. Choose three collinear points A,B,C in PG(2,3), and two off-line points U,V: the six independent triangles UAB,UBC,UCA,VAB,VBC,VCA admit an oriented suspension cycle (the difference of the two cones over boundary ABC). Every one of its six triangles is essential by edge-cancellation propagation, so its 6-triangle support is inclusion-minimal; it spans FIVE vertices and is not a quadrangle tetrahedral boundary. The submitted proof establishes only shortest/minimum-cardinality support (four vertices), not all inclusion-minimal supports. Finite verification of the 234 quadrangles cannot eliminate larger support-minimal cycles. Thus the final claim as worded fails C even though its central lattice invariant is correct.

## originality

FAIL

The 2026-10-25 published “Three independent 3-torsion classes in the ternary projective cap complex” RESULT.md directly states the SAME finite 13-point rank-three matroid K=X^(2), H_2(K)=Z^168, all 234 quadrangle boundary cycles forming a rank-168 lattice of index 27, quotient (Z/3)^3, and PGL3 transitivity. Its exact 234-column 3-boundary Smith form 1^165,3^3 implies the assigned computation verbatim. This is decisive statement-and-implication coverage from a full prior mathematical text, not merely a parameter match or title similarity. The submitted result changes proof/coordinates but cannot claim originality of its unchanged main invariant.

## value

FAIL

The object/invariant are naturally motivated, but the precise index and cyclic 3-torsion quotient, group orbit count and shortest quadrangle supports have already been established for exactly this complex in the 2026-10-25 published record. Recomputing a known Smith invariant with a different 168x234 matrix does not supply a new useful mathematical fact. The extra literal claim about all support-minimal cycles is false, not an incremental contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
