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

Execute `python3 verify.py` in a directory with `CENSUS.json`. The checker uses only standard Python integers, permutation tables, sets, elementary free-face collapse operations and finite graph traversal. It checks the full 336-element automorphism group, closure of all 413 subgroups, the partition into 23 conjugacy classes, the exact fixed-orbit simplicial model, the validity of every collapse pair, the vertex links of every claimed two-sphere, and all six nonidentity class-weighted counts. The output is in `verification_output.txt`.

The mathematical proof also uses elementary facts: a connected closed triangulated two-manifold of Euler characteristic two is a sphere; a connected finite graph has first Betti rank equal to edges minus vertices plus one; gluing two spheres along a filled triangle yields their wedge up to homotopy. The exhaustive check applies only to the fourteen-vertex incidence graph. It does not constitute independent verification or show that no prior equivalent publication exists.
