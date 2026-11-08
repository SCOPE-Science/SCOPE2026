# Self-review

## Correctness — PASS

The renewal-reward/Green formula sets the threshold reset rate to the reciprocal of \(\int_0^a(a-x)w(x)\,dx\). The stationary Poisson resolvent gives the flux jump \(h'(0+)=-r/2\) and strict convexity \(h''=rwh>0\) away from zero. Because the threshold speed-normalized potential has slope \(-r/2\), their difference is strictly increasing. Its negative initial sign is forced by normalization and the positive Poisson tail beyond the threshold; hence there is exactly one crossing, which implies strict first-order stochastic dominance. The statement includes time-change conventions for singular diffusivity at the origin and excludes per-reset work and search-time claims. Independent BVP tests support, but do not prove, these implications.

## Originality — PASS (qualified)

The strongest nearby paper is Frimpong, Bresque and Roldán (arXiv:2610.21962, Sections 4 and 7), which separately derives the two stationary laws and studies reset costs. Its identified comparisons do not set the two reset-event frequencies equal or assert a universal first-order stochastic order. De Bruyne, Randon-Furling and Redner (arXiv:2009.03419) analyze first-passage threshold resetting instead. A previously recorded result for arXiv:2610.21962 concerns Poisson-reset exponential cost singularities and neither implies nor duplicates the matched-frequency threshold comparison. Published-record searches found no explicit equivalent statement. The remaining priority risk is a general Green-kernel or stochastic-resetting comparison theorem that entails this claim implicitly.

## Value — PASS

A physically interpretable fairness constraint, equal expected number of resets per unit time, yields an entire distributional ordering, not just an isolated moment or numerically optimized parameter. It resolves simultaneous comparisons of every increasing radial occupation penalty and gives a non-power-law universality result whose proof is a strict one-crossing structure. It also distinguishes occupation penalties from the reset-event costs that are not ordered by this result.

## Boundaries and risks

This does not determine energy expenditure at reset instants, time-to-target or entropy production. General asymmetric diffusions and lattice effects remain outside the theorem. An unindexed earlier general theorem could dominate the originality claim. Reproducibility checks sample finitely many diffusivities and radii, not the quantified class.

Self-review: passed. Independent audit: not yet performed.
