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

# Verification
The proof and four-sector character table in RESULT.md are the basis for the assertion for every odd prime power. The bundled `check_symmetric_three.py` uses NumPy FFT to calculate all rank-one and rank-two Fourier coefficients directly for prime fields of orders 3, 5, and 7; it independently classifies each frequency by rank and projective isotropic-point count, and compares all coefficients with the exact table. Run `python check_symmetric_three.py --primes 3 5 7`. The recorded complete runs passed, ending in the marker `SYMMETRIC_THREE_RANK_NEGATIVE_TYPE_PASS`.

At orders 3, 5, and 7, the complete tests involved, respectively, 729, 15,625, and 117,649 symmetric matrices, including the zero frequency. The theorem's critical root, endpoint nullity, and minimal embedding dimension follow analytically from the Fourier formula and rank-stratum cardinalities. Only odd characteristic is addressed. Numerical FFT agreement is corroboration, not independent mathematical validation or an all-field proof.
