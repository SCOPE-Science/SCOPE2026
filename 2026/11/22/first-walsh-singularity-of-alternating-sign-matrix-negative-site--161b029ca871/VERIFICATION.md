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

The standalone standard-library verifier enumerates the two independent ASM descriptions and the exact Fourier projection data. Execute `python3 verify_asm_negative_support.py`. The output must contain `PASS: two independent ASM generators, exact transforms, orbit and endpoint certificates`. The check includes full integer transform inversion, Parseval, the 24 orbit representatives, direct signed character sums at those representatives, all zero-frequency counts and weight counts, the minimum nonzero gap, and the sharp endpoint kernel sum. The finite enumeration itself, together with the bijection proof in RESULT.md, establishes exhaustiveness for the stated sizes; it does not establish higher-order cases or historical priority.
