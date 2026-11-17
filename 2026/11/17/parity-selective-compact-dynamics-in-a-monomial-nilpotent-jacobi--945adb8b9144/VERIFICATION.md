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

# Reproducibility and verification scope

The central all-integer claims are verified by the analytical proof in `RESULT.md`, not by a finite computation. The exact coordinate change \(u,v,w)=(x,y+x^2,z)\\ is a polynomial automorphism preserving physical time; multiplying the general symbolic Jacobian in that proof gives \(J^3=0\). The one-degree-of-freedom Hamiltonian and the drift quadrature are derived without a limiting approximation. The finiteness argument uses analyticity plus nonzero endpoint signs, not a bounded search for zeros.

The standalone `check.py` is ordinary reproducibility code written using the standard Python library only. Execute `python3 check.py` from the directory containing this file. In a clean replay it checked the exact Jacobian cube on rational test points for six integer degrees, the period and drift quadratures on sample energies for five degrees, the strict even-degree drift sign, and odd-degree root brackets for degrees one, three and five. Its expected markers are `EXACT_JACOBIAN_CUBE_ZERO_ON_TEST_POINTS_OK` and `FINITE_QUADRATURE_CROSSCHECK_OK`. It prints approximate roots, which are illustrative and not exhaustive algebraic root certificates.

The results do not determine the exact number of zeros for each odd degree. Source-comparison confidence is limited by incomplete access to the later journal version of the originating preprint. Independent audit has not been performed.
