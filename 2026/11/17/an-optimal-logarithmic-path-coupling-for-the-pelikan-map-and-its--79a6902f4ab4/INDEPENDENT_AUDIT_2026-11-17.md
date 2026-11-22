# Independent mathematical audit

## correctness

PASS

Under a uniform initial interval point, conditional shell-position distributions remain uniform through contractions, ordinary doublings and the top-shell reset. Hence the exact dyadic-shell chain moves +/-1 away from zero, and at a doubling from depth zero draws a geometric G with Pr(G>=d)=2^-d. Coupling to the same-sign Skorokhod-reflected simple random walk makes M-W nonnegative, nonincreasing except at a zero-reset, yielding Pr(max_{k<=N}(M-W)>=d)<=Np2^-d. For each fixed p>1/2 the chain has negative drift off zero and positive recurrent visits to 0 at linear rate; independent geometric extremes attain log_2 N almost surely (Borel–Cantelli on dyadic times). Under p_N=1/2+beta/sqrt(N), the sign triangular array has drift -2beta/sqrt(N) and variance tending to 1, so Donsker plus continuous Skorokhod reflection and o_P(sqrt N) path error prove J1 convergence. Brownian level sets have zero Lebesgue occupation, supporting the deep-shell occupation functional limit. Integrating 2 Phi-bar(a/sqrt t) over t in [0,1] yields the stated 2(1+a^2)Phi-bar(a)-2a phi(a). Independent numerical quadrature checked the expectation formula for a=.1,.4,1,2 to machine precision. Reviewed actual rational-coordinate checker.py. The log optimality assertion only holds at fixed p>1/2, not uniformly in the window.

## originality

PASS

Monthus (arXiv:2409.19999) already derives the Pelikan dyadic-shell Markov chain, geometric reset and auxiliary reflected-walk/erased-bit representation. That prior fact is properly used as an ingredient. A complete joint coupling with the stated finite-horizon geometric max tail and sharp logarithmic error, plus the actual coordinate process-level critical-window and exponential-shell occupation law, was not found in material read. The other Pelikan records concern stationary correlations, mean coordinate crossovers or isolated excursions. The new result is narrower than claiming discovery of the shell chain or reflected Brownian invariance principle.

## value

PASS

A uniform error coupling of an actual random interval trajectory to a standard reflected walk gives quantitative pathwise control through the intermittent transition, identifies the optimal order of approximation, and transfers a whole-path functional limit and a nontrivial deep-shell occupation statistic. This is a motivated mechanism-level refinement beyond first moments or stationarity and applies at all finite horizons via a usable tail bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
