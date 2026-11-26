# Independent mathematical audit

## correctness

PASS

Length bias followed by a uniform inspection point gives the joint age/residual density f_T(b+f)/μ; multiplying by the Brownian heat kernel and integrating gives (1). Finite mean controls the large-age integral, b^{-1/2} the origin, and dominated convergence supplies continuous conditional tails in x, including zero. For independence at each fixed u, the signed mixture with density weight S(b+u)−P(F>u)S(b) is integrable, so Fourier transformation in x gives its Laplace transform at every s=Dξ²≥0. Uniqueness and continuity make its weight zero for every b; b=0 identifies P(F>u)=S(u). This forces the continuous multiplicative survival to be positive and then exponential (finite mean rules out zero rate); the converse follows by substitution. In Gamma cases the posterior age density ratio at larger versus smaller |x| is strictly increasing, and the positive full-support posteriors therefore give strictly different expectations for a bounded strictly monotone residual tail. The reciprocal hazard integral changes strictly in the requisite direction at k≠1, giving precisely the stated ordering. Strictly increasing costs, or nondecreasing costs genuinely nonconstant on (0,∞), inherit strict order by tail integration when finite; constant costs are not strict. For the far field, write J_m=∫b^{k−3/2−m} exp(−λb−x²/(4Db))db. The Bessel integral gives J_m/J_0=b_x^{−m} K_{k−1/2−m}(a)/K_{k−1/2}(a)=b_x^{−m}(1+O(a^{−1})), with b_x=|x|/(2√(Dλ)) and a=2λb_x. On any sufficiently large fixed half-line the Gamma survival relative to the leading kernel contributes a factor 1+O(b^{−1}); its weighted moment errors are controlled by J_{m+1}. Below that half-line, the Gaussian suppression is exp(−c x²) up to polynomial factors, negligible compared to the saddle exp(−a), also for the inverse moments. This verifies (3) for the actual posterior. The fixed-u Gamma tail ratio has first correction (k−1)u/b. For the mean, independently set z=λb and use λm(b)=k−z+z^k e^{−z}/Γ(k,z); expansion through the second relative Gamma coefficient gives 1+(k−1)/z+O(z^{−2}), so no uniform-in-u assumption is needed. The small-age residual mean is bounded on compact ages. The heat resolvent and its first two λ derivatives give the quoted Erlang formulas (the k=3 denominator before scaling is (a²+7a+15)/8). The k=1 correction is zero and independence exact. The supplied checker was inspected as supplementary numerical evidence, not executed or used as an infinite-case proof.

## originality

PASS

The established conditional forward-density representation and exponential sufficiency are prior work; Gamma hazard monotonicity and the classical age/residual characterization are also prior. The verified distinct results are the converse for the Brownian observation, the strict all-horizon Gamma spatial order, and the first nonzero spatial corrections to the survival forecast and mean at k≠1. In a related return model, the leading exponential residual-time limit is already known; it is not credited as independent novelty. This comparison is bounded and does not certify priority.

## value

PASS

The scientific observable is the predictive value of a current displacement for the timing of the next reset. The independence converse identifies the exponential clock among arbitrary admissible renewal clocks under this observation; the Gamma order resolves the direction for every horizon and the asymptotic terms quantify the effect on far excursions. The result is not a stationary marginal, a return-speed comparison or a single special-shape computation. It addresses equilibrium instantaneous resetting only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
