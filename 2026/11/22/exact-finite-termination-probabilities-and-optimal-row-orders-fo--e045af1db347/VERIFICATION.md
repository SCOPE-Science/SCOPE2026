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

For a consistent system the linear error projector is v_j v_j^T for a unit tangent v_j. Composing these rank-one matrices gives the endpoint outer product times the adjacent cosine factors, so a zero operator is equivalent to at least one adjacent orthogonal pair. At odd n the factor minimum is sin(pi/(2n)); its equality edges have modular steps ±(n−1)/2, forming one cycle by coprimality. Cutting and orienting it gives exactly 2n minimizing paths (including n=3). At n=2m the orthogonal pairs are disjoint. Compressing any j specified pairs gives 2^j(n−j)! orders, and binomial inversion of these joint counts yields every mass of X, including n=2. For j≤n^(1/3) the product over s<j of (1−s/(n−s)) expands as 1−j(j−1)/(2n)+O(j^4/n^2); the ratio product is at most 1, so factorial tails justify the summed error and dominated binomial inversion yields Poisson(1). The iid no-hit probability is (1−1/n)^(n−1) by constant conditional hazard; its first correction has the opposite sign from reshuffling's. The regular frame average of the projectors is I/2 for either parity, so iid exact squared-error contraction follows by conditioning. Independent bounded enumeration reproduced even n=4 counts [8,8,8], even n=8 counts [13824,15744,8064,2304,384], and 14 minimizing orders at n=7 (replay: /workspace/branches/87f708e6-b35f-423e-9ac7-3b1711c779b2/independent_check_record2.py and accompanying check_n*.txt). Read but did not execute the frozen verifier; its cosine tests are finite diagnostics, not independent matrix-product tests or an all-size proof. Termination here is of the whole error operator in exact arithmetic, not of a special starting vector or a perturbed system.

## originality

PASS

The supported distinct result is the exact distribution of zero-producing adjacencies for this reshuffled planar sweep and its quantitative comparison with exactly n iid draws, alongside the all-orders extremal classification. The planar geometry, cyclic rate, projection-angle argument, matching block count and iid framework are not themselves new. The strongest compared records do not establish the combined exact sweep comparison, in particular the opposite signed 1/n corrections.

## value

PASS

This standard planar test geometry gives a sharp, interpretable distinction between two natural sampling schemes: the same leading one-sweep extinction probability masks opposite signed finite-size corrections, although the iid mean-square rate alone cannot show that. The count law and all-optimizer classification supply useful exact benchmarks beyond the known natural cyclic sweep. The value is not a universal reshuffling claim or a new generic combinatorial technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
