# Review of partition-discrepancy Lipschitz variance on clique windmills

**Correctness (PASS).** Anchored variance is strictly convex; maximizing functions are vertices of the product of clique Lipschitz polytopes. Each blade has a connected tight-edge graph to the common hub, so its values belong to \(\{-1,0,1\}\) with only one nonzero sign per blade. Grouping blade signs yields two integer capacities. The exact minority-saturation and majority quadratic optimization is fully derived; its envelope strictly decreases with partition imbalance, proving the all-size-vector formula and classifying every equality case. The dominant-blade condition follows from a greedy discrepancy bound and the exact large-blade minimum partition. The binary-input PARTITION reduction is explicit. Exact rational finite tests corroborate these proof steps but are not infinite certificates.

**Originality (PASS; qualified).** Alon–Boppana–Spencer's general integer-extremizer structure, Addario-Berry–Janson–McDiarmid's random-graph spread framework, and Yancey's odd-cycle/long-path results were inspected at the relevant primary full-text sections. None supplies this heterogeneous clique-windmill signed-partition formula or the succinct complexity consequence. Closest searchable windmill results concern dissociation polynomials, while an earlier separate two-clique bridge problem changes the graph and does not imply the present arbitrary blade-size family. A precise unindexed prior exact calculation remains possible.

**Value (PASS).** This is a natural complete family of block graphs, with an exact centered Lipschitz embedding constant, every extremizer, a sharp structural transition and a binary-encoded number-partition equivalence. The invariant's dependence on imbalance is mathematically motivated by how positive and negative clique leaves contribute to variance.

**Scope and risk.** Unit edges, uniform masses, real functions, one shared hub. No claim for general block graphs or polynomial-time complexity on explicitly expanded graphs. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
