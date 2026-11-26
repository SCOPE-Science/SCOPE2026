# Independent mathematical audit

## correctness

PASS

Each vertex in one induced facet is a sink with probability p=2^(1-d). With 2^(d-1) vertices and d-1 ordered neighbors per vertex, the variance is 1-dp; only adjacent sink indicators have negative covariance. Opposite facets use disjoint edges. For adjacent facets the shared vertex can be a sink in both iff all d incident edges point in. The contribution summed over the 2^(d-2) shared vertices is 1/4-2^(-d); the only other overlapping demands are ordered adjacent pairs inside the intersection, giving -(d-2)2^(-d). The sum is positive iff d≥4. At d=2 there are no shared edges; at d=3 conditioning on the sole shared edge leaves independent residual orientations. Reversing that edge preserves each square's conditional sink-count law by reflection, so the mixture is still independent. For the quantitative limit, each intersection vertex supports three mutually exclusive atoms requiring d directions; exterior atoms require d-1. Total atom means are 3/4, 3/4 and 1/4, with common atoms counted in both coordinates. The same-or-neighbor vertex neighborhoods have ≤3(d+1) indices, so b1≤(7/4)·3(d+1)·2^(1-d). Distinct same-vertex atoms are incompatible, and adjacent vertices' requirements overlap in at most one Bernoulli edge; b2≤2b1 and b3=0. The published AGG process bound 2(2b1+2b2+b3) uses doubled TV, yielding ordinary TV ≤63(d+1)2^(-d). The grouping map contracts TV and gives the specified independent Poisson marks, hence the joint no-sink limit e^(-7/4). The opposite pair has independent marginals with the same Poisson(1) limit. Replay: frozen RESULT.md §§1–4 and AGG Theorem 2, printed pp. 10–12. The uploaded checker was inspected, not run; its finite independence calculation reports the Boolean, and the dimension-uniform result rests on the proof, not the finite calculation.

## originality

PASS

The surviving claim is a joint law and exact dependence classification for two specified induced facets under independent fair orientations. The general Chen–Stein method and its use on the whole-cube sink count are prior. The specific shared-edge covariance/independence analysis and positive limiting common component are not stated or mechanically supplied by the inspected prior claims.

## value

PASS

A natural joint statistic shows a finite independence threshold invisible to either facet marginal and persistent dependence even while each count becomes Poisson. The exact common intensity distinguishes adjacent from opposite facets, for example e^(-7/4) versus e^(-2) for joint absence. The classification and quantitative joint approximation are useful benchmarks for dependence among local optima on cube faces, without requiring the TV prefactor to be sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
