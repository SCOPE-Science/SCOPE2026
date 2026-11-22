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

Run `python3 check_exact.py` and `python3 check_prefix.py` with Python 3 standard library. The scripts have no external dependencies. Captured stdout appears in `check_exact.out` and `check_prefix.out`.

The exact template program checked 1,161 parameter pairs, alphabets two through ten and lengths one through 129, comparing exact weighted signature dictionaries with the closed formulas. The distinct literal-prefix program checked 140 alphabet/length pairs against prefixes of 131,072 starting positions, with correct supports and maximum frequency error below 0.00000738. The finite-prefix test does not establish the infinite limiting frequency; the arithmetic phase argument proves it. The pivotal quartet-collision lemma and its precise range are spelled out in RESULT.md. A separate independent mathematical audit has not been performed.
