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

# Verification of the adjacency-code theorem

The symbolic proof in `RESULT.md` establishes the theorem uniformly. The finite computation is a cross-check, not a certificate of the infinite assertion.

Run `python verify_adjacency.py` with Python 3 and NumPy installed. The program constructs all nonzero nonunits in \(\mathbb F_q[u]/(u^\ell)\) for \(q=2,3,4,5\), uses actual quotient multiplication to test every unordered vertex pair, and then reduces the resulting simple adjacency matrix over \(\mathbb F_p\). It independently checks rank, rank of the square (hence hull dimension), the proposed kernel and rowspace generators, and all possible weight-one supports.

The fourteen tested cases have \(q=2\) and \(\ell=3,4,5,6,7,8\); \(q=3\) and \(\ell=3,4,5,6\); \(q=4\) and \(\ell=3,4\); and \(q=5\) and \(\ell=3,4\). The program finishes with the exact status `VERIFY_OK configurations=14 direct_ring_multiplication=yes rank_hull_code_dual_weight_one_checks=yes`, recorded in `verification_output.txt`.

For \(q=3,\ell=4\), the direct graph gives rank nine, squared rank eight, and eight weight-one coordinate supports. For \(q=2,\ell=8\), it gives rank sixteen, squared rank fifteen, and nine weight-one supports. The finite tests cover neither every residue prime power nor mixed-characteristic chain rings; those cases are handled by the ideal-count argument in the proof. Independent mathematical audit: not performed.
