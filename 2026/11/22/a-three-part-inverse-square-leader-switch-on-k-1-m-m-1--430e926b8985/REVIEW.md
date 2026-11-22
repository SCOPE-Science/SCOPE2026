# Review of the \(K_{1,m,m+1}\) inverse-square placement theorem

## Correctness — PASS

The claim is exact for every integer \(m\ge2\) and all unordered two-element leader sets. The Laplacian normalization, pinned-vertex operation, five orbit types and positive-definiteness are explicit. The derivation uses the full spectrum of a complete multipartite Laplacian, an explicit shifted resolvent, Jacobi's complementary-minor formula, and the identity \(\operatorname{tr}(L_{FF}^{-2})=-\partial_z^2\log\det(L_{FF}+zI)|_{z=0}\). Four exact rational gap identities are checked symbolically; their denominators are positive and their shifted numerator polynomials have strictly positive coefficients for every \(m\ge3\). At \(m=2\) all other orbit costs exceed the middle–middle orbit by four displayed positive rational amounts. All 154 pair matrices for sizes 2--5 and 25 representative matrices for sizes 6--10 agree exactly with the symbolic formulas. The infinite-family proof is algebraic and does not depend on numerical sampling.

## Originality — PASS on inspected sources, qualified

The 2013 Lin–Fardad–Jovanović leader selection manuscript establishes general optimization formulations for first inverse traces; the inspected formulation, algorithm and examples do not classify \(\operatorname{tr}(L_{FF}^{-2})\) for this graph. Patterson–Bamieh (2013) treats second-order coherence through squared inverse nonzero Laplacian eigenvalues on *ungrounded* fractal networks, not pinned-leader selection. The closest public theorem, *A gain-independent three-phase two-leader law on \(K_{1,m,m+1}\)*, was read in full: it considers finite equal-gain \(\operatorname{tr}(L+\kappa D_S)^{-1}\), not inverse-square grounded matrices, and selects the middle–middle pair at \(m=3\). The present theorem rigorously selects universal–middle at \(m=3\), so the old theorem neither states nor implies the proposed result. The public unequal-multipartite first-inverse theorem specifically excludes singleton parts. Indexed searches and claim comparisons found no equivalent squared-inverse all-size statement. This is not a proof that no unindexed or inaccessible equivalent exists; priority risk remains.

## Value — PASS

The result settles every two-leader placement on a natural, infinite, nearly balanced three-community network family. Its sharp structural threshold \(m=3\) differs from the first inverse-power threshold \(m=4\), and the same eight-vertex graph has disjoint exact optimizers for two standard spectral performance criteria. The theorem therefore supplies a concrete design boundary showing why first-order leader prescriptions cannot automatically be reused for inverse-square performance. The exact minimum and optimizer multiplicities are included. This is a narrow but motivated natural classification, not a random finite instance or an arbitrary parameter slice.

## Closest work and limitations

The main comparison is the public 2026 finite-gain first-inverse tripartite theorem, whose full proof was read. General source papers include Lin–Fardad–Jovanović (arXiv:1302.0450, originally posted 2013-02-03) and Patterson–Bamieh (arXiv:1310.2592, originally posted 2013-10-09). An unequal-multipartite 2026 first-inverse theorem excludes singleton parts, and a bipartite second-order theorem concerns a graph without the universal vertex. The current theorem does not cover arbitrary spectral powers, budgets other than two, weighted edges, or all complete multipartite graphs. Unindexed equivalences remain a scientific priority risk; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
