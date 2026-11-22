# Scientific review

## Correctness — PASS

The cube distance formula is exact: for the direction-\(j\) edge \(e=(x,x\oplus2^j)\), with bit \(j\) of \(x\) zero, the distance to \(s\) is the number of coordinates other than \(j\) where \(s\) and \(x\) differ. An exhaustive scan of all \((d-1)\)- and \(d\)-element vertex sets for each \(d=2,3,4,5\) proves the sharp minima and exhaustively identifies every optimum. Two independent embedded checkers use separate techniques (Hamming signature-separation masks versus graph-BFS distance vectors) and agree on all four counts and on the exact geometric families, not just their cardinalities. The lower-size exclusion propagates to all smaller sets because adding landmarks cannot destroy either property. For \(Q_4\) and \(Q_5\), smaller edge-resolving-only cardinalities are checked separately.

## Originality — PASS (provisional)

The 2022 introduction of the vertex-edge dominant edge-metric dimension treats paths, cycles, standard complete graphs and certain two-factor Cartesian products but not these cubes. The 2021 hypercube edge-metric paper determines distance-identification properties without requiring vertex-edge domination; its scalar results do not imply the intersections classified here. A distinct 2023 *dominant edge metric dimension* uses vertex cover, a strictly stronger condition: previously recorded results for that invariant on hypercubes do not yield the smaller vertex-edge-dominating optimum or its optimizer geometry. Searches for names, cube aliases, counts, antipodal constructions and stronger variants yielded no covering statement. Risks include unindexed exact enumerations and literature not fully retrievable; no claim of exhaustive priority or independent validation is made.

## Mathematical value — PASS

The first two binary cubes where joint vertex-edge coverage is provably more expensive than edge identification exhibit a sharp one-landmark premium. All optimum sensor placements are classified, including three distinct geometry classes in dimension four and a single rigid antipode-plus-neighbors class in dimension five. This is an exact natural benchmark for a published composite network-identification parameter on successive Cartesian powers, not a merely renamed or arbitrary subset enumeration.

## Closest literature and limits

- H. M. Ikhlaq, S. Hayat, H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327, 2022.
- A. Kelenc et al., *On Metric Dimensions of Hypercubes*, arXiv:2102.10916, 2021.
- M. Tavakoli et al., *The dominant edge metric dimension of graphs*, DOI:10.5614/ejgta.2023.11.1.16, 2023; a different, vertex-cover-based parameter.

Only \(2\le d\le5\) is proved; no general formula for higher cubes or exhaustive priority certification follows.

Self-review: passed. Independent audit: not yet performed.
