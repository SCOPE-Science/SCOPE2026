---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the degree-two truncated-octahedral symmetry barcode

Run `python3 verify.py` using Python 3.8 or later; no third-party modules and no network access are required. The program constructs the graph from the exact signed-coordinate definition; computes every shortest-path distance and every simplex at scales two and three; constructs exact integral two-cycles for all eight hexagonal faces; checks cycle boundaries, triangle witnesses, and unsigned transport under all 48 signed coordinate symmetries; calculates signed Lefschetz traces in both complexes; and reduces complete mod-two simplicial boundary matrices to determine the rank of the scale-two-to-three map.

The recorded run found face vectors (24, 96, 112, 30) and (24, 168, 472, 618, 384, 92). Its mod-two second- and third-boundary ranks were respectively (73, 30) and (145, 326), giving mod-two degree-two Betti numbers nine and one. It found sixteen distinct alternating triangles, each with no containing scale-two tetrahedron, and identified the eight coherent octahedral sphere cycles as an unsigned permutation system. Both full 48-element Lefschetz identities passed; the mod-two inclusion map had rank one, witnessed by a twenty-triangle cycle. The executable output ended with `VERIFIED_OK`.

The pre-existing mod-two numerical barcode and inclusion rank for the isomorphic four-letter permutahedron are explicitly credited; this script independently reproduces their relevant finite calculations. The pre-existing integral homotopy classifications of the two stages (nine two-spheres and one two-sphere) are an expressly cited input. Mod-two calculations alone would not prove rational nonvanishing in the presence of integral torsion or nontrivial first-homology torsion; neither obstruction occurs under that input. The verifier does not certify any separate, independent review or any homotopy classification beyond these stages.
