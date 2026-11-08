# Scientific assessment

## Correctness — PASS

The claim is fully quantified for Brownian diffusivity and Poisson rate strictly positive, an arbitrary fixed positive initial point, and iid reset locations in a compact interval strictly to the right of the target. The proof first recovers the mean absorption time, then independently solves the doubly killed interval exit problem and sums regenerative cycles to obtain the exact rational exceedance formula. The derivative in the positive exponential moment is strictly positive for every threshold strictly larger than the support and initial point. Jensen's inequality and a strict chord inequality characterize the only extremal laws and continuity of mixtures supplies every intermediate value. The inversion of the second exponential moment and the large-threshold limit follow by exact algebra. Boundary cases where the fixed mean forces a point mass are handled explicitly. The standalone checker was replayed successfully with 8,276 counted diagnostic assertions; no finite test is substituted for the universal proof.

## Originality — PASS (subject to independent literature verification)

The closest published primary sources are Evans–Majumdar (2011, arXiv:1107.4225: spatial reset distributions and mean time), Guo–Yan–Chen (2023, arXiv:2306.15929: maximum for one fixed reset location), Julián-Salgado–Dagdug–Boyer (2023, arXiv:2311.11897: two-point optimal-rate phase diagrams), and Méndez–Flaquer-Galmés–Campos (2024, arXiv:2401.01125: random reset locations, absorption-time laws and effective reset points). Their accessible relevant full-text sections do not establish the fixed-mean complete simultaneous envelope for the path maximum. A separate previously available result on the same search model gives fixed-mean absorption-time Laplace/variance envelopes; this is acknowledged and compared by implication, because it does not establish above-support path maxima or their sharp bounds. published-finding corpus searches on the maximum, fixed mean absorption time, stochastic order, and distributed spatial resets returned unrelated general bounded-moment and maxima results, not the claim. Related general renewal and convex-order principles remain potential stronger antecedents, as does unindexed literature.

## Mathematical value — PASS

The natural performance observable of a resetting search is its absorption-time mean; a distinct experimentally and operationally relevant observable is the largest outward excursion before success. The theorem answers a complete optimization question under exactly the same search-efficiency constraint, giving a global risk ordering for *all* thresholds outside the allowed reset region, not just one selected cutoff. It identifies both unique extreme designs and all intermediate attainable risks, and shows that one extreme-event measurement reveals a hidden exponential reset-location moment. In the explicit example two designs with the identical mean time have excursion risks approximately 0.34445 and 0.5 at the same threshold. No claim is made concerning the full path law or thresholds within the reset support.

## Literature and remaining uncertainty

The primary papers focus respectively on mean first passage, optimal resetting rates, first-passage distributions, or maximum statistics with a single reset site. The available prior fixed-mean Laplace envelope has overlapping extremizers but a different observable and is not a logical covering theorem. Extending a general killed-process convex-order theorem could potentially cover this result without identical wording; independently checking specialized literature remains necessary. No assertion of formal priority or external certification is made.

Self-review: passed. Independent audit: not yet performed.
