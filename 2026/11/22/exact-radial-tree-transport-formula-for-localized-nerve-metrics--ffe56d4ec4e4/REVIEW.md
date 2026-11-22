# Mathematical review

## Correctness

**PASS.** The source cost and the explicitly defined radial tree agree on all possible center/shell/outside pair types, using only the ultrametric inequality. The shell dendrogram has nonnegative edges because the shell diameter is bounded above by its radius; the trunk is monotone. The classical tree flow-balance identity then proves the exact transport minimum for arbitrary real probability weights, including identified zero-cost outside sites. The code independently compared all pair distances and 7,920 optimal-transport evaluations across 3,960 generated center/radius instances. The argument's correctness does not depend on the numeric experiments.

## Originality

**PASS on inspected sources, with priority risk.** McCabe–Perea [1] define the exact localized cost and prove pseudometric and nerve stability statements, but their §3 does not identify the restricted cost as a radial tree pseudometric on finite ultrametrics, nor give a mass-cut evaluation formula. Skandalis–Valette [2] and Chen–Tabaghi–Wang [3] provide the established tree transport machinery, but not the nontrivial radial realization of the localized cost. Semantic searches of an indexed mathematical research database found related ultrametric and transportation claims but no covering statement. This is an evidence-based literature comparison, not a proof that an equivalent source cannot exist.

## Mathematical value

**PASS.** The result computes an entire recently introduced topology-relevant optimal-transport metric without a transport optimization on a natural hierarchical class of data. It applies uniformly to every finite ultrametric, scale, pair of probability weights and center, providing an explicit formula suitable for comparisons of hierarchical landmark weights. The four-point non-ultrametric obstruction clarifies why the exact decomposition has structural content rather than following for arbitrary metrics.

## Closest literature and limitations

[1] McCabe and Perea, *Wasserstein Stability of the Nerve Map*, arXiv:2611.15938v1 (2026-11-11), https://arxiv.org/html/2611.15938v1. Original definition, metric and nerve-map stability bound, not the radial-tree special case.

[2] Skandalis and Valette, *On the transportation cost norm on finite metric graphs*, arXiv:2601.16859v1 (2026), https://arxiv.org/abs/2601.16859. Tree-flux transport framework, not the localized cost realization.

[3] Chen, Tabaghi and Wang, *Learning Ultrametric Trees for Optimal Transport Regression*, arXiv:2210.12288 (2022), https://arxiv.org/abs/2210.12288. Standard ultrametric-tree and transport framework, not the nerve metric.

Only finite ultrametrics are covered. Priority risk from unindexed equivalent literature and independent mathematical review remain unresolved.

Self-review: passed. Independent audit: not yet performed.
