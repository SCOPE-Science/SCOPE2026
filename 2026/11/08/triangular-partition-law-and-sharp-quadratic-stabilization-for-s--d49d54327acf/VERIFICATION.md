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

# Reproducing the exact enumeration checks
Run `python3 verify_scattered001.py` under Python 3 with only the standard library. Expected result:

`PASS direct=280; independent_dp=735; eventual_quadratic=240; sharp_preboundary=40`

The first checker directly constructs all binary words of lengths 0 through 13, counts each scattered 001 occurrence using zero-pair accumulation, and compares 280 fixed-(n,k) counts. The second independently evolves a transition-count dynamic program to length 48, comparing 735 (n,k) cases. The third compares the algebraic quadratic to exact coefficient extraction at and above its claimed onset for 40 distinct positive occurrence counts and checks the immediately preceding one-unit discrepancy. The symbolic gap decomposition and maximal-core inequality provide the proof for arbitrarily large parameters; these finite tests are corroboration and do not establish infinite exhaustiveness.

Scientific scope: positive occurrence counts, indexed binary linear words, scattered subsequences. Historical priority not independently certified. No external mathematical audit was performed.
