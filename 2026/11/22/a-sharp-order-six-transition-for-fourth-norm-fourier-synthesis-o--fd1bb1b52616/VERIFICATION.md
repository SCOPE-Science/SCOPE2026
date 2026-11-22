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

The proof is analytic and exact. Parseval with the stated unitary Fourier normalization gives the energy identity; uniqueness follows from strict convexity and coercivity on the fixed-sum hyperplane; exact reflection symmetry produces the two-weight ansatz; the rational quartics are obtained by cyclic aggregation of seven explicit convolution coefficients; their derivatives have the claimed global sign patterns. Character modulation gives every extremizer.

Run `python3 artifacts/verify.py` in this package to independently rebuild the convolution polynomials using rational arithmetic and compare the normalizations with direct finite Fourier sums. The checker observed `VERIFY_OK exact_polynomials=16 roots=4 group_cases=14 randomized=720 assertions=774`. Those 774 assertions are finite stress tests, not an exhaustive mathematical proof for all group orders or coefficient vectors.

The fourth-moment source date and primary MSC were checked against the publicly accessible motivating article. The related comparisons identify differences between the inverse fourth-norm optimization and prior Fourier projection, forward Lambda(4) and sixth-moment optimization. Priority beyond checked sources remains uncertain, and independent audit has not been performed.
