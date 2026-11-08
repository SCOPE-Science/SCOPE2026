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

The standalone standard-library program `verify_cube_plaquette.py` enumerates all perfect matchings of the 2-, 3-, 4-, and 5-dimensional hypercubes in two distinct ways, using least-unmatched-vertex recursion and reversed even-vertex bipartite assignment respectively. It compares the complete square-flippability histograms, enumerates all square-flip edges in the four-cube, performs an exhaustive connected-components traversal, and checks the exact four-base witness and complete eight-base disjointness condition. The program terminates with `VERIFY_OK` upon successful checking. These finite checks certify their exhaustive domains only. The general lower bound is justified separately by a product-layer proof in `RESULT.md`; no computational experiment is presented as an infinite proof. No independent audit has been conducted.
