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

# Verification details

Run `python3 verify_excited.py` from the extracted package. It independently exhausts every edge subset of the underlying complete graphs \(K_5\) and \(K_7\), giving ground/first-excitation degeneracies \((45,170)\) and \((420,5250)\). It independently evaluates the path/cycle defect-class formula and its simplification for each odd \(n\) from 5 through 35, inclusive, and checks selected larger exact values.

The exhaustive finite tests confirm the finite cases only. The general identity rests on the graph-degree energy reduction, parity, and bijective path/cycle enumeration in RESULT.md. The correction term is controlled only at fixed finite \(n\); no joint temperature/order limit is verified.
