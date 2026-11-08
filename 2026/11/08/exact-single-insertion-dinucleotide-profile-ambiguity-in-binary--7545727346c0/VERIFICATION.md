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

## Executable checks

Run `python3 verify_direct.py` in the directory containing this file. It enumerates all binary source words of lengths 1 through 16; generates inserted **words** at every position using both symbols; collects distinct **linear adjacent-pair multiplicity profiles**; checks the five-indicator pointwise formula for every source word; verifies all four Fibonacci–Lucas enumeration formulas; and checks the four length-five extremizers. Observed result: PASS.

Run `python3 verify_structural.py` in the same directory. It verifies the transfer-matrix trace formula by independent matrix multiplication and exhaustive word enumeration through length 16, and separately checks that any word exhibiting six deletion profiles also exhibits six insertion profiles through length 12. Observed result: PASS.

Representative observed distributions \((C_3,C_4,C_5,C_6)\): length 4 gives \((2,6,8,0)\); length 5 gives \((0,16,12,4)\); length 6 gives \((2,18,34,10)\); length 9 gives \((0,88,260,164)\); length 16 gives \((2,2438,33056,30040)\).

## Analytical limits

The indefinite-length statements are proved by a complete enumeration of the six possible local profile-change vectors, a two-state integer transfer matrix for equal endpoints avoiding repeated zeros, and inclusion–exclusion; the finite tests are confirmation, not a replacement for those proofs. The results exclude multiple insertions, nonbinary alphabets and cyclic profiles. Scientific historical-priority review has not been performed independently.
