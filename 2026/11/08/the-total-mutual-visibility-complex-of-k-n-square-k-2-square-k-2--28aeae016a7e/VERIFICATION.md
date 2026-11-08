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

Run `python3 verifier.py` from a directory containing this exact standalone script. It uses only the Python standard library and constructs \(G_n=K_n\square K_2\square K_2\) directly. The program independently derives forbidden pairs from common-neighbor sets for distance-two endpoints, enumerates the feasible complex for \(2\le n\le6\), checks exact face and facet polynomials, and computes every fixed-size token-jumping component count on these instances.

For \(2\le n\le4\), it additionally checks every one of the \(2^{4n}\) possible subsets against the structural classification; for \(n=2,3\), it independently tests every subset against existence of unobstructed shortest paths between *every* ordered endpoint pair (endpoints are permitted to lie in the selected set). The binary chain-complex ranks for \(n=2,3,4\) agree with the wedge homotopy formula. The homotopy equivalence for general \(n\) is proved by identifying two joins of zero-spheres and attaching \(4n\) one-cells, not by extrapolation from finite homology.

The last successful program output in the reproducibility session is:

```
VERIFY_OK n=2..6 total_faces=2253 exact_enumerators=PASS maximal_spectrum=PASS exhaustive_masks_n2..4=PASS mod2_homology_n2..4=PASS direct_shortest_paths_n2..3=PASS all_token_jumping_components=PASS
```

These calculations do not establish independent mathematical validation or publication priority.
