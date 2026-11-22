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

# Finite checks and theoretical boundary

Run `python verify.py` with Python 3.10 or newer. The script performs exhaustive polynomial-ring arithmetic for \(\mathbb F_2[t]/(t^k)\), for \(k=1,2,3\), and exhaustive characteristic-four-field arithmetic for \(\mathbb F_4\). Each case enumerates all determinant-one summands, all ordered pairs, and all additive targets, checking the exact claimed minimum, residue-rank equality criterion and valuation-stratum estimates. Five specified targets over \(\mathbb F_4[t]/(t^2)\) are additionally checked by enumerating every first summand and solving for the second. `verify_output.txt` records the exact console output with `VERIFY_OK` and `VERIFY_DUAL_OK`.

This is a finite check, not a proof for unrestricted \(q\) or \(k\). The arbitrary-ring proof in `RESULT.md` uses reduction of a determinant trace equation, smooth lifting along successive square-zero ideal quotients, and explicit residue-field conjugacy-class counts. No external theorem-prover certification or independent mathematical review was undertaken.
