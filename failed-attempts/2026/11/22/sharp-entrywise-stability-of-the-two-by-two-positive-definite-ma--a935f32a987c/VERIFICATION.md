---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For S=A^(1/2) the derivative solves SX+XS=H and has the stated positive semigroup sandwich integral. Independently, center E_t=e^(−tS) between e^(−vt)I and e^(−ut)I for u=√a, v=√b: the centered rescaled matrix is a spectral contraction, so its absolute row sums are at most √2. Thus the absolute row sum of E_t is bounded by c e^(−ut)+(1−c)e^(−vt), where c=(1+√2)/2. Cauchy–Schwarz on rows or the common row envelope gives the sharp upper bound by the integral of this square. For the positive rank-one low-eigenvalue projection at angle π/8, the first row sum of P is cos²(π/8)+cos(π/8)sin(π/8)=c. Then E_t is entrywise nonnegative and saturates the envelope in that row for all t, and the symmetric all-ones direction gives equality in the (1,1) derivative entry. Integrating gives c²/(2u)+2c(1−c)/(u+v)+(1−c)²/(2v), the stated constant. The scalar-angle derivative in RESULT.md is also obtained by differentiating the row coefficient (1+x)/(1+x²) against its nonnegative kernel. Convex segments give the global bound; admissible interior pairs approach the derivative value and do not assert attainment by distinct matrices. Any finite pair in the unbounded-band domain belongs to some finite band, and the sharp constants tend to the stated unbounded-band value and scalar ratio. RESULT.md lines 23–80, VERIFICATION.md, and check_square_root.py were read; the reported 16,515 finite checks were not executed.

## originality

FAIL

The exact finite-band coefficient, extremal angle, and limiting witnesses are covered by the distinct indexed absolutely-monotone matrix-function theorem under X=I−A/b. The transformed square root is a positive-coefficient series, despite the alternating signs one would obtain from a different expansion. The no-upper-bound result is a direct limit over nested finite bands. No chronological ordering or authorship conclusion is drawn from the same-date records.

## value

FAIL

The sharp square-root sensitivity is a useful benchmark, but the exact coefficient and rotation here are a direct function and dimension specialization of a broader sharp invariant. The scalar comparison and unbounded-band limit are elementary consequences, not an independent surviving contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
