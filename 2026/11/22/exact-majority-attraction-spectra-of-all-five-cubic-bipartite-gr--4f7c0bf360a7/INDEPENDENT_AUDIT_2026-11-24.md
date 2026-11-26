# Independent mathematical audit

## correctness

PASS

Equal shore degree sums force a 6-by-6 biadjacency matrix. I independently enumerated matrices by adding one column of weight three at a time, keeping high-bit row prefixes sorted and only pruning when residual row sums are impossible. This represents every graph up to left relabelling. It yields 550 sorted-row matrices, 540 connected, 147 with a row mask 7. The five listed representatives produce disjoint complete orbits of sizes 90,180,60,180,30 under permutations of both shores and transpose, exhausting the 540. Connectedness makes the bipartition unique up to reversal. The minimal tuples and the independent prism and Franklin constructions match. For dynamics I formed all 4096 outputs per graph by expanding winning neighbor pairs to supersets, then traversed the reverse graph from exact fixed and 2-periodic states. Every initial state is reached and the largest depth is two in each case, proving F^4=F^2 and excluding longer periods; in order B1–B5, masks 5,5,6,6,5 give depth two. Independent counts match every first-entry/period cell, all individual-attractor basin size multiplicities in GRAPH_DATA.json, and all stated extrema and square counts. The 3516 states eventually oscillating on the prism give 879/1024; its 231 primitive two-cycles and Franklin's basin maximum 722 are the claimed unique extrema. The held-fixed graph labels and temporal orbit quotient were used exactly as defined. The authored programs were inspected, not executed.

## originality

PASS

The complete order-twelve graph classification and the prism's own recurrent population were already known; the fully flipping prism subpopulation was also separately known. Pass for the distinct sharp two-update bound on all five, the complete entry and basin spectra, and the resulting dynamical comparisons across the entire class. Those are not obtained from known recurrent populations, graph-class counts or generic voting-time bounds.

## value

PASS

A complete isomorphism class at a fixed small cubic bipartite order is a natural controlled comparison. All classes share the same sharp entry clock while actual oscillation probabilities and largest basins differ; the graph with the most oscillatory orbits is not the graph with the largest basin. Two graphs even share the square count but not these spectra. The exact tables are useful for checking stronger convergence or attractor predictions and add information beyond the prior classification and B3's recurrent count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
