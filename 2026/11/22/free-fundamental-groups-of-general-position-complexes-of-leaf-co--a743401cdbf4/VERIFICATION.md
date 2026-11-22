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

# Reproducibility and scope

Run `python3 verify_general.py` and `python3 verify_sunlet.py` using the standalone files in this package. Compare standard output byte-for-byte with `verification_general_output.txt` and `verification_sunlet_output.txt` respectively. Only the standard Python library is used.

`verify_general.py` enumerates all simple labeled graphs on three, four and five vertices; it retains exactly those for which every vertex deletion leaves a connected graph (249 graphs in total) and checks a further 220 deterministic pseudorandom two-connected examples at orders six, seven and eight. For each, the code constructs the actual leaf corona, runs breadth-first-search distances, enumerates all allowable graph-geodesic triples, and computes first homology over the two-element field. Its independent equidistance count must match the predicted rank.

`verify_sunlet.py` constructs the cycles directly and independently checks all-pairs geodesics, all permissible triangles, the complete first-homology rank over fields of characteristics 2, 3 and 5 through order fourteen, and over characteristic 2 for four larger cycle lengths. It also checks the exceptional-edge criterion and one-root leaf-link connectivity.

These computations do **not** establish the nonabelian fundamental group in general, do not assert integral torsion-freeness, and do not resolve all graphs at untested orders. Those conclusions are obtained in the mathematical proof by cone attachment and van Kampen. No external or independent validation is asserted.
