# Scientific review

## Correctness — PASS

The direction-specific confidence indicators, including the fact that a selected edge may update one endpoint without updating the other, are independently substituted into the three-agent path. For \(\sigma<2\varepsilon\), the two leaves are immobile because the minimum of each leaf's confidence score is \((1-\sigma)/2>\varepsilon\), using \(0<\varepsilon\le1/4\). For \(\sigma\ge2\varepsilon\), the symmetric initial profile is absorbing. On the remaining range, the center follows the exact gated fair-binary affine recurrence. The event of a length-\(m\) constant edge block gives a geometric tail for leaving the two-influence region when \(\varepsilon<\sigma<2\varepsilon\); infinitely many matching edges then force endpoint convergence. The full dyadic distribution and moment formula in the low-weight phase follow by induction, and almost-sure oscillation follows from independent blocks. The verifier checks representative finite rational trajectories, not the infinite-time theorem.

## Originality — PASS (best-knowledge comparison)

The initiating Krishnagopal–Porter model and its revised directional update appear in arXiv:2402.05368. The inspected full-text sections introduce the model and report numerical phenomena, including nonconvergent-looking opinion trajectories, but do not establish the complete three-agent, all-\(\sigma\) parameter classification with two exact threshold points. The pure neighborhood case \(\sigma=0\) and affine Bernoulli distributions are known constructions; these are not the claimed new contribution. The claim's distinguishing content is the **mixed-model** transition \(\sigma=\varepsilon\) from perpetual fluctuating opinions to almost-sure polarization and the further transition \(\sigma=2\varepsilon\) to exact stasis, producing the jump \(1/12\to1/4\to0\) in a fixed graph with fixed confidence and fixed initial opinions.

Zhang–Hong–Hu (2017) analyze fluctuations in a different nonlocal opinion model that assumes stubborn agents explicitly. Its accessible abstract describes a confidence-bound threshold and is a meaningful analogous result, but does not state the direction-specific NDW gate, the emergent immobility of the leaves, the two weight thresholds, or this exact limiting-variance triad. Access to that article's full text was not obtained; the degree of prior generalization remains a priority risk. Chu–Porter (2024) study random interaction times in conventional bounded-confidence rules, not the same neighborhood score. A nearby published mathematical research record analyzes a seven-agent switching system rather than this mixed NDW model.

## Value — PASS

The smallest connected network permitting different neighborhood means at two endpoints already exhibits three sharply distinct qualitative phases as one social-influence parameter changes while all other data are held fixed. More direct dyadic weighting first increases the asymptotic variance of the central opinion from \(1/12\) to \(1/4\) before suppressing it to \(0\); thus stronger individual similarity weighting is not a monotone regularizer. The paired exact thresholds and finite-commitment bound are a natural complete classification of this minimal three-agent test case, not an isolated numerical example.

## Scope and publication-priority limitations

The initial opinions are symmetric, the topology is fixed, updates are uniform and asynchronous with one edge per step, and the compromise weight is \(1/2\). There are no claims for general graphs, arbitrary initial conditions, or adaptive rewiring. The 2017 nonlocal-aggregation full text remained inaccessible; unindexed equivalent coverage is possible. The initiating February 2024 preprint's explanatory prose describes asymmetric receptiveness, while the later version explicitly prints the distinct direction-specific indicators used in this proof.

Self-review: passed. Independent audit: not yet performed.
