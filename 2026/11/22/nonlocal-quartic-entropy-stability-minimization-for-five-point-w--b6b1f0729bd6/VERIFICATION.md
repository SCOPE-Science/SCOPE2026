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

With Fourier multipliers (0,1,2,2,1), Parseval gives energy S+z² for u=a+x+y, where a=sqrt(1-S), S=||x||²+||y||², and z=||y|| for the second harmonic. Expansion of u² log(u²) gives deficit 2z²-2<x²y>-2<xy²>+< (x+y)^4 >/6+S²/2+O(S^(5/2)); the separate third moments vanish. In this real five-point Fourier decomposition ||P₂(x²)||=||x||²/sqrt(2) and <x⁴>=3||x||⁴/2. If z/S tends to infinity, the quadratic term dominates the numerator on the S² denominator scale. Consequently finite liminf sequences can be restricted to z=O(S), on which the pure first-harmonic quartic term gives 3S²/4 together with the normalization correction. The estimate reduces to 2z²-sqrt(2)Sz+3S²/4=2(z-S/(2sqrt(2)))²+S²/2. The displayed cosine path saturates the inequality because its second harmonic has the optimal norm and phase. Thus the exact local limit is 1/2. I independently computed the witness using integer cyclic correlations combined with Parseval, and exact rational enclosures of the entropy using the range-reduced -log(1-t) series. Its ratio is in (0.472467667182636,0.472467667182637), with exact rational comparison to 19/40. A neighborhood of 1 has quotient exceeding the witness; its compact admissible complement contains a global minimizer by continuity, even if some entries are zero.

## originality

PASS

The contribution supported as distinct is the strict global comparison for this word-length form and resulting nonconstant attainment. The earlier exact local constant and global lower estimates are credited separately.

## value

PASS

For a canonical cyclic-group word-length energy, this resolves a concrete question left by the near-constant upper bound: the minimizing regime is genuinely nonlocal. The strict witness gives both a better certified bound and attainment rather than just a minor numerical improvement. Its second-mode cost and threshold distinguish it from the nearest-neighbor example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
