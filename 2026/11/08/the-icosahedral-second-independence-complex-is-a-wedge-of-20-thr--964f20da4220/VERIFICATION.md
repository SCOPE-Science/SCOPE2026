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

The finite certificate is `morse_certificate.json`, generated from the explicit pentagonal-belt adjacency. To replay, put that file next to `verify_icosahedron.py` and execute `python3 verify_icosahedron.py` with Python 3. The checker uses no external packages. It checks all subsets, matchings and directed Hasse edges, computes the exact signed Morse boundary, checks a unit integer minor, and computes the mod-two simplicial boundary ranks by a different routine. `verification_output.txt` records the observed output.

The enumerated graph has 12 vertices, 30 edges and 20 triangular faces. The second independence complex has 323 nonempty simplices. The matching has 147 pairs and 29 critical cells: one vertex, four 2-cells and twenty-four 3-cells. The acyclicity test covers all 972 face-poset covering relations. The 24-by-4 signed boundary contains a 4-by-4 unit minor. The original simplicial mod-two boundary ranks are 11, 55 and 85. These computations are exhaustive for this finite complex; no extrapolation to larger graphs is made.

The further claim of integral homotopy equivalence uses the general discrete-Morse theorem, the Hurewicz isomorphisms and Whitehead's theorem applied as detailed in `RESULT.md`. The finite mod-two computation alone is not a proof of this stronger claim. Independent external mathematical audit has not been performed.
