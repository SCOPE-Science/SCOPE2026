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

The theorem is proved symbolically in `RESULT.md` by a kernel-rank reduction and a census of alternating-form restrictions to subspaces. Computation is an independent finite corroboration, not an infinite certificate.

The embedded standalone `verify.py` recomputes direct weighted adjacency ranks by elementary row operations and compares them with the closed transfer. Its companion `verification_output.txt` records the exact outcomes of ten complete finite-field cases, including the \(K_{2,2,2}\) graph over \(\mathbb F_2\) and \(\mathbb F_3\). It separately verifies the Gaussian subspace-partition identity for every admitted dimension through six over fields of orders two, three and four. The test of the four-element field uses \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\).

All reported tests pass. The exact target counts in the table and the general theorem hold for all prime powers by the proof, not because of the finite experiments. No exhaustive test of all graph orders, field sizes, or character representations was performed. The group-theoretic character multiplicity statement invokes the classical class-two orbit method only in odd characteristic.
