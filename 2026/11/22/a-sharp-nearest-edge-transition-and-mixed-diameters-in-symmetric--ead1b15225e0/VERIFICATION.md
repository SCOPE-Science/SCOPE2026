---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Under total-entry-sum-one and full Frobenius normalization, each normalized hollow block has squared norm 1/(2ab); a star has squared norm (n+1)/(2n²), with its diagonal counted once. Top-right overlaps are coordinatewise minima in a and b; they do not intersect lower-left blocks even across different vertices, since simultaneous overlap would violate admissibility. This gives the three distance families in Proof §1. Hollow distances are strictly below 1/2 and star–star distances equal 1/n, so only H_(1,1)/interior-star pairs attain the printed larger diameter for n≥3; the n=2 star pair is checked separately. Strict convexity of squared distance in each argument shows that an arbitrary diametral pair must be a vertex pair. For a star in the top a rows, increasing b strictly decreases the mixed distance, then at b=n−a the resulting expression strictly increases with a, selecting a=1, i=1. Simultaneous reversal of the row and column indices gives the other minimum at i=n (ordinary matrix transpose fixes every vertex, so it is index reversal that is used in Proof §3). A nested hollow pair minimizes only if it differs by one step, since all steps have positive increments. For a crossing pair each exclusive support contributes at least 1/(4M_n), with joint equality impossible for n≥4: equality in b²≤2(b−1)b and c²≤2(c−1)c forces b=c=2, then a=d=1, whereas M_n≥(n−2)(n−1)>2. The forward difference of the cubic changes sign at b=(2n−4)/3, producing one maximizer except for two adjacent maximizers at n≡2 mod 3. The explicit n=2,3,4 comparisons and the bound M_n≥2(n−3)(n−2) for n≥5 complete the full-simplex comparison; rescaling b by n gives M_n∼4n³/27 and the stated ratio. The cutoff is at matrix order n=5, not affine dimension five. Replay RESULT.md Proof §§1–5; the exact-rational checker and its finite coverage through n=12 were inspected, not executed. This is a full-matrix metric result for the stated simplex, not a minimum distance between arbitrary points.

## originality

PASS

The full vertex description and the hollow-only minimum and minimizing pairs are already covered. The supported distinct claim is the mixed minimum and diameter classification in the full symmetric simplex and the exact order-five switch that results from comparing the mixed and known hollow extrema. The frozen record expressly excludes the hollow-only calculation from its priority claim.

## value

PASS

These are natural metric invariants of normalized symmetric Monge cost matrices. The smallest separation distinguishes nearest extreme cost patterns, and the diameter controls maximum separation. The exact equality cases expose a geometric contrast: the longest pairs remain mixed while the shortest pairs switch to hollow at a sharp matrix order. The full-dimensional classification and scale ratio add information beyond the vertex list and previously classified hollow face.

The dated certificate retains the supplied scientific assessment, sources and limitations.
