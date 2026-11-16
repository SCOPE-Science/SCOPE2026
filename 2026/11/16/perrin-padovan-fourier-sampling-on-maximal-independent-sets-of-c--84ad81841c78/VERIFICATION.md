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

# Verification evidence and boundaries

The complete standalone `verify.py` is included in this package. It runs with Python 3 standard library only and requires no external files. Executing `python3 verify.py` in the extracted package passed 553 exact-rational and numerical checks, including direct enumeration of all inclusion-maximal independent sets of cycles of orders \(3\) through \(15\), exact rational comparison of every sampled two-point moment, exact rational covariance rank, and comparison of the Fourier eigenvalues to the limiting density at additional cycle orders.

The all-order finite covariance formulas follow from the three-state transfer-matrix trace identity. The all-order rank statement follows from the gap-interchange and cardinality arguments. The uniform asymptotic statement follows from the characteristic-root error estimate, an absolutely convergent centered renewal series, and optimization of a strictly positive quadratic. No finite test substitutes for these proofs. The spectral ratio is a **squared-energy**, not an unsquared singular-value condition ratio.

Existing mathematical literature provides cyclic maximal-set enumeration and stationary renewal diffraction principles. Historical priority for the precise finite Fourier sampling classification remains subject to independent review. Independent audit has not been performed.
