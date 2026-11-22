# Review: Sharp Fibonacci-to-dyadic Fourier-rank bounds for permutation comparisons on trees

**Correctness — PASS.** The Fourier factorization and prior bipartite graph-Eulerian nonvanishing theorem identify the rank with the odd-component subforest count. The two-state recurrence and Fibonacci inequalities are exact, the leaf argument proves unique minimizers, and the parity count with two-disjoint-edge obstruction proves unique maximizers. The verifier checks 1,441 labelled trees and 2,142 direct multipliers. The computations do not replace the infinite proof.

**Originality — PASS under bounded source comparison.** Foata--Schützenberger [1] covers the path-era Eulerian background. Celano--Sieger--Spiro [2] supplies the nonvanishing theorem and even-edge tree positivity, and therefore much of the *support criterion* is known. Their extremal theorem concerns the magnitude of one evaluation rather than the number of nonzero frequency evaluations on each tree. The new claim is only the global sharp rank bound, the two unique extremal tree types and the recurrence. Indexed comparison searches did not reveal an equivalent claim; unindexed earlier combinatorics remains the main priority risk.

**Value — PASS.** A genuine all-order Fourier identifiability classification for the natural distribution of edge comparisons, not a small finite improvement or an isolated special case. It directly quantifies shape dependence and gives a linear arithmetic-time exact algorithm.

**Limits.** Does not give inverse norms, individual multiplier magnitudes or graph-general bounds; full external priority and correctness reviews remain open.

Self-review: passed. Independent audit: not yet performed.
