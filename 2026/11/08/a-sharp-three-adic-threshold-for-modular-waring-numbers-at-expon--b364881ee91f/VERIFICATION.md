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

# Verification procedure

Run `python3 verify_local.py` and `python3 verify_composite.py` with Python 3 (standard library only) in the directory containing the files. Concatenate their outputs in that order to reproduce `checks/exact_enumeration.txt`. Both programs have been executed successfully using the actual saved standalone code. The first enumerates all power residues and iterated sumsets for 105 prime-power/exponent cases; the second independently performs breadth-first enumeration at 458 composite or prime moduli.

The complete proof uses cyclic unit groups, a Cauchy–Davenport inequality, a one-variable Hensel lift, and the Chinese remainder theorem. No computer enumeration is used to infer a statement about arbitrary exponents or moduli. Literature originality remains subject to the stated full-text access limitations.
