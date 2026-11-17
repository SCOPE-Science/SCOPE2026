# Independent mathematical audit

## correctness

PASS

A fixed proper h-arc subset of a directed k-cycle consists of disjoint directed paths, which collapse to n−h ordered blocks; the probability of all arcs in one uniform successor path is (n−h)!/n!=1/(n)_h. A complete directed cycle in a single path has probability zero, requiring truncation at k−1. One avoidance and one union inclusion-exclusion prove the exact finite-k expectation including k=n and r=1. For vertex-disjoint cycles of total L edges, color each required arc by one of r paths: every assignment is feasible except a monochromatic cycle. Their (∏_i(r^{k_i}−r)) n^−L leading probability has O(n^−L−1) overlaps from arcs assigned to more than one path. Overlapping distinct cycles have strictly more distinct arcs than vertices per multicyle component, making their total factorial-moment contribution O(n^−1). Thus each fixed mixed factorial moment tends to that of independent Poisson((r^k−r)/k), giving joint weak convergence and the directed girth law. Scope is fixed r and finite K; finite n is not Poisson.

## originality

PASS

The most relevant new 2026 successor papers address FO² finite satisfiability and signed cycle elimination, not random uniform path sampling, uncolored mixed directed short-cycle probabilities, or exact finite expectation. Random-permutation and undirected regular-graph Poisson analogues have different ensembles. A known two-path two-cycle overlap case is credited, but it does not imply the general r,k joint law.

## value

PASS

A union of naturally sampled linear-order successors can have directed cycles despite each constituent being globally acyclic; the exact Poisson means measure the nontrivial deficit r/k relative to independent sparse arcs, and yield directed girth and non-zero-one limiting first-order cycle events. This is a meaningful structural random-finite-model statistic, not a tiny special-case count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
