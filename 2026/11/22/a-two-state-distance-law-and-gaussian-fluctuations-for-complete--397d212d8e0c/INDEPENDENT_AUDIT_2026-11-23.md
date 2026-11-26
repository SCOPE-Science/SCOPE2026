# Independent mathematical audit

## correctness

PASS

Unit flow on this DAG decomposes into increasing source-to-sink paths, and each indicator path is extreme (its support alone carries only that unit flow). Two independent uniform subsets of the m internal vertices give four equiprobable membership symbols per site. Squared distance counts the edge symmetric difference; a common arc joins consecutive 11 symbols after deleting 00 symbols, with 11 at the two endpoints. Thus tracking whether the last nonzero symbol is 11 gives exactly the stated matrix and the sink charge 2 only in state 0. Direct path comparison at m=2 gives (4+8z³+4z⁴)/16; m=0 gives 1. Independently, the probability r_j of state 1 after j sites is 1/3+(2/3)4^(−j). A site charges 1 or 1/2 in expectation conditional on state 0 or 1. Summing 1−r_j/2 over j=0,...,m−1 and adding 2(1−r_m) yields the exact mean. The characteristic polynomial is λ²−(3+2z)λ/4+(1+2z−z³)/8; implicit differentiation at the simple root 1 gives λ′(1)=5/6 and λ″(1)=7/27. Hence the log eigenvalue at z=e^t has second derivative 43/108. The other root is 1/4 at z=1, so analytic spectral projection yields the CLT via characteristic functions and the variance rate by differentiation; the square-root identity gives 43/360 for the ordinary-distance limit.

## originality

PASS

The supported distinction is the evaluated random-pair law and fluctuation constants in the full arc-coordinate metric for the complete DAG. The path encoding, analytic transfer matrix method and extremal distances are not claimed as novel. The checked statements do not supply the random-pair law or imply the evaluated constants.

## value

PASS

Uniform vertex-pair distances in the canonical edge metric describe the geometry of a standard flow polytope beyond its incidence structure or diameter. A two-state exact full law makes distance probabilities computable and quantifies both typical scale and the nonvanishing ordinary-distance fluctuation, rather than reporting a few cases or a big-O bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
