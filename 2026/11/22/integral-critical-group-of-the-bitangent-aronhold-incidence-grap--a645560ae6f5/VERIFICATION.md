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

# Verification record
The executable verifier checks exactly \(288\) heptads by two independent constructions, the actual incidence matrix \(B\), and its Gram identity \(BB^{\mathsf T}=56I+16J\). The reduced integer Laplacian has dimension \(315\). For four deleted vertices, the explicit p-adic modular elimination returns \(2\)-adic Smith valuation multiplicities \(\{0:288,4:1,6:26\}\) and \(7\)-adic multiplicities \(\{0:54,1:235,2:26\}\). Valuation sums \(160\) and \(287\) coincide with the independent matrix-tree determinant. The modular precision is \(p^{10}\); no pivot remains unresolved at that precision. Run `python3 verify_critical_group.py` with NumPy installed and `verify_aronhold_octad.py` in the same folder.

The calculation concerns only finite integer matrices. It does not independently verify the entire historical literature, establish unindexed priority, or identify the graph's critical group with a geometric curve Jacobian. Independent mathematical audit is not performed.
