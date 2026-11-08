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

Run `python CHECK.py` with a standard Python 3 interpreter. It computes every Fourier coefficient directly from the two-branch point set for primes \(5,7,11,13,17,19,23,29,31,37,41,43,47\), independently computes the one-dimensional exact formula, and checks both the one-parabola normalization and indicator Fourier-ratio relation. The printed `CHECK_OK` confirms finite-case numerical agreement within \(10^{-9}\); no use of a floating-point test is made to establish an all-prime identity.

The general proof is in `RESULT.md`. Its critical steps are: remove the duplicated origin, evaluate the two Gauss sums with both signs of the quadratic coefficient, classify the zero/nonzero Fourier-coordinate slices, count exactly \(p-1\) preimages of each nonzero \(t\), identify the convolution endpoint norm by aligning phases, use a Riemann sum for \(|\sin|\) or \(|\cos|\), and bound the signed quadratic-character sums over intervals by Fourier completion. These statements hold for all odd primes \(p\ge5\), independently of the listed computations.

All mathematical limitations are given in the result. This verification document provides no external or independent mathematical certification.
