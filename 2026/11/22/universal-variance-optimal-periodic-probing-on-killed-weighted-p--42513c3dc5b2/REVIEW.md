# Scientific review

## Correctness — PASS

For every positive weighted path, a left/right fundamental-solution construction produces a Green matrix of the form \(G_{ij}=a_{\min(i,j)}b_{\max(i,j)}/\omega\), with strictly increasing \(a\) and decreasing \(b\). Squaring gives a positive sum of interval indicator outer products, and the independent Rademacher variance becomes a positive weighted sum of within-interval color-count squares. For each interval, the minimum possible integer count-square sum is attained by balanced counts; periodic coloring simultaneously balances every interval. Equality in all length-\(k\) windows forces periodicity, proving uniqueness. The exact rational checker independently verifies the critical formulas and all unlabeled partitions through seven vertices in three independent positive-weight families (14,337 assertions). Its finite cases are not used as an infinite proof.

## Originality — PASS, subject to publication-priority risk

The 2013 hierarchical-probing paper develops distance-coloring and incremental probing on toroidal lattices, not all-partition variance optimality for killed nonuniform paths. The full text of Frommer–Schimmel–Schweitzer (2020), especially Section 2.1, already writes the periodic \(k\)-class coloring for banded paths, but calls it optimal for *minimum number of colors subject to distance constraints*, not for global variance with \(k\) fixed. The full text of Frommer–Rinelli–Schweitzer (2023) establishes stochastic probing variance and analyzes its bounds, without the strict all-interval equality certificate for this weighted path class. An indexed exact even-cycle two-color theorem and an indexed complete-bipartite two-color transition cover different kernels and graphs. No implication from those inspected results yields the claimed all-\(k\), all-positive-parameter global theorem. Search/index coverage is not exhaustive; a relevant unindexed theorem or general interval discrepancy principle could affect priority.

## Mathematical value — PASS

The result determines a full finite-budget estimator design problem for nonuniform killed one-dimensional diffusion operators, rather than merely constructing a distance coloring. It rules out any beneficial irregular grouping even when edge and killing rates vary freely, and gives an exact nonnegative variance certificate and a local strictness gap for arbitrary competitors. This is an interpretable optimal-design guarantee, particularly where nonuniform inverse entry magnitudes make graph-distance heuristics a priori insufficient.

## Limitations and comparison risks

The claim assumes independent class-supported Rademacher probes, strictly positive killing, a simple path, exact linear-algebra operations and one solve per class. Neither general graph optimizers nor correlated/full-vector probe optimizers follow. Searchable mathematical records are not exhaustive; full text of closely related indexed even-cycle work was inaccessible and was not labeled as excluding the claim on that basis alone.

Self-review: passed. Independent audit: not yet performed.
