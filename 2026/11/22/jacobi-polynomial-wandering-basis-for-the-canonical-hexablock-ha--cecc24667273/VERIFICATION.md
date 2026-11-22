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

The proof rests on the exact boundary parametrization, the three commuting Haar characters, the beta moment integral, classical Jacobi orthogonality and the classical Wold decomposition for the pure coordinate isometry. Both endpoints \(r=0\) and \(\alpha=\beta=-\tfrac12\) are explicitly handled in the norm convention.

The supplied `check.py` (Python 3 with `sympy`) was executed as packaged and returned `HEXABLOCK_JACOBI_CHECK_OK 1400`. It runs 245 parameter triples, checking moment orthogonality, norm identity, and Gram principal-minor nonnegativity. The infinite-dimensional basis assertion is analytic and is not inferred from these finite tests.

An independent audit has not been performed. The model is the unweighted canonical Haar-pushforward hexablock Hardy space, not arbitrary weighted hexablock Hardy spaces.
