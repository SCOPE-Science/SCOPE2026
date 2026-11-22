---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For any real input on K_{a,b}, coarea reduces edge-TV bounds to cut indicators. Bernoulli differences P−Q for the two part choices and integrality b−ell≥a−k+1 (or its negative-delta counterpart) force the sharp 2(b−1)/b partwise centering bound; the B-only projection has the same bound by scalar ℓ1-centering and Jensen. Laplacian modes b,a,a+b then give H_t edge differences as the nonnegative-coefficient combination (r−s)T_B+(s−z)T_AB+zI with r=e^(−at), s=e^(−bt), z=e^(−(a+b)t). The bound is attained by a B singleton for every t, yielding exactly 2(b−1)/b r−(b−2)/b z. Its derivative has sign (a+b)(b−2)e^(−bt)−2a(b−1), proving the b−a≤2 threshold, unique positive peak otherwise and b→∞ limit two. The a=b=1, t=0 and b=2 cases are covered. Independent rational small-graph cut enumeration reproduced 1,257 inequalities and all singleton equalities; it corroborates rather than replaces the general proof.

## originality

PASS

PASS for the actual all-time graph BV norm and sharp bipartite centering lemma, with strong prior credit: complete-multipartite edge-TV literature already determines contractivity and Lipschitz-heat calculations already give the same scalar profile for a different seminorm. Neither equality of the numeric profiles nor the threshold alone yields the graph-TV operator inequality for all real signals; the centering argument supplies that missing implication. Potential old polyhedral/Markov ℓ1-gradient norm aliases remain a priority risk.

## value

PASS

Edge-gradient ℓ1 total variation is a natural stability quantity for finite graph diffusion, distinct from the Lipschitz sup-edge gradient. A sharp *all-time* seminorm and extremizer with the exact amplification transition is mathematically more informative than known sign-of-derivative thresholds. The cross-difference centering inequality is a reusable structural lemma, not a direct renaming of the earlier Lipschitz theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
