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

# Verification and limits

The proof is algebraic; it does not depend on finite enumeration. For a positive least-period-two candidate, relabel so that \(0<x_0<x_1\) and write \(s=x_1/x_0>1\). Direct substitution into the two prey equations yields \(\Delta y=(s-1)(1+s^{-1}-x_0)>0\). The predator equations imply ordered positive growth multipliers with product one, so \(\Delta y<0\), contradiction. The two coordinate axes and the equal-prey case are addressed separately in the main proof.

The accompanying Python 3 script `verify_period_two.py` reproduces an exact symbolic identity (with SymPy) and evaluates \(7{,}225\) rational parameter/state grid cases (Fractions, exact arithmetic). Command: `python verify_period_two.py`. Observed output:

`VERIFY_OK symbolic_identity=1 exact_grid_cases=7225 exact_parameter_pairs=25`

Finite tests do not establish a universal theorem. The program checks only a finite grid and one symbolic identity, not exhaustive real-parameter dynamics. Independent scientific audit has not been performed.
