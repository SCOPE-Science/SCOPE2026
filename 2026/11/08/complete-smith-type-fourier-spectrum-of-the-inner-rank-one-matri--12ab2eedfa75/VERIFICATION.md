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

# Reproducibility

Run `python check_spectrum.py` with NumPy available. The checker independently enumerates the union of primitive outer-product valuation layers in \(M_2(\mathbb Z/p^k\mathbb Z)\), constructs the adjacency indicator, takes a four-dimensional discrete Fourier transform, and compares the rounded exact integer histogram to the independently evaluated Smith-type formulas.

Direct enumerations cover \((p,k)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1)\). A separate exact integer test checks the formula's total multiplicity and the sharp inverse spectral gap for primes \(2,3,5,7\) and depths \(2\) through \(8\).

Expected successful terminal line: `INNER_RANK_ONE_CAYLEY_SPECTRUM_PASS`. The module-level assertions fail if any histogram, degree, or finite spectral comparison differs. The argument for arbitrary exponent is the proof in `RESULT.md`; finite enumeration is only corroboration. No independent mathematical audit has been performed.
