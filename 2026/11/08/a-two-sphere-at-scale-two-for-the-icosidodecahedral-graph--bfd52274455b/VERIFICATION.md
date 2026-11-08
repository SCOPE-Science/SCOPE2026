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

# Reproducing the finite homotopy certificate

Execute `python3 verify_icosidodecahedron.py collapse_certificate.json` in a directory containing the two named files. This command uses only the Python standard library. It reconstructs the graph \(GP(10,2)\), its 30-edge line graph and exact integer graph metric; exhaustively enumerates simplices at radii one and two; checks all 468 simplicial collapse pairs against every remaining proper coface; independently re-generates the deterministic selection sequence; and verifies the resulting simplicial surface.

The expected output is stored in `verification_output.txt`. The checker must print `ICOSIDODECAHEDRAL_RIPS2_SPHERE_OK` and report the face vectors \((30,60,20)\) and \((30,180,380,330,102)\), a target face vector \((16,42,28)\), sixteen single-cycle vertex links, connectedness and Euler characteristic two.

A complete finite enumeration proves the collapse for this one specified complex. The topological conclusion additionally uses the elementary-collapse theorem and the classification of connected closed surfaces. This verification does not classify other graphs, higher Rips radii, or equivariant actions. Independent mathematical audit has not been performed.
