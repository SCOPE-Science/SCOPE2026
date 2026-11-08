# Scientific review of the cyclic \(k\)-path cover slide metric

## Correctness — PASS

The theorem precisely excludes the only nontrivial disconnected layer, \(kt=n\). A token slide is an adjacent exchange preserving the cyclic upper-gap bound. Flow conservation proves a lower bound in every realization. Choosing a median sets at least one flow edge to zero; the ordered line matching across that cut has exactly the bound's cost. The bounded-gap feasible lifts are closed under coordinatewise maxima, and a blocked-move dependency argument constructs monotone unit-coordinate paths between ordered feasible lifts whenever \(t<n<kt\). This realizes the lower bound without violating coverage. Both full BFS programs and the independent explicit-path construction passed for their stated finite scopes. The infinite assertion relies on the combinatorial argument, not the experiments.

## Originality — PASS, qualified historical priority

The 2010 introduction of \(k\)-path vertex covers is the foundational source. The closest primary text, Hoang–Suzuki–Yagita, Section 4.2.2 and Theorem 16, proves exactly the reachability dichotomy and gives a polynomial cycle reconfiguration algorithm, while expressly stating that the cycle algorithm is not always shortest; only the path algorithm is shown to be shortest. That is an implication comparison, not merely title matching. The new claim strictly strengthens the known nonfrozen **existence** statement by identifying all pairwise shortest lengths and an isometric metric structure. It leaves the older reachability result as prior art. Searches for cyclic bounded-gap, 3-path vertex cover, median earth-mover, reconfiguration graph and shortest-sequence formulations found no equivalent published statement. The possible existence of an equivalent treatment under exclusion-process terminology remains a residual historical-priority risk.

## Value — PASS

The exact minimum number of protection relocations is a natural optimisation target in the dynamic path-cover problem, not a renaming of the known cover number or an arbitrary finite statistic. The result removes a genuine limitation in the closest cited paper (non-shortest cycle sequences) for every order, every path length and every feasible token layer. The flow formula is linear-time evaluable, and the legal-geodesic proof identifies a strong isometric subgraph property with reuse potential in bounded-gap token systems. The frozen boundary is sharp.

## Scope and risks

The graph is an unweighted labelled cycle, moves are one-edge token slides, and the exact metric excludes the known frozen layers. The literature comparison is substantial but does not amount to independent priority verification. The standalone programs check finite orders, not all orders. No claim about shortest token-jumping sequences is made.

Self-review: passed. Independent audit: not yet performed.
