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

# Verification of the diagonal-rook parity theorem

Run `python3 verify_core.py` and `python3 verify_states.py` from this directory. Both use only the Python standard library. The first constructs matrices over the two-element field, checks the six minimal primary decompositions via nullities of powers of the three coprime primary polynomials, and tests rank sequences, operator identities and all primary signatures on all 100 size pairs \(2\le m,n\le11\). The second constructs labeled undirected rook-plus-diagonal neighborhoods independently and exhaustively classifies all \(2^{mn}\) binary initial states for six core boards, plus all \(4^6\) configurations on the \(2\times3\) board over a four-element field. Recorded outputs appear at `verification/core_output.txt` and `verification/states_output.txt`.

The proof of the unbounded parameter theorem is the explicit invariant tensor decomposition in `RESULT.md`, which reduces all sizes to six core matrices and elementary rank-one maps. Finite tests alone would not prove a statement for all board sizes; the direct state classifications do not test infinite fields or all possible finite fields. Independent mathematical auditing has not been performed.
