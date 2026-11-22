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

# Verification and reproducibility

Run the included standard-library-only Python 3 file `verification.py` using `python3 verification.py`. It reconstructs \(G\) as affine pairs modulo \(N=2^k\), computes all units and exact nonidentity involutions, compares the actual commuting adjacency matrix with the proposed partition for each \(k\) from \(3\) through \(8\), and checks degrees, edges, triangles and explicit maximal-clique candidates. Successful output terminates with `QUATERNION_AUTOMORPHISM_INVOLUTION_GRAPH_VERIFIED`.

The standalone checker uses integer congruences and exact sets, not floating-point sampling. The proof for all \(k\ge3\) is algebraic and independent of the finite checks. Finite checking cannot rule out a failure at untested ranks and does not verify historical priority. All resulting counts and subgroup statements refer to nonidentity involutions of the automorphism group, not to elements of the original quaternion group.
