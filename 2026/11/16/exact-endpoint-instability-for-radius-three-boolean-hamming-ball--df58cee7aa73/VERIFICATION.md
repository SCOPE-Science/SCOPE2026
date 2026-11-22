---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n>=3 the Fourier multiplier of the Boolean radius-three Hamming ball is sum_{j=0}^3 K_j(k;n)=(t+1)((t+1)^2-3n+5)/6 with t=n-2k. For odd n=2m+1>=5 and nonsquare 3n-5 only the layer h=m+1 is missing; the other square-resonant cases are covered solely by the general rank formula. Translation averaging of arbitrary ℓ1/ℓ∞ projections onto the Fourier-defined range forces the canonical projection I-E_h as minimum norm. Its convolution kernel absolute sum equals 1−2r/2^n+(1/2^n)sum_x binom(n,x)|K_h(x;n)|. Krawtchouk duality and (1-z)^(m+1)(1+z)^m=(1-z)(1-z²)^m evaluate this absolute sum exactly as 1+r(2^(-m)−2^(-2m)), r=binom(n,m+1). Stirling central binomial asymptotics give exponential endpoint norm but vanishing relative nullity. Independent exact Walsh checks n=3..13 and kernel norm checks for all qualifying odd cases confirm the formula; finite calculations are not used as an infinite proof.

## originality

PASS

PASS, with substantial prior-implication risk. Defant et al Theorem 3.1 already gives the minimum projection norm of ANY Walsh-frequency subspace as an unevaluated character absolute sum; Krawtchouk/Lloyd theory already gives the multiplier zeros. Their inspected full manuscript does not evaluate the special middle-layer absolute sum in the closed binomial form or identify the radius-three nonsquare odd family and its exponential/vanishing-nullity separation. The specialized exact evaluation is the retained proposed original content; it may prove to be a routine application of known absolute Krawtchouk identities, so this is bounded best-of-knowledge, not priority certification.

## value

PASS

Sharp complementability constants for natural low-radius convolution ranges quantify recovery instability in endpoint norms. The explicit numerical closed form exposes exponential projection cost even while the missing-frequency density decays like n^(-1/2), a structurally meaningful separation. This is a motivated exact family, not a requirement for a new general projection theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
