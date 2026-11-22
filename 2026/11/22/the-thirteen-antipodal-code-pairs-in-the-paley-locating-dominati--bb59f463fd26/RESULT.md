# The thirteen antipodal code pairs in the Paley locating-domination slide graph

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb Z/13\mathbb Z\), adjacent when the difference is a nonzero quadratic residue. Its minimum locating-dominating sets have size four; there are exactly \(247\). Under one-sensor replacement (token jumping) they form a connected graph with \(1599\) edges and every state has eccentricity four. Under one-sensor moves along edges of \(P_{13}\) (token sliding), they form a connected graph with \(858\) edges, radius five, and diameter six.

The \(247\) states split into six orbits under the \(78\) affine automorphisms \(x\mapsto ax+b\), where \(a\) is a nonzero quadratic residue. The complete orbit profile \((\text{size},\text{slide degree},\text{slide eccentricity})\) is
\[
(26,3,6),\ (26,9,5),\ (39,6,5),\ (39,8,5),\ (39,10,5),\ (78,6,5).
\]
Precisely the \(26\) states in the first orbit are identifying codes (all thirteen *closed*-neighborhood traces are nonempty and distinct). They are also precisely the states of slide eccentricity six, and every one has a unique distance-six partner. Those \(13\) unordered antipodal pairs are exactly
\[
\bigl\{\{A+t,B+t\}:t\in\mathbb Z/13\mathbb Z\bigr\},
\qquad A=\{0,1,3,9\},\quad B=\{0,4,10,12\}.
\]
Each antipodal pair has a one-vertex intersection. All other locating-dominating optima have slide eccentricity five.

## Assumptions and scope
This is an exact result for the single *labelled* thirteen-vertex undirected simple graph, not an assertion for all Paley graphs. Write \(R=\{1,3,4,9,10,12\}\) and define \(N(v)=\{v+r:r\in R\}\) with arithmetic modulo thirteen. A set \(S\) is locating-dominating if every \(v\notin S\) has \(N(v)\cap S\ne\varnothing\) and these subsets are pairwise different over distinct \(v\notin S\). An identifying code satisfies the stronger condition that all \(N[v]\cap S\), for \(v\) in the entire vertex set, are nonempty and pairwise distinct. The configuration graphs contain **only minimum-cardinality locating-dominating sets**. An edge replaces exactly one chosen vertex by one unchosen vertex, with the extra requirement that the two vertices be adjacent in \(P_{13}\) for sliding. Sensors are indistinguishable.

## Proof
The complete finite proof is encoded by two standalone, independently formulated exhaustive checkers: `verify_bitmask.py` and `verify_sets.py` (Python 3, standard library). The elementary finite universe has just \(\sum_{j=0}^{4}\binom{13}{j}=1093\) candidate sets, allowing an exact exhaustive certificate rather than sampling. One checker uses integer bitmasks and residue-based neighborhood traces, the other uses an independently constructed \(39\)-edge list and sorted tuples.

Both programs evaluate the defining locating-dominating predicate directly for **every** candidate of size zero through four. The counts by cardinality are \((0,0,0,0,247)\), certifying the minimum four and the exhaustive list of \(247\) states. Both independently evaluate the identifying-code condition on this same list and find exactly \(26\). Both construct each permitted one-vertex replacement or adjacent slide by checking the two endpoint sets and the original host adjacency, not by assuming graph connectivity. Exhaustive breadth-first searches from **every** state (rather than selected samples) establish all eccentricities, distances, and connectedness.

The resulting *unordered pair* distance histograms at distances \(1,2,3,4\) for jumping are
\[
(1599,7995,15483,5304),
\]
and at distances \(1,2,3,4,5,6\) for sliding are
\[
(858,3432,9087,13403,3588,13).
\]
Each sums to \(\binom{247}{2}=30381\), confirming complete connected-pair coverage; the programs explicitly reject unreachable states. The slide degree counts are \(26\) of degree three, \(117\) of degree six, \(39\) of degree eight, \(26\) of degree nine, and \(39\) of degree ten. The first checker verifies that the affine group preserves the configuration set and constructs all six disjoint orbits. The independent second checker confirms the distance-six endpoints coincide exactly with the identifying codes and that all \(13\) farthest pairs are translates of the displayed pair \(\{A,B\}\). The first checker independently verifies the same antipodal identity, including the one-vertex intersection.

All loops, predicates, graph construction, and breadth-first search operations are visible in the included source. The code assertions supply explicit finite proof obligations that terminate over bounded integer and finite-set ranges. No randomized testing or unproved extrapolation enters the conclusion.

## Verification
With Python 3, run `python3 verify_bitmask.py` and `python3 verify_sets.py` from the directory containing the two files. Their expected output is recorded in `bitmask.out` and `sets.out`. Both checkers were executed and passed from the artifact package. The two implementations use distinct vertex-set and graph-construction representations. A checker assertion failing means this finite claim has not been verified in that execution; merely printing a log without executing the source is not a substitute for the proof.

## Relationship to prior work
The preprint *Locating-dominating sets: from graphs to oriented graphs* (arXiv:2112.01910, originally posted December 3, 2021) defines the locating-dominating condition and investigates general orientation parameters and bounds. It does not state the \(P_{13}\) minimum-code reconfiguration graph, its affine orbit census, or the relationship between its identifying-code subset and slide eccentricity. The work *Shortest Dominating Set Reconfiguration under Token Sliding* (arXiv:2307.10847, originally posted July 20, 2023) develops shortest-move algorithms for ordinary dominating sets on trees and interval graphs; it does not analyze locating-dominating sets or this Paley graph. Closely related exact finite computations for other strongly regular or incidence graphs do not imply the labelled Paley-thirteen result. The minimum vertex count and the exact reconfiguration geometry here arise from direct exhaustive certificates, not from a claimed universal formula.

## Limitations
This is a computer-assisted exact finite theorem with independently written executable checkers, not a hand-derived symbolic classification for an infinite family. Independent human verification has not been carried out. The supplied affine orbit action is explicitly checked; no claim about characterizations of all possible automorphisms beyond the group used for the orbit decomposition is necessary. Failure to find an indexed or repository match cannot exclude an unindexed historical equivalent.

## References
1. N. Bousquet, Q. Deschamps, T. Lehtilä, A. Parreau, *Locating-dominating sets: from graphs to oriented graphs*, arXiv:2112.01910 (original submission 2021-12-03), https://arxiv.org/abs/2112.01910.
2. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847 (original submission 2023-07-20), https://arxiv.org/abs/2307.10847.
3. E. W. Weisstein, *Paley Graph*, MathWorld, https://mathworld.wolfram.com/PaleyGraph.html (the finite-field graph definition and affine automorphisms).
