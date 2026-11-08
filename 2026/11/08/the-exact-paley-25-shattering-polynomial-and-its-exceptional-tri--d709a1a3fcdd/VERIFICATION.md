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

The included file `paley25_verify.py` is the complete exact finite certificate. Run `python3 paley25_verify.py` on an ordinary Python 3 interpreter. It uses only standard-library `itertools` and `math` and asserts (i) all field residue counts, (ii) direct versus bitset shattering for zero-containing supports at sizes 1–4 in each of five fields, (iii) the full 12,650-support four-set census over F25, (iv) all 2,300 triples and the exact 100-element square-equilateral exception set, (v) closure and partition into eight group orbits, and (vi) first-order dimensions for P5/P9/P13/P17. On success it prints `PALEY25_SHATTERING_PASS` with all profiles. This is fully exhaustive for the stated finite cases but not independent external audit; no claim concerning higher field orders or closed neighborhoods is checked.
