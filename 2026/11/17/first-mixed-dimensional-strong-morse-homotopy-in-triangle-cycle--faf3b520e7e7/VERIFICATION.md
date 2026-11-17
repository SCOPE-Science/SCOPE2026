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

# Verification of the finite homotopy classification

Run `python3 check_sm_mixed.py` using Python 3 standard library only. The source deterministically reconstructs both the graph and the complex for each \(n=3,4,5,6\), with full nonempty face counts \(36,104,292,764\). It checks two independent enumeration traversals of all vertex orderings; verifies acyclicity on the **entire** face-poset Hasse digraph; calculates integral signed Morse differentials via recursion over matching paths; and independently calculates simplicial mod-two Betti ranks from full boundary matrices. The exact certification orders are embedded in `CERT_ORDERS`. All four cases pass, including the complete zero integral \(2\times11\) Morse matrix at \(n=6\).

The file `verification_output.txt` is the recorded executable output for precisely the embedded source; no older-run certificates or unexamined paths are used. The proof of the finite statements is mathematical exhaustion, not statistical extrapolation. This verification does not establish results for \(n\ge7\), or certify that no unpublished equivalent treatment exists. Independent mathematical validation has not been performed.
