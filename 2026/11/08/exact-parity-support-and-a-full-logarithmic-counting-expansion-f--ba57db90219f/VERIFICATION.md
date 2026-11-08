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

# Reproducibility and mathematical limitations

Run `python3 verify_parity.py` using the standard Python 3 runtime. `verify_output.txt` is the actual output of this checker and can be reproduced without packages or network access. The checker independently implements: (1) \(16\)-regular partition dynamic programming modulo two, (2) triangular-number pair counts modulo two, (3) prime-exponent characterization by a sieve, and (4) direct signed ordered two-square counts. All calculations are exact integers.

The checker covers \(0\le n\le5000\) for the three coefficient tests and \(0\le n\le400\) for the representation identity. These finite checks are not a proof of the all-index result or of the asymptotic expansion; see RESULT.md for the complete arguments and the use of classical external theorems. In particular, no machine calculation certifies prime-number-theorem error bounds. Self-review verified the displayed algebra and the saved code and output; no independent audit was performed.
