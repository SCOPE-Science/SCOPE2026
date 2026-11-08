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

Run `python3 verify.py` beside `RESULT.md` and `verification_output.txt`. The checker uses no downloaded data, third-party packages, or external calls. Its recorded output must conclude with `VERIFY_OK`.

The checker exhaustively compares the adjacent-minor map on several finite fields and cycle lengths with the constructive induction; it computes direct quandle products of Fourier basis vectors; it obtains the complete linear span rank of elementary commutators by modular Gaussian elimination; and it constructs a single commutator for each of 80 preselected randomized or structured targets across nine splitting-field test cases. It compares the resulting product in the original quandle basis with the independently computed target.

The mathematical proof, not finite computation, establishes the theorem for all permitted groups and fields. In particular, a finite sample does not establish a statement for all coefficient fields or group sizes. No external or independent audit has been performed.
