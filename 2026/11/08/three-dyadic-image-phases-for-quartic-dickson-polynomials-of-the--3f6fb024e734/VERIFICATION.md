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

The proof in `RESULT.md` uses the odd-unit square theorem, explicit isometries of \(2\)-adic balls, a normalized square-coordinate isometry, and elementary finite-level counting. It proves the complete image for all odd \(2\)-adic parameters and the fiber formulas for every specified exponent.

Execute `python3 verify_e4.py` from the package's directory using Python 3.8 or later. The program enumerates all target fibers modulo \(2^k\) for \(5\le k\le13\) and odd \(1\le a\le31\), and checks exact predicted preimage counts, image counts, and square-root counts. Its expected success line is `VERIFY_OK targets=261632 k=5..13 odd_parameters=1..31`.

The finite checks do not establish the infinite-level result, and historical priority has not been independently certified.
