# Independent mathematical audit

## correctness

PASS

The stationary Bessel density is the stated input. Substitution t=2√r x^(p/2)/p and the Mellin integral of K yield gamma factors Γ(1)Γ((α+1)/p), giving the stated normalization; at α=0, K_(1/2) gives (√r/2)e^(−√r|x|). The small-x density is bounded uniformly (its leading power is x^α). Uniform large-x K asymptotics for orders near 1/2 give the two-sided amplitude B x^(3α/4), with B→√r. For λ<√r the exponent has a uniform negative linear majorant on x≥1 for small α and the limit follows by dominated convergence. At λ=√r set b=2/(√r α log(1/α)). Then the excess exponent G(bu)→u at each u>0. Its global minimum is at x=1 and equals −√r α/(2+α); x^(3α/4) is bounded up to b. Convexity and bG′(b)→1 dominate the scaled tail by an integrable exponential times a fixed power, giving the factor r b√r=2r/(α log(1/α)). For supercritical λ, put δ=α/2 and M=δ λ x_*. The rescaled loss is exactly [f(x_*)−f(x_*y)]/M = Hδ(y)=[y^(1+δ)−(1+δ)y+δ]/[δ(1+δ)]. Pointwise convergence alone would not justify tails at RESULT.md line 85: Hδ(1)=Hδ′(1)=0 and Hδ″(y)=y^(δ−1), uniformly bounded above and below on [1/2,2]. Left of 1/2 monotonicity gives a fixed positive lower bound; to the right of 2 convexity gives a uniform positive initial gap and linear growth. The part x<1 is bounded directly by stationarity. These bounds give uniform tail suppression, and with y=1+v/√M the loss tends to v²/2 with bounded local third derivative and M→∞. The Bessel error and relative amplitude converge uniformly in each fixed Gaussian window; domination then gives the normal factor x_*√(2π/M)=√(4πx_*/(αλ)). The exact saddle height is αλx_*/(2+α), which dominates the logarithms of all prefactors. This establishes the full equivalent for fixed r and λ, not a joint critical window or a first-passage law.

## originality

PASS

The distinct supported results are the exact critical equivalent and the full supercritical equivalent, with a controlled moving-saddle prefactor. The source paper already supplies the stationary model, normalized density, fixed-α finiteness, Brownian threshold, saddle location and saddle height. Those and the standard Bessel/Laplace methods are not credited as new. The subcritical Brownian limit also follows routinely from that density and uniform domination.

## value

PASS

The bare finiteness threshold does not quantify whether physically weak sluggishness provides effective regularization. At the threshold the exact cost grows on the inverse α-log scale, while above threshold an exponentially remote distance dominates and the full prefactor quantifies the cost beyond logarithmic accuracy. These are distinct regimes at a natural boundary of an existing model, with exact constants and no implied lattice or finite-time conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
