# Scientific review: triangular Johnson graph visibility

## Correctness — PASS

For a width \(k\), the permanent pebble invariant is an endpoint-support bijection. Removing one pebble leaves at most \(2(k-1)\) occupied ground elements, so each side of ground-set size at least \(2k\) can realize any new two-element subset pattern using at most two fresh points. This preserves the atomic equality/adjacency diagram for unlimited play. To distinguish each smaller ground-set order \(n\), let \(t=n+1\le2k\) and use \(\lceil t/2\rceil\) distinct graph vertices making either a matching (even \(t\)) or exactly one adjacent pair plus isolates (odd \(t\)); these require exactly \(t\) ground points. Explicit inequality constraints exclude coincident graph vertices. The theorem and all enumerative and width consequences follow. Two independent computational procedures tested the unlimited-round game on finite samples and the exact witness thresholds, with no mismatches.

## Originality — PASS, with historical-priority qualification

Searches by the aliases \(J(n,2)\), triangular graphs, and line graphs of complete graphs were compared at the level of statements. The directly relevant inspected sources address general graph logical complexity (Pikhurko–Verbitsky), broad line-graph fixed-point definability with counting (Grohe), and automorphism groups of Johnson graphs (Ganesan); none states or immediately proves the exact counting-free \(2k\) threshold. A Johnson distance-extension paper concerns \(J(n,3)\), not the requisite two-subset intersection game. A prior rectangular-rook-graph finding treats \(L(K_{a,b})\), whose two-coordinate incidence structure does not imply this result. An unidentified general pebble-extension theorem remains a real priority risk; absence from searches is not proof of priority.

## Mathematical value — PASS

This is a complete sharp classification on a standard infinite graph family, not an isolated small-order computation: each of \(k\) pebbles represents a graph vertex but controls two hidden ground-set coordinates. The sharp and uniform \(2k\) stabilization cutoff, exact number \(2k-2\) of width-\(k\) theories, largest minimal representative \(\binom{2k}{2}\), and strict width hierarchy quantify that interpretational bottleneck. The distinction between graph-vertex number and hidden ground-set order matters in finite model theory and for testing logical invariants of line graphs.

## Scientific limits

The minimum defining width is only relative to the triangular graph family. Historical completeness is not established, the distance-extension paper's full text was not reviewed, and the unrestricted theorem rests on its proof rather than finite checks. The current review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
