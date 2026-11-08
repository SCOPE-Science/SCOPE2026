# Scientific review

## Correctness: PASS

The claim is for positive \(\beta,E,k,t\), an initial excited-state probability \(p>(1+e^{\beta E})^{-1}\), and a load kept fixed throughout discharge. The work formula follows from the exact two-state master equation and the pathwise equality between net jump count and initial minus final occupation. Strict log-concavity is proved using the positive, increasing auxiliary function \(A(y)=1-y/(e^y-1)\) and the strictly negative second derivative of the finite-horizon factor. Endpoints establish existence; implicit differentiation and evaluation at \(w=E\) give the sharp duration-monotonicity boundary, including the case \(p\le1/2\). The fully occupied limiting loads are derived analytically. The independent checker recomputes work by transition probabilities and compares roots across parameter families. Risks: mathematical results use symmetric exponential rate splitting and positive finite horizons; they do not cover arbitrary load feedback or microscopic implementations.

## Originality: PASS (qualified)

The 30 September 2026 active-matter battery paper uses the same two-state rates and derives an instantaneous-power optimum at fixed occupation; the objective here instead integrates the evolving occupation for a single constant load over an arbitrary finite deadline and gives a rate-independent reversal boundary for its *global* optimum. The related 3 July 2026 constant-current battery scheduling paper studies RC/circuit models, not the same stochastic finite-horizon fixed-load objective. The classical Brownian cycle result addresses a different optimization. Semantic searches in the mathematical research index and the accessible preceding local claims found no explicit or dominating theorem about the simultaneous uniqueness and duration-monotonicity boundary. Failed search is not proof of novelty; unlocated papers and broader finite-time stochastic control theory remain priority risks.

## Value: PASS

The model is a recently studied minimal thermodynamic energy store. A finite deadline with one load that cannot be adjusted during discharge is a natural operational restriction distinct from instantaneous power maximization. The exact threshold separates two genuinely opposite scheduling responses: longer discharge windows demand a larger or smaller optimal load depending on energy gap and initial occupation. The equality case supplies a duration-independent matching rule for all kinetic rates, and strict log-concavity precludes competing local optima. This is a structural optimization classification, not a numerical fit or a restatement of two-state relaxation.

## Closest literature and limitations

Primary comparison: Lin--Liu--Ma (arXiv:2610.00428v1), discharge equations (11)--(15). Additional comparison: Liu--Lin--Ma (arXiv:2607.03157v1), circuit-based constant-current scheduling; Schmiedl--Seifert (EPL 81, 20003), finite-time cyclic Brownian engines. The work omits charging cost and maintenance cost, and does not claim optimality over dynamically varied loads. The mathematical result has not undergone independent validation. Publication priority should be independently checked against additional literature.

Self-review: passed. Independent audit: not yet performed.
