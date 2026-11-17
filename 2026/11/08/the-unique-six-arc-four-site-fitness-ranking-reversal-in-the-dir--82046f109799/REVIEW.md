# Independent mathematical audit

## correctness

PASS

The finite birth–death Moran Dirichlet equations on mutant subsets correctly sum rates r A_ij/outdeg(i) for mutant additions and A_ij/outdeg(i) for resident removals; strong connectivity ensures absorption and positive-denominator rational fixation. Source verify_symbolic.py enumerates all oriented loopless arc sets for n<=3 and n4 with <=6 arcs, tests both-way reachability, canonicalizes under all permutations, and solves the 2^n−2 linear equations over Q(r). Independent graph-orbit enumeration reproduced n4 strong-connected class counts by arcs 4:1, 5:4, 6:16; independent rational Dirichlet solution on exceptional graph yields ρ2(2)−ρ4(2)=−34255931/1147634834 and ρ2(4)−ρ4(4)=168843849728/21235908109693. The exact rational difference r³P(r)/D(r) with D all positive and P one sign variation and bracket 3<r*<4 proves one crossing. No unbounded n claim; full exhaustive symbolic script inspected, not an infinite-graph proof.

## originality

PASS

Foundational Lieberman–Hauert–Nowak directed birth–death evolutionary dynamics and Broom et al positional fixation on undirected small graphs do not give a complete strongly-connected directed four-site six-arc classification of fitness-induced *relative introduction-site ranking* reversals. Related Resultary work concerns edge-addition effects or position dependence under other update policies; no exact previously published crossing polynomial or six-arc uniqueness was located.

## value

PASS

It is scientifically useful to identify the smallest topology where increasing the same mutant fitness reverses the ranking of two introduction sites, while rigorously distinguishing fixed source-site comparison from graph modification or average fixation. The sharp 4-vertex/6-arc finite cutoff and exact algebraic crossover constitute a natural complete small-graph classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
