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

For a nonedge the first nonzero walk coefficient is B=(L²)_ij>0 by support diameter two. Set t=εu and divide by ε²u, extending analytically at the removable zeros. The terms linear through cubic in t give B(u/2−1)+εC(u−u²/6)+O(ε²), C=(L³)_ij, uniformly in C¹ on [0,3]. The positive derivative and opposite endpoint signs give a unique zero in that interval, and implicit differentiation at u=2 gives u′(0)=−8C/(3B). Uniqueness on this scale does not establish all-time uniqueness; separately, on 3ε≤t≤t₀ the leading term B(t²/2−εt) is at least Bt²/6 and the Taylor error divided by t² is O_G(t₀+ε). Beyond t₀ the ordinary heat entries have a strictly positive uniform lower bound by irreducibility and convergence to J/|V|. The sup in time of the spectral multiplier perturbation is at most ελ_max/e; the zero eigenspace is unchanged. On edges the initial term tw_ij dominates the O_G(t²+εt) corrections, and diagonal positivity is immediate by positive definiteness. Thus the largest nonedge root is the full positive-time cutoff, with t=0 also entrywise nonnegative. The finite maximum selects the minimum C/B at second order; it does not break ties. Independent replay: python /workspace/replay/checks.py 1 uses 52-digit spectral computations on three diameter-two examples, checks the reported eight integer-example ratios exactly and confirms the predicted scaled root correction and sampled signs. Only the analytic estimates prove the all-time statement. The coupling radius and remainder are for each fixed weighted graph, not uniform over families.

## originality

PASS

The exact mixed-kernel sign behavior and special-case expansions are covered on some indexed unweighted classes. The supported distinct result is their weak-coupling extension to arbitrary positive weights on arbitrary fixed support-diameter-two graphs, with a nonconstant pairwise three-step correction and all-time exclusion of further zeros. The mathematical scope comparison does not assert historical first publication.

## value

PASS

The result locates the genuine last sign obstruction for arbitrary fixed weighted diameter-two diffusion and proves there is no later sign reentry; a purely local zero calculation would not do that. The leading scale is universal while the three-step ratio selects the obstruction from competing nonedges. This is a graph-wide sharp stability statement in a natural mixed-diffusion regime, not an evaluation of a known family-specific root formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
