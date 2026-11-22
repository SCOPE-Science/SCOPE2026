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

The deterministic files `verify_symbolic.py` and `verify_independent.py` build the ten-vertex Hamiltonian directly from the lexicographic pairs. Both are standalone and use no private data.

`python verify_symbolic.py` checks the parameterized characteristic polynomial, the exact \(-2(t-1)^3\) three-sink Krylov determinant, the symmetric-point spectrum, the rank-seven three-sink exception, and the nonzero five-sink determinant. Output observed: `SYMBOLIC_PETERSEN_CERTIFICATE_PASSED: characteristic polynomial, minors, ranks`.

`python verify_independent.py` uses integer Bareiss elimination to check the degree-at-most-thirteen three-sink determinant polynomial at fourteen different integer edge weights, uniquely establishing the identity by interpolation; it also checks the five-sink determinant and the three-sink exceptional rank using rational elimination. Output observed: `INDEPENDENT_INTEGER_PETERSEN_CERTIFICATE_PASSED: 14 evaluations, rank, unweighted minor`.

The mathematical bridge from finite Krylov rank to eventual absorption uses finite-dimensional semigroup contractivity, proved in `RESULT.md`; the scripts do not independently validate all dynamical modeling assumptions. Generalizing the theorem to other graphs or obtaining a uniform near-symmetric capture-time bound remains unproved. Independent audit is not performed.
