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
# Verification and limits

The accompanying `verify.py` and `independent_check.py` are complete standalone Python standard-library programs. Run each under Python 3.8 or later. They recompute the eight radius values, factor counts and all explicitly exhibited lower witnesses. The first constructs the Thue–Morse prefix with the bitcount formula; the second constructs the relevant factors through substitutions \(\mu^h(ab)\), and separately computes witness bits by digit parity. All tests passed in the assembled source files.

The finite-to-infinite bridge is independently mathematical: \(\mu^3(0)=01101001\) contains all four adjacent binary pairs, so \(\mu^{11}(0)\) contains all occurrences of \(\mu^8(ab)\) needed to represent every infinite Thue–Morse factor of length at most \(256\). Every factor checked is of length at most \(130\). Thus all infinite starting positions are genuinely covered. The witness checks give matching lower bounds.

No claim outside \(3\leq k\leq10\) has been verified. Neither program performs historical-priority validation or external independent certification.
