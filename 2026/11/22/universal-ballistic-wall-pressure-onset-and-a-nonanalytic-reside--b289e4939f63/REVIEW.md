# Independent mathematical audit

## correctness

PASS

Regeneration can be taken at arrivals at the left wall. From anywhere in the interior, a flip-free block of length L/v hits a wall; from the right release it reaches the left with probability exp(-γL/v). These geometric bounds, with finite independent wall means, give finite cycle mean and the unique stationary renewal law. Interior directional occupation is absolutely continuous by piecewise-linear motion. Zero spatial current in stationarity gives equal directional densities; the bulk transport equations then make them constant. Directional crossing flux as position tends to a wall gives its arrival intensity vc (equivalently the boundary flux); renewal reward gives q_i=vc m_i and normalization fixes c. Conditioned on attachment at 0 the residual has density (1-F₀(s))/m₀, not the law of a new hold. Strict positivity and this continuous residual imply zero cross-wall joint mass even at t=L/v. At lag τ+ε the straight flight of duration τ gives exactly vc exp(-γτ) times the convolution of the two fresh-hold survival functions on [0,ε]: the left factor arises from the residual density and the right from surviving the first arrival. Independent remainder check: condition on residual s≤ε. Before first arriving at L, net displacement forces total backwards bulk time to be at most (ε-s)/2, since holds consume slack as well. If the first excursion returns to 0, its backwards time equals its forwards time and is at least the interval to the first flip, which must therefore be at most ε/2. If it reaches L in that excursion but flips, its first backwards run must end in a second flip within ε/2, since only + motion can arrive at L; this is an O(ε) event by the exponential waiting-time bound. After a direct crossing, release and return to L during the slack requires a bulk flip within ε of that release, also O(ε). These exhaust the excluded paths regardless of the number of subsequent visits. The residual-window mass is O(ε), giving the joint O(ε²) remainder, uniform in holding-law shapes at fixed means and motion parameters. Expanding the survival convolution isolates the sum of the coefficients at the minimal exponent divided by 1+β; the product of CDFs is of higher order and ε² is negligible because β<1. No smoothness or second moment is needed; the argument is symmetric on swapping walls. Independent particle terms add only on matched particles, producing Nf₀² for outward magnitudes, as stated. The inspected script verification/check_front.py was not executed; its source-reported quadrature and simulations are illustrative only and cannot establish the remainder or arbitrary-law theorem.

## originality

PASS

Qualified pass for the explicit stationary opposite-wall covariance's first right-hand slope and the wall-specific independent-renewal fractional correction. Finite propagation and equilibrium renewal weighting are prior principles. The nearest same-setting findings concern integrated correlations with exponential residence; inspected transient pressure and renewal-propagator papers change the initial ensemble, the boundary law, the geometry, or the observable. The slope is not novel simply as a finite-speed front, and the result is not an all-time propagator.

## value

PASS

The theorem separates two effects in a natural observable: the first arrival slope calibrates finite-speed persistence and the residence means, while the next right-hand power detects the minimal short-hold exponent and the associated sum of amplitudes. The quantitative uniform control of nonstraight paths is necessary for that separation. This is more informative than a propagation delay or a long-time covariance alone. The identification is a noiseless asymptotic signature, not a stable estimator or a promise of recovering both hold laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
