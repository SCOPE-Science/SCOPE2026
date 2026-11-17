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

The mathematical proof relies on (i) explicit half-circle flows and the identity \(P=f^2\); (ii) the strict \(n\)-lap Chebyshev crossing geometry; (iii) fixed points of every inverse-word branch via the intermediate value theorem; (iv) saturation of the polynomial-degree bound and root simplicity; (v) Möbius inversion and the doubled-period exclusion of multipliers \(-1\); and (vi) persistence of simple critical points under polynomial-coefficient perturbations. Those arguments apply simultaneously to all integers \(n\ge2\), \(k\ge1\), and all \(\delta>0\).

The included `checks/verify.py` needs Python 3 and `sympy==1.14.0`, listed in `requirements.txt`. It performs exact-rational Sturm root counts and simplicity checks at three finite instances and numerical high-precision diagnostic checks of several Chebyshev critical values. Execute `python checks/verify.py`. These computations do not independently prove an infinite statement or constitute an independent external mathematical audit.

The claims exclude singular-switch, nonalternating, and general different-center trajectories; the full hybrid orbit classification is not asserted. Source overlap comparison is based on inspected named results and full text when accessible, not a guarantee of bibliographic uniqueness.
