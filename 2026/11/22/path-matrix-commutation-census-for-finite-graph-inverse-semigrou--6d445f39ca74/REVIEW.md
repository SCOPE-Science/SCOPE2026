# Independent mathematical audit

## correctness

PASS

Reassessed /workspace/repairs/5/RESULT.md. The frozen Finding overstated the matrix-only input for individual centralizers; the repair distinguishes the aggregate count from an individual query with its concrete path-pair argument and gives a chain example where the same terminal vertex yields sizes 11 and 9. For each terminal v there are p_v^2 normal forms. In a DAG distinct paths ending together are prefix-incomparable. A nonzero commuting product of two off-diagonal pairs would force each of the second pair's paths to be a common prefix of the first pair's paths; those prefixes are comparable, a contradiction. With an idempotent, either both tested paths fail prefix comparability (both products zero), or both satisfy it (the products agree). The independent baseline for nonzero elements contributes Q+sum(A_vw^2), by counting pairs whose tested paths are incomparable; the comparable pairs omitted from the baseline are exactly the diagonal correction sum_alpha sum_w c_w(alpha)^2 and the off-diagonal common-prefix count. A proper prefix contributes once, an extension contributes the square of a suffix-path count in the diagonal correction, and distinct extensions give m_vw*(m_vw-1) in the off-diagonal correction. Counting prefix-suffix splits gives their total as 2*sum(p_v*m_vw^2)-sum(p_v). Zero as first element contributes 1+Q; the baseline already includes zero as second element for each nonzero first element. This also handles isolated vertices, parallel edge identities, and the empty graph (Q=K-1=0). A separate direct finite partial-map composition replay matched all centralizers and K on 35 DAG multigraphs; no frozen script was executed. The general proof, not the finite replay, establishes the formulas.

## originality

PASS

For the corrected claim, the path-pair formalism, general partial-injection commutation test and Brandt-class structure are prior. The repair credits Bardyla's cross-class product information as well. The checked work does not perform the exact cross-class counts or aggregate them into a vertex-matrix formula; the nearby Resultary census is for a different semigroup.

## value

PASS

The corrected aggregate claim computes a natural statistic of the semigroup from vertex-indexed data without constructing its exponentially many paths or still more path pairs. It handles cross-class interactions and multiplicities, where individual matrix-unit counts alone do not recover the statistic. The separate prefix formulas explain local commutation and provide efficient targeted queries without promising the entire per-element output at vertex-matrix cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
