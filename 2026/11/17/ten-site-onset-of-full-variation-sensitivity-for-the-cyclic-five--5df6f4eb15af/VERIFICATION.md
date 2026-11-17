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

The exact witness checker is `checks/median_five_cycle.py`, run with `python checks/median_five_cycle.py`. It directly reconstructs the finite input pair \(b=a+\frac14h\), takes the median of five cyclic coordinates using Python's exact `Fraction` arithmetic, and verifies \(V_n(M_nb-M_na)=5V_n(b-a)\) for each of the ten listed witnesses (\(10\le n\le19\)) and multiple lengths of the uniform tail construction. It also independently checks the local five-crossing combinatorial bound in randomly generated selection chambers.

The proof of the global upper bound and the dimension obstruction is analytic. The finitely tested larger lengths do not replace the uniform two-gadget argument. All historical-priority claims remain provisional; independent audit has not been performed.
