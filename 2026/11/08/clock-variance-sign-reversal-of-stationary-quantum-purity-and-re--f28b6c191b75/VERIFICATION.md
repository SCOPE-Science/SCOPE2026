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

# Verification and reproducibility

The proof in `RESULT.md` provides the required infinite-dimensional-parameter logical argument for every finite Hilbert-space dimension and all admissible rates. `verify.py` independently checks the renewal transform, coefficient-of-variation factorization, the two endpoint clock laws, and the stationary-purity comparison by two distinct routes: algebraic rational transforms and direct numerical survival-function quadrature.

Install dependencies listed in `requirements.txt` and run `python verify.py`. The execution must report `PASS ALL`; the tests include nine symbolic identities, 24 independently integrated mixed-state matrices in dimensions two, three and five, and seven exact-rational balanced-qubit checks. These finite tests are not a proof of universal quantification and do not establish scientific originality or publication priority.

The normalized clock uses rates \(a,b>0\), independent Bernoulli branching probability \(0\le q\le1\), finite-dimensional unitary time evolution and the stationary equilibrium-renewal age. In a pure reset state, overlap is squared fidelity; for mixed reset states it is not Uhlmann fidelity. A synchronized reset run with a nonlattice Coxian clock converges to the stationary ensemble, but transient claims are outside the theorem. No external independent audit has been performed.
