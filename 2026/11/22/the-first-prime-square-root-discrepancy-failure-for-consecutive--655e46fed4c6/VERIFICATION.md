---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The two recursions on consecutive residues arise by replacing n with 2n and 2n+1, so starting at (0,1) gives exactly the full prefix vector. Both maps are permutations; the uniform vector and its zero-sum complement are invariant, and the computed simplicity of eigenvalue 2 isolates the centering term. Independently recovered the five characteristic polynomials by tracing powers with the inverse predecessor maps and applying Newton identities over the integers. All displayed factors and multiplicities matched. The nontrivial reciprocal quartics for p=5,7 reduce at y=x+2/x to the stated three quadratics, with real y-roots strictly between ±2sqrt(2); the two x-roots at each y are conjugate with product 2. All other nonprincipal factors for p<11 have roots of modulus at most sqrt(2). A possible polynomial factor from Jordan blocks does not affect the root limsup. For p=11, exact scalar counts and det(I−zT) give the generating-function numerator from its first 120 coefficients by the adjugate degree bound. Canceling its gcd with the denominator leaves the irreducible 1−z²+2z³, once, so z=−1/rho is an actual pole, not a merely available eigenmode. Subtracting the uniform geometric series cannot remove it. The frozen scalar certificate also independently reproduced as 573530441763580574433280. The cubic for rho is negative at sqrt(2) and increasing on [1,infinity), proving the strict failure and the prime minimum.

## originality

PASS

The supported distinct result is the evaluated first-prime threshold and the active order-eleven cubic at the designated pair. The transfer matrices, spectral bounding argument, and the square-root upper bounds at 2 and 3 are not new. The earlier modulus-nine phenomenon does not settle the asserted prime threshold.

## value

PASS

The natural benchmark is square-root error for a length-2^k prefix. Known power saving does not decide this benchmark, and a composite counterexample leaves it open along the primes. Proving the exact prime onset by excluding every smaller prime and certifying an active, explicitly specified pair at the next prime gives a useful boundary, rather than just finding a large-modulus numerical eigenvalue or reproducing the general transfer method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
