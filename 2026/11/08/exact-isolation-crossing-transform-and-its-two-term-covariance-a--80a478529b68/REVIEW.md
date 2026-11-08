# Mathematical assessment

## Correctness — PASS

The exact mixed polynomial follows from cutting at an isolated chord: the two residual arcs must be internally matched, and their crossing-polynomial weights multiply. Summing over all oriented descriptions counts each isolated chord twice. Differentiation and the classical four-endpoint crossing mean produce the strictly negative finite covariance. An explicit ratio bound for the isolation probability of an arc yields the \(-n/3-1/6+O(n^{-1})\) expansion. All boundary cases, including \(n=1\), are addressed. The standalone standard-library checker enumerated all matchings through seven chords and passed 339 exact assertions, including full coefficient comparison; finite enumeration does not certify the asymptotic proof.

## Originality — PASS, subject to historical-priority risk

The inspected Flajolet–Noy paper (2000, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf) separately gives a component-count generating function and the marginal crossing polynomial. The inspected Acan–Pittel preprint (2014, https://arxiv.org/abs/1406.2867) concerns crossing-conditioned sparse regimes and giant components; the Acan preprint (2015, https://arxiv.org/abs/1501.01489) concerns chord degrees, lengths and isolation asymptotics. The inspected Paguyo preprint (2021, https://arxiv.org/abs/2104.01134) provides separate approximation rates for crossing and simple-chord marginal laws. Their displayed results do not assert the mixed transform or the two-term covariance. The isolated-chord statistic is distinct from the simple-chord count. Relevant broader component-count formulas and potential unlocated multivariate refinements remain a legitimate priority risk; this assessment is not an independent literature certification.

## Value — PASS

The result relates two canonical but differently scaled features of the same random intersection graph: a locally rare count of degree-zero vertices and a global crossing/edge count. The exact mixed polynomial determines every factorial cross-moment with one isolated-chord factor, and the covariance has a nonzero, unbounded negative leading term with a definite constant-order correction. This fills a natural joint-statistics gap left by the separate Poisson and Gaussian marginal theories, rather than selecting an arbitrary numerical parameter. It neither claims a full bivariate law nor infers independence from vanishing normalized correlation.

## Closest literature and limitations

The strongest adjacent general framework is Flajolet–Noy's independent analyses of components and crossings. The 2014 and 2015 Acan papers establish model-level and component/degree results in related settings. Exact Touchard–Riordan polynomials make computational evaluation possible, but no inspected source supplies the isolated-chord weighted convolution, its strict sign, or its second asymptotic coefficient. Wider priority is not settled; no independent review was performed.

Self-review: passed. Independent audit: not yet performed.
