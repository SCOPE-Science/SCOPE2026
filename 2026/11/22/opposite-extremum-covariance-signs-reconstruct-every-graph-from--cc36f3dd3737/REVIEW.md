# Self-review

## Correctness — PASS

The statements quantify over all finite labelled simple graphs, iid atomless vertex scores, and distinct vertex pairs. Adjacent covariance positivity follows by conditioning on the higher-ranked endpoint and gives a uniform explicit lower bound. For nonadjacent vertices, conditioning on common-neighbor priorities yields opposite monotone functions of their minimum/maximum and strictly negative covariance whenever there is a shared neighbor; with no shared neighbor the indicators are independent. The explicit joint-probability integral follows by partitioning neighbor sets, and its binomial integration is exact. The recovery guarantee uses Hoeffding bounds for at most \(n(n+1)\) empirical means and a verified covariance margin. Exhaustive exact checker: 1,098 labelled graphs, 74,708 assertions, up through five vertices. The finite computation is supplementary, not offered as proof for general graphs.

## Originality — PASS, with residual risk

Closest checked primary sources: Billey–Burdzy–Sagan (2012), arXiv:1209.0693, fully accessible HTML, including section on peaks and valleys on paths; Billey–Burdzy–Pal–Sagan (2013), arXiv:1308.2183, full HTML with cycle-local extrema; and Diaz-Lopez et al. (2017), arXiv:1708.08493, accessible full HTML on enumerating general-graph peak sets. None of the materially inspected results states or directly implies the arbitrary-graph opposite-extremum covariance sign law or its quantitative graph reconstruction. Published graph-covariance tomography for vertex-threshold subgraphs uses an unrelated edge-threshold degree vector. A separately catalogued aggregate peak/valley covariance on complete bipartite graphs is a different statistic and does not settle signs for all ordered vertex pairs across all graphs. Residual risk: an equivalent theorem may exist under random-ranking, acyclic-orientation or local-extrema terminology outside indexed search; the originality claim is best-knowledge and not a certificate of historical uniqueness.

## Value — PASS

The exact sign matrix recovers the full labelled adjacency relation from local-ranking extrema alone and simultaneously identifies graph-distance-two pairs. The adjacent-edge lower bound enables a nontrivial finite-sample identifiability theorem using only simple Bernoulli observations. These are meaningful structural and statistical results, rather than an arbitrary small-graph table, routine restatement of a known enumerator, or a small parameter increment. The polynomial sample bound is conservative; optimal inference and noisy observation are not claimed.

Self-review: passed. Independent audit: not yet performed.
