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

The `verify.py` script uses Python 3 standard library only. Run from the directory containing the files with `python3 verify.py`. It enumerates all cyclic binary words of lengths 1 to 17, tests the shift relation, run condition, and four forbidden factors independently, and compares all resulting counts against trace(A^n) and dual-cubic recurrences for 100 periods. The expected output begins with `PASS: 262142 exhaustively enumerated cyclic binary words`. This is finite corroboration only; algebraic and symbolic arguments in RESULT.md establish the infinite theorem. No external or independent audit has been conducted.
