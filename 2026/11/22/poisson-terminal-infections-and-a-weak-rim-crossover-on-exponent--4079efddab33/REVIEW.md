# Self-review

## Correctness — PASS

The source-to-site first-passage description of Markov SI spreading follows from memoryless independent exponential edge clocks. The infinite-line one-point survival law is derived exactly by a Poisson Laplace functional; finite-radius truncation and independent outward rays yield a concrete Chen–Stein dependency estimate for rare susceptible sites. Both fixed-rate and weak-rate Gumbel centering follow from the computed Poisson intensities, and a direct first-moment bound proves escape of the star-centered window when the vanishing rim rate exceeds the reciprocal-log scale. A pure-Python, independently built finite-state continuous-time Markov solver verifies 12 finite-wheel survival probabilities. Those tests do not substitute for the asymptotic proof.

## Originality — PASS on examined evidence, provisional

The closest checked material includes Bhamidi–van der Hofstad–Hooghiemstra (arXiv:0903.5136) on typical FPP paths in random configuration models, Renlund (arXiv:1102.4744) on speed along infinite width-two ladders, Leskelä–Ngo (arXiv:1806.09568) on sparse random-graph flooding, and Jiao–Guo–Wang (2025) on stationary wheel SIS infection. The graph ensembles, dynamics, or observables differ in material ways. Published indexed studies of clique-bouquet FPP and static wheel bond percolation were also compared by implication, not only wording. None of the inspected statements gives the fixed-rate wheel survivor-Poisson law or weak-rim crossover; the latter's proof depends on specific local correlation bounds. Indexed GitHub full-text access and global historical-priority completeness remain limitations.

## Mathematical value — PASS

The exact rate \(\alpha+2\beta\), additive Gumbel shift \(2\beta/\alpha\), and sharp \(1/\log n\) crossover identify how very weak rim contacts alter the final infection/extreme flooding statistics of the star. The count-level Poisson theorem provides structural information beyond a leading mean and reveals a rare-site-local-isolation mechanism relevant to contact-network spreading.

## Limits and sources

The findings apply only to the stated irreversible exponential SI process and wheel geometry; they do not assert exact finite-size distributions or arbitrary edge-time universality. The reviewed literature and mathematical comparisons are recorded in AUDIT.json and RESULT.md. Historic priority and independent scientific validation remain open.

Self-review: passed. Independent audit: not yet performed.
