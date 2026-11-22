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

# Reproduction and evidence

The standalone `e8_weighted_component_group_checker.py` reconstructs every integer entry from the classical eight-dimensional root coordinates and, separately, from the seven degree/multiplicity families of \(240\) exceptional classes on an eight-point blowup. Six distinct rooted cofactors (three per representation) were reduced at powers of primes two, three, five, and seven using legal Smith row/column operations modulo prime powers. The cofactor determinant is independently fixed by the rank-eight Gram identity and the matrix-tree theorem. The exact valuation sums agree with its factorization, so the modular caps do not hide further torsion. The local sequences combine to nine unit Smith factors, 222 factors of 240, and eight factors of 72000.

Invoke `python e8_weighted_component_group_checker.py` in a Python 3 environment with NumPy installed. Successful exact replay prints `E8_WEIGHTED_ALL_240_EXCEPTIONAL_SMITH_OK`. The underlying mathematics is an integral finite computation; no continuous numerical approximation, randomized test, unbounded enumeration, or black-box external certification is used. The result does not assert a semistable smoothing of the full exceptional divisor.

Independent mathematical audit has not been performed.
