# A single diametral orbit in minimum sensor-slide reconfiguration of the Nauru graph

## Finding
Let \(G=\operatorname{GP}(12,5)\) be the Nauru graph. Standard power domination has minimum cardinality \(\gamma_P(G)=3\), with exactly \(576\) minimum sensor sets. Let \(\mathcal J\) and \(\mathcal S\) be the reconfiguration graphs on these sets, using respectively unrestricted one-sensor jumps and one-sensor slides along an edge of \(G\). Then both are connected, and
\[
|E(\mathcal J)|=6660,\quad \operatorname{rad}(\mathcal J)=\operatorname{diam}(\mathcal J)=4,
\qquad |E(\mathcal S)|=1152,\quad \operatorname{rad}(\mathcal S)=9,\quad \operatorname{diam}(\mathcal S)=10.
\]
The slide graph is bipartite and four-regular. Precisely \(144\) configurations have slide eccentricity \(10\); the other \(432\) have eccentricity \(9\). Under an explicit subgroup of \(144\) graph automorphisms, the minimum configurations form five orbits of sizes \(72,72,144,144,144\). One choice of representatives for the five configuration orbits is
\[
\{u_0,v_6,v_{10}\},\quad\{u_0,v_5,v_6\},\quad\{u_0,v_6,v_9\},\quad\{u_0,u_3,u_6\},\quad\{u_0,u_7,u_{10}\}.
\]
Their respective orbit sizes are \(72,144,144,72,144\). All \(144\) eccentricity-ten configurations belong to the orbit of \(\{u_0,v_5,v_6\}\), and the \(72\) unordered pairs at slide distance \(10\) form a *single orbit of pairs*. Each of those \(144\) configurations has exactly one diametral partner.

For all distinct minimum configurations \(S,T\), the slide-versus-jump distance penalty satisfies
\[
0\le d_{\mathcal S}(S,T)-d_{\mathcal J}(S,T)\le 7.
\]
The upper bound is attained at exactly \(396\) unordered pairs: \(324\) pairs require eight slides instead of one jump, and the remaining \(72\) pairs require ten slides instead of three jumps. A representative of the latter kind is
\[
S=\{u_0,u_2,v_4\},\qquad T=\{u_6,u_8,v_{10}\}.
\]

## Assumptions and scope
The simple undirected graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/12\mathbb Z\), and undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+5}\), with indices reduced modulo \(12\). It has \(24\) vertices and \(36\) edges. For the programs, \(u_i\) is encoded by integer \(i\), and \(v_i\) by integer \(12+i\).

From an initial sensor set \(S\), observe all vertices of its closed neighborhood \(N[S]\). Thereafter repeatedly observe any vertex that is the unique unobserved neighbor of some already observed vertex. A power-dominating set is one for which this process eventually observes every vertex. The two configuration graphs have *only* minimum three-element power-dominating sets as vertices. A jump from \(S\) to \(T\) requires \(|S\setminus T|=|T\setminus S|=1\). A slide additionally requires that the removed and inserted vertices be adjacent in \(G\). All moves preserve optimality. Distances are ordinary undirected shortest-path lengths. Counts distinguish labelled vertex subsets; none are divided by automorphism orbits.

## Proof
**Power-domination minimum and exhaustive configurations.** Enumerate the \(24\) one-element subsets, \(\binom{24}{2}=276\) two-element subsets, and \(\binom{24}{3}=2024\) three-element subsets of the completely specified graph. For each, start with its closed neighborhood and repeatedly mark every unique unmarked neighbor of an already marked vertex. This monotonically increases the observed set and halts after at most \(24\) additions; it is exactly the defining closure, not a bounded-time heuristic. The finite exhaustive computation gives respectively \(0,0,576\) successful subsets. Therefore the optimum is exactly three and all \(576\) optima have been enumerated. `check_gp.py` performs simultaneous forcing with integer bit masks, while `check_cayley.py` performs sequential forcing on an independent permutation-star representation. The second program verifies an explicit bijective graph isomorphism with the stated generalized Petersen representation before counting.

**Complete configuration graphs and distances.** For each enumerated pair of optimum configurations, test whether their symmetric difference contains exactly one removed and one inserted vertex. This is precisely the jump criterion; require adjacency of those two vertices for the slide criterion. Two independent implementations, one by generating legal moves and the other by comparing every unordered pair, obtain \(6660\) and \(1152\) undirected edges. Every slide configuration has exactly four neighbors. Breadth-first search from each of the \(576\) vertices reaches all \(576\) vertices in both reconfiguration graphs; thus both graphs are connected, and the search determines *all* \(\binom{576}{2}=165600\) unordered distances, not a sample.

The complete jump distance distribution, indexed by distances one to four, is
\[
(6660,46800,110844,1296).
\]
The slide distribution, indexed by distances one to ten, is
\[
(1152,3456,8856,19368,32472,40464,37116,19296,3348,72).
\]
The eccentricities are respectively \(576\) occurrences of four for jumps, and \(432\) occurrences of nine plus \(144\) of ten for slides. Subtracting the *paired* distances gives the exact penalty-frequency vector, indexed by penalties zero through seven,
\[
(7416,15192,30528,39312,43164,22860,6732,396).
\]
The same all-pairs check separately verifies that the final \(396\) pairs split into \(324\) of jump/slide lengths \((1,8)\) and \(72\) of lengths \((3,10)\). Both implementations assert these values.

**Bipartition.** Colour \(u_i\) by the parity of \(i\), and colour \(v_i\) by the opposite parity. Every edge of \(G\) crosses the colouring because the outer step is one, the inner step is five, and spokes connect opposite colours. Sliding a sensor therefore changes the parity of the number of sensors in one colour class. This gives an explicit bipartition of \(\mathcal S\), without relying on enumeration.

**Symmetry and the diametral orbit.** A second presentation of \(G\) uses the \(24\) permutations of four labels: from a permutation, an edge swaps its first position with one of its other three positions. The explicit isomorphism to the labelled generalized Petersen graph is checked by `check_cayley.py`. Relabelling the four symbols and permuting the three remaining coordinate positions yields \(24\cdot6=144\) distinct graph automorphisms. `check_symmetry.py` checks every image of every edge, computes the induced action on the \(576\) optimal triples, and obtains the five orbit sizes stated above. In the complete distance table, the eccentricity-ten configurations form exactly one orbit of size \(144\), each appearing in exactly one of the \(72\) distance-ten pairs. Applying the \(144\) automorphisms to the displayed pair generates exactly these \(72\) pairs, proving the single-orbit claim. These are finite exhaustively checked action and distance assertions, not consequences inferred from transitivity alone.

## Verification
Using Python 3.9 or later and only its standard library, run `python3 check_gp.py`, `python3 check_cayley.py`, and `python3 check_symmetry.py` from a directory containing the three scripts. The first program constructs the graph by the generalized Petersen edge rule; the second constructs the permutation-star Cayley graph, checks a \(24\)-vertex isomorphism, and uses a different closure and move enumerator; the third checks the full explicit \(144\)-element symmetry action and extremal-pair orbit. Their deterministic JSON output is reproduced in `gp_output.json`, `cayley_output.json`, and `symmetry_output.json`. Each program recomputes its data, with internal assertions on all decisive counts and distances; the output files are not proof substitutes.

## Relationship to prior work
Bjorkman et al., *Power domination reconfiguration* (first public January 5, 2022), introduce the power-domination reconfiguration framework and study token-jump graphs of several families, but do not derive the Nauru optimum-triple or local-slide metric asserted here. Anderson and Kuenzel, *Power domination in cubic graphs and Cartesian products* (first public September 8, 2022), prove general bounds for cubic graphs, including a sharper result for claw-free cubic graphs; the Nauru graph is not claw-free, and their bounds do not imply the present exact counts.

Existing Nauru-graph computations on edge-colouring Kempe switches, anti-forcing of perfect matchings, and non-matching homology concern different state spaces and invariants. In particular, the edge-colouring state space has \(504\) colourings, whereas the sensor state space here has \(576\) vertex triples. Their numerical or symmetry conclusions neither identify this sensor space nor determine its jump/slide adjacency or metrics. The Nauru graph's classical graph-theoretic structure and automorphisms are not claimed as new.

## Limitations
This is an exact finite theorem for the single specified \(24\)-vertex graph, not a formula for arbitrary generalized Petersen graphs or a theorem about general cubic monitoring networks. Exhaustive finite checking is sufficient for the stated finite universes because the algorithms explicitly enumerate every candidate and every pair; it supplies no conclusion about larger unspecified graphs. Complete historical uniqueness cannot be proved by available searchable literature, and unindexed equivalent computations may exist. No independent external mathematical validation has been performed.

## References
1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, and C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1, first public 2022-01-05. https://arxiv.org/abs/2201.01798
2. S. E. Anderson and K. Kuenzel, *Power domination in cubic graphs and Cartesian products*, arXiv:2209.03931v1, first public 2022-09-08. https://arxiv.org/abs/2209.03931
3. D. Eppstein, *The many faces of the Nauru graph*, 2007-12-12. https://11011110.github.io/blog/2007/12/12/many-faces-of.html
4. *A Cayley sector and an irregular sector in Nauru edge-colouring reconfiguration*, public finding dated 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-cayley-sector-and-an-irregular-sector-in-nauru-edge-colouring--1a193aab529a
5. *Nauru-graph anti-forcing spectrum and the hidden split of two-factor profiles*, public finding dated 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-nauru-graph-anti-forcing-spectrum-and-the-hidden-split-of-two-fa--7dd6a167fbed
6. *Ninety-one three-spheres and the full symmetry character of the Nauru non-matching complex*, public finding dated 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-ninety-one-three-spheres-and-the-full-symmetry-character-of-the--87dc24545753
