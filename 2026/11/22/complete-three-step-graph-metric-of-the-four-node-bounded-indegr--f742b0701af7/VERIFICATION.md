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

# Exact verification

Run `python imset_verify.py` in the same directory as `imset_certs.json`. The verifier uses only Python 3 standard-library integer arithmetic, reconstructs all characteristic-imset vectors from 729 ternary potential-edge configurations, checks 443 legal DAGs and 150 distinct imsets, and checks all 11,175 classified vertex pairs via exact certificates. Each edge gets a strict integer separation on an exposed coordinate face (or has no other vertex in that face). Each nonedge gets an explicit positive integer midpoint decomposition excluding the endpoints. BFS from every vertex checks the exact distance census, the radius, the diameter and the degree spectrum.

The 150 vertices and 2508 edges agree with the published face vector. Floating-point linear optimization helped discover witnesses but is not used in the verification. The finite certificate and its checker are bundled; no externally hosted files or results are required.

The computation concerns exactly the specified finite ten-dimensional polytope. It is not a universal theoretical claim for larger node sets. No independent audit has been performed.
