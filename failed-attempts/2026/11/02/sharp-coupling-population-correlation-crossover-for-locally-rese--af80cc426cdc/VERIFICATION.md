---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The Finding states that the time-covariance matrix has precisely two relaxation rates, but its stated domain includes λ=0. At that allowed point the exact formulas give K(t)=[Q/(2ν+r)]e^{−(ν+r)t}I: one rate, not two. The finite-N formulas and scaling limits themselves check out. With P the mean projector and b=ν+r, the centered linear conditional drift is −bI−λ(I−P). The stationary expected quadratic increment is (Q+rS_N)I, since each independent replacement affects only one coordinate. The two covariance eigenvalues u,v consequently satisfy 2bu=2(b+λ)v=Q+rS_N; together with S_N=[u+(N−1)v]/N this gives the stated S_N and C_N. The conditional semigroup yields the lag formulas, with distinct rates and both modes present for λ>0. At λ=cN, u→Q/(2b) and Nv→Q/(2c), which recovers both time limits. Common-noise pathwise contraction and the confining quadratic Lyapunov bound justify the finite-moment stationary law. I inspected RESULT.md lines 35–101, VERIFICATION.md and verify_correlation.py; I did not execute the code. Its rational raw-moment checks replay the finite-N equations, while its floating lag checks recombine the same two modal terms and are not independent evidence for large-N limits.

## originality

PASS

The positive-diffusivity, arbitrary-iid-reset-law statement is not literally supplied by the prior positive-growth fixed-target process: its assumptions do not include the harmonic diffusion, and the needed negative intrinsic drift is outside the prior theorem. This is a narrow pass for that change of model, not a finding that the scalar correlation law or the crossover and layer profiles are distinct mathematics. The exact analytic overlap is detailed below and is decisive for value.

## value

FAIL

The Brownian model is natural, but the distinct part is a routine transfer of a known covariance calculation: Brownian noise and independent random reset values only add a scalar diagonal forcing, and putting the confining sign into the already-known linear coefficients gives identically the same stationary solve. Normalization removes the entire noise-law dependence. The lag regression is the exponential of the same two affine drift modes, and the two large-N profiles are mechanically implied by the prior finite-size equations even in its valid growth regime. No distinct covariance phenomenon or nontrivial extension beyond this scalar-forcing transfer is established. Correcting the zero-coupling sentence would not address this failure, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
