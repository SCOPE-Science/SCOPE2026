# Independent mathematical audit

## correctness

PASS

Reconstructed finite-state Bellman equation V(v)=1+d(v)^-2 sum_{u,w in N(v)} min(V(u),V(w)), with uniform finite expected hitting under forced same-neighbor shortest-path offers. Solved decorated C5+leaves linear Bellman system and checked all order comparisons; k>=2 gap is positive quadratic and k=2 is 4/415, while k=0,1 have distance-first solutions. Independently checked all connected unlabeled graphs n<=6 from the full graph atlas, all marked targets (809 rooted cases), with exact rational solutions satisfying Bellman equality and no distance inversion. Inspected separate submitted exact policy-iteration code which exhausts all 27475 rooted labeled cases, with no pruning of graph masks. Infinite pendant k family rests on algebra, not these finite checks.

## originality

PASS

Known two-choice walk papers optimize by continuation values and discuss non-greedy behavior, but the first failing graph order 7 and explicit infinite decorated-C5 obstruction in the precise two-offer target model are distinct from covered target-hitting bounds and cover-time results.

## value

PASS

Sharp first-order counterexample and exact robust pendant-load gap settle the natural question whether a shortest-path greedy heuristic is always optimal in a well-defined stochastic control process. An all-graph cutoff at 6 is a mathematically meaningful boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
