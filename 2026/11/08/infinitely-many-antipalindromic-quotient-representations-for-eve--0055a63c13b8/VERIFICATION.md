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

# Computational reproducibility

Run `python3 verify.py` with ordinary Python 3. The program uses no external packages and verifies all block identities and exact integer products for `r=2..30` and `t=1..20` (580 independent parameter pairs), including actual binary reverse-complements and bit lengths. Its recorded stdout is in `verification_output.txt`. The proof, not the finite tests, establishes all integer parameters `r>=2,t>=1`.

The visible check covers only a finite region and is not an independent scientific audit.
