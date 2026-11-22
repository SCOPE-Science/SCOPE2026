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

# Exact verification evidence

The specified zero-detuning Hamiltonian is reconstructed on every one of the 69 allowed configurations, with even/odd block sizes 37 and 32. `verify_exact.py` uses symbolic characteristic-polynomial and minor-determinant identities on explicitly constructed matrices. `verify_independent.py` builds the graph separately and uses only integer matrix products plus Newton identities to reconstruct all 33 characteristic-polynomial coefficients; additional finite-field row reductions verify the specialized ranks. Both ran successfully after the code was finalized. To reproduce, use `python verify_exact.py` (SymPy) and `python verify_independent.py` (NetworkX), with Python 3.10 or newer.

The verified factor has zero-root multiplicity six for the 32-dimensional Gram matrix. The symbolic 32-by-32 minor has determinant \(2(t^2-1)^6\). The remaining steps converting ranks to Hamiltonian nullities are exact block linear algebra. The codes are not floating-point sampling, and neither code assumes that checking finitely many values of \(t\) proves a continuous-parameter assertion: the determinant polynomial does that.

These checks address the finite mathematical statement only. They do not independently validate scientific novelty, grant external certification, or establish applicability when the perfect-blockade assumptions fail.
