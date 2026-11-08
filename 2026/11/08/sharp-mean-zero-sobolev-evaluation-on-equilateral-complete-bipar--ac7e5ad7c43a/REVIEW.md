# Scientific review: complete-bipartite Sobolev evaluation

## Correctness — PASS

The single claim has a fully specified domain (real continuous edgewise \(H^1\), arclength-mean-zero, unit physical edges, integers \(m,n\ge3\)). Integration by parts derives the Riesz representer; explicit vertex potentials satisfy every Kirchhoff condition; the tent source and edgewise bulk forcing are normalized and integrated; strict concavity and a complete square locate every maximizer and give exact equality cases. A second rational calculation, independent of the unsplit-edge formulas, checks the energy identity on subdivided physical graphs. A symbolic checker verifies the algebra for arbitrary indeterminates. Finite tests are supporting evidence, not an infinite proof.

## Originality — PASS, qualified

Solomyak (arXiv:math/0206235) gives uniform graph Sobolev approximation estimates. Baker–Faber (arXiv:math/0407428) develops Kirchhoff graph methods; Baker–Rumely (arXiv:math/0407427) develops Green spectral theory and explicitly lists a \(K_{3,3}\) spectral example. The inspected primary sections do not state the complete-bipartite point-evaluation quadratic, its shifted interior maximizers, or its sharp global constant. Gervacio (DOI:10.1016/j.dam.2015.09.017) computes resistance between *original vertices*, not explicitly the continuum arclength Green diagonal; only its abstract was accessible. Published-record searches and checks against the closest available graph-Sobolev claims revealed no equivalent, but absence in searches cannot certify novelty. The \(K_{2,n}\) theta-graph boundary is excluded from the novelty claim.

## Mathematical value — PASS

The all-dimensional result answers a natural sharp stability question for a canonical family of highly connected metric graphs. Unlike a naive vertex-based guess, every maximizing evaluation lies strictly inside an edge, and imbalance in the two part sizes shifts it explicitly toward the lower-degree endpoint. The exact quadratic deficit gives quantitative localization and the two asymptotic regimes distinguish fixed-side from jointly growing connectivity. This is an invariant and complete equality classification, not an arbitrarily selected numerical instance.

## Closest literature and remaining limitations

The general Green function and its Kirchhoff construction are prior art. The accessible same-graph spectral table in Baker–Rumely concerns eigenvalues rather than the pointwise extremum, and Gervacio's inaccessible complete text leaves a specific priority risk. The theorem does not cover unequal lengths, higher-degree Sobolev norms, or general multipartite graphs. No external mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
