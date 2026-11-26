# Independent mathematical audit

## correctness

PASS

Independently constructed the graph from the 12 golden-ratio icosahedron vertices with exact integer-pair arithmetic and checked isomorphism to the stated two-ring graph by adjacency-preserving backtracking. Computed distances by Floyd–Warshall, exhausted every subset of size at most 3, and tested set equality with the two specified families (both directions). Enumerated 120 automorphisms by backtracking and checked transitivity on each sector. Tested every pair of states for membership in each move graph by its symmetric difference and the underlying exchanged pair's adjacency; Floyd–Warshall and per-state invariants give degrees (13,9)/(7,9), eccentricities (3,3)/(4,3), 480/300 edges and finite distances throughout. Among all 3160 pairs the differences have counts 2440/690/30. Exact equality of the extremal set with the retained-antipodal-pair and exchanged-antipodes predicate holds, and every extremal pair has distances (1,3). Closed neighborhoods each have size six and a dominating pair must be disjoint in closed neighborhoods, hence antipodal and infeasible; enumeration separately covered the smaller sizes. All move paths stay among global minima.

## originality

PASS

The distinct content is the classification and exact local-versus-global move metric on the minimum semitotal family, especially the complete obstruction criterion; not the ordinary domination number, semitotal predicate, or token-move definitions.

## value

PASS

Minimum semitotal domination is a motivated constraint between ordinary and total/paired domination; the regular icosahedron is a natural highly symmetric test case. Comparing sliding and jumping exposes a precise shortest-path phenomenon explained by the ambient antipodal involution, rather than only a finite count of minima. The exact iff description and its distances are useful as a benchmark for constrained reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
