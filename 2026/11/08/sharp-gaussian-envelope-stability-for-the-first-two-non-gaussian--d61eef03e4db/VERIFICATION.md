---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The normalized centered Hermite ambiguity functions are A h_j(x,ξ)=exp(−τ/2)L_j(τ) for τ=π(x²+ξ²), with L1=1−τ and L2=1−2τ+τ²/2. The true Gaussian-relative weighted squared gain is F_w(τ)=wL1²+(1−w)L2², w∈[0,1], τ≥0. At τ0=3−sqrt5, L1(τ0)=sqrt5−2 and L2(τ0)=−(sqrt5−2), so every w obeys inf F_w≤9−4sqrt5. For w*=1−1/sqrt5, the exact certificate F_w*−(9−4sqrt5)=(sqrt5/20)(τ−τ0)²((τ−1−sqrt5)²+4) is nonnegative on all reals with unique equality radius; independently verified symbolic difference identically zero. Differentiating at interior τ0 forces unique optimal w*. The Gaussian factor decays, so theorem is only Gaussian-relative, not uniform unweighted inversion; no global nonlinear STFT phase-reconstruction guarantee.

## originality

PASS

Alaifari–Yang primary work establishes multiwindow STFT ambiguity deconvolution and Hermite–Laguerre multipliers, but inspected Sections 2.2 and 3.2 do not give this exact h1/h2 global weighted minimax value or unique allocation. The same-day published three-window h1/h2/h3 optimum, read in full, places weight zero on h2 and optimizes using h1+h3; it neither implies nor states the constrained h1+h2 optimum. Gaussian+h1 disk-weight problems use different window pair and a finite unweighted disk. No stronger/identical read result covers the submitted two-window theorem; historical priority remains best-of-knowledge.

## value

PASS

The smallest natural pair of non-Gaussian Hermite ambiguity windows has different radial zero circles. Its sharp normalized all-radius noise amplification margin and unique optimal acquisition split are mathematically motivated exact design information, with a nontrivial SOS lower certificate and full equality geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
