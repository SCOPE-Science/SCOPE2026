# Scientific review: log-periodic killed-chain asymptotics

## Correctness

PASS. The finite-state Perron normalization converts killed transitions to a strictly positive stochastic base matrix plus a log-periodic inverse-time perturbation. The Poisson equation removes the first-order spatial residual of the proposed positive approximate harmonic vector. Its residual is summable at order \(n^{-2}\), so positive product comparisons construct an exact harmonic limit. A spectral contraction on the zero-mean subspace gives the sharper vector expansion, and contraction of normalized forward rows gives the full survival amplitude with relative error \(O(n^{-1})\). The explicit two-state arithmetic and 63 finite checks from `check.py` support the algebra. The infinite conclusions are proved by those arguments, not by testing.

## Originality

PASS on the accessible scientific comparisons, with historical-priority reservations. Theorem 1.2 and Proposition 2.10 of Iba (arXiv:2610.38590v1) require coefficients independent of time at the \(1/n\) scale; a nonconstant profile \(f(\log n)/n\) violates that hypothesis. Champagnat and Villemonais (arXiv:1603.07477) construct a time-dependent conditioned limit and survival ratios, not the displayed explicit periodic multiplier and response coefficient. Oçafrain (arXiv:1707.08419) treats genuinely periodic moving absorbing sets, not an inverse-time perturbation of a common strictly positive kernel. General asymptotic-integration theory of Benzaid and Lutz (doi:10.1002/sapm1987773195) is potentially relevant, but its full text was not accessible; it may subsume aspects of the survival prefactor. Its abstract does not establish coverage of the particular conditioned transition response. No claim of universal priority follows from a negative search.

## Mathematical value

PASS. Inverse-time perturbations form a natural boundary between summable changes and cumulative survival effects. The result determines how a smooth slowly oscillating time profile affects *both* survival and the limiting never-killed dynamics. In particular, a nonconstant log-periodic profile can destroy ordinary regular variation without destroying the conditioned process, and a two-state model demonstrates nontrivial state-dependent response. This is a structural boundary to a recent explicit asymptotic theorem, not an arbitrary finite numerical slice.

## Closest literature and limitations

The 2026 Iba paper provides the reference conditioning framework, with a fixed first-order coefficient; the 2018 Champagnat–Villemonais paper establishes broad ratio and mixing theory; the 2017 Oçafrain paper studies a different form of periodic nonstationarity. The 1987 Benzaid–Lutz matrix-asymptotics paper is a material unresolved overlap risk because only its abstract could be accessed. The theorem here assumes a primitive positive finite kernel and a differentiable periodic profile. It neither settles broader aperiodic oscillations nor claims a higher-order transformed-kernel expansion.

Self-review: passed. Independent audit: not yet performed.
