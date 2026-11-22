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

# Verification record

The complete mathematical proof is included in `RESULT.md`. Independently, `verify_gap_spectrum.py` computes the original three-coin representability predicate by bottom-up dynamic programming, selects multiples of the quotient modulus, and counts every maximal missing interval. It compares the exact histogram and genus to the formulas without using the interval decomposition in the checker.

Executed command: `python verify_gap_spectrum.py`.

Observed output: `PASS 219 parameter pairs gap blocks 6989 missing integers 40685 coin membership positions 2708025`.

The tested domain includes all \(2\le p\le15\), \(1\le k\le15\), plus nine larger-modulus cases. Testing points outside the theorem's scope provides boundary stress tests only, not an expanded claim. The proof establishes the unbounded parameter domain; no finite simulation does. No independent audit or external certification has been performed.
