# Mathematical review: logarithmic Dirichlet concentration

## Correctness — PASS
For every fixed r, Dirichlet beta-sum integration gives the exact factorial moment (q)_r ((q-r)a)^(up m)/(qa)^(up m). A uniform logarithmic product expansion has error O_r((a+1)/q), tending to zero when a~kappa log q, and the prescribed centering gives factorial moments e^(-rx). This proves a Poisson vacancy limit and hence a Gumbel cover time. The posterior Beta(a,(q-1)a+m) law for an unseen label has normalized mean tending to e^(-1/kappa) and variance tending to zero. Tightness of vacancy counts and a lower cutoff in the Gumbel window prove the final-label mark. Boundary conditions q->infinity, fixed kappa>0, real x and positive a are explicit. Rational verifier checks finite identities; infinite claims follow analytically.

The correctness check reconstructs the exact Dirichlet–multinomial occupancy probabilities, verifies the logarithmic error scale, and derives final-label mass concentration from posterior Beta variance, bounded expected unseen counts and an earlier-window cutoff. The finite checker passed 621 rational assertions and 108 numerical scale diagnostics. Those experiments are not used as infinite proofs.

## Originality — PASS (qualified)
Full-text comparison with Holst (fixed shape) and Neal (deterministic unequal rates), plus published records of reinforced-urn cover time, Dirichlet-multinomial covariances, Pólya–Friedman dynamics and marked Zipf coupons, did not identify the same moving-shape annealed completion and terminal-mass joint result. Holst is credited for the fixed-shape Fréchet law and random-rate embedding. Broader triangular-array extreme-value literature and uninspected records remain priority risks.

The nearest inspected primary full texts are L. Holst, *Extreme Value Distributions for Random Coupon Collector and Birthday Problems* (2000 public preprint; 2001 journal publication) and P. Neal, *The Generalised Coupon Collector Problem* (2008). The checked published records named in AUDIT.json were searched by aliases, coverage, implication and terminal-mark observables. Missing full texts are declared in that file, not designated noncovering on abstract evidence.

## Value — PASS
Symmetric Pólya sampling with a growing number of colors provides a natural interpolation between heterogeneous fixed-Dirichlet reinforced coverage and ordinary uniform coupon collection. Logarithmic per-color mass is a motivated critical regime where color weights concentrate while rare terminal colors retain a nontrivial systematic bias. Exact centering, Gumbel crossover and the final coupon’s latent rarity quantify this transition and are not merely generic finite algebra, renaming or a marginal limit already displayed in the closest literature.

## Limitations and risks
The result is annealed and conditional on \(a_q/\log q\to\kappa\in(0,\infty)\); it does not give quenched convergence, uniform error estimates, full growing-shape phase diagrams, or moment convergence. Global historical priority is not certified; close unread primary texts are described as residual originality risks.

Self-review: passed. Independent audit: not yet performed.
