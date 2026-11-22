# Scientific review of covariance-matched random diffusivities

## Correctness — PASS
The proof checks exact stationary Markov and Gaussian covariances, conditional Brownian Wick reduction, the three-time cumulant crossing and the strictly positive ordered fourth-diffusivity-cumulant gap. The last implies a global eighth-displacement-cumulant strict inequality through an explicitly integrated positive kernel. The analytic formula for the gap follows from its Laplace transform. `CHECK.py` independently evaluates the two infinitesimal-generator moment hierarchies and passed 949 assertions. The numerical sample grid is corroboration, never a proof of the infinite domain.

## Originality — PASS (qualified)
The inspected 2018 generalized-grey/diffusing-diffusivity comparison addresses a different pair of models. The 2019/2020 squared-OU paper and the 2020/2021 Markov-switching paper give the individual stochastic foundations. Guéneau, Majumdar and Schehr's 2025 exact finite-time switching transform covers binary forward moments, which are explicitly not claimed new. The closest published two-state cumulant inversion and harmonic eighth-moment studies give different inverse statements, not equality across these distinct dynamics. Dedicated comparisons of aliases, parameter values, stronger forward results, and exact claimed implications did not identify the stated all-time order-six crossing and eighth-order obstruction. Priority remains qualified by unindexed equivalents and by derivability from known forward formulas.

## Mathematical value — PASS
This is a precise observational-equivalence and identifiability classification for transport through heterogeneous diffusivities. Matching the entire diffusivity covariance hides all fourth-order multi-time tracer information, a unique physical contrast hides all sixth-order multi-time information too, and a strict eighth-order gap remains at every positive time. The latter is a natural discriminator at a mathematically sharp lower-order blind spot, not an arbitrary computed parameter slice.

## Scope and limitations
The lower Markov diffusivity is strictly positive, while squared OU can touch zero. The environment is stationary, the Brownian driver independent, and the rates calibrated. This is an exact population-cumulant theorem; finite-sample inference, uniform numerical stability, and global equality of full trajectory laws are not claimed. Independent scientific validation and publication-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
