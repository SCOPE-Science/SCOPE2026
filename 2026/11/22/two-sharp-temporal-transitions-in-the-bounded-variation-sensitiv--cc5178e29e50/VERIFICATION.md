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

Orient all spokes out of the center and write their difference matrix as E. Then L=EᵀE and EEᵀ=I+11ᵀ. The edge map is onto, so the common absolute column sum of −(I+11ᵀ) exp[−t(I+11ᵀ)] gives the attained norm, including t=0. The off-diagonal changes sign at t₀=log(k+1)/k while the diagonal stays negative. The late derivative has the sign of −2(k−1)+(k−2)(k+1)²e^(−kt); its sign at t₀ is the sign of k(k−3). Thus at k=3 the right derivative vanishes only at the joining time and strict decrease still holds. For k≥4 this proves the cusp and the unique later peak. The displayed logarithmic derivative of the real extension of the peak is positive: the log term is at least log(25/3) and the negative rational part is bounded below by −2/15. Independently tested the actual vertex matrix E(−L)e^(−tL) on lifted coordinate columns at k=2,3,4,8,9,25 and checked the derivative identity symbolically and the two rational powers exactly (10330523392/10460353203 < 1 < 536870912/341796875). These finite checks supplement the all-k proof. The frozen Python code was read, not run; it records finite floating-point and rational comparisons, not a proof or formal certificate. Scope is unit masses, unit conductances and edge ℓ¹ on the combinatorial star.

## originality

PASS

There is stronger prior overlap than a mere analogy between scalar norms. The weighted-tree edge equation gives the star generator immediately, and the complete-bipartite edge-BV heat norm N_k gives the late branch by the exact relation D_k(t₀+s)=e^(−t₀)N_k(s), s≥0. In particular the shape of the rebound and the degree-four boundary carry over by scaling and translation; they are not credited as an unrelated discovery. The sharp temporal norm over the sign switch and, specifically, the unit threshold for the scaled peak and its strict ordering in k require an additional signed-column comparison and an all-size height inequality. The inspected prior results do not supply that comparison to the k-dependent level e^(t₀). Pass for that precise temporal classification, not for the evolution, edge reduction, or unscaled semigroup amplification.

## value

PASS

The norm measures the sensitivity of the heat trajectory's velocity to an edge-BV perturbation, not whether the trajectory itself smooths that perturbation. For degrees four through eight the temporal response rebounds but its secondary peak stays below unit gain in the fixed normalization, while the ordinary heat norm already amplifies. The degree-nine change is therefore a distinct, attained, sharp diagnostic across the whole natural branching family, not just a selected graph or a new name for the known contraction boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
