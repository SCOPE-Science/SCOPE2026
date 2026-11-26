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

The probability-integral transform yields iid uniform edge weights and preserves the finite rankings almost surely even for a continuous CDF with flat intervals. With internal order statistics a≤b≤c on [0,1], the endpoints of c have threshold c and the third vertex has threshold b. All 3(n−3) outside edges are distinct, so the closure probability conditional on the internal weights is (1−b)^(n−3)(1−c)^(2n−6). Multiplying the integral by 6 and integrating first over a and then c gives 6/(2n−5) times ∫_0^1 b(1−b)^(3n−8) db, hence the stated finite mean after multiplication by binom(n,3). It gives 1 at n=3 and 4/15 at n=4. Distinct triples sharing a vertex cannot both be closed by outdegree two. For r disjoint ordered triples, edges to the n−3r outside vertices impose their own single-endpoint thresholds, and the finitely many edges between selected triangles impose maxima of two thresholds, each such edge counted just once. Under the scale n, the latter factors tend to one for any assignment of the sorted marks to the three edges. The former tend jointly to the product of exp(−b−2c). The number (n)_{3r}/6^r of tuples cancels the sorted density 6^r/n^(3r) in the limit. For n≥6r, domination by exp(−sum(b+2c)/2) on the product of ordered cones controls all fixed factorial integrals; in particular the first moment gives tail tightness for the whole finite measure. Joint factorial moments of continuity-set counts identify the Poisson law, and the bounded first moments and tight marks yield the finite point-process convergence. The intensity integrates to (1/2)∫_0^∞ b exp(−3b) db=1/18. Its mass for c≤t has derivative exp(−2t)−(t+1)exp(−3t) and value zero at t=0, matching the stated formula. The frozen VERIFICATION.md and CHECKER.py were inspected, not executed; the source's finite n=4 computation does not establish the limit.

## originality

PASS

The closest primary model match is Cooper–Frieze's symmetric random k-nearest-neighbor graph. The stated distinction between directed closure and undirected isolation is mathematical, not terminological: the latter adds the requirement that no outside vertex point into the triangle. The supported finding counts all directed closed triples including incoming arcs, and gives their full quantile-edge law. The original paper's exact isolation calculation was not recovered legibly; I do not exclude overlap with an ancillary calculation and do not rely on the isolation intensity quoted by the frozen record. The distinct same-date reciprocal-nearest-neighbor result has a different outdegree and concerns edge indicators and a variance, not closed directed triangle profiles.

## value

PASS

Directed sink triples are a natural minimal closed motif at outdegree two, including those hidden by an undirected isolation requirement. The quantile-weight profile quantifies their occurrence at every maximum-edge threshold, and the disjointness and joint Poisson law describe the population beyond a finite expectation or a single boundary check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
