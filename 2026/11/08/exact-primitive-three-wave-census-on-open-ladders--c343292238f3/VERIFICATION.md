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

# Verification details

`verify_transfer.py`: Python standard library; computes all 27 normalized states and the integers in the proof's component table, then checks the polynomial identity exactly, with additional recurrence tests through rung length 71. The identity is the infinite-range proof certificate.

`verify_direct.py`: independently implements the synchronous rule on all vertices, enumerates every configuration for lengths two through six (597861 states in total), checks the third iterate and nonfixedness, and independently counts valid successor-color configurations using an unnormalized 81-state transfer through rung length 30. Neither program consults precomputed files or a previously saved ledger.

To reproduce: run `python3 verify_transfer.py` and `python3 verify_direct.py` from the same directory. Their exact captured outputs are in `transfer.out` and `direct.out`. Both program files and their output hashes are embedded alongside this document. The full infinite theorem depends on the componentwise transfer identity and the local periodicity reduction, not on the finite dynamic enumeration.

Limitations: the programs test only the exact finite cases specified; they do not provide any external or independent scientific audit. The literature originality comparison is incomplete for the 1980 Greenberg–Greene–Hastings full text.
