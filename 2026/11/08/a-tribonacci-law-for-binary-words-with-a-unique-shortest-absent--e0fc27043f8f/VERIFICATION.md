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

`verify.py` performs literal set-of-absent-subsequences testing on all nonempty binary words through length \(12\), checks membership in the recursive grammar and compares each universality-index coefficient. It printed `DIRECT_GRAMMAR_VERIFY_OK`.

`verify_fast.cpp` performs an independently written shortest-absent dynamic program over first occurrences for every binary word through length \(22\). It compares every length/index coefficient against the recurrence \(U_{n,k}=U_{n-1,k}+U_{n-2,k-1}+U_{n-3,k-1}\) with \(U_{1,0}=2\), where absent entries are zero. It printed `DYNAMIC_CENSUS_VERIFY_OK`.

Commands: `python3 verify.py` and `g++ -std=c++17 -O3 verify_fast.cpp -o verify_fast && ./verify_fast`.

The all-length identity relies on the displayed first-occurrence proof; finite tests do not certify infinitely many lengths. No external independent scientific audit has been performed.
