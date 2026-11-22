# Scientific review: fixed-mean Poisson–geometric entropy laws

## Correctness — PASS

The claim fixes the common mean and states the entire parameter interval, including both limiting distributions. Its proof uses the exact compound-Poisson logarithm to derive a positive convex-order derivative, proves strict log-concavity of every interior mass sequence by an explicit positive partial-sum identity, and consequently proves a positive Shannon-entropy derivative. The Poisson endpoint law follows from the second generating-function derivative; the geometric endpoint law follows from a same-mean relative-entropy identity and an explicitly summed squared score. The endpoint interchange arguments use exponential moments and separately controlled tails, not a numerical cutoff. `verify.py` passed multiple mean settings, entropy comparisons and both endpoint-coefficient tests. Numerical tests supplement rather than replace the all-index proof.

Scientific limits: The result does not assert uniform endpoint asymptotics as the mean varies, or classify other entropy functionals. The score expansion and the strict-order derivative are specific to the declared fixed-mean path.

## Originality — PASS, with identified priority risk

The count law is the shape-one Delaporte (Poisson–negative-binomial convolution) law; the PoiG name and the underlying convolution are existing work, not novelties. Nandi–Chakraborty–Biswas (arXiv:2301.01480 and doi:10.1080/03610918.2024.2329997) report generating functions, moment results, log-concavity and stochastic ordering. Their full text was inaccessible, so their detailed stochastic-order implications have **not** been ruled out. Xia–Lv (doi:10.1017/S0269964823000293, Theorem 1.1) reproduce the general Yu implication from convex order plus log-concavity to entropy order; the general implication and the terminal maximum-entropy inequality are treated as prior knowledge. The claim's distinguishing statements are the model-specific strict fixed-mean entropy path **with its two exact quadratic endpoint coefficients**, neither implied quantitatively by those prior results. Checked published mathematical-record searches for the Delaporte alias, entropy, geometric–Poisson convolution and quadratic endpoint laws found no directly dominating claim; failure to find one is not proof of absolute historical priority.

Residual priority risks: the original source full text was not retrievable; an undiscovered paper under the Delaporte or Poisson–gamma alias might calculate an equivalent curvature; independent literature priority review is needed before public claims of first discovery.

## Value — PASS

Holding the expected count constant while increasing overdispersion is a natural statistical perturbation for count-model selection, and entropy measures a distributional aspect distinct from variance. The theorem supplies an all-parameter entropy ordering and quantifies precisely the locally **quadratic** information sensitivity near both limiting models; the limiting coefficients differ in structure (a Poisson expectation versus a rational geometric coefficient). These exact sensitivity laws have potential use when benchmarking fitted count models near equidispersion or near the geometric extreme. This is a motivated, self-contained distributional classification, not a claim of a new probability family, estimator, regression model, or general entropy inequality.

Self-review: passed. Independent audit: not yet performed.
