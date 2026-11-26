# Independent mathematical audit

## correctness

PASS

A shortest path changes just the differing coordinates, once each; an unused coordinate can always be changed at an end, so maximal paths change all d coordinates. Independent alphabet permutations are transitive on each E_i. Each maximal path uses one edge from E_i, giving each edge marginal 1/|E_i| under uniform choice of path. Thus any hitting set has size at least min_i |E_i|, achieved by a smallest class; equality forces exactly one hit on every path. For any coordinate square, the two different pairs of opposing corners give two independent path comparisons, with common suffixes changing every other coordinate. Subtract the two path-sum equations to equate one pair of parallel indicators; substitute to equate the other. The indicator for a fixed letter pair in a fixed coordinate is therefore independent of background coordinates. Now the sum across any independently chosen letter pairs is one, so varying a single pair makes its indicator independent of that pair as well. The binary constants therefore select exactly one whole class. This also covers d=1, with no square needed. Comparing class sizes gives the labelled optimizer census.

## originality

PASS

The known binary optimum and coordinate-cut example are not treated as novel. The distinct claim supported by the comparison is the full mixed-factor theorem, especially the exact-one classification without a size restriction. Neither the retrieved two-side-cut criterion nor the indexed binary packing and multipartite theorems cover this scope.

## value

PASS

It identifies every labelled minimizer of a natural path-hitting invariant for unequal complete factors, where an optimum value alone gives no description of the hitting sets. The stronger exact-one result is a structural characterization independent of cardinality and explains why the minimum lies in one direction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
