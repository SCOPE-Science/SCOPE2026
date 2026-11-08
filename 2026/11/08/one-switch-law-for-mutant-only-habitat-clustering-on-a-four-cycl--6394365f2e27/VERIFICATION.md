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

# Verification of the mathematical identities

The supplied `verify.py` is a standalone exact checker requiring Python 3 and SymPy. Run `python3 verify.py` from the directory containing this file. Its run returned `PASS: 77 exact assertions; symbolic 8/7-orbit identities and independent 14-state solutions`.

The script independently constructs the complete birth–death first-step equations, with absorbing all-resident and all-mutant states. It verifies orbit partitions, obtains fixation formulae by exact symbolic matrix inversion, checks their rational difference against the stated factorization, and reconstructs the full 14-state system at seventeen rational parameter pairs. It also checks the cubic and diagonal algebra, the isothermal limit and explicit rational examples. The positivity of the denominator and uniqueness of positive roots are analytical deductions presented in RESULT.md; finite checks do not purport to certify all parameter values by enumeration.

The verification is a reproducible check of the finite-state symbolic identity and a self-review of its implications. No independent audit or expert certification is asserted.
