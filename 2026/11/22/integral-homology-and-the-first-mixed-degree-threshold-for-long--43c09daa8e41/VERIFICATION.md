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

The bundled `check_homology.py` exhaustively constructs the full-cycle generating words and all faces for each alphabet size from two through six. It performs exact signed integer-boundary calculations and unit-pivot chain contractions, checks that all remaining differentials are identically zero, and independently checks modular ranks using primes 2, 3, and 101. The supplied `CHECK_OUTPUT.txt` records a complete fresh replay; the script is authoritative and directly reproducible. A modular rank check by itself cannot establish absence of integral torsion; the exact unimodular reductions establish this. The results make no claim about larger alphabet sizes. Independent mathematical validation is not yet performed.
