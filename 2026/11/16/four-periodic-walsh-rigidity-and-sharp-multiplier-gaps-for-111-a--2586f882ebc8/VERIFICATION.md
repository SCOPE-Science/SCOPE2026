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

# Verification of the finite and symbolic checks

Run `python verify.py` in a directory containing the included script. The script uses only the Python standard library. It first verifies the exact integer matrix identity `M(-1)^4 = I`, the congruences `M(1)^4 = I mod 2` and `M(1)^8 = I mod 4`, and the even coordinate-incidence checks through dimension 34. It then compares independent direct Walsh–Hadamard and signed-transfer computations of **all coefficients** in every dimension 1 through 16. Finally it verifies extremizing sign vectors in additional dimensions 17–24 and 97–100.

The expected terminal line is `TRIBONACCI_CUBE_WALSH_PERIOD_FOUR_PASS`, and the complete output is embedded as `verification_output.txt`.

The finite computation cannot certify the infinite statement by itself. Its proof is the symbolic matrix argument in RESULT.md. The program does not compute the exact nullity for every singular dimension or Banach-space endpoint norms. Independent mathematical validation has not been performed.
