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

Execute `python verify_cartier.py` (Python standard library only) to independently expand the cubic power of the genus-four defining polynomial as a trivariate polynomial, compare all 16 Cartier positions, and check the genus-one quotient Hasse coefficient. The expected output is `C7_CARTIER_SYMBOLIC_COEFFICIENTS_PASS` and `C7_ELLIPTIC_QUOTIENT_HASSE_PASS`.

Execute `python verify_strata.py` (requires SymPy) to independently reconstruct the matrix by coefficient extraction, verify the Hasse determinant, restrict the discriminant and elliptic Hasse coefficient to the Prym nonordinary graph, check squarefreeness and excluded-root conditions for the quintic, and enumerate all 49 prime-field coefficient pairs with separability and semilinear stable-rank checks. Its expected output includes `C7_RANK_STRATA_GF7_PASS {(4, 0): 29, (2, 2): 2, (1, 2): 2, (3, 1): 4}` and `C7_EXACT_FIVE_GEOMETRIC_PRYM_RANK_ZERO_PARAMETERS_PASS`.

The symbolic identities and semilinear rank-one factorization in `RESULT.md`, not the prime-field census, prove the theorem over \(\overline{\mathbb F}_7\). The quintic's geometric five-root statement follows from its exact degree, derivative and disjointness with the singular boundary. No independent audit or finite-field point-count certification was conducted.
