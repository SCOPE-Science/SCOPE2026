# Scientific review

## Correctness: PASS
The claim is a finite enumeration of all 8,191 nonempty vertex subsets of a thirteen-vertex graph, with explicit graph construction, admissibility predicate and exchange adjacency. Python and C++ source implementations separately construct adjacencies, test connectedness by different methods, and independently calculate the full connected domination polynomial, all inclusion-minimal sets, five affine orbits and all-source exchange distances. They agree on 260 minima, 1,911 exchanges and radius/diameter four. Since every graph subset and every exchange pair is covered, this is a logically exhaustive finite claim, not an extrapolation or a timeout-based exclusion.

## Originality: PASS (bounded historical risk)
The closest graph-specific foundational text describes Paley graphs and their invariants; the relevant connected-domination enumeration paper develops algorithms, not this particular thirteen-vertex minimum-backbone census. Other checked results concern topology of Paley-thirteen complexes, minimum connected-domination exchange on a four-cube, or finite-field graph clique structure. Their statements do not logically determine the joint five-orbit exchange distance data. Independent archival and unindexed database coverage is incomplete, so exact priority remains provisional.

## Value: PASS
Connected dominating sets model the smallest connected backbone dominating a network, equivalently internal vertices of a spanning tree with many leaves. The Paley graph on thirteen vertices is a canonical quadratic-residue network, not a parameter-chosen artificial slice. Its complete minimal backbone classification exhibits uniformly four-vertex solutions and a nonregular but self-centered exchange graph with five explicit symmetry types; these exact mobility facts would not be obtained from the domination number alone and are usable as a sharp finite benchmark for connected-backbone reconfiguration.

## Risk and boundary
The claim concerns only the named thirteen-vertex Paley graph; no general Paley-family formula, random-network claim or independent peer review is asserted. Historical exact tables not located could contain overlapping results.

Self-review: passed. Independent audit: not yet performed.
