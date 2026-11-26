# Independent mathematical audit

## correctness

PASS

For the process defined in the Finding, independent Bernoulli marks on the Poisson epochs give positive-rate clearing times. Coupling at the first clear proves uniqueness; in the stationary past the backward gaps are iid exponential and the number of consecutive amplifications is independent geometric with P(N=n)=(1-p)p^n. This gives the stated finite-sum perpetuity at a stationary time, not the post-jump law. Conditional reversal gives Z distributed as 2^N times the corresponding truncated q-weighted exponential sum with q=1/2. Under the natural growing-sum coupling the limiting Y has a continuous law (it includes an independent exponential summand) and small positive exponential moments. Uniform convergence of the survival functions to this continuous limit, combined with a geometric bound on the nonnegative window indices and the exponential-in-2^(-k) bound on the negative indices, gives the locally uniform dyadic-window limit. The hypoexponential coefficients and termwise Mellin transform are correct: after integration each exponential supplies q^(js), so Euler's product has argument q^(s+1). Fourier periodization uses s=kappa-2 pi i ell/log 2 and gives the stated positive product times Gamma(s). Vertical-line gamma decay justifies the series and gamma has no zeros. The largest weighted exponential term bounds positive moments below, and 2^N times Y bounds them above, proving convergence exactly for p 2^s<1, with divergence at equality. Independently, the survival is the normalized pantograph solution described below, giving the same coefficients. VERIFY.py was inspected, not run; its p=0.4 calculations are only diagnostics. The literal Assumptions sentence that epochs are independent of the holding times is imprecise: the latter are the differences of the epochs, not independent of them. The proof checks the unambiguous marked-Poisson construction in the Finding, with iid holding times and marks independent of the epoch process.

## originality

FAIL

The principal asserted advance, the closed Fourier spectrum including nonvanishing of every harmonic, is a direct specialization of Changgui Zhang's 2023 pantograph connection formula, not merely a related qualitative tail theorem. For q=1/2 the stationary survival S satisfies S'(x)=p S(qx)-S(x), S(0)=1. To see this, write Z=E+W with E exponential rate one independent of W=CZ'. The density at x>0 is the integral of exp(-(x-w)) over w<=x against the law of W, which is S(x)-P(W>x)=S(x)-p S(qx). Thus S(x)=F(mu;q,x) in Zhang's notation with q^mu=p and mu equal to the record's kappa. Zhang's Theorems 1.1–1.2 give the exact positive-axis expansion at infinity, with leading coefficients (p;q)_infinity Gamma(mu-2 pi i ell/h)/[h(q;q)_infinity] after indexing by ell and h=log 2. Since (p;q)_infinity=(1-p)(p/2;1/2)_infinity, these are exactly the frozen coefficients. They are all nonzero by the same gamma fact. This is demonstrated coverage, not a verdict based on an inaccessible plausible source. The normalization and the moment threshold do not leave a distinct finding.

## value

FAIL

The reset model is natural and the coefficients can be useful, but the asserted exact invariant and all-harmonic conclusion are already obtained by specializing a stronger pantograph theorem. The stationary model identification is a one-step exponential convolution identity; the moment cutoff follows immediately from the exact mixture. No separate new mathematical theorem remains after crediting that coverage. The standalone probabilistic rederivation can be explanatory, but it is not a distinct valuable finding under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
