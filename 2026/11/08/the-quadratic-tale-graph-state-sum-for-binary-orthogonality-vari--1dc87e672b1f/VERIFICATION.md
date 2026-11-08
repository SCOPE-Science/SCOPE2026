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

# Reproduction

Run `python3 verify_graph_frames.py` from the directory containing this file. It computes independent brute-force vector assignment counts over odd prime fields for 57 graph/field cases with at most four vertices, checking against the closed state sum. It checks 380 complete-graph polynomial identities for both splitting signs. It produces the exact marker lines

```
DIRECT_LABELED_GRAPH_ENUMERATIONS_OK 57
COMPLETE_GRAPH_SPECIALIZATION_OK 380
UNRESTRICTED_RESULT_FROM_PROJECTIVE_LINE_SUPPORT_STRATIFICATION
```

The first test enumerates actual assignments and checks orthogonality edge-by-edge; the second verifies polynomial specializations. Neither is an infinite proof. The general proof is the projective orthogonal-complement involution, bipartite/nonbipartite propagation, and locally trivial line bundles in `RESULT.md`. The arithmetic passage uses the two Frobenius eigenvalues on the isotropic-line scheme. No external proof certificate or independent mathematical audit is asserted.
