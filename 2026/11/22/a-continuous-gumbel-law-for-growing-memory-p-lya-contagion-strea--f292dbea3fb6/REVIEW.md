# Self-review

## Correctness
PASS. The initial \(M\)-block has the classical beta-mixture law and is invariant under the sliding-window predictive kernel. The exact stationary length-\(k\) run-start probability \(u_M(1-q_M)q_M^{k-M}\) follows by subtraction. A shared-uniform coupling gives geometric contraction on scale \(M^2\); the growth condition makes the clustered factorial-moment error \(O(M^{\beta+3}\log n/n)\) vanish. Separating initial-boundary runs and taking \(\tau_M\to0\) yields continuous Gumbel convergence. Exact finite rational checks passed; they are not substituted for the infinite proof.

## Originality
PASS under available primary evidence, not a guarantee of priority. Yu–Alajaji–Gharesifard (2026) use finite-memory Pólya graph indicators but do not state growing-memory long-run extremes. Alajaji–Fuja (1994) develop finite-memory contagion transitions. Chryssaphinou–Papastavridis–Vaggelatou (2001) and Roquain–Schbath (2007) offer stationary Markov word-count Poisson theory; the assessed claim requires an explicit uniform-in-growing-memory bound and its exact continuous Gumbel centering, rather than a fixed-kernel corollary. Existing finite-memory threshold-graph Gaussian results concern edge or triangle counts, not extremes of consecutively arriving universal vertices. Potential unindexed triangular-array rare-word theory remains a risk; the 2001 and 2007 articles were evaluated from accessible abstracts rather than full text.

## Value
PASS. The longest consecutive set of universal-vertex arrivals is a natural extreme local growth statistic for reinforced random threshold graphs. The parameter-dependent centering captures how memory length suppresses or amplifies rare uninterrupted streaks. Its continuous Gumbel law distinguishes growing-memory behavior from discrete subsequence oscillations at fixed memory, and the point-process formulation supplies temporal locations of multiple extremal streaks.

## Scope and risk
Sufficient rather than optimal memory-growth exponent; possible stronger general Markov rare-word results remain to be checked against the uniform mixing estimate. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
