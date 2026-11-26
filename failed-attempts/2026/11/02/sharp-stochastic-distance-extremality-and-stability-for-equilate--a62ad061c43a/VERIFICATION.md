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

For same-edge samples (probability 1/m), distance is |U−V|. For any distinct pair, distance is δ+U+V where δ counts intervening edges, since the geodesic exits and enters at fixed endpoints. A pendant edge can have at most m−1−k other edges with separation at least k for 0≤k≤m−2: if a far edge exists, a route to it exhibits k closer intervening edges. Deletion preserves all other separations; induction gives the sharp path count binom(m−k,2). The star has δ=0. Applying the common nonnegative-noise kernel and the identical same-edge mixture proves FOSD. Below threshold 1 the only contributing distinct pairs are incident pairs, giving the stated coefficient. The identities A−(m−1)=Σ_v binom(deg(v)−1,2) and A≤binom(m,2) with equality iff all edge pairs meet give the two uniqueness conclusions. The mean is 1−2/(3m)+2Σδ/m², with Σδ=Q by counting intermediate edges via cuts. Q for the path counts triples by the middle edge, and Q for the star is zero. Ordered real laws have W1 equal to the mean difference. Each internal edge contributes at least m−2 since its positive cut sizes sum to m−1; equality forces just one such edge with cut sizes 1 and m−2, precisely the subdivided-edge star, including m=3. The endpoint mean and W1 constants follow. Independent line-graph BFS checks on 5910 increasing-label trees corroborated the discrete tails and sharp gap.

## originality

FAIL

The frozen result is correct, but its main whole-law comparison is a direct consequence of an earlier componentwise extremal theorem for complete discrete distance sequences (Dankelmann, arXiv:2411.13439, Lemma 2), combined with the already known edge/vertex-Hosoya identity and the elementary uniform-edge sampling kernel. This is verified prior implication, not an inference from matching titles, means, or unavailable literature. The small-distance coefficients are read directly from the adjacency count under that kernel. The transport conversion uses ordered-law mean differences, and the second-minimum cut sum and shape are already the unit-weight case of Wang–Hu's second-minimum Wiener theorem. The exact continuous wording need not appear in those sources for the claim to be covered.

## value

FAIL

The continuous stochastic interpretation is useful as an exposition of the discrete ordering, but the asserted advance is a direct equal-edge sampling conversion of the known distance-sequence order. The local tail formulas are the first mixture coefficients, and the nonstar gap is the known discrete second-minimum Wiener value in the corresponding W1 units. No distinct independently useful new invariant, threshold or stability phenomenon survives those reductions in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
