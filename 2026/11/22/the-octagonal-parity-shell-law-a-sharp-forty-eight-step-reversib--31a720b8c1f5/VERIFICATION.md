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

# Verification

The two standalone scripts are executable with Python 3 alone:

```
python3 check_shell.py
python3 check_polynomial.py
```

Both output `PASS` on the actual embedded source. `check_shell.py` reconstructs the exact nine-shell matrix, verifies its rank/minimal-polynomial conditions, constructs the eighteen-dimensional reversible wave matrix, and independently calculates all ten divisor return-space dimensions and primitive populations. `check_polynomial.py` uses an independent binary-polynomial quotient representation and a Fibonacci-type matrix-power recurrence, comparing full kernel eliminations with the proposed rank formula.

A passing test means the algebra of the radial quotient and the formulas for its temporal module have been checked. It is not an exhaustive computation on a complete Ree–Tits incidence graph. The geometric recurrence itself is proved symbolically from girth sixteen, diameter eight, odd local degrees and unique geodesics below the antipodal shell. No stochastic experiments, guessed rank values, independent audit or physical-network assertions are used.
