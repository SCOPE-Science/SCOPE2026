# Scientific review — rare frozen propulsion and restart reversal

## Correctness — PASS

For the precisely specified absorbing/reflecting frozen-drift diffusion, the backward equations yield exact conditional moment integrals. Gaussian averaging, an interior-free unique corner in each compact integration polytope, and dominated Laplace scaling prove the distinct exponential first- and second-moment laws and the centered Gaussian moment-biased velocity limits. Renewal theory gives the resetting slope. A small-time Gaussian/Brownian estimate proves divergence at large reset rate and hence finite positive existence of a minimizer at high width. The passive Brownian slope factors exactly into a polynomial with critical starting distance \(x/L=1-1/\sqrt5\). The included deterministic checker passed 45 tests. Infinite-parameter claims use the proof, not the tests.

## Originality — PASS, qualified

The closest primary source is Georgiou, Bressloff and Bertrand (arXiv:2609.21124v1): it investigates the same mixed-boundary active-particle first-passage setting with velocity resampling, but its analytical solution is weak-activity and finite-persistence. Montero, Masó-Puigdellosas and Villarroel (arXiv:1706.04812) supply a randomly oriented monotone walk and general renewal framework, not the reflected Gaussian-drift model. Woillez, Kafri and Lecomte (arXiv:1912.04010) study metastable-potential escape in a small-active-noise regime. Standard stochastic-resetting literature already supplies the renewal condition, which is credited as prior. The distinct contribution is the exact high-width Gaussian-moment asymptotics, biased velocity scales and consequent reset-sign reversal. Relevant published records and accessible previous mathematical claims were compared by implication, not wording; undiscovered broader literature remains a priority risk.

## Value — PASS

Rare frozen outward propulsion can dominate mean search time despite its small Gaussian probability, and its second moment grows at a still faster exponential scale. The result provides a concrete mechanism explaining why resetting can become beneficial even where ordinary Brownian resetting initially hurts, and identifies the moment-conditioned velocities responsible. This supplies a motivated exact benchmark for highly persistent active search and restart-protocol design.

## Limits

The proof is for a frozen velocity re-drawn at every attempt; finite-persistence active Ornstein--Uhlenbeck trajectories, unique optimizing rates, physical resetting costs and independent scientific validation are outside the result.

Self-review: passed. Independent audit: not yet performed.
