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

Two standalone, independently constructed standard-library Python programs were executed.

- `python3 checks/direct_check.py` reported `DIRECT_OK: exact paired-index sets and counts, 1<=m<=15, 0<=r<m`. It checks the exact *sets* of valid starting positions directly from binary zero-run parity against the explicit tile construction, and counts their cardinalities.
- `python3 checks/carry_automaton.py` reported `CARRY_DP_OK: 1830 independently computed cells, 1<=m<=60`. This algorithm uses digit-by-digit addition with carry and two independent zero-run parity states; it never uses the classified paired-index description in its state evolution.

The theorem for every integer \(m\ge1\), \(0\le r<m\) relies on the binary carry-rigidity proof in RESULT.md. No finite experiment proves all infinitely many cases. All exact polynomial and Fibonacci quantities are integers, with no numerical tolerances. Separate independent mathematical auditing has not been performed.
