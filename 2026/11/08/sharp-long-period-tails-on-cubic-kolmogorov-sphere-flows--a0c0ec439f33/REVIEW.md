# Scientific review: Sharp long-period tails on cubic Kolmogorov sphere flows

## Correctness: PASS
The cubic field is tangent to the unit sphere, and in the open octants the squared-coordinate system exactly obeys the three-species antisymmetric replicator equations. Direct algebra proves conservation of the weighted product. Its strictly concave logarithm yields one periodic Jordan curve per noncritical level. The three vertex times are respectively \(\log(1/H)/(2ab)\), \(\log(1/H)/(2ac)\), and \(\log(1/H)/(2bc)\), each up to a bounded error: coordinate decay/growth estimates give an integrable error in the logarithmic velocity. The remaining connecting arcs contribute bounded time. Uniform sphere area induces a Dirichlet \((1/2,1/2,1/2)\) law, and its exact negative-moment integrability threshold proves both the long-period exponential rate and the borderline moment divergence. Exact symbolic identities and two high-accuracy return-time comparisons are reproduced by `check.py`.

## Originality: PASS within inspected primary literature
Benny–Jana–Sarkar (arXiv:2310.14238v1, §5) defines this family, classifies signs and local phase portraits, but does not compute the global physical-time period divergence, spherical-area period distribution, or exponential-moment threshold. Boone–Piliouras (arXiv:1910.01334v1, §§3,6) establishes qualitative periodicity for zero-sum three-strategy replicator games; their periodicity theorem neither gives the sharp period coefficient nor implies a surface-area probability law without separate metric analysis. Related published results concern other cubic Kolmogorov Hamiltonian centers or stationary May–Leonard measures; their accessible statements do not cover this theorem. Classical heteroclinic slowing and the weighted-product conservation are not claimed as new. Unindexed equivalent period asymptotics or probability tails remain a residual risk.

## Mathematical value: PASS
For this source-motivated family the known distinction between periodic and nonperiodic regimes does not quantify the distribution of extremely slow cycles. The result supplies an explicit parameter-dependent phase-volume exponent and the exact threshold for exponentially weighted periods, including divergence at equality. These facts explain how a flow with almost-everywhere periodic motion can nonetheless have arbitrarily long cycles while retaining finite moments below a calculable limit. Unequal coefficients are covered without requiring symmetry or a numerical cutoff. No general theorem about all replicator dynamics is claimed.

## Limits and status
The probability tail is characterized at logarithmic-exponent accuracy; no multiplicative asymptotic prefactor is asserted. Sampling must use spherical area, and time must be the original cubic-flow time. Closely related older work outside the inspected corpus may alter priority. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
