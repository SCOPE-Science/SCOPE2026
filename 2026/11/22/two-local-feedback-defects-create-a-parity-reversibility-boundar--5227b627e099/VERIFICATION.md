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

# Verification

The exact proof rests on the polynomial two-generator presentation, parity evaluation, elementary Smith decomposition, and characteristic-two Fibonacci doubling identities in `RESULT.md`. Checks below are exact integer and binary-polynomial arithmetic, not floating-point approximations or a substitute for the universal proof.

From the directory containing both scripts, run `python3 verify_transfer.py` then `python3 verify_direct.py`. The first checks the closed characteristic polynomial, monodromy Smith factors, determinant parity, and nilpotent-family examples for 1,023 placements with ring lengths 3 through 64. The second constructs the actual bit-matrix update independently, checks predicted fixed-iterate kernel dimensions for 80 placements with lengths 3 through 18, exhaustively verifies all initial states through length 10, and directly checks sharp nilpotence at lengths 7, 9, 15, and 17.

Observed output: `TRANSFER PASS: 1023 ...` and `DIRECT PASS: 80 ...`. No checking of all ring lengths was attempted computationally; the two infinite families and general exact formula are mathematical assertions proved in the result. External validation was not performed.
