# Scientific review: dimensional obstruction to Gaussian detector separation

## Correctness — PASS

The statement identifies the sole free design variable as half-separation within a reflection-symmetric detector pair. Exact Gaussian completion of squares computes both marginal detections and their product; one derivative factorization gives a strictly decreasing sign factor in the squared distance. Consequently the claimed maximizer, including equality and zero boundaries, is unique and global. A separate logarithmic derivative of the critical baseline quality proves the dimension-one/two versus dimension-three-and-higher distinction. Bracketing the unique positive root on the exponential dimensional scale and controlling the remainder of the logarithmic expansion proves the asymptotic. The supplied standard-library diagnostics completed 86,581 assertions, including independent numerical quadrature. No numerical enumeration substitutes for proof.

## Originality — PASS under available evidence, subject to historical-priority risk

The planar symmetric detector model is **not claimed to be new**. Its formula does not imply the new three-dimensional co-location region, the explicit golden-ratio threshold at dimension four, or the exponential dependence on spatial dimension without new argument. The relevant inspected primary papers establish common half-normal detection models, show through simulation that trap placement affects estimation, and develop approximate density-precision design algorithms. They do not claim the present all-quality obstruction for a *fixed symmetrically placed pair and a Gaussian prior*. The main scientific risk is implicit or equivalent coverage in generic Gaussian sensor-placement or facility-location literature not identified in the reviewed sources; publication priority requires further independent review.

## Value — PASS

Three-dimensional usage distributions are scientifically motivated for aerial and aquatic organisms, and a two-detector monitoring decision can be governed by the probability of recording the individual at least once rather than by parameter-estimation precision. The result reveals a change of kind, not just a coefficient shift: in dimensions one and two, perfect individual detection always makes positive separation worthwhile for any nonzero spread, whereas from dimension three onward there is a positive *unavoidable co-location regime* for all physically allowed qualities. The sharp frontier and its exponential dimensional scaling show when that design restriction matters, without asserting field realism or a general recommendation.

## Closest literature and restrictions

Sun, Fuller and Royle (2014, doi:10.1371/journal.pone.0088025) discuss cluster spacing under parameter-estimation simulation. Durbach et al. (first published 2020, doi:10.1111/2041-210X.13517) use approximate density-precision optimization of full arrays, and Tracey et al. (2014, doi:10.1371/journal.pone.0101205) motivate three-dimensional home-range analysis. The theorem is restricted to an isotropic Gaussian prior, conditionally independent half-normal Bernoulli detectors, one fixed observation, and symmetric detector locations. It is not independently validated and does not supply a general two-location design.

Self-review: passed. Independent audit: not yet performed.
