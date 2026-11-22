# Review: class-level arborescence factorization for finite monoids

## Correctness — PASS

The theorem is quantified over every finite monoid, every unit root, and arbitrary class-constant arc variables. The edge relation is precisely the Green \(\mathcal J\) ideal order. A finite monoid's top \(\mathcal J\)-class is its unit group; all arcs change class monotonically, so any directed cycle lies wholly in one class. For a non-top class of size \(w\), \(k\) designated exit vertices admit exactly \(k w^{w-k-1}\) internal complete-graph directed forests. After summing over exit targets and summing on \(k\), its contribution is \(Q(wt+Q)^{w-1}\). The unit class contributes Cayley's factor. Their product is exactly the claimed polynomial; normalized factors give the independent class-exit laws. The special cases \(w=1\) and a one-unit monoid are included. The checker separately computed exact Laplacian cofactors, direct parent-map counts, and Green orders from small monoid multiplication tables. Finite experiments are evidence only for implementation consistency, not a proof for all monoids.

## Originality — PASS, with residual priority risk

The motivating article by Xuan Yang, Yong Shao and Lingli Zeng, *Divisibility graphs of semigroups as weighted poset blow-ups* (arXiv:2611.13455v1, first posted November 10, 2026), provides the class-block graph decomposition, but its full-text sections on structure and saturation do not compute rooted spanning in-arborescences or their probability law. The prior arbitrary-digraph polynomial-factorization work by Mihalák, Uznański and Yordanov (arXiv:1507.07727) implies general algorithmic ways to compute an arborescence polynomial but does not state the explicit classwise formula. The older Cayley forest formula supplies the local enumeration, not the full monoid factorization and joint exit-count law. Claim- and alias-level literature searches found no explicit covering statement; historical priority remains conditional on unindexed results and equivalent reformulations using directed matrix-tree determinants. This is not claimed to be independent validation.

## Mathematical value — PASS

The entire rooted in-arborescence class-edge polynomial of every finite monoid is an intrinsic invariant of its weighted \(\mathcal J\)-poset. The exact product gives counts for all finite transformation and inverse monoids from their class sizes, and the independent multivariate exit laws supply more information than a total tree count or a connectivity result. The natural object is the newly described divisibility graph, and the gap between a structural blow-up and quantitative spanning-tree enumerators is mathematically motivated. The deduction uses classical forests, but the closed all-class theorem and probability law are not a mere numerical recomputation.

## Sources and limits

- Yang, Shao and Zeng, arXiv:2611.13455v1, especially Theorem 3.5 and Sections 3–4: the structural blow-up, no corresponding enumerator found.
- Mihalák, Uznański and Yordanov, arXiv:1507.07727: general Kirchhoff-polynomial factorization, not the class-specific product.
- Avron and Dershowitz, *Cayley's formula: A page from the book*: the classical rooted-forest identity used in the proof.

Only finite unital semigroups and arborescences directed toward a specified root are treated. The formula groups arcs by source and target \(\mathcal J\)-classes; it does not determine fully edge-individual polynomial coefficients. The originality judgment is literature-limited; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
