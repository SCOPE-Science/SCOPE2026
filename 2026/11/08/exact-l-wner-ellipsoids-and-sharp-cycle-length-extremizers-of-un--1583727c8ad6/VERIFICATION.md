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

The proof is self-contained modulo standard Euclidean ellipsoid facts and the matrix-tree theorem. The exact rational checker `check_unicyclic_ellipsoid.py` requires SymPy and verifies weighted-Laplacian shape identities, all sign-pattern inclusions and contacts, the isotropic covariance certificate, and the matrix-tree cofactor for 51 constructed graph instances on 3 to 8 vertices. It also checks the cycle-length comparison for indices 3 through 40. Run `python check_unicyclic_ellipsoid.py`; the recorded output is `UNICYCLIC_GRAPHICAL_ZONOTOPE_LOEWNER_CHECKS_PASSED 51 3468 6696`.

Limits: the finite enumeration does not establish the infinite theorem. General optimality is supplied by the expectation, trace, and determinant argument in the proof; strict monotonicity is supplied by Bernoulli's inequality. Independent mathematical audit has not been performed. The earliest publicly verified lead among the cited paper versions is arXiv:1912.02439 on 2019-12-05.
