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

## Verification performed

The proof has four steps: a fixed-offset branching recurrence, a count of offset regimes, a constructive golden-mean embedding when \(\beta<1\), and use of the cited exact endpoint entropy. The step with the greatest logical risk is allowing an arbitrary starting history; a real-offset sweep and its finite critical thresholds are included explicitly, so no uncountable union is taken at exponential cost.

The standalone `entropy_plateau_check.py` enumerates all binary words through length \(14\) for \(p=1/5,2/5,499/1000,1/2,2/3\). For each value, the program checks feasible-offset word counts and the polynomial-Fibonacci bound, counts all paths at one fixed offset and tests the Fibonacci recurrence, and for \(p<1/2\) embeds each golden-mean finite word after an explicit negative-drift prefix. It also reports the entropy constants. The program completes with `PASS` under a standard Python interpreter.

## Limits

Finite computations do not establish the all-parameter or infinite-length assertions. Those follow from the written combinatorial proof. The value at \(p=1/2\) is cited from Reyes, Theorem C(c), rather than independently reproved. No full historical access to Becker–Baraviera (2023), no claim about \(p>1/2\) exact entropy, and no independent audit are asserted.
