---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The displayed limits, extremizer locations and normalization hold. The Sturm–Liouville primitive equals -(1-x²)^(λ+1/2) p'(x)/[n(n+2λ)]; its endpoint values vanish, and the Sonin energy derivative has sign -λ for x>0 off the zeros. It orders the absolute primitive values at zeros as stated. Dividing the classical norm by the square of the endpoint value gives h = 2^(2λ-1) Γ(λ+1/2)² Γ(n+1)/[(n+λ)Γ(n+2λ)], tending to (π/2)e^(-2τ) in the moving window. The odd-degree central derivative and even-degree center ODE give nM ∼ a_(floor(n/2),λ) ∼ n^(-λ) when λ≥0 tends to zero. On the negative side, the normalized endpoint hypergeometric expression tends to cos z in C¹ on compact intervals; the first rescaled zero tends to π/2 and the weighted derivative contributes n^(-2λ). The frozen differentiated-series majorant is too small near z=0 if read as a pointwise bound of order |z|^(2j) on differentiated summands. For j≥1 one may instead use 2^(1-j) j |z|^(2j-1)/[(1/4)_j j!], since |(-n)_j(n+2λ)_j|≤2^j n^(2j) and s=(1-cos(z/n))/2 obeys |s|≤z²/(4n²), |s'|≤|z|/(2n²). The resulting compact-set majorant is summable, so the claimed convergence and limits follow. The sign-changing τ=0 case is covered by the coinciding limits. BV integration by parts and a unit jump prove the sharp norm. The attached script was inspected, not run. The rejection is for prior implication, not a counterexample to the theorem.

## originality

FAIL

This is a direct leading-term corollary of published uniform Gegenbauer asymptotics applied to the shifted derivative index, plus Wang's exact maximizer comparison and the classical norm and BV duality. It matters that the shifted index is 1+λ, positive even on the negative side of the proposed window. Comparing only the unshifted index, or treating Dunster as a fixed-λ estimate, misses that coverage. The precise implication is detailed below; no exact match of phrasing is required.

## value

FAIL

The kink and the jump-location interpretation are natural and useful as an exposition. As a new mathematical finding, however, the first-order law is obtained by direct normalization and evaluation of already published uniform polynomial asymptotics at already known maximizers. No novel extremizer result, error bound or higher-order term remains in the frozen claim. Correcting the summand majorant would not supply such a remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
