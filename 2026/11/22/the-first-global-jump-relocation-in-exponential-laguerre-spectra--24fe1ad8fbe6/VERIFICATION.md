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

The sharp real \(BV\)-to-weighted-\(L^2\) norm is reduced analytically to the maximum of a one-variable Laguerre step residual. `CHECK.py` establishes the complete classification at degrees zero through five via exact rational arithmetic, independently of floating-point root estimates. Run `python3 CHECK.py` using Python 3's standard library.

The script constructs ordinary Laguerre polynomials and the polynomials \(B_n,Q_n,A_n\), checks the derivative identity, isolates every root of \(A_n\) by rational sign changes (the count equals its degree), determines the signs of all critical values of \(e^{-t}Q_n(t)-1/2\), isolates and counts every stationary point, bounds the exponentials by Taylor polynomials with a rigorous positive remainder, and proves strict inequality between the winning and competing stationary residual values. The success line is `LAGUERRE_EXACT_CERTIFICATE_PASSED 84`.

The comparison at degree five is especially narrow, so rounded decimals are not accepted as a certificate. The checker works with rational enclosures of width \(10^{-11}\) for the stationary roots; the lower bound at the third root is larger than the upper bound at the first. The complete critical-point count rules out additional larger stationary maxima. The endpoints have zero residual, hence cannot maximize.

A separate numerical quadrature cross-check at the six winning jump locations agreed with the exact finite-term residual formula to roughly \(10^{-16}\). This corroboration is not used to prove the theorem. The result is limited to degrees zero through five, real ordinary variation, exponential probability weight and exact orthogonal polynomial projection. No independent mathematical audit has been performed.
