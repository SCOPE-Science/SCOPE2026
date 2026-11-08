# Scientific review

## Correctness — PASS

The full statement is for all triangular arrays of positive integers with \(n\to\infty\), \(k\to\infty\), and \(0\le u<n\), \(u=o(n)\). The exact success probabilities are \(\binom{kj}{k}/\binom{kn}{k}\) at \(kj\) vacant sites; successive waiting times are independent geometric variables. Defining \(r=u+1\) and normalizing by the final success probability \(\pi\) gives the exact weight product and bound \(a_\ell\le(r/(r+\ell))^k\). For finite \(u/k\), a fixed-index logarithmic limit and a quantitative integrable tail show convergence to the weighted exponential sum, including first and second moments. For \(u/k\to\infty\), Riemann sums for powers one, two and three of the weights, followed by the Berry–Esseen inequality for independent geometric waits, give both the Gaussian limit and absolute-constant \(O(\sqrt{k/u})\) Kolmogorov error. Critical boundary \(u/k\to0\), \(u=0\), and increasing \(u\) with \(u=o(n)\) are covered. The standalone checker passed 2,249 finite exact/diagnostic assertions, which do not certify the infinite-limit argument.

## Originality — PASS, with historical-priority risk

Turban (arXiv:1908.00940, publicly posted 2019-08-02) derives this exact finite model and its waiting-time generating function; Sections 4.4.1–4.4.6 examine fixed-length near-saturation asymptotics and explicitly note the qualitative Gaussian tendency as the vacancy parameter increases. The present claim does **not** claim either result as new. Turban's analyzed scaling keeps the block size fixed and the number of residual vacant blocks bounded, whereas the new theorem takes block size to infinity simultaneously with the near-saturation limit. It identifies the \(u/k\) critical scale, a full one-parameter limit family, convergence of the first two moments, and a uniform quantitative Gaussian rate. Vajna–Tóth–Kertész (arXiv:1211.1175, Section 3.2 and Appendix A.1) contain an equivalent abstract geometric-exponential series in another stochastic model; **that isolated law is therefore prior art** and is not claimed as a new distribution. Targeted overlap searches, including parameter and equivalent-formulation variants, identified no implication-dominating adsorption theorem. Full mathematical priority has not been independently audited; unindexed or inaccessible specialist literature remains possible.

## Value — PASS

The ratio between the number of as-yet-needed depositions and the deposition block size is a natural variable because it controls the adjacent waiting-time ratio, approximately \(e^{-k/(u+1)}\). The theorem gives a complete nontrivial transition from one-extreme-wait domination to a continuum of non-Gaussian laws and then Gaussian fluctuation with a quantitative rate. It supplies the missing double-scaling law between the two natural previously studied coverage regimes, with direct application to near-saturation hitting-time statistics; it is not merely a numerical evaluation or renamed old formula.

## Boundaries and risks

The theorem does not address spatial exclusion, growing positive vacancy fractions, or any independent expert certification. Exact finite formulas from Turban remain antecedent; proof only adds the stated joint scaling. Searches cannot establish universal novelty.

Self-review: passed. Independent audit: not yet performed.
