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

The rank (original face cardinality) of each barycentric vertex is preserved by D4 and occurs at most once in any flag. Thus two points of the same closed flag simplex in the same group orbit have identical supports and barycentric coordinates; the closed simplex embeds in the geometric quotient. This also makes the alternating deletion boundary well defined with distinct boundary facets, even though different orbit cells can have the same vertex set. Reviewed the complete frozen verifier and its recorded output, then independently enumerated all placements by choosing rows and permuting columns and all flags by ordered nonempty blocks. Running /workspace/queen_replay.py reproduced the placement and flag counts and orbit-cell vector (63,373,711,546,150). A separate descending-dimension free-face sequence leaves (45,148,108,0,0); choosing a spanning tree on this reduced complex and eliminating 104 generators (66 by unit relators, the rest by reversible single-occurrence substitutions) gives an empty presentation. Another independent replay checked signed boundaries and the original full two-skeleton's 311 generators; it found an alternative 826-pair collapse rather than the frozen script's 823. Different valid collapse orders need not leave the same model. A connected simply connected 2-complex of Euler characteristic five has H2 free of rank four and no higher homology; Hurewicz and the simply connected homological Whitehead theorem give the claimed wedge. This result is for the actual ordinary orbit space, not a rational invariant-space computation.

## originality

PASS

The exact geometric D4 quotient homotopy type is distinct from the unquotiented five-queen result, placement enumerations and the other checked symmetry quotients. No dominating prior description was found among the inspected statements.

## value

PASS

The board and full symmetry group are intrinsic to the standard queen placement problem; the geometric quotient accounts for stabilizers rather than treating symmetry as a mere count of different placements. Its exact integral homotopy type distinguishes simple connectivity, absence of torsion and survival of four two-spheres, useful beyond either a face inventory or the ordinary homotopy type of the cover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
