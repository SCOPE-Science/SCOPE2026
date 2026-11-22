# Scientific review

## Correctness — PASS

The proof derives the two distinct conditional containment probabilities \((v-u)^2\) and \(2u(1-v)\) from independent uniform endpoints. Exact finite integrals yield the gamma-ratio expression and a finite binomial sum, and an explicit integral comparison with harmonic numbers establishes the leading constants and error terms. The included checker exhaustively enumerates all matchings through seven arcs and compares rational expectations, but the infinite assertions follow analytically. The continuous-CDF normalization relies only on almost-surely distinct endpoint ranks. No joint or distributional statement is inferred from mean formulas.

## Originality — PASS, with residual priority risk

Research-record searches for inclusion-minimal/maximal intervals, nesting-free arc frontiers, Pareto records on the endpoint triangle, and matching containment extrema found no statement implying these two exact means or their asymptotic ratio. A matched primary full-text comparison with Chen et al. (2005), arXiv:math/0501230, separates **nesting depth** and fixed partition-block endpoint sets from the counts of arcs with zero inner/outer inclusion degree. Justicz et al. (1990), DOI:10.1080/00029890.1990.11995679, uses the exact random-interval model, but its accessible abstract identifies disjoint packing and universal intersection questions, not inclusion frontiers; the complete original text was not accessible and remains the principal historical-priority limitation. General Pareto-record results with independent coordinates do not directly cover the triangular dependence of the endpoints. No claim of exhaustive literature coverage or mathematical independence is made.

## Value — PASS

Containment-minimal and containment-maximal intervals are the two intrinsic nonredundant summaries of a collection under inclusion. Their sizes provide natural storage and boundary-complexity invariants for interval covering and dominance queries. The result gives all-size distribution-free calibrations for each and demonstrates a structural difference of order \(\sqrt n/\log n\) between their *expected* sizes, with sharp constants, rather than a small numerical improvement or an arbitrarily chosen slice. It does not claim downstream statistical optimality or a full frontier limit law.

## Evidence and limits

The analytical derivations and `verify.py` support correctness. Chen et al. (2005) and the accessible abstract of Justicz et al. (1990) support the literature comparisons; the latter creates an explicit residual priority risk. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
