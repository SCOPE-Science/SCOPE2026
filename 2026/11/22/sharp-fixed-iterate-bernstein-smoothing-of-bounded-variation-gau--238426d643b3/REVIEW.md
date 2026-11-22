# Scientific assessment

## Correctness — PASS

The claim concerns fixed \(r\) and finite \(p\) on real \(BV(0,1)\), plus the separately stated \(L^\infty\) boundary. The proof reduces the complete variation unit ball to unit jumps, verifies exact one-step mean/variance for the two Markov kernels, obtains a fixed-time Gaussian random-walk limit with variances \(r x(1-x)\) and \(2r x(1-x)\), and integrates the limiting jump profile. The key boundary argument is a uniform Chebyshev integral bound excluding jumps approaching either endpoint; uniqueness of the Gaussian coefficient maximum then forces location \(1/2\). A strict outside-midpoint norm gap proves rigidity of the full derivative variation measure. The separate uniform endpoint norm uses positivity and the non-atomic transition kernel. Exact-rational checker results comprise 266 assertions, with 16 additional finite numeric checks; these do not replace the asymptotic proof. The limiting constant depends on exactly the normalization in RESULT.md.

## Originality — PASS, qualified

Hoeffding (1971) and prior sharp one-step \(L^1\) work cover an important special case; this is credited, not claimed as independent novelty. Jones (1976) treats a Bernstein polynomial error but the accessible description concerns absolutely continuous input for point sampling, not integrated operators and fixed iterates; the complete original was inaccessible, explicitly retained as a historical risk. Öksüzer–Karsli–Yeşildal (arXiv:1605.03976, material sections 1–4) establish variation seminorm results. Berdysheva–Dyn–Farkhi–Mokhov (arXiv:2212.00439, material sections 3–6) give pointwise and nonsharp integrated \(L^1\) bounds involving the same operators. Adell–Garrancho–Martínez-Sánchez (arXiv:2410.19893, full method and examples) address pointwise jumps. No inspected accessible theorem implies the joint all-finite-\(p\), fixed-iterate sharp limit with its factor-of-two variance distinction and variation-measure rigidity. It remains possible that a different, unindexed classical result subsumes it.

## Value — PASS

The integral kernels are standard alternatives for discontinuous-data approximation. The theorem gives exactly calibrated worst-case convergence rates in every fixed finite \(L^p\) metric, including the precise penalty of adding the Durrmeyer posterior sampling stage, the effect of repeated smoothing, and the non-convergent \(L^\infty\) endpoint. The concentration theorem identifies the sharp worst-case geometry, beyond a generic upper rate bound. These quantities are motivated by selecting smoothing operators for edge-preserving approximation, not by an arbitrary degree-specific parameter.

Self-review: passed. Independent audit: not yet performed.
