# Scientific review: sharp stationary-memory oscillation threshold

## Correctness — PASS
The unique Gibbs stationary correlations, normalized generator, exact Fourier kernel, Bessel identity, pole term, critical case and oscillatory residue are reconstructed in `RESULT.md`. In the oscillatory region, the asymptotic coefficient is \(H=(1-z^2)/((1+iq)(1+ip))\ne0\), and alternating sign extrema are a genuine consequence. The physical parameter constraints and boundaries are retained. The standalone code passed 4743 deterministic assertions, including an independent nine-spin Markov generator and high-time Bessel checks; finite checks do not replace the proof.

## Originality — PASS (qualified)
Weiderpass–Sharma–Sethi, arXiv:2410.23615v1 (2024-10-31), provide the exact model, Gibbs pair law, propagator and general two-point function. Godrèche, arXiv:1102.0141v2 (2011), provides the older exact stationary integral and a decay-rate crossover for nonnegative left/right influence weights. Both were inspected in primary full text; the old kernel is conceded and never presented as new. Godrèche's domain has \(|\eta|\le e\), while the new infinite-sign-change wall requires \(g>g_*>e\). The 2024 paper addresses different exceptional-point and scaling claims, not this precise stationary on-site sign trichotomy. Published-record semantic comparisons, including aliases, Bessel forms and nearest mean-field/reset kinetic Ising claims, did not identify dominance. An unindexed continuation or equivalent proof remains a publication-priority risk; the 2004 alternating-bath paper was not accessible in full.

## Mathematical value — PASS
The theorem distinguishes the previously known propagator oscillation criterion \(g>e\) from the stricter stationary temporal-memory sign criterion \(g>\sinh(2\beta J)\). It proves a new physically meaningful temperature accessibility boundary, an explicit critical case, and exact nonzero oscillatory asymptotic amplitude. Eventual (not all-time) positivity is claimed in the intermediate regimes, so no unsupported stronger statement is made.

## Limitations
Infinite chain; strictly positive single-spin Glauber flip rates; zero field; stationary preparation; no classification of finite-time sign crossings, finite chains or general nonlinear flip rules. Independent expert checking is absent; the originality conclusion is best-knowledge within inspected sources.

Self-review: passed. Independent audit: not yet performed.
