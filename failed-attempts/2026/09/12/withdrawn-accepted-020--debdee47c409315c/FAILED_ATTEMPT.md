# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/12/020`  
Independent audit date: 2026-09-28 (UTC)  
Task: `758bb954e2a7613516b4a5a78bd7008d`

This package is not accepted as a validated research finding under the three-axis audit. It is retained intact for provenance and should be relocated to the assignment-designated failed path.

## Correctness

The spectral and connectivity claims are reproducible. Rebuilding the 48-vertex Z3 lift for voltage pattern (1,0,1) gives a connected simple cubic bipartite graph whose largest nontrivial adjacency absolute value is sqrt(6), below 2*sqrt(2). Exhaustive recomputation of all 27 orbit-constant patterns gives exactly the three (0,b,0) patterns disconnected and all other 24 connected patterns Ramanujan.

## Originality

The witness is not a new named 48-vertex graph. An independent graph-isomorphism check identifies the (1,0,1) lift with the classical generalized Petersen graph G(24,5), recorded as F048A in the Foster census and as CubicVTgraph[48,4]. Zhou and Feng already classified edge-transitive cyclic regular covers of the Möbius-Kantor graph. Thus the source's framing as the first named Ramanujan 3-cyclic lift of this base is untenable; after identification, the spectral check is a finite computation on a long-catalogued graph.

## Scientific value

The exact voltage description and 27-pattern census are useful reproducibility data, but the central witness is a classical 48-vertex symmetric graph and the Ramanujan test is a routine finite-spectrum calculation. Without a new family, structural theorem, or nontrivial classification beyond the already studied cyclic-cover setting, the package does not clear the standalone scientific-value threshold.

## Consequence

The original package remains useful as computational evidence or target triage, but its research headline must not be represented as an independently validated standalone finding.

## Evidence

- [Zhou–Feng, Edge-transitive cyclic regular covers of the Möbius-Kantor graph](https://doi.org/10.1016/j.ejc.2011.09.034): Classifies cyclic regular covers of the Möbius-Kantor graph whose fibre-preserving groups are edge-transitive, placing the claimed cover in an established classification setting.
- [House of Graphs, graph 36514](https://houseofgraphs.org/graphs/36514): Identifies the 48-vertex graph as generalized Petersen G(24,5), CubicVTgraph[48,4], and F048A in the Foster census.
