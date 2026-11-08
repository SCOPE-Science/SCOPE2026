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

# Reproducibility checks

Run `python3 stretched_tm_gap_verify.py` with Python 3. The program generates the four 64-symbol Thue–Morse superblock pairs, reconstructs gap contexts of six consecutive marker symbols, derives the exact signed threshold and palindromic signature lists, and asserts the displayed piecewise spectrum against independently extracted factors for parameters 1 through 9. The program reports `STRETCHED_TM_GAP_VERIFY_OK 306 cases; symbolic signatures 14 8`. It additionally checks arithmetic evaluations at parameters 20, 51, 100 and 1000.

The proof is the finite context-exhaustion and exact inclusion–exclusion reduction in `RESULT.md`; numerical tests alone would not prove the universal theorem. No claim of independent audit or formal theorem certification is made.
