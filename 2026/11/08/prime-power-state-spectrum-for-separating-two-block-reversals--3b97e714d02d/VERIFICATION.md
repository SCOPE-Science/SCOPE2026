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

# Verification of the separation formula

Run `python3 checker.py` using Python 3 with no third-party dependencies. The program independently computes every permutation and power evaluation at degrees one through five for all \(24\times24\) exponent pairs, as well as nine degree-six boundary pairs. It checks that noncommuting powers exist exactly when the proposed minimum does not exceed the tested degree. It separately verifies the primality-power condition for the least nondivisors of all integers from one through 19,999.

Replay outcome: `PASS: all 2889 symmetric-group cases and 19,999 arithmetic cases`.

The infinite result rests on (i) the equivalence between permutation-word separation and noncommuting powers, (ii) nontrivial power-generated normal subgroups of \(S_n\) containing \(A_n\) for \(n\ge5\), (iii) the explicit low-degree normal-subgroup tables, and (iv) the minimal-nondivisor argument. None of these general steps is justified solely by finite enumeration. No exhaustive historical-priority or independent mathematical audit has been performed.
