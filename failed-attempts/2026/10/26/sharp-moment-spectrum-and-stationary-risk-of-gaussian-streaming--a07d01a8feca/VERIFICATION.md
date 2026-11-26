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

PASS

Set S=ΣRᵢ²/σ² and Wᵢ=Rᵢ²/(σ²S). The chi-square total is independent of the Dirichlet proportions, and selection depends only on the latter. For m>1, E[W_I^(−p/2)] is comparable to E[W₁^((α−p)/2)] since ΣWᵢ^(α/2) is uniformly bounded above and below by positive constants. The beta density gives p<d+α; S contributes p<md. Both endpoints are excluded, and m=1 reduces directly to the chi law. The selected direction is uniform and the selected measurement independent with finite nonzero moments of every positive order. Orthogonality gives the innovation as a norm lower bound, with the triangle inequality giving finite-time finiteness below threshold. For d≥2, E||Qv||^p=q_p||v||^p with q_p<1 provides a summable backward series in L¹ and finite p-moment by Minkowski or subadditivity. Synchronous contraction conditional on arbitrary finite initial displacements proves uniqueness without assuming second moments; for d=1 the update is a fresh draw. Orthogonality transfers divergence to stationarity. At α=2 the selected proportion is its size-biased beta; multiplying its negative moment by the independent chi-square negative moment gives the stated gamma formula (the m=1 simplification is consistent). At p=2 the innovation contributes mτ²/[σ²(md−2)] and the contraction is 1−1/d, giving the stated risk including the divergent cases.

## originality

FAIL

The frozen fresh-response chain is not the same chain as the fixed-response Resultary result. However, all claimed formulas and sharp moment boundaries transfer from its explicitly covered centered, constant-nonzero-response special case: changing the offset multiplies the same innovation by an independent scalar with every positive moment, preserves the projection contractions, and rescales the forcing in the risk recursion. The closest catalogue entry is dated later; the finding here is mathematical coverage in the material now available, not a claim of historical priority.

## value

FAIL

The two competing small-radius mechanisms and the stationary risk are worthwhile in stochastic projection methods. But the same threshold, radius formula and affine risk/uniqueness mechanism are already established by the comparison; adding an independent light-tailed multiplier neither uncovers a new sharp mechanism nor requires a new invariant estimate. The frozen record does not classify the fresh-response invariant law beyond those transferable facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
