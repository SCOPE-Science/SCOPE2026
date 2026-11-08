# Self-review

## Correctness — PASS

The theorem concerns the centered embedding from the finite graph Lipschitz space into uniform vertex \(L^2\), hence the operator norm squared is exactly variance maximized over the Lipschitz unit ball. Every tree-edge coordinate must be \(\pm1\): the variance has strictly positive coefficient \(r(N-r)/N^2\) in the square of every edge increment. Fixing the hub difference to one yields the exact two-count objective \((N(a+1+4j)-(a+1-2k+2j)^2)/N^2\). Its constant-sum diagonal is strictly increasing toward a saturated face, and on the other face strict monotonicity forces the smaller leaf class all the way to level two. Minimizing one residual integer square proves the formula, every optimizer and the parity ties. The fixed-order monotonicity proof uses a strictly decreasing concave quadratic joined tangentially to a decreasing affine envelope; alternating parity corrections cannot reverse a full integer step. The standalone checker, executed from its actual package path, reproduced the 64 exhaustive signed-edge cases, 6,400 exact integer optimizations, fixed-order balance through 300 leaves, and transition profiles. None of the universal conclusions rests on a finite-only extrapolation.

## Originality — PASS, with residual literature risk

The principal published foundation is Alon–Boppana–Spencer, *An Asymptotic Isoperimetric Inequality* (1998, DOI 10.1007/s000390050062), whose Theorem 2.1 proves integral extremizers for graph spread but does not give the present two-parameter formula. The full author-hosted text was inspected for the relevant definitions and theorem and searched for double-star/tree formulas. Addario-Berry–Janson–McDiarmid, *On the spread of random graphs* (arXiv:0902.1156, original posting 2009-02-06), was inspected for the definition and exactly computed examples; its main statements address random graphs, complete graphs and Cartesian products, not diameter-three tree equality classifications. Semantic published-record comparisons found no exact double-star variance source. A source on double-star fractional zero forcing is about a different invariant and does not imply the result; a source on variance of widths of graphical zonotopes of trees instead studies a different random quantity. The nonappearance of a matching claim in these searches is not a proof of novelty. The remaining risk is an equivalent calculation in unindexed, inaccessible, or differently named older literature.

## Mathematical value — PASS

Every diameter-three tree is a double star, so the theorem exhausts the first non-star tree diameter class rather than an arbitrary subfamily. The optimal centered Lipschitz-to-\(L^2\) embedding norm is directly connected to the graph-spread constants controlling sharp product isoperimetry. The theorem gives not only a closed numerical invariant but all equality patterns, an exact imbalance transition, and the uniquely sharp fixed-vertex balancing envelope. The parity-corrected deficit from the elementary \(\operatorname{diam}(T)^2/4\) bound is an exact quantified finite-size statement.

## Limitations and outstanding checks

The proof assumes uniform masses, unit edges, real functions, and diameter exactly three. A full independent audit has not been performed. The accessible primary comparisons do not eliminate every possible older equivalent formula; this residual risk is disclosed rather than treated as an originality certificate.

Self-review: passed. Independent audit: not yet performed.
