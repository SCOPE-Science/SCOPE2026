# Scientific review: Singular weak-sluggishness law for exponential reset costs

## Correctness (PASS)

The asserted quantity is the stationary continuum cost rate \(Q_\alpha(r,\lambda)=r\mathbb E[e^{\lambda|X|}]\) for fixed \(r,\lambda>0\), not the expected total cost before absorption. The published Bessel density is normalized, and its constants recover the bilateral exponential at \(\alpha=0\). The proof uses a Bessel large-argument approximation uniform for orders near \(1/2\). The subcritical limit follows by a uniform exponential majorant; at criticality, the scale \(2/(\sqrt r\alpha\log(1/\alpha))\) yields the exact constant from an integrable rescaled limit, with exponential tail control from the exact derivative of the excess exponent. Above threshold there is a unique exponentially remote saddle, and a uniform Laplace calculation gives both its exponent and its Gaussian prefactor. Tests use the original Bessel expression rather than substituting the claimed asymptotic into itself. The three separate regimes and the limitation to fixed parameters are explicit.

## Originality (PASS, with residual risk)

Frimpong, Bresque and Roldán, arXiv:2610.21962v1, already provide the stationary Bessel density, the fixed-parameter spatial tail and the finiteness boundary for exponential costs; the finding does not claim those results. Their section 7.1.4 discusses \(\alpha=0\) versus \(\alpha>0\) but does not quantify the singular \(\alpha\downarrow0\) transition, its critical logarithmic scale, or a full supercritical saddle prefactor. Frimpong, arXiv:2610.34568, covers maximum and last-passage functionals of the same walk, not exponential stationary reset costs. Sunil and colleagues, arXiv:2304.09348, give the Brownian exponential-cost threshold and cost framework but not the weak-sluggishness singular limits. DLMF §10.40 supplies the standard Bessel expansion used, not the model-specific asymptotic.

Relevant public-index and literature searches did not reveal a stronger published statement that immediately covers these exact three regimes. Absence of a search hit is not a proof of novelty; a general asymptotic theorem for stretched-exponential Laplace transforms may reproduce the supercritical mechanism, and unindexed theses or appendices remain a priority risk.

## Value (PASS)

The model exposes a physically consequential discontinuity: arbitrarily weak positive sluggishness regularizes every fixed exponential return cost, yet the regularization becomes extremely expensive as the Brownian mobility limit is approached. The critical inverse-logarithmic divergence and supercritical full essential-singularity prefactor tell quantitatively how much cost is hidden by the bare statement "finite for every positive sluggishness." They distinguish the two mechanisms: a slowly growing critical distance scale and a supercritically remote rare excursion. This is a motivated boundary of an established nonequilibrium resource-cost problem, not an arbitrary parameter slice or a recomputation of a known table.

## Limitations and outstanding checks

Independent scientific validation and comprehensive publication-priority examination have not been performed. Results concern the continuum stationary distribution with strictly fixed positive reset and cost parameters; simultaneous approaches of \(\lambda/\sqrt r\) to one, lattice cutoffs, and first-passage accumulated costs are outside scope. Numerical checks are finite tests only. The strongest relevant primary text was accessible and its cost section was inspected; broad asymptotic methods may encompass the Laplace mechanism in a more general setting.

Self-review: passed. Independent audit: not yet performed.
