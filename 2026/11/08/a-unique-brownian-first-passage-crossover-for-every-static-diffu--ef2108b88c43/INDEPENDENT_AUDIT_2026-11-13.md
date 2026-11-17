# Independent mathematical audit

## correctness

PASS

PASS. Conditional reflection principle gives the erfc CDF. Early positive sign follows from positive mass D>mean and Gaussian tail dominance; late negative sign uses strict Jensen and dominated convergence or Fatou for infinite E[D^-1/2]. Differentiation of K(y)=E[D^-1/2 exp(-y(1/D-1/mean))] is valid for positive y despite singular diffusivities; K''(y)>0. With both endpoint values above 1/sqrt(mean) and a dip below (from the two CDF endpoint signs), strict convexity gives precisely two simple roots and hence two strict nondegenerate CDF extrema, a single intervening zero, and exact a² scaling. Strict diffusivity-curvature Jensen gives the d-/d+ bracket. Independent SymPy differentiation and singular-law integral/crossover tests support the computations; no finite test substitutes for the convexity proof.

## originality

PASS

PASS, narrowed to the genuinely stronger integrable-unbounded and near-zero diffusivity regime. A same-model 2026-11-08 Resultary theorem already proves all claimed sign counts and bracket when D has compact support bounded away from zero, plus weak-disorder positions. The present actual theorem rigorously extends those counts to every positive finite-mean distribution including E[D^-1/2]=infinite; that extension is neither a corollary of the bounded-only statement nor claimed earlier there. It requires modified endpoint and derivative-integrability arguments. Date-only records cannot establish intra-day priority for shared bounded results. This is a qualified best-knowledge PASS, not a novelty claim for bounded D.

## value

PASS

PASS. All-integrable-law extension answers the motivated regularity question left by bounded-diffusivity proofs, and handles the natural physically heterogeneous singular case where the usual long-time inverse-half-moment coefficient diverges. Complete one-crossing/two-extremum classification is a useful shape theorem, not an arbitrary size cutoff. Same-day bounded result must be cited before public release.

The dated certificate retains the supplied scientific assessment, sources and limitations.
