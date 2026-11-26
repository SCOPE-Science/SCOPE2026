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

Uniform compositions are fair independent internal cuts with forced exterior cuts. Interior indicators for size r use r+1 consecutive positions and boundary effects are bounded at fixed m. In the covariance sum for r,s, offsets outside [−s,r] are independent; the two touching offsets give joint density 2p_r p_s, strictly overlapping distinct intervals are incompatible, and coincident intervals add p_r when r=s. This recovers the stated covariance per n. Fixed-width gaps between blocks of length floor(n^(1/4)) leave discarded variance o(n); the centered block bound is o(sqrt n), so the independent-block CLT applies to each projection. Independently, coefficient extraction from the first and mixed marked derivatives gives the exact finite covariance for n>r+s, with n=r+s treated using the constant coefficients, and n<r+s using impossibility of simultaneous occurrence and positive individual means. These three regimes give strict negativity for all distinct r,s≤n, including the marginal singleton-doubleton pair despite its zero limiting off-diagonal coefficient. The quadratic form is (1/2)Var(h(G)−λG) with Geom(1/2) length G, h truncated to the first m values and λ=E[h]/E[G]. A zero variance forces λ=0 on the infinite tail, then h=0. Woodbury with rows p_r(1,r) gives the inverse of the inner 2×2 block [[a_m,−d_m],[−d_m,−e_m]], yielding exactly the displayed precision. Its off-diagonal numerator is minimized at {1,2}, with value 1−(m²+m+2)/2^(m+1), zero at 2 and strictly positive from 3 onward by induction. Rescaling the precision by Δ_m gives entrywise ij/2 for fixed indices including the diagonals, so the normalized negative ratio tends to −1. The provided finite rational script was inspected, not executed; the argument covers the universal claims without it.

## originality

PASS

The uniform-composition marking function, fixed-dimensional CLT and a general formula specializing directly to the covariance are prior. Exact finite mixed moments are obtainable by coefficient differentiation. The distinguishable result is the explicit evaluated precision and its global off-diagonal sign classification and dependence on the observed size cutoff, rather than the underlying covariance or a new general Gaussian limit theorem.

## value

PASS

The first m positive part lengths are a natural increasing observation scheme, and the precision asks which dependencies survive after adjusting for all currently observed lengths. The complete sign classification, its two-dimensional exception, and degeneration to −1 show when the fixed-sum constraint becomes visible through Gaussian conditional dependence. That is a sharper structural consequence than any one marginal covariance or a table of a few small dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
