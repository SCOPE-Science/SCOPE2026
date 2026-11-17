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

# Verification and scope

The statement is proved analytically for all \(0<\varepsilon<1/2\) and all \(x_0\in[0,1]\). The exact scalar formulas arise from solving lower and upper quadratic fixed-point equations and the unique upper-side preimage of the switching point. Exhaustion follows from forward-invariant intervals and the exclusion of upper-branch period-two solutions using the strictly negative discriminant \(b^2(b+1)(b-3)\) for \(2<b<3\).

Run `python verify_discontinuous_logistic.py` from this package in an environment with SymPy installed. The checker verifies rational polynomial identities, the exact threshold equation, multipliers and the square-root response. It also samples 995 initial states at five rational dispersal strengths. Those finite computations are diagnostics only: the proof of every-state convergence does not depend on the sampling. At \(\varepsilon=1/8\), the exact check includes \(c=2/3\) and the exceptional orbit \(c\mapsto1/2\mapsto1/2\). The full primary paper's model and Appendix A were inspected; full text of some potentially related papers remained inaccessible. Independent validation has not been performed.
