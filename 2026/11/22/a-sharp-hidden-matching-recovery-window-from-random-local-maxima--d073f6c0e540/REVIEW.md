# Scientific review: hidden-matching recovery from local maxima

## Correctness — PASS

The event decomposition is exhaustive: a maximum-priority vertex is always a peak, and only its one nonneighbor can also peak; that nonneighbor peaks precisely when it is second in priority. Both singleton and two-peak probabilities sum to one. Because the singleton likelihood is independent of the missing matching and every two-peak event reveals an actual missing edge with equal probability, the uniform prior stays uniform over completions. This establishes the exact minimax posterior identity. Factorial moments of unseen pairs prove the critical Poisson law and the explicit hyperbolic-cosine curve. Negative pairwise covariance of unseen indicators proves the subcritical side. Exhaustive permutation tests for every perfect matching through six vertices and exact rational checks support the finite identities; the infinite results use analysis, not the finite tests.

## Originality — PASS, with residual priority risk

Burdzy and Pal, *Twin peaks*, arXiv:1606.08025 (first public posting June 26, 2016), investigate local-maxima positions conditional on one or two peaks, especially on tori, ladders and trees. Their primary full HTML does not supply a hidden-matching inference problem or its minimax recovery law. The classical coupon collector provides the unseen-coupon limit, but not the exact observation channel, uniform-completion likelihood, or recovery profile. Published graph reconstruction by covariance of maxima and minima is different data: it uses both extrema and does not supply an exact sample-complexity transition for peak-only observations. Other graph tomography results likewise use degree or threshold-graph observations. Overlap searches found no direct covering claim; absence of a search hit is not a mathematical proof of priority. Possible unindexed statistical reconstruction literature remains the main risk.

## Value — PASS

Random priorities provide a natural repeated observation mechanism when only the locations of local maxima are accessible. The matching-deleted complete graph is the sharp dense test case: one nonedge can only be exposed when its two endpoints lead a random ranking. The exact minimax law describes both an information-theoretic lower bound and an attaining estimator; the transition scale is \(\Theta(n^2\log n)\). The curve differs from the ordinary full-coupon-collection probability because the last unseen edge is uniquely determined by the remaining two labels, and two or more unseen edges leave ambiguous completions. The explicit critical recovery probability therefore makes a substantive inference distinction, not merely a rephrased coupon collector.

## Scope and limitations

The result assumes a known labelled vertex set, a known complete-minus-perfect-matching graph family, independent uniform random priority orders, and full visibility of the local-maximum vertex set. It does not establish a general-host-graph minimax rate. The source comparisons cannot exclude an equivalent theorem in historical literature not indexed or available for examination. Numerical tests do not substitute for the analytic asymptotic proof.

Self-review: passed. Independent audit: not yet performed.
