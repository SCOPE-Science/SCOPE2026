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

# Checks and limits

Run `python hom_even_girth_check.py`. The code enumerates every length-six or length-eight closed walk in eight finite graphs and every single-coordinate reconfiguration edge, reconstructs all connected components, and checks the regular dihedral action on rigid vertices. For the five length-six targets, it independently constructs every Cartesian-product cell and verifies the alternating cellular Euler sum against the exact homotopy-predicted value. The archived output is `verification_output.txt`.

Examples include the pentagon, hexagon, Petersen graph, Heawood incidence graph, a five/six-cycle rose, heptagon, octagon, and a seven/eight-cycle rose. The Petersen case has ten six-cycles and therefore 120 isolated Hom vertices, plus one remaining nonbipartite-cover component. The Heawood case has 28 six-cycles, 336 isolated vertices and two remaining cover components. These checks do not establish homotopy equivalence by themselves. That claim depends on the exact closed-walk argument and the independently published square-free Hom-complex theorem, Theorem 5.8 and Lemma 5.11 of arXiv:2412.19144v1.

No integral positive-degree homology action, canonical equivariant splitting, or extension to graph targets of smaller girth is asserted. Independent audit: not performed.
