# Independent mathematical audit

## correctness

PASS

Complete the graph on the marked endpoints and two fresh vertices: every possible trace is the union of the incident-mark signatures of the endpoints of an unmarked edge. Equal nonempty signatures at distinct vertices occur exactly at the ends of an isolated marked K_2. If r is the number of distinct nonempty signatures, ℓ the number of K_2 components and p the number of P_3 components, r=|V(S)|−ℓ. Among the empty, singleton-signature and distinct signature-pair candidates, discard m−ℓ signature pairs used exclusively by marked edges and p valid leaf pairs whose union already equals the middle signature. This gives 1+r+binom(r,2)−(m−ℓ)−p. A connected e-edge component has at most e+1 vertices, so D=3m−2r≥ℓ; the only zero contribution is P_3, and deficit one means K_2 or a three-edge tree. Substituting ℓ≤3m−2r gives the lower-r bound 1+binom(r,2)−r+2m, increasing for r≥1. It is strictly below the proposed extremum if r≤3k−1 for even m=2k≥4 or r≤3k for odd m=2k+1≥3. At D=0 only kP_3 is possible; at D=1 the P_4 option has an extra collision (its two distance-two nonedges both hit all three marks). For attainability, cross-component traces recover the two signatures on their disjoint component supports. Within K_2 there is just one nonempty trace, within P_3 the two singletons and their union, and within a claw the three singleton leaves, three leaf-pair unions, and the center signature. Summation, including one empty trace, gives exactly the displayed values and both m=2 equality types; m=1 has exactly two attainable traces. This establishes classification of marked graphs that can attain, not of all ambient graphs. Independent direct line-adjacency enumeration checked the bound and equality predicate for 17,421 labelled small marked-edge families on up to six possible endpoints and at most seven marks.

## originality

PASS

The trace definition and the inverse locating-domination interpretation are not new. The distinct exact result is the line-graph capacity at a fixed number of marks, with both parities and the complete marked-edge equality types. The closest inspected indexed trace-capacity result is for permutation representations; the closest primary extremal theorem is for the stronger all-edge identification condition and yields a different coefficient and different extremizers.

## value

PASS

The number of distinguishable unmarked edges at a fixed marking budget is a natural extremal invariant, exactly equivalent (up to the empty trace) to inverse edge-locating domination. The completed ambient construction and full marked-component characterization determine which sparse mark configurations achieve the sharp quadratic capacity; the difference between a three-edge path and a claw is invisible to a crude endpoint bound. These conclusions are useful beyond the generic fact that the growth is quadratic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
