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

# Reproducible verification

The package includes `artifacts/check_odd_commuting_spectrum.py` and its actual replay output `artifacts/verification_output.txt`. Run `python3 artifacts/check_odd_commuting_spectrum.py` after extracting the files. Python 3 and NumPy are required. For each of the prime fields of orders three, five and seven, the checker independently computes 30,000 exterior-odd-products using the degree-two and degree-four formulas and compares with the graph's clique/incidence rule, and checks all projective-point incidence Gram products. For the field of three elements it additionally enumerates all 6,561 odd elements to reconstruct clique sizes and compares every eigenvalue of the symmetric 201-class compressed graph with the theorem (maximum numerical error less than \(4\times10^{-13}\)). The decomposition of within-class sum-zero subspaces adds the remaining \(-1\) eigenvalues. No exhaustive search over all fields is claimed.

The exact symbolic calculations in the proof show that the quotient determinant is nonzero for every odd prime power, and each other spectral band excludes zero. No Lean, external certification or independent mathematical audit is claimed.
