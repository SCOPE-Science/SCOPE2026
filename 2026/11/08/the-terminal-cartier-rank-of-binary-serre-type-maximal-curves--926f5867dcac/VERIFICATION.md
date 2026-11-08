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

The proof uses an exact \(Q\)-power decomposition for odd \(n\ge3\), with \(Q=2^{n-1}\). Each basis differential is checked against the unique congruence class modulo \(Q\) that survives Cartier iteration. The only terminal nonzero inputs are those displayed in the theorem; their distinct outputs have even exponents and are killed by one additional Cartier application.

A standalone Python 3 verifier is included as `cartier_terminal_check.py`. Run `python3 cartier_terminal_check.py` to compare the direct \(Q\)-power expansion, repeated one-step Cartier action, and closed-form survivor set for \(n=3,5,7,9,11,13,15\). The checker tests all basis elements in these finite cases and asserts that the next Cartier iteration kills the image. This finite sweep does not independently prove the theorem for all \(n\), for which the written congruence argument is required.

References: Shafighi arXiv:2610.15266 (differential basis and one-step Cartier action), Garcia--Tafazolian doi:10.4064/aa135-3-1 (known maximality vanishing bound). External independent audit has not been performed.
