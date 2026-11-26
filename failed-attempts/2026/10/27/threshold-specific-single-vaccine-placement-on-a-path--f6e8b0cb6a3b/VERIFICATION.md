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

A fixed seed on a path reaches precisely the vertices connected by retained independent edges. Summing the resulting infected-size probabilities over all M unvaccinated seeds gives the numerator without any extra size normalization. For a piece of j=s vertices the source-weighted tail is s p^(s-1); adding a rightmost vertex to a piece of j>=s increases the weighted tail by 1 if the joining bond is open and the old terminal component has at least s vertices, by s if the bond is open and it has exactly s-1, and by zero otherwise. The mean increment is p[p^(s-1)+s(1-p)p^(s-2)], giving the frozen affine formula. When exactly one gap is short, extending it strictly improves the risk until it reaches s-1; the two-long numerator exceeds that optimum by (s-1)p^s. If both gaps can be short they give exactly the zero optima. The assumptions s=1, s>M, and strictness for 0<p<1 are all handled. The expected cluster size uses pair connectivity p^distance, and its piecewise forward differences are strictly increasing with length, giving exactly the central splits. For M>=4 the stated two thresholds have incompatible minimizers, whereas for M=2,3 the central splits minimize all tails. The five-vertex numerical example is correct. `python3 /workspace/reviews/replay_finite.py 1` used independent left/right truncated geometric reach distributions and checked 342 exact all-placement threshold cases and 36 mean minimizer sets through M=13. The frozen program and recorded verification were inspected, not executed.

## originality

FAIL

The one-vaccine threshold law is mathematically covered by two complementary indexed records under exactly the same percolation and source convention. For s>=3, 201e633bac83 states the identical single-gap weighted tail formula and its strict profile optimization uses only two-gap moves and the number of gaps, so it mechanically gives the stated one-vaccine result (or restrict the three-gap model to profiles with one gap identically zero). For s=2, 194241dddabb already gives the full optimum, central mean minimizers, and the sharp disjointness threshold. Since E[C] is the sum of integer upper tails, disjoint s=2/mean optima already preclude the existence of a simultaneous all-tail minimum. The n=3,4 positive boundary and the n=5 instance are immediate substitutions. This is verified coverage, not a priority decision based on catalogue dates.

## value

FAIL

The all-threshold question is well motivated, but its evaluated optimizer sets are obtained by restricting the established gap analysis, while the sharp stochastic-minimum cutoff is an immediate implication of the already known mean and first-transmission conflict. The small instance and combination of known regimes do not provide an independently valuable new remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
