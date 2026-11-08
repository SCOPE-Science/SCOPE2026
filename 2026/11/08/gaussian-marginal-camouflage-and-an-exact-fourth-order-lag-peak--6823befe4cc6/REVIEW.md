# Scientific review

## Correctness — PASS

The generator is the sum of two self-adjoint, invariant-preserving operators on Gaussian \(L^2\), and the Poisson refresh gives the explicit minorization ensuring unique stationarity. Conditioning on whether at least one refresh occurs gives a two-component bivariate Gaussian mixture and its exact covariance, conditional variance and fourth cumulant. Differentiation establishes a single global lag optimum and a scaling argument establishes strict peak monotonicity. A Gaussian cross-entropy identity with matched covariance proves that mutual-information excess is an exact, strictly positive relative entropy. The supplied reproduction code checks symbolic formulas and illustrative numerical instances. None of these limited numerical checks is used as an infinite proof.

## Originality — PASS, qualified

The random-position resetting formalism and renewal equations are established in Mori–Olsen–Krishnamurthy (arXiv:2211.15372), the OU/fixed-reset stationary regime is discussed by Trajanovski et al. (arXiv:2301.12304), and all stationary OU moments under general distributed resets are addressed by Olsen (arXiv:2310.04840). The inspected text does not give the jointly reversible Gaussian-marginal but temporally non-Gaussian refresh classification, covariance-matched conditional variance, strict mutual-information gap, or the exact unique fourth-cumulant lag optimum. Earlier renewal constructions and generic Gaussian maximum-entropy facts supply conceptual ingredients but do not by themselves state this complete diagnostic theorem. Additional derivations could be implicit elsewhere; this is a qualified originality judgment, not certified publication priority. Comparisons with related known results on non-Gaussian reset Brownian noise and Gaussian stationary-state synthesis show different reset laws and/or one-time marginals.

## Mathematical value — PASS

The result addresses a natural, experimentally measurable ambiguity: a reversible process with exactly Gaussian stationary histograms, exponential autocovariances and linear conditional means need not be Gaussian in time. It supplies a closed-form positive fourth-order diagnostic, a unique best lag and explicit rate scaling, together with strict information-theoretic separation. This is a structural distinguishability theorem rather than an arbitrary parameter slice. It does not optimize sampling error or claim novelty for standard OU covariance formulas.

## Limits and priority risk

All assertions concern constant-rate complete equilibrium refreshing in a harmonic trap, not partial or deterministic resets. General renewal identities can make special-case formulas implicit, and the absence of an exactly matching published statement is not proof of priority. Scientific value here is the bundled positive, sharp temporal diagnostic and information distinction. Independent replication has not occurred.

Self-review: passed. Independent audit: not yet performed.
