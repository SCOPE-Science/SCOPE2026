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

# Reproducibility and mathematical checks

Run `python3 verify.py` with Python 3.10 or newer. The program requires no third-party packages.

The checker evaluates \(m\), \(q\), \(v\), neutral velocities, \(G\), and all three exact moment equations using arbitrary-precision rational arithmetic for 1,400 nonnegative empirical configurations of size one through fourteen. It then independently evolves eight empirical configurations using Runge–Kutta with a step of \(0.02\) for 72 time units and checks both the invariant and the predicted consensus. The executable prints pass counts when all assertions succeed.

The proof does not depend on simulations: the invariant follows from exact integration of the source's transport drift and the limit follows from \(\dot v=-2mvG\) with \(m\ge m_0>0\) and \(G\ge1/2\). The sharp extremal condition is the pointwise inequality \(x^2\le x\) on \([0,1]\). Tests cannot certify unrelated models, nonzero selection, noise, or a claim of historical novelty.
