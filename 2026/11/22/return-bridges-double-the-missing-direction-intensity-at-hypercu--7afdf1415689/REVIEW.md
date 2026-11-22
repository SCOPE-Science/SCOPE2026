# Mathematical review of return-bridge coordinate coverage

## Correctness

**PASS.** The marked \(\cosh\)-coefficient formula follows from multinomial word counting with even coordinate frequencies. Conditioning independent even-Poisson variables on their total gives the identical finite law. A two-dimensional lattice local limit theorem with an explicit Schur-complement calculation yields the fixed-density Gaussian statement, and a one-dimensional growing-parameter lattice local limit ratio proves convergence of all fixed factorial moments in the critical window to those of \(\operatorname{Poisson}(2e^{-c})\). Parity, exact centering, scaling, and endpoint-versus-first-return distinctions are explicit. The standalone checker passed 482 exact assertions; finite checks are not used as proofs of asymptotics. Remaining analytical limitation: no uniform quantitative error bound or first-return variant has been established.

## Originality

**PASS, with historical-priority qualification.** The relevant full primary texts on infinite occupancy variance, nonuniform bit-flipping recovery, infinite-urn odd occupancy, and hypercube stopping times do not state an equal-probability fixed-time **return-conditioned** law for the smallest supporting face. A published exploration-versus-displacement covariance theorem concerns unconditioned walks; the exact finite cosine hyperbolic generating function alone is not counted as a novel contribution. No inspected source derives the conditional critical \(2e^{-c}\) intensity, its coverage-time shift, or the companion fixed-density Gaussian law. Classical conditional occupancy limit theorems might imply special cases, and the full 1989 hypercube sample-path article was not accessible; historical priority is therefore not independently certified.

## Value

**PASS.** The conditioning fixes a natural and highly structured endpoint event rather than an artificial parameter slice. The number of unused coordinate directions is the geometric codimension of the smallest face containing the entire bridge path, not the count of unvisited vertices. Its full-coverage transition is a canonical coupon-collector question. A factor-two change in the critical Poisson intensity, together with the fixed-density Schur-complement variance and strict increase in unvisited-direction fraction, quantitatively identifies how the closed-bridge constraint changes exploration. These effects are not provided by an unconditional covariance calculation.

## Closest literature and limitations

Bogachev–Gnedin–Yakubovich (arXiv:math/0609498) studies unconditional infinite-urn occupancy variance; Muratov–Zuyev (arXiv:1310.1306) studies infinite-system bit-flip recurrence and active bits; Durieu–Wang (arXiv:1508.01506) studies infinite-urn occupancy and odd-occupancy functional limits; Peixoto–Marcondes (arXiv:1709.02359) studies hypercube stopping and first-return events. Diaconis–Graham–Morrison (1990) gives hypercube mixing behavior in a different walk setup, and Matthews (1989) is a plausible full-text priority risk. The theorem is restricted to fixed even-time return of a non-lazy uniform flip walk, with no first-return or nonuniform-weight claim.

Self-review: passed. Independent audit: not yet performed.
