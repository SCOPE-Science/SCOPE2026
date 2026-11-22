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

# Verification procedure

Use Python 3 to run `python verify.py` in the directory containing this file and inspect `verify_output.txt` as the saved exact comparison log. The script constructs the full two-dimensional tolerance face set for every finite graph in the tested range, constructs the given discrete Morse matching, and independently checks mod-two boundary ranks and critical-cell counts.

The test exhausts all 33,866 labeled simple graphs with 2 through 6 vertices. The directed Hasse acyclicity test exhausts all graphs on 2 through 5 vertices and representative path, star and cycle families up to 12 vertices. The two-independent computational approaches agree in all recorded tests. The general theorem is **not** inferred from finite testing: its proof is the uniform combinatorial gradient-decrease argument, the component-root simplicial retraction and the free-group attaching-map argument given in RESULT.md.

The theorem applies only to one-tolerance of finite simple graphs interpreted as one-dimensional simplicial complexes, with unfilled original graph triangles. No claim is made for higher tolerance or filled flag clique complexes. Independent audit and reproduction outside this package have not been performed.
