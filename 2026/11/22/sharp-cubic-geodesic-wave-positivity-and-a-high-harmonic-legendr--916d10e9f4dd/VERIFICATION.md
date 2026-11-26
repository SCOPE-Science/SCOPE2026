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

For a>0 on the unit round S², applying the Legendre recurrence three times gives only degrees n±3 and n±1 in T₃Pₙ; the displayed four rational coefficients are positive for n≥3, and at n=2 the lower outer term is absent. At n=0 and n=1 the negative coefficients are respectively −3/5 at degree 1 and −1/5 at degree 0. Normalization at 1 gives the convex combinations; the absolutely summable nonnegative expansion justifies applying the multiplier to the whole supported cone. The exponential moment recurrence follows by integrating the Legendre derivative identity and the angular Sturm–Liouville equation; the boundary terms are zero (the derivative difference vanishes at the endpoints and the latter equation has a sin(θ) factor). Together with A₀ and A₁ this gives every Aₙ>0. Independently, exp(−a arccos t)=exp(−aπ/2)exp(a arcsin t) has a convergent nonnegative power series on [−1,1] with all monomial coefficients positive; the tⁿ term contributes positively to Pₙ and powers of t have nonnegative Legendre coefficients by recurrence. The mixed-product expansion thus forces Bₙ>0 for n≥2. The elementary sin(4θ)−sin(2θ) and sin(5θ)−sin(θ) integrals give the signs of B₀ and B₁ as those of a²−8 and a²−5, respectively. Schoenberg's criterion gives the iff including its endpoint; all positive degrees survive there, so both parities are infinite and strict positive definiteness follows. At equality all RKHS elements have zero mean, while above it the RKHS contains all finite spherical harmonic sums, giving exactly the stated uniform-density transition. RESULT.md, VERIFICATION.md and check.py inspected; the reported 230 assertions are supplementary, not a fresh replay or an all-degree proof.

## originality

PASS

Best of current knowledge, neither the sharp third-harmonic S² threshold with its exact endpoint spectrum nor the mixed T₃Pₙ positivity cutoff is covered by the inspected sources. Standard criteria and the Legendre recurrence are not credited as new.

## value

PASS

For a natural sign-changing isotropic wave, the exact threshold distinguishes admissible from inadmissible covariance parameters and specifies the critical loss of constants without loss of strict positive definiteness. The mixed multiplier also acts on the entire high-degree Schoenberg cone despite failing as a multiplier of the full cone, a structural property useful independently of the exponential family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
