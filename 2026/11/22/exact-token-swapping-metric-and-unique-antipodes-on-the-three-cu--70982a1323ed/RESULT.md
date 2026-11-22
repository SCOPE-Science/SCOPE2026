# Exact token-swapping metric and unique antipodes on the three-cube

## Finding

Let \(Q_3\) be the graph on the eight three-bit strings, with edges between strings of Hamming distance one. In the **sequential distinct-token swapping graph** \(\mathcal T(Q_3)\), a state assigns each of the eight distinct vertex-labelled tokens to one vertex, and one move exchanges tokens at the two ends of one edge of \(Q_3\). Then \(\mathcal T(Q_3)\) is a connected, vertex-transitive, twelve-regular graph on \(8!=40{,}320\) states. Its radius and diameter are both **12**. Every state has exactly **one** state at distance 12, so there are **20,160** unordered diametral pairs. In particular, the unique antipode of the identity placement (token \(v\) at vertex \(v\)) is the placement \(p(v)=v\mathbin{\mathrm{xor}}7\).

The exact numbers of states at swapping distance \(j=0,1,\ldots,12\) from any fixed state, in order, are

\[
(1,12,90,476,1903,5472,10388,11756,7347,2408,430,36,1).
\]

For a state \(p\), let \(d(p)\) be its minimum number of moves to reach the identity, and put

\[
B(p)=\frac12\sum_{v=0}^{7}\operatorname{popcount}(v\mathbin{\mathrm{xor}}p(v)),
\]

where the popcount is the number of nonzero binary coordinates. Then \(B(p)\) is a lower bound for \(d(p)\). The exact frequency distribution of the integer gap \(d(p)-B(p)\), at values \(0,1,2,3\) respectively, is

\[
(19064,18088,3144,24).
\]

In particular, the largest additional cost beyond the elementary transportation bound is **three** moves, attained by exactly 24 placements.

## Assumptions and scope

The underlying graph is the ordinary, undirected three-dimensional Boolean cube, not a square, an arbitrary hypercube, a Cayley graph on three symbols, or a parallel-swap architecture. All eight tokens have different destinations. At each discrete step **exactly one** ordinary cube edge may be used. States are indexed by the vertex labels \(0,\dots,7\), interpreted as three-bit strings. The entry \(p(v)\) is the label of the token currently at vertex \(v\), not the destination vertex occupied by token \(v\). Distances count swaps, not parallel layers or average physical path length. No claim is made for Boolean cubes of dimensions four or higher.

## Proof

**The finite state space and moves.** The edge set is exactly the twelve unordered pairs \(\{u,v\}\) whose integer labels differ in exactly one bit. A configuration is an eight-entry permutation. An adjacent configuration is obtained by exchanging the two entries at the endpoints of exactly one cube edge. Different edges give distinct neighboring configurations, so every state has degree 12. As the transpositions of edges in any connected spanning tree generate all permutations of its vertices, this graph is connected and has exactly \(8!\) states.

**Exhaustive exact-distance recurrence.** Start the breadth-first search at the identity permutation \(e=(0,1,2,3,4,5,6,7)\). Let \(D_0(e)=0\) and let other states initially have unknown distance. At each step remove a state from the first-in-first-out queue, and enqueue each of its as-yet-unseen twelve edge-swapped neighbors at its parent's distance plus one. The standard BFS induction says that each first-visit distance equals the minimum number of legal swaps from \(e\): any shorter route would visit its predecessor at an earlier queue level, and the recorded route itself gives the matching upper bound. The standalone file `verify_q3.py` implements this recurrence twice, once by tuple/dictionary keys and once by an independently coded Cantor-factoradic ranking into an array of exactly \(8!\) cells. The implementations agree **at all 40,320 individual states**, independently of the printed aggregate table. The check also verifies rank/unrank for every permutation. Exhausting this *entire finite state space*, rather than merely sampling configurations, gives the displayed histogram, the maximal distance 12, and exactly one distance-12 state, \((7,6,5,4,3,2,1,0)\). The accompanying `verification_output.json` contains the output of the successfully executed verifier. The complete executable algorithm, including its exact integer assertions, is part of this finding.

**Transfer to arbitrary sources.** Relabel tokens by any permutation \(s\). This maps the state \(q\) to the state \(s\circ q\), where \(s\) is applied to each token label. It commutes with each permitted *position* swap and is therefore a graph automorphism. Since any state is the relabeling of \(e\) by a unique permutation, the distance histogram, eccentricity 12, and one-antipode property hold from every source. Counting each unordered diametral pair twice gives \(8!/2=20{,}160\) pairs.

**Transportation deficit.** A cube-edge swap moves exactly two tokens by one graph edge. Each token's distance to its home vertex therefore changes by at most one, so the sum of all eight token-home distances can fall by at most two in one swap. Thus every sorting sequence uses at least \(B(p)\) moves. Because the cube is bipartite and each placement is a permutation, the total token-home distance is even, so \(B(p)\) is integral. The verifier evaluates both \(d(p)\) (already proved exact by the complete BFS) and \(B(p)\) for every one of the 40,320 permutations and checks the complete exact gap distribution \((19064,18088,3144,24)\). Its sum is 40,320, proving the frequency statement and the sharp gap of three.

## Verification

From the directory containing the files, run `python3 verify_q3.py`. No nonstandard packages, network services, or random seeds are needed. The code constructs the twelve edges from bit differences; executes two independently indexed BFS traversals; checks all 40,320 rank/unrank roundtrips and all 40,320 per-state distance equalities; asserts the printed distance shells, unique farthest placement, and transportation-gap counts; and emits the JSON in `verification_output.json`. The proof is exhaustive because the problem's complete state set is exactly the finite set of eight-symbol permutations. The two BFS encodings are a consistency check, not an independent peer review or a proof for larger graphs.

## Relationship to prior work

The underlying token-swapping model, its relation to Cayley graphs, and general approximation/complexity results are established literature; they are not claimed as new. In particular, Biniaz, Jain, Lubiw, Masárová and Turcotte's publicly available 2021 work develops token swapping on trees, and Bonnet, Miltzow and Rzążewski analyze complexity and constrained graph classes. Samos Sáenz de Buruaga and collaborators' 2025 hypercube-sorting analysis supplies general structural/average bounds for permutation implementations, but the examined section does not give the exact 40,320-state sequential three-cube distance spectrum or unique-antipode/deficit results. Related indexed work provides an exact token-swapping census on the **Petersen** graph, a different base graph with ten vertices and 10! placements. The precise claim here is the joint exact three-cube metric classification and transportation-deficit spectrum, not the generic BFS method or the transportation lower bound themselves.

## Limitations

This is an exact **finite** theorem, with exhaustive integer computation constituting the numerical certificate; it is not a symbolic all-dimension theorem. The source code and recurrence allow direct reproduction, but no independent external verification has been performed. The priority comparison is based on identified primary literature, relevant source sections, and available indexed records; an older result using a different terminology for the three-cube Cayley graph might exist. The most specific potential risk is an unpublished or difficult-to-index all-pairs distance census of the twelve-generator subgroup metric of \(S_8\).

## References

1. A. Biniaz, K. Jain, A. Lubiw, Z. Masárová, and A. Turcotte, *Token Swapping on Trees*, arXiv:2103.06707, first submitted March 11, 2021, https://arxiv.org/abs/2103.06707. Later expanded conference version: https://doi.org/10.4230/LIPIcs.ESA.2022.3.
2. É. Bonnet, T. Miltzow, and P. Rzążewski, *Complexity of Token Swapping and its Variants*, STACS 2017, https://doi.org/10.4230/LIPIcs.STACS.2017.17.
3. N. Samos Sáenz de Buruaga et al., *Fidelity decay and error accumulation in random quantum circuits*, SciPost Physics 19, 013 (2025), Appendix E.2, https://doi.org/10.21468/SciPostPhys.19.1.013.
4. See the accompanying `verify_q3.py` and `verification_output.json` for the exhaustive integer certificate and its exact reproduced outputs.
