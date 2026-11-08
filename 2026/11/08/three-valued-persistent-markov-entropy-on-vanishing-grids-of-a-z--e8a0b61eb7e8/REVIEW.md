# Scientific review

## Correctness
**PASS.** The candidate is an exact theorem for every integer \(N\ge10\): the source image of the zero cell spans exactly the two or three consecutive target cells, the slope \(-2\) yields their overlap weights, and all these cells lie on the constant branch so form a closed two-step class. Every other cell admits positive transition paths into this class because all nonfixed deterministic orbits eventually enter the clipped branch. The unique stationary vector follows by balance, giving a three-valued entropy rate. Monotonicity of every map iterate proves zero topological entropy with a separated-set bound. Exact rational checks for \(10\le N\le200\) corroborate but do not replace these arguments.

## Originality
**PASS within examined literature.** The primary 2026 study defines and computes weighted transition graphs and Markov entropy rates but does not give a fixed zero-entropy map with nondecaying exact Markov entropy under all mesh refinements. Classical Ulam and graph-entropy studies establish the general distinction between coarse transition chains and deterministic trajectories; their stated results do not imply this unique-stationary-law residue-class classification. In particular, graph path entropy upper bounds are not the stationary, row-weighted Shannon entropy considered here. The 2023 article on coarse-grained Kolmogorov entropy concerns a broader stochastic-process framework; its full proof was not inspected, leaving an explicit historical-priority risk. Database search is not proof of novelty.

## Mathematical value
**PASS.** Entropy rate of a finite weighted transition graph is a natural quantitative diagnostic, so determining whether it converges as cell size vanishes is mathematically motivated. This example provides an all-resolution classification, proves stationary-measure weak convergence, and quantifies an entropy gap uniformly bounded below despite zero entropy and a finite attracting orbit. It isolates irreversible within-cell resampling rather than deterministic chaotic motion as the source of entropy. It is a meaningful sharp boundary for interpreting coarse-grained Markov statistics, not merely a toy finite count.

## Limitations and risks
The result does not concern finite Monte Carlo samples, filtering, teleportation, or a specific experimental classification. The exact gap is not asserted for every grid alignment or every interval map. Related historical coarse-graining literature may contain other constructions; independent review and exhaustive priority verification remain open.

Self-review: passed. Independent audit: not yet performed.
