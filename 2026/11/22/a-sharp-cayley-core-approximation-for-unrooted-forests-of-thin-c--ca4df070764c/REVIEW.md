# Scientific review

## Correctness — PASS

Every acyclic incidence pattern has at most \(a-1\) large-side vertices of degree at least two, by the rank identity \(\sum(\deg(v)-1)=a-c\). Exactly \(a-1\) such vertices give a bijection to labelled Cayley trees, proving the full conditional law and exact leading count. The exhaustive second-coefficient classification into a two-component edge forest or one degree-three hyperedge plus an attached weighted Cayley tree yields \(H_a\); all lower-order patterns are uniformly bounded for each fixed \(a\). The total-variation constant follows by a controlled ratio expansion, and the binomial/CLT statements follow by transfer under vanishing total variation. Independent exact enumerations test the structural coefficients and forest counts. Risk: no uniformity as \(a\to\infty\), and finite checks alone do not prove the theorem; the written finite-pattern proof supplies the all-\(b\) argument.

## Originality — PASS (priority provisional)

Wu–Lu–Dong (2026) give a lower-bound family built from independently isolated-or-leaf large-side vertices, but do not classify or show dominance of the \(a-1\) degree-two connectors. Stones (2014) and Stark (2013) supply forest enumeration and a balanced-growth asymptotic respectively; neither contains the fixed-small-shore Cayley-core conditional-law/first-order total-variation theorem. Dong–Ge (2022) counts spanning-tree completions, which cannot imply a uniform-unrooted-forest distribution by changing wording. Published rooted-biclique forest and complete-split-graph spanning-tree comparisons use distinct probability measures or host graphs, and the two-hub \(a=2\) probability is acknowledged as known. Residual risk: an older unindexed fixed-width forest theorem may cover some or all claims; independent historical priority assessment remains pending.

## Value — PASS

The motivating sparse-side examples establish only that independent isolated-or-leaf states generate many forests. The mathematical gap is whether typical uniform forests have a connected core, what the core's law is, and how quickly the exact forest measure approaches a tractable model. The result answers all three: a sharp \(1/b\) total-variation scale with explicit coefficient for each fixed width, exact Cayley-tree conditional uniformity, and a giant-component/isolated-component limit law. This is a natural infinite family of randomly sampled unrooted forests, not an arbitrary selected statistic or a small finite recomputation.

## Closest literature and limitations

Primary materials reviewed: Wu–Lu–Dong, arXiv:2611.18076v1 (especially the sparse-biclique construction, page 3); Stones (2014), DOI 10.46298/dmtcs.1248 (component and edge-count enumeration); Stark (2013), DOI 10.1016/j.disc.2012.10.026 (asymptotic theorem and forest generating function); Dong–Ge (2022) (spanning-tree completions); and D'Achille–Enriquez–Melotti (2026) (complete-graph weighted forests). No claim of novelty for the known two-hub connection identity. Constants are only fixed-width asymptotics. Independent scientific assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
