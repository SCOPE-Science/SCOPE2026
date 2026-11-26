# Independent mathematical audit

## correctness

PASS

For a two-step return on the connected graph, the sum of the two firing vectors is in the kernel of the Laplacian. The only constant possible for a nonfixed return is one. Given the first firing pattern, solving the complementary threshold inequalities gives exactly c_v consecutive nonnegative chip counts at each vertex, all below 2d_v. A nonzero product has a mixed pattern, so the first update is not fixed. Complementary time phases give the factor 1/2. Once the old vertices are colored, same-shore subdivision vertices are forced with weight two, and each cross edge contributes to exactly one old endpoint. In the product expansion the only conflicts are reciprocal selections, and any consistent set of j forbidden pairs is a j-matching on the selected shores. This proves the stated inclusion–exclusion, including empty shores under the specified power convention. Polynomial precomputation and four bounded indices suffice for the exact arithmetic bound; this is not an optimality or unit-bit-cost claim. In fact, summing the k and ell binomial terms at fixed j gives factors (a−1+b/2)^(a−j) and (b−1+a/2)^(b−j), with prefactor (−1)^j binom(a,j)binom(b,j)j!/4^j. My replay of this collapsed form reproduced all six listed integers and a separate direct threshold update on all 4^6 states for n=3 gave 100 orbits. Replay: /workspace/branches/independent_replay.py, chip(). The packaged source and its recorded tests were inspected, not executed.

## originality

PASS

The unrestricted cut census already determines the orbit number via an exponential cut enumeration. The supported distinct contribution is the efficient exact evaluation for the fully subdivided labelled clique, not the cut-degree identity, its threshold proof, or a generic algorithm for all graphs. No equivalent efficient census was established by the bounded comparisons.

## value

PASS

This is an exact dynamical invariant for a natural incidence-graph family. The subdivision makes a naive firing-pattern sum exponential in a quadratic number of vertices. Removing that enumeration with a computable conflict sieve gives a usable all-size census, not merely a list of small cases or a parameter substitution into the known exponential sum. The result is limited to primitive two-step temporal orbits; it does not address longer periods or basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
