---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Orthogonality of 1 and z gives the exact squared phase distance; rotational invariance reduces the moduli to t=||F|| and s=|a|/t. For s<1, strict E|s+sqrt(1-s^2)Z|>s follows by taking the real part (the imaginary part is almost surely nonzero); strict Cauchy–Schwarz gives m(s)<1. The derivative of t/(t^2+1-2tm) has sign 1-t^2. Thus t=1 uniquely maximizes the ratio for each s<1. For the Rice formula, polar integration gives the radial density 2r exp(-r^2-2x) I_0(2sqrt(2x)r) for |Z+sqrt(2x)|, with x=s^2/[2(1-s^2)]. Integrating the power series termwise gives the mean exp(-2x) sum_k (2x)^k Gamma(k+3/2)/(k!)^2 before rescaling; this is the Bessel expression in the proof. Differentiating that expression yields the stated factor 2x I_0-(2x+1) I_1 for m''. The Riccati equation for q=I_1/I_0 and barrier b=2x/(2x+1) give a strictly positive excess 3/(2x+1)^2 at any putative first contact. Hence m lies strictly below its endpoint chord inside (0,1). The resulting optimum is attained only at s=0,t=1, i.e. a=0, |b|=1, and has value 2.9646965828533536. Non-unimodular constants, including zero, have ratio one; unimodular constants give both norms zero.

## originality

PASS

The supported distinct claim is the sharp global unsquared ratio and exact equality set for the affine subspace, not the Rice mean formula, an isolated Bessel ratio bound, or existence of some Fock stability constant. The strongest Gaussian phase-retrieval candidates concern full-space existence, a squared restricted inequality, or the differential of squared intensity. No inspected statement determines the global affine ratio and equality. Known Bessel-ratio bounds may supply the convexity ingredient, a plausible partial implication explicitly separated from the norm and two-parameter optimization.

## value

PASS

The constant-plus-first-mode truncation is the first nontrivial test of vacuum modulus stability and a natural calibration for any full-space inequality. The result not only provides a sharp constant but identifies a maximally displaced affine competitor (zero vacuum component, unit first mode) and excludes every coherent offset. A global benchmark of this kind is not supplied by a local singular value or by evaluating a Rayleigh mean at one challenger.

The dated certificate retains the supplied scientific assessment, sources and limitations.
