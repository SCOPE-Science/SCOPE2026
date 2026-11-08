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

# Verification

The standalone `verify_crown_gt.py` checker was executed directly with Python 3 using only its standard library. For each integer \(n\) from \(4\) to \(8\), it constructs \(K_{n,n}-M_n\), computes shortest-path distances by breadth-first search, enumerates all simple paths of length at most three, and tests whether a path is maximal by searching for a geodesic extension at each endpoint.

It then exhaustively tests all \(2^{2n}\) selected-vertex masks using the actual maximal-geodesic incidence masks; inclusion-minimality is tested by deleting each selected vertex. The resulting all-transversal and minimal-transversal coefficient counts are compared with independent polynomial expressions. Finally, an explicit family of \(\lfloor n/2\rfloor\) disjoint maximal geodesics is checked against the constructed paths.

Actual execution output:

```
VERIFY_OK orders=4..8 maximal_geodesics=750 all_subsets=87296 transversals=13403 inclusion_minimal=566 independent_BFS=PASS all_polynomials=PASS minimal_families=PASS packing_construction=PASS
```

The computed number of maximal geodesics at order \(n\) agrees with \(n(n-1)(n-2)\). Minimal cardinality histograms are \(\{3:8,4:12\}\) at \(n=4\), \(\{4:10,5:20,6:10\}\) at \(n=5\), \(\{5:12,6:50,8:15\}\) at \(n=6\), \(\{6:14,7:112,10:21\}\) at \(n=7\), and \(\{7:16,8:238,12:28\}\) at \(n=8\).

Limits: exhaustive computation does not prove the formula beyond tested orders, and no external or independent mathematical audit has been performed. The analytical argument in `RESULT.md` supplies the unrestricted proof.
