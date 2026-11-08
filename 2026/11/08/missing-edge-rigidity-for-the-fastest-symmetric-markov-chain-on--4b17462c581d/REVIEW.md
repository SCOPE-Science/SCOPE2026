# Scientific review

## Correctness — PASS

The proof specifies the domain, stochastic constraints, uniform stationary distribution, and SLEM norm exactly. For every vertex the Cauchy--Schwarz minimum among columns with \(r\) forbidden positions gives \(\|Pe_v-J e_v/N\|_2^2\ge r/[N(N-r)]\); dividing by \(\|e_v-\mathbf1/N\|_2^2=(N-1)/N\) gives the stated uniform lower bound. A nonmatching complement has a vertex with two forbidden neighbors, giving strict separation. For matching complements the matrix \((J-Q)/(N-1)\) is feasible and its centered square equals \((I-J/N)/(N-1)^2\), establishing equality. Exact rational replay from the accompanying verification file passed. Finite checking supplements, rather than replaces, the proof for arbitrary size.

## Originality — PASS on inspected evidence, with a publication-priority risk

Boyd--Diaconis--Xiao (2004) gives the overall convex optimization framework; Boyd--Diaconis--Parrilo--Xiao (2007/2009) includes edge-transitive special cases and a symmetry reduction, so a fully paired complete graph is already covered at the level of an exact spectral solution. The new assessed claim is the universal lower frontier *over every noncomplete graph*, the iff characterization by missing-edge matchings (including nonregular examples), and a local quantitative exclusion bound. Neither inspected relevant primary-text treatment supplies those two general statements. Searches for an equivalent matching-complement equality characterization did not find one, but they cannot establish priority over unindexed material.

## Value — PASS

The theorem answers the extremal-design question of precisely which noncomplete network topologies can mix as fast as any noncomplete topology of the same order. It shows that disjoint missing edges carry no additional SLEM penalty beyond a single missing edge, while even one vertex with two missing neighbors creates a provable strict gap. The construction and universal obstruction are exact for an unlimited graph family, not a single numerical instance or a minor change of notation.

## Scientific boundaries

Symmetric row-stochastic, nonnegative chains only; diagonal holding allowed. The local obstruction for two or more missing neighbors is a lower bound, not an exact SLEM formula for every such graph. Independently established mathematical priority and validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
