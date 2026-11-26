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

Independently reconstructed RESULT.md lines 32–88. Eliminating the ungrounded leaves at a free hub with a grounded opposite hub and a grounded leaf gives residual diagonal t+1; the inverse has N−2 unit eigenvalues and the two stated roots. For the same-side hub–leaf placement the free-hub inverse is diag(0,I_a)+(1/t)11ᵀ. The largest special eigenvalue exceeds that of the cross-side placement by principal-submatrix comparison and strict increase in the rank-one coefficient; its special-pair sum is strictly larger too. These strict weak-majorization comparisons imply strictly larger power sums for r≥1. For cross-side placements increasing a increases the pair sum at fixed product, hence increases the larger root and the power sum. With both hubs unpinned, the two-hub inverse has diagonal (1/2,1/2+1/t) for two same-side pinned leaves (pinned side first) or ((t+1)/(2t+1),(t+1)/(2t+1)) for oppositely pinned leaves. The trace is N−2 plus each diagonal weighted by one plus its number of unpinned leaves. Both yield strictly more than N, so Jensen excludes every leaf–leaf pair at all r≥1. The hub–hub cost is N. These comparisons give all equality cases, including either cross orientation when p=q. The trace derivative in t is strictly negative; the power sum starts above 2 at t=0+ and tends to 1. As a function of r its strict convexity and value 2 at r=0 put every positive-order root on the increasing branch, yielding strictly increasing t_r. The root sum/product give the stated t_1,t_2. As r→∞ the threshold must diverge because the larger root exceeds 1 at any finite t. Then the smaller-root power vanishes and r log α_+ tends to log 2, while (t+1)log α_+ tends to m−1, proving the slope. A fresh exact check enumerated 63 pairs at p=2,q=3 and t=3/4,1,5/4 at r=1, confirming both the asymmetric winners and the exact tie. Replay in the review workspace with `OPENBLAS_NUM_THREADS=1 python /tmp/opencode/frozen-review-diagnostics.py` (check 5). The frozen checker and verification notes were inspected, not executed; the exact check is supplementary, not a proof of arbitrary order or the asymptotic.

## originality

PASS

The first-inverse-moment placement and its exact threshold are established endpoint coverage, not a novel part of the finding. The distinct real-order optimum, strict migration, explicit r=2 disagreement and high-order slope survive the checked comparisons; same-day related records were compared without assuming priority among them. This is a best-of-evidence decision.

## value

PASS

Choosing which vertices to pin on this bridged two-community tree is a meaningful discrete decision. The theorem shows that different penalties on slow modes make strictly different choices on an explicit nonempty interval, classifies all ties, and quantifies how the bridge scale moves at large order. This goes beyond recomputing the known first-order endpoint or substituting a new objective at one placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
