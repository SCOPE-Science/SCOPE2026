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

# Reproducibility and verification

Run the bundled `verify.py` with Python 3. It uses only the standard library, enumerates Mallows permutations for \(2\le n\le6\), and checks their surplus distributions against an independently evaluated Poisson--binomial product. It also enumerates every parking function and every allowable code vector in those sizes, with exact rational arithmetic. The script exits with an assertion error on any failed test.

These checks substantiate exact finite combinatorial identities, not the infinite conclusion. For the infinite theorem, independently inspect: (1) the support condition implies the parking inequalities; (2) bulk surplus is an independent Bernoulli sum; (3) variance is at most mean; (4) Theorem 15 of Diaconis--Hicks gives a non-atomic, tight limit for the uniform bulk surplus; (5) the two Chebyshev regimes and the small-ball lemma produce one error bound independent of the coordinate laws. The proof explicitly treats the parameter \(q=1\) and all other positive parameter values without using any limiting regime assumptions.

Published ingredients: https://arxiv.org/abs/2509.24452 ; https://doi.org/10.1016/j.aam.2017.05.004 ; https://doi.org/10.37236/1558 .
