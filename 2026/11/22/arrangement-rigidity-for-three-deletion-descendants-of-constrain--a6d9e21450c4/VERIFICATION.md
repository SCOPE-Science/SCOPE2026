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

# Reproducibility and scope

Run `python3 verify.py` from the folder containing the supplied checker. It requires only the Python standard library. Expected output begins `VERIFY_OK` and reports 612 exhaustive admissible words and 15 Fibonacci depths.

The first check literally enumerates all sets of three deleted positions for every word beginning `10` and avoiding `00` and `111` at lengths three through twenty, deduplicates outputs, and compares their sizes to the exact formula. The second check uses an independent earliest-embedding subsequence automaton to count distinct length-\(|w|-3\) outputs for finite Fibonacci words through depth seventeen, comparing that count both with the run theorem and with the closed Fibonacci formula. These finite checks are corroboration only; the arbitrary-length proof is the run-by-run recurrence and algebra in `RESULT.md`.

No independent mathematical review or external certificate is claimed.
