# Review of the two-band Fourier concentration trace law

## Correctness — PASS
The operator is a positive trace-class contraction because the time/frequency restriction map is Hilbert–Schmidt. Trace cyclicity yields the exact cross-band term, and the Fourier transform of a time interval gives the triangular-weighted sinc-square integral. The algebraic identities for the triangular Fourier transform supply the complete leading oscillation. At an integer single-band time–bandwidth product, both the transform and its first derivative vanish, suppressing the order-three denominator correction and making the derivative eventually strictly negative. Away from integer products, the leading first and second derivatives enforce exactly one alternating local extremum near each sufficiently large half-period. The standalone quadrature checker passed 117 assertions, but the proof—not finite testing—establishes the quantified results.

## Originality — PASS (historical priority provisional)
The closest 2023 concentration-operator literature establishes general eigenvalue deviation bounds, rather than the present exact fixed-length large-gap trace interaction. An earlier multiband-prolate sampling article develops an exact spectral matrix and bandpass approximation, but its inspected theory and examples do not state the sharp quadratic leakage coefficient or integer/noninteger monotonicity phase diagram. A 2012 bandpass concentration paper is closely relevant; its abstract and bibliographic details were accessible, but its full text was unavailable. An equivalent formulation there or in other earlier bandpass spectral work remains a meaningful unresolved historical-priority risk; no independent novelty certification is claimed.

## Mathematical value — PASS
The squared trace defect is a natural eigenvalue-based measure of how far a time–frequency concentration operator departs from a projection. For two bands of fixed width, their separation leaves the total trace fixed yet induces a nonzero positive interference term. The finding gives the sharp leakage order and coefficient and shows a qualitative reversal of the apparent intuition that more frequency separation always decreases coupling: for every noninteger time–bandwidth product there are infinitely many local reversals, while precisely integer products have eventual monotonic decay. It is a natural complete phase distinction rather than an arbitrary single numerical computation.

## Nearest related work and limits
Marceca–Romero–Speckbacher, arXiv:2301.11685 (2023); Israel–Mayeli, arXiv:2301.09616 (2023); Lakey–Hogan, SampTA 2013; SenGupta–Sun–Jiang–Chen–Mariani, J. Fourier Anal. Appl. 18 (2012), 182–210 (full text uninspected). The result is fixed-parameter and quadratic-trace only; it does not determine individual Slepian eigenvalues or their exact convergence.

Self-review: passed. Independent audit: not yet performed.
