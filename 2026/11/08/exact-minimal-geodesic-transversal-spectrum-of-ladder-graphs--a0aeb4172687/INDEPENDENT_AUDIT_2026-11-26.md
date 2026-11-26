# Independent mathematical audit

## correctness

PASS

Distances are rung difference plus the column-change indicator. Thus shortest paths are monotone in the rung and use at most one switch. Extension gives exactly the two diameter-endpoint pairings with h switch positions each. If both columns are chosen, a path in one orientation misses the set exactly when its switch index t lies strictly between the maximum selected rung of its ending column and the minimum of its starting column; both orientations give the two gap inequalities. With one chosen column, the two extreme switches force its boundary pair. Only column extrema can be essential. In a 2+2 selection, both minima being essential would require each column maximum to exceed the other by at least two, an impossibility. In a 2+1 selection the singleton must be at least two rungs inside both extrema; removing it fails unless the two extrema are the full boundary pair. This proves both directions for all three labeled families. Pairs total 2+h+2(h−1)=3h. Per doubled column the count is binom(h−2,3)−(h−4) for h≥4, and is zero at h=2,3. Complementation makes minimal transversals correspond to facets, so positivity of the triple term from h=6 gives the stated purity cutoff.

## originality

PASS

The minimum value 2 is prior, even on all rectangular grids. What survives is the labeled inclusion-minimal classification, size spectrum, and resulting purity cutoff. A distinct same-day ladder homology record has exactly the same cubic coefficient as a Betti number, but not the transversal spectrum or the complement complex.

## value

PASS

The smallest nontrivial Cartesian strip is a natural test family for the maximal-geodesic covering hypergraph. The formula distinguishes optimum from inclusion-minimality and locates the first non-pure order h=6; the labeled families identify exactly which irredundant covers cause that distinction rather than merely giving a scalar optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
