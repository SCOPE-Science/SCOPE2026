# Independent mathematical audit

## correctness

PASS

Reconstructed the porous obstruction: with three same-shore sources there is a line (dually point) outside their incidences, at distance 3 from all; with one selected line and at most three selected points, the eight lines disjoint from it cannot all meet the selected points. For four same-shore sources the (15,6,1,3) collinearity graph needs ≥2 selected neighbors per outside vertex. The 24−2e count forces e≤1; counting common neighbors of selected pairs then contradicts either possible outside degree distribution (no triangle through three selected vertices when e≤1). In the 2+2 case every other duad meeting both point sources must be incident to at least one selected line. Intersecting sources yield three pairwise intersecting required duads, which two synthemes cannot cover. Disjoint sources force the two cross matchings on their four symbols and thus one flag on the remaining duad. Independently ran `python3 /workspace/branches/reproduce-3.py`: on the exact 30-vertex graph, exhaustively checked all subsets of sizes 0–4 with porous screening, then blocked-distance integer scores scaled by 2^28. The porous counts were 0,0,0,0,45; all 45 survived exactly and matched the flags, with profile counts 16,8,2 at 9/8,21/16,3. Exhaustively checked that distinct winners intersect in at most one source, the intersection graph has degree 20, and each nonadjacent pair has a common neighbor. This gives 450 edges, excludes universality of each vertex, and verifies both radius and diameter 2. As an analytical cross-check, line-graph distances 1 and 3 between incidence flags give an exchange edge: at distance 1 the flags share a third neighbor at their common endpoint, and at distance 3 the opposite ends of a shortest two-step endpoint path have its interior as a common source. Line-graph diameter is at most 4 since opposite-shore endpoint distances are ≤3. Distances 2 and 4 split into 1+1 or 1+3 on a geodesic, giving exchange distance at most 2. The six-symbol action is transitive by relabeling the three duads of the flag's line and its designated duad. The new exact enumeration is for this one graph; the packaged programs were not executed.

## originality

PASS

The blocked-source definitions, graph model and general subcubic bounds are classical. The closest indexed exact match is the frozen record itself; other checked exact Tutte–Coxeter results use different invariants. The inspected sources do not establish the joint minimum, flag classification, weight profile and optimizer replacement geometry. This is a bounded, statement-level assessment, not a priority certification.

## value

PASS

The 8-cage is a canonical test of exponential influence in a small cubic graph with large girth. The exact classification explains which local incidence configurations attain the optimum, supplies a quantitative strict margin under source blocking, and identifies when those choices are disconnected or connected under local replacement. That establishes a reusable benchmark for both weighted domination and reconfiguration, beyond an isolated minimum number or a brute-force count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
