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

`check_local.py` enumerates signed two-gram change vectors for every four-letter context on each alphabet size from 2 through 8, sorts changes by exact symbol support and checks the universal coefficients (2, 14, 24) and zero count. Run using `python3 check_local.py`; the recorded output is `local_output.txt`. The finite-support reduction in RESULT.md converts this bounded exhaustive equality-pattern check into the formula for every alphabet size.

`check_global.py` independently recomputes every adjacent-pair profile from the actual interchanged word, exhausts the binary words of lengths 2 to 8, checks all explicit binary saturation witnesses through length 39, and independently generates de Bruijn witnesses for alphabet sizes 2 to 6. Run using `python3 check_global.py`; its recorded output is `global_output.txt`.

The limiting probability statement is proved with a union bound on missing four-letter factors and independence of disjoint boundary inequalities; it is not extrapolated from experiments. The exact shortest saturation length for alphabet sizes at least 3 and any stronger priority conclusions are not verified. No independent scientific audit has been performed.
