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

# Verification and reproducibility

The included `check_quartic_A.py` is an ordinary deterministic Python 3 standard-library script. Run it as `python3 check_quartic_A.py`. A passing run prints `QUARTIC_A_EXACT_CHECK_OK: n=4..25; recurrence, harmonic projection, direct Gram eigenvectors, trace, positivity, equiangular exceptions`.

Finite rational tests: for integer dimensions 4–25, verify the normalized Gegenbauer recurrence against the Laplacian-derived quartic polynomial at all five inner-product values, positivity and multiplicity-weighted trace; for dimensions 4–12, construct the entire Gram matrix directly and check its action on all standard-sector star differences and two-row-sector four-cycle vectors. For dimensions 5, 15 and 21 verify the equiangular correlations exactly, and for 21 verify the 209-fold collapse and the rank-one Gram identity through its entries.

The infinite-dimensional-family conclusion follows from the proof's exact symbolic formulas: Johnson eigenspace decomposition, positive rational branches, factorization of the two equiangular equations, and analytic or discrete-monotonicity comparisons for the sharp dimension bound. The code does not claim to certify infinitely many dimensions; it is a reproducibility cross-check. Independent audit has not been performed.
