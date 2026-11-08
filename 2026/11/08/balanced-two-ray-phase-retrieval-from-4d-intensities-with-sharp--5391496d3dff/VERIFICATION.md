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

# Verification of two-ray finite phase retrieval

The proof is algebraic and valid for every integer \(d\ge1\), positive distinct radial nodes on each ray, and angle with \(\sin(m\theta)\ne0\) for each \(1\le m\le d\), provided the products of radii differ. The submitted `RESULT.md` establishes these quantifiers. The finite checks below are supplementary.

## Executed reproducibility

The included `verify.py` was executed with Python 3 and `mpmath`, configured to 90 decimal digits. It completed with:

`TWO_RAY_PROFILE_CHECKS_PASS 5355 degrees 1..6 plus resonant boundaries 1..8`

For degree bounds 1 through 6, twenty randomly chosen complex-coefficient test vectors per degree were sampled at \(2d\) distinct positive radii on each of two rays. The direct intensity coefficients were compared to coefficients reconstructed from two Lagrange interpolants and a common leading term. Off-grid intensities were checked. For every resonance order \(1\le m\le d\le8\), the code compared the explicit two distinct polynomials \(1\pm iz^m\) at points on both rays. An additional degree-one instance used exact rational arithmetic for both recovered polynomial profiles.

## Analytic steps not replaced by computation

1. The shared constant and top-degree coefficient identities for both radial intensities are polynomial identities, independent of numerical tests.
2. For any unequal pair \(p,q\) with equal whole profiles, the first nonconstant quotient coefficient would force \(\sin(k\theta)=0\) for some \(k\le d\).
3. The span of valid Hermitian-lifted profile pairs has real dimension \(4d\), by independent coefficient-sector controls; numerical sampling is not used as a proof of the dimension for all degrees.
4. Resonant angles defeat **any** sample count on the two rays; the explicit counterexample is exact.

## Limits

Floating-point Lagrange interpolation becomes ill-conditioned for large degree or clustered radii: a preliminary ordinary double-precision degree-six test suffered cancellation. The completed reproducibility check therefore uses high precision. No deterministic noise-uniform conditioning bound, nonlinear global sample-count optimum, or independent mathematical certification has been established.
