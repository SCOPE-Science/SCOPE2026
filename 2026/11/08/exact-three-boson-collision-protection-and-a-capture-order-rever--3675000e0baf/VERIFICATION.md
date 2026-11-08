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

# Reproducibility

The analytic all-size proof and explicit bright projector appear in RESULT.md. Two independent executable checks accompany this document:

- Run `python verify_symbolic.py` with SymPy. It checks the rank-determining Gram eigenvalue polynomials, the three rational eventual-capture identities and the exact crossover difference as symbolic identities in the number of network sites.
- Run `python verify_fock.py` with NumPy and SciPy. It constructs the three-boson Hamiltonian directly in occupation coordinates, determines collision-dark subspaces by separate eigenspace nullspace computations for sizes \(n=3\) through \(8\), and verifies exact fraction predictions numerically. It additionally checks the undamped spectral multiplicity for nonuniform positive loss rates for sizes \(n=3\) through \(6\).

Both scripts were executed successfully from the packaged source versions. The symbolic checks support the all-integer algebraic derivation; the finite matrix tests are numerical corroboration and are not offered as exhaustive verification of an infinite family. The verification does not test finite-time loss profiles, interactions, or graph perturbations. No independent validation has been performed.
