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

The endpoint perturbation is zero on the even reflection space and changes only the first diagonal of the odd Jacobi block by 2w. Each block is simple. At w=1 each nonzero even eigenvalue occurs also in the odd block; the odd characteristic polynomial at this fixed eigenvalue is affine in w with nonzero slope, because the eigenvalue at w=1 is simple in that block and its eigenvector has nonzero endpoint coordinate. Thus no such collision persists at any other positive w; zero stays simple by connectedness. The even path cosines vanish at j only when (2j+1)r=(n/2)(2h+1). This is impossible for odd n and equivalent to gcd(2j+1,n/2)>1 for even n. For odd n the center misses every odd mode. For a noncentral odd nodal site j>=1, the last independent coordinate cannot vanish, so a nonempty right tail remains. Its matrix has usual diagonal 2 with a 3 at the last site only for even n; it and its reflection about 2I are positive definite (the latter after alternating signs, with terminal diagonal 1 rather than 3). Hence 0<lambda<4. With lambda=2-2cos(theta), the nodal solution is proportional to sin((i-j)theta) and the reflected tail boundary gives (n-2j-1)theta a multiple of 2pi, with both endpoints of (0,pi) excluded. Matching the left endpoint gives the stated sine ratio with nonzero denominator; conversely the constructed sine wave satisfies both boundaries at that weight. The odd block's first coordinate cannot be zero, so j=0 has no odd resonance. At w=1/2 on odd n the odd block is the size-m Dirichlet matrix and its zeros at j are exactly the positive multiples of (m+1)/gcd(m+1,j+1) through m. For simple spectrum the Krylov rank is the number of visible modes by the Vandermonde rank, giving the exact gcd deficiency and the central loss, and pairing reflected sites gives the totient count. Independent exact fractional Krylov ranks passed 96 half-weight odd-size site tests and 24 endpoint/one-in checks including uniform weights.

## originality

PASS

Pass for the explicit inverse placement problem: the finite list of exceptional positive weights and the permanent obstructions at arbitrary reflected distance, without solving for the eigenvalues at each weight. The endpoint and one-in classifications and the uniform baseline are already covered. General spectral formulas cover the eigenproblem and yield a direct fixed-eigenpair PBH calculation. In particular, the half-weight rank/totient law follows directly from the prior explicit half-weight spectrum and eigenvectors plus arithmetic; it is a useful corollary, not a separately original spectral or arithmetic discovery for this assessment. The nontrivial remaining comparison is eliminating the eigenvalue and listing every bad weight for each site, including weights above one.

## value

PASS

A cycle with one tunable conductance is a natural minimal departure from the repeated modes of uniform consensus. The useful new control-design answer is an explicit list of forbidden weights and permanent locations for any sensor site, separating geometry from exact resonance without requiring a fresh eigensolve. Arbitrary sites and weights above one cannot be designed from the endpoint and one-in results alone. The half-weight arithmetic illustrates the placement issue and the possible rank loss; it is a consequence, not the independent basis of this value pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
