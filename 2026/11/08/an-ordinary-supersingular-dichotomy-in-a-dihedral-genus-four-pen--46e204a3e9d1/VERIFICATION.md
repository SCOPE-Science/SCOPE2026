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

# Exact calculation and proof verification

Running `python3 verify_cartier.py` reconstructs the characteristic-seven Cartier–Manin coefficients, checks the single-four-cycle support for primes \(3,7,13,17,23,37,43\), and evaluates the characteristic-seven rank exceptions over \(\mathbb F_{49}\). It prints `PASS: exact genus-four Cartier matrix, 4-cycle support, 3 exceptional parameters`.

Running `python3 verify_quotient.py` independently verifies the reciprocal Laurent identity defining the genus-two quotient and computes the characteristic-seven genus-two determinant \(2a(a^2+1)\). It prints `PASS: involution quotient identity and genus-two determinant 2a(a^2+1)`.

Both programs use only Python's standard library. Neither is an exhaustive search over all algebraic parameters or characteristics. The universal theorem follows instead from dihedral eigenspaces, the single Cartier cycle, and classification of Newton polygons of abelian surfaces. No independent mathematical audit has been performed.
