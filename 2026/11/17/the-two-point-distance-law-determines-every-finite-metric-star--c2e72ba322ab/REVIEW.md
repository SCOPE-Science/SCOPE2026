# Scientific review

## Correctness — PASS

Every step follows from intrinsic arm coordinates and exact area integrals: same-arm geodesic distances give \((\ell_i-t)_+^2\), and cross-arm distances give the stated truncated-square convolution. Expanding the exact tail near zero establishes total length and branch degree. Differentiating the piecewise quadratic formula yields signed knots with positive weight \(m-2\) at each arm and negative weight at each unordered pair sum. At the first arm length where two candidates disagree, their shorter lengths—and hence all possible pair sums at that value—agree; the positive coefficient forces equality. This proof handles repetitions and cancellations without a genericity assumption. The interval boundary is explicitly excluded from branching recovery. The standard-library checker passed 808 exact inversion cases and independent finite-grid integral comparisons.

## Originality — PASS, with residual historical risk

Searches for a metric-star arclength two-point inverse law and alternative names, plus publicly searchable research records, did not locate an equivalent exact injectivity theorem. Vershik's general metric reconstruction uses infinite distance-matrix distributions rather than a single pair-distance law. Chazal–Sun recover metric graph structure from much richer sampled metrics. The accessible full 2024 *Mean Distance on Metric Graphs* article computes only the equilateral-star mean in Example 4.1, not the full law or injectivity from it. Discrete vertex-pair histograms (Gaspers–Lau) and fixed-vertex tree majorization (Dahl) concern different observations. A public result on star configuration-space persistence uses topology of separation filtrations, not the arclength volume of separated pairs, and its full paper was inaccessible. Stronger undiscovered inverse theorems remain possible; absence of a hit is not a novelty proof.

## Mathematical value — PASS

The two-point distance distribution is a natural low-dimensional statistic of a metric-measure space. In general, reconstructing a space requires richer distance data; showing that one scalar probability law determines an unrestricted positive real arm-length multiset for all finite branching stars is a complete intrinsic inverse classification. The cancellation example \((1,1,2)\) shows the recovery is not a simple reading of positive knots and motivates the monotone pair-sum inversion. Exact identifiability provides a benchmark for geometric inference while making no unwarranted finite-sample stability claim.

## Sources and limitations

Closest accessible primary full text: Baptista–Kennedy–Mugnolo (2024), full publisher HTML, §4 Example 4.1 and main theorems. Related first-public archive sources: Vershik (2002-05-08), Dahl (2007-09-04), and Chazal–Sun (2013-05-06). Specialized configuration-space persistence on the same metric-star objects is a genuine material-access risk. Formal completeness among all publications has not been certified. Proof assumes a finite number of strictly positive arms and exact normalized-arclength sampling; practical noisy reconstruction is not established.

Self-review: passed. Independent audit: not yet performed.
