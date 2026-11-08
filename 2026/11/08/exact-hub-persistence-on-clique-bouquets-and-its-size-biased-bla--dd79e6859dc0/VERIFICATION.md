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

Verification is limited to reproducible finite computations and symbolic mathematical checks. The infinite-family proof uses Poisson thinning, Feynman–Kac first-step equations, a tridiagonal Cramer identity, and a uniform fixed-blade-size Laplace expansion; computation cannot establish those quantifiers by itself.

Run `python verification/check_birth_death.py` with Python 3, SymPy, and the package's requirements. This checks symbolic resolvents for private clique sizes one through six, their derivatives at zero, and multiple exact heterogeneous products. The saved output is `verification/birth_death_output.txt`.

Run `python verification/check_full_state.py` with NumPy and SciPy. This independently builds the entire finite labelled-state Markov generator with the hub-change event killed, solves its Dirichlet boundary problem, and compares all forty tested compositions (one to eight private vertices, each private clique size at most three) with the independent rational formulas. The saved output is `verification/full_state_output.txt`.

The test programs were executed with Python 3.13.5, SymPy 1.14.0, NumPy 2.3.5 and SciPy 1.17.0. The numerical linear solves use floating-point tolerances of \(4\times10^{-12}\). These tolerances and tested size bounds do not constitute an exhaustive proof for unbounded graph size.
