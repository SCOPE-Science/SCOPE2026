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

# Verification record

The archived `verify_klein120.py` program uses only exact Python integers and Gaussian-integer pairs, not floating point, external algebra packages, or a saved matrix. It reconstructs 60 projective point representatives and the same 60 dual plane normals. It tests all 3,600 point–plane incidence decisions and 900 positive incidences. Matrix polynomial multiplication and the first six traces certify all 60 rational incidence eigenvalues and multiplicities; their associated 120 Laplacian eigenvalues give the exact matrix–tree determinant.

For each of primes 2, 3, 5, 7, the verifier reduces a 119-by-119 integer Laplacian modulo a prime power. Unit row and column pivots are invertible in the local quotient; when all entries in a remaining block are divisible by the prime, the block is divided and the valuation increases. Explicit moduli are 2^12, 3^8, 5^6, 7^5. No valuation reaches the modulus cutoff. Calculations are repeated with the first point vertex and last plane vertex deleted separately, and both resulting valuation lists agree. The determinant is verified against the entire product of invariant factors and excludes any other prime factor. The nonzero divisibility-chain factors are checked exactly.

Actual command: `python3 verify_klein120.py`.

Actual output is saved as `verify_output.txt`, ending `KLEIN_60_15_INTEGRAL_CRITICAL_GROUP_OK`.

This finite exact computation supports a complete finite Smith decomposition. It does not certify original publication priority, any positive-characteristic geometric realization, or a canonical surface degeneration.
