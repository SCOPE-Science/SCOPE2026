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

# Reproducible checks and limitations

Run `python verify.py` using Python 3 and SymPy. The standalone verifier reconstructs the four-dimensional epidemic–opinion field in exact rational arithmetic; it checks the positive synchronous equilibria, the healthy spectrum, both Jacobian mode blocks, the equilibrium elimination identities, the two nonzero branch derivatives, and the critical center-manifold cubic coefficient. The verifier exits with an exception if a claimed identity fails and reports `PASS` otherwise.

The global quantifier over \(w\geq0\) for linear stability follows from two explicit \(2\times2\) Hurwitz tests. The local analytic branch and its uniqueness follow from an invertible \(2\times2\) implicit-function Jacobian. The critical nonlinear instability follows from a one-dimensional center manifold with positive cubic coefficient; stable eigenvalues remain separated by continuity. These are analytic deductions, not consequences of finite parameter sampling.

The full original opinion system is nonsmooth on the opinion sign-switching surfaces. All equilibrium bifurcation assertions concern a neighborhood of original opinions \(o_1=o_2=-1/6\) and therefore avoid these surfaces. The conclusions do not classify distant equilibria or long-time behavior after the synchronous endemic state loses stability. External independent validation has not been performed.
