# Independent mathematical audit

## correctness

PASS

For any two selected K_n edges, a disjoint pair of unselected edges can meet both, whether the selected edges meet or not. For three selected edges, the only failing type is P4: its two diagonally crossing witnesses are disjoint and meet all three selected edges. A triangle or 3K2 leaves nothing; a star or P3 plus K2 leaves only edges through a single common point. There are 12 forbidden triples per four-set. Deleting one selected edge leaves either an adjacent pair (2(n-3) P4 extensions) or a disjoint pair (4 extensions); subtracting these from the Johnson degrees gives every table entry. Independently checked the universal upper bound by a different reduction from the frozen partition program: any pair uses at most 12 endpoint labels, so embed in K12 and relabel the first triple to one of four type representatives. Directly testing the original isolation condition gave 39,820 K12 states; for each representative and each such target (159,280 pairs), testing for a direct edge, common neighbor, or adjacent first/last neighbors inside the union gave a path of at most three. Since paths only use edges of that union, they pull back to every original n, including n<12. Two disjoint states in K5 force three steps, and the nonisometry witness has all four potential Johnson intermediates forbidden. The independently written check also reproduced the example state and edge counts at n=5,6,7,8.

## originality

PASS

The known numerical Petersen case is explicitly not a contribution. The strongest related published statements concern different predicates or extremal ranges and do not yield the all-order minimum configurations, induced exchange graph, or its sharp diameter/nonisometry. The exact Resultary hit is this same record.

## value

PASS

This gives a complete optimal-state space for a natural infinite family, not a new label for the Petersen scalar minimum. The simple forbidden-pattern description exposes degree heterogeneity and a uniformly sharp exchange bound even though ambient Johnson geodesics need not remain feasible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
