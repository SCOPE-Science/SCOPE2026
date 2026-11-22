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

# Verification of the cyclotomic GCD classification

The standalone script `check_degree_six.py` was executed with Python 3 without third-party packages. It verifies the exact Sylvester determinants \(53824\) and \(253783\); the complete finite lists of common roots modulo \(29,19,37\); all Hensel lifting digits and their incompatibility; all four direct integer GCD formulas at all \(20387\) residue classes; and the eight asserted histogram entries. It also tests negative arguments. The script's output is:

```
RESULTANTS: m=7: 53824 = 2^6*29^2; m=9: 253783 = 19^3*37
ALL COMMON MOD-p ROOTS AND UNIQUE LIFT DIGITS VERIFIED; NO COMMON MOD-p^2 LIFTS
ALL 20387 RESIDUES, FOUR INDICES: DIRECT GCD FORMULAS VERIFIED
AGGREGATE COUNTS: [(1, 11375), (19, 5250), (29, 1820), (37, 650), (551, 840), (703, 300), (1073, 104), (20387, 48)]
SHARP MAXIMUM: 20387, AT n=8839 MOD 20387
```

The infinite statement is proved by the exact resultant, modular root, lift, reflection and Chinese remainder arguments in `RESULT.md`. The residue sweep is a corroborating check and is not the justification for the absence of prime-square divisors at arbitrary integer arguments. No external independent audit or formal verification has been carried out.
