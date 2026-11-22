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

Actual code is supplied as three separate standalone Python 3 standard-library scripts, with matching captured `.log` files.

`verify_even_motzkin.py` exhaustively checked the two target conserved occupancy sectors for each even \(n=4,6,8,10,12\). The exact last-entry populations per sector were respectively \(8,48,336,2540,20040\). Every candidate at mass \(n-1\) satisfied the exceptional-peak iff penultimate nonrecurrence criterion, with at most one exceptional peak. The independent transfer-meander Motzkin identity was checked for eighteen consecutive lengths. `verify.py` separately checked all \(88,572\) labelled configurations at lengths one through ten and the max-plus height identity at \(22,245\) time slices. `verify_independent.py` checked the full recurrent-by-mass spectrum through length nine, and confirmed local ternary rule number `6171534259461`.

The proof in RESULT.md establishes the result for all even lengths. No finite enumeration, test log or numerical limit is asserted to prove its infinite generalization. The classical traffic phases have prior literature support, and this artifact has no independent scientific audit.
