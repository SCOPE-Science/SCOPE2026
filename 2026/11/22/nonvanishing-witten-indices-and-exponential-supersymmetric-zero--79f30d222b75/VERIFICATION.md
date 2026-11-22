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

# Verification and scope

The finite-state proof uses a 27-by-27 signed transfer matrix with states consisting of three consecutive column choices. Its exact characteristic polynomial is verified symbolically; the two nonzero factors are \(z^2-z+1\) and \(z^5-z+1\). Each closed transfer walk corresponds to exactly one independent set of \(\mathrm{GP}(n,3)\) for \(n\ge7\).

`verify_transfer.py` checks the determinant and the eighteen initial index values for \(7\le n\le24\), then isolates all quintic roots into rational boxes that prove modulus separation, nonvanishing and exponential lower growth. `verify_graph.py` independently implements the signed independent-set deletion recurrence on explicitly constructed graph adjacency masks for \(7\le n\le14\); it does not use the transfer matrix. Both programs executed successfully on the file contents included in this package.

This evidence proves the Witten index and a lower bound on total zero-energy multiplicity, not the complete cohomology or exact number of ground states. It is not an independent mathematical audit, and no formal theorem-prover certificate is asserted.
