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
# Reproducibility and limits

Run `python verify.py` in a Python environment satisfying `requirements.txt`. The program reproduces the symbolic identity \([f_1,[f_1,f_2]]=\gamma^2 f_2\) for an arbitrary formal potential \(V\), the exact cancellation step and derivative of the corrected duration, the exact linearized trace formula, and the sharp slow-root coefficient. It also performs nonproof numerical diagnostics on \(V(y)=y^2/2+y^4/4\) and a quadratic model using high-accuracy exact-flow approximations.

The universal conclusions follow from the written analytic proof, not a bounded collection of test cases. The results assume exact subflows, strict convexity and coercivity of the potential, and a single planar damped Hamiltonian. Local detuning estimates are not a statement about nonlinear global iteration rates. No independent audit has been performed.
