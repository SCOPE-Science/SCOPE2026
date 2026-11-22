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

# Reproducible exact arithmetic checks

Run `python3 formula_validation.py` in the directory containing both source files. The Python script compiles the standalone C++17 cyclotomic-divisibility enumerator, then independently generates the closed rank-by-weight formulas and checks all 2,129,920 sign words of lengths 15 and 21. It compares each weight-specific rank table as well as the global counts. Requires Python 3 and a C++17 compiler. Every finite computation is exact; there are no floating-point rank thresholds.

The source-level all-prime proof in RESULT.md, including mixed-orbit rigidity, is essential. Computations on two moduli do not establish the infinite statement. No independent audit was performed.
