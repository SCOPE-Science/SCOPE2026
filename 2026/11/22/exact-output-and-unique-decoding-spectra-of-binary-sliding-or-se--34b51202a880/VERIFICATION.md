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

From the delivered package, run `python3 verify.py` with Python 3.9 or later (standard library only). It exhaustively enumerates binary inputs for every width `h` in 2–6 and output length `m` in 1–10 subject to input length `m+h-1 <= 16`. In each of the 50 cases, it compares: (i) the number of realized outputs with the coefficient of the exact image generating function; (ii) the number of single-preimage outputs with the singleton coefficient; (iii) every non-all-one inverse-list size with the runwise product formula. Expected last line: `ALL PASS 50`.

Independent mathematical auditing, historical-priority verification and extension to noisy or circular measurements have not been performed. Finite checking alone cannot prove universal identities; see the argument in `RESULT.md`.
