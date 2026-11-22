# Exact minimum-sensor propagation and connected slide geometry of the Gray graph

## Finding

Let \(G\) be the Gray graph, the incidence graph between the \(27\) points of \(\{0,1,2\}^3\) and its \(27\) axis-parallel three-point lines. A power-dominating set \(S\) initially observes its closed neighborhood and then observes, in each simultaneous forcing round, every as-yet-unobserved vertex that is the unique unobserved neighbor of an observed vertex. Write \(\tau(S)\) for the first round at which all \(54\) vertices are observed, **counting the initial domination step as round one**.

**Theorem (exact minimum-sensor census, delay and relocation).** The power domination number is \(\gamma_P(G)=6\). There are exactly \(880632\) labelled minimum power-dominating sets. Every one selects two, three or four point-vertices; the numbers with \(j\) selected point-vertices and monitoring time \(\tau\) are:

| \(j\) | \(\tau=5\) | \(\tau=6\) | \(\tau=7\) | \(\tau=8\) | \(\tau=9\) | \(\tau=10\) | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 15552 | 83592 | 63504 | 33696 | 16200 | 0 | 212544 |
| 3 | 36288 | 180144 | 126360 | 73872 | 31104 | 1296 | 449064 |
| 4 | 13608 | 96552 | 65448 | 33048 | 9072 | 1296 | 219024 |
| Total | 65448 | 360288 | 255312 | 140616 | 56376 | 2592 | 880632 |

In particular the minimum monitoring time among minimum sensor sets is \(5\), while the maximum is \(10\). Under **token sliding**, a move replaces one sensor at vertex \(v\) with a sensor at an unoccupied neighbor of \(v\), retaining a six-vertex power-dominating set after every move. The resulting graph of all \(880632\) minimum configurations is **connected** and has exactly \(3412368\) undirected edges. Its degree multiplicities are

\[
\begin{array}{c|rrrrrrrr}
\text{degree}&4&6&7&8&9&10&11&12\\
\hline
\text{multiplicity}&77760&58968&182736&316872&130896&92016&9072&12312.
\end{array}
\]

The \(2592\) slowest sets, with \(\tau=10\), form exactly two orbits of size \(1296\) under the full automorphism group of \(G\), one with three and one with four point-vertices. There are no other minimum configurations with monitoring time \(10\).

## Assumptions and scope

The point-vertices are \(p_{abc}\), with \(a,b,c\in\{0,1,2\}\), encoded by integers \(9a+3b+c\) from \(0\) to \(26\). Axis-zero lines are encoded by \(27+3b+c\), axis-one lines by \(36+3a+c\), and axis-two lines by \(45+3a+b\); these are distinct vertices from their incident points. The graph has \(54\) vertices, \(81\) edges, and every vertex has degree \(3\).

For a nonempty vertex subset \(S\), define
\[
P^1(S)=N_G[S],\qquad
P^{t+1}(S)=P^t(S)\cup\{w:\exists v\in P^t(S),\ N_G(v)\setminus P^t(S)=\{w\}\},\quad t\ge1.
\]
All forces in one round use the *preceding* round's observed set. If no change occurs before full observation, the set fails. A configuration is minimum precisely if it has six vertices and eventually observes all vertices. The census and slide graph count labelled subsets, not symmetry-orbit representatives. The claimed connectivity does not assert any slide diameter or shortest-path formula.

## Proof

**1. Canonical graph and independent representation.** Every point belongs to one axis line in each of three directions; each line consists of three points. Thus the incidence graph has \(27+27\) vertices and \(27\cdot3=81\) edges, with degree three. Independently, the published Hamiltonian LCF representation \([-25,7,-7,13,-13,25]^9\) defines a cubic graph on \(54\) vertices. The explicit \(54\)-entry bijection in `verify_slowest_orbits.py` maps all \(81\) incidence edges onto the \(81\) LCF edges. This supplies a reproducible, exact identification of the two graph presentations.

**2. Exact minimum-cardinality certificate.** The lexicographic combination iterator in `verify_grid.cpp` visits all \(\binom{54}{5}=3162510\) five-vertex subsets and all \(\binom{54}{6}=25827165\) six-vertex subsets. Given any candidate, its observed set is initially the union of the selected closed neighborhoods. The program applies the displayed simultaneous forcing recurrence until full observation or stabilization. Exactly zero five-subsets succeed, while exactly \(880632\) six-subsets succeed. A power-dominating set remains successful after adding vertices, so the nonexistence of a successful five-subset also excludes every smaller subset. This proves \(\gamma_P(G)=6\).

The entirely separate implementation `verify_lcf.cpp` constructs the LCF graph rather than the incidence graph, keeps an explicit *unobserved* bitmask rather than the first program's observed bitmask, and independently enumerates every five- and six-subset. It obtains the identical totals. These are finite exhaustive proofs: they do not infer a general infinite-family claim from samples.

**3. Joint point-count/time census.** For every successful six-subset the iterators calculate \(j=|S\cap\{p_{abc}\}|\) and the smallest \(t\) such that \(P^t(S)=V(G)\). Both programs produce all eighteen cells of the displayed table (including the zero cells) and check the expected totals. In the LCF coordinates, the point side is exactly the even-labelled vertices, as verified by the explicit isomorphism. Summing the rows gives \(212544+449064+219024=880632\), and summing the time columns gives the displayed total row. No set has \(j\) outside \(\{2,3,4\}\) or time outside \(\{5,6,7,8,9,10\}\).

**4. Full token-slide certificate.** Both programs retain the \(880632\) successful six-subsets. For each such subset \(S\), each \(v\in S\), and each unoccupied neighbor \(w\in N_G(v)\setminus S\), they test membership of \(T=(S\setminus\{v\})\cup\{w\}\) in the successful-set dictionary. The pair is a legal slide edge if and only if \(T\) is present. Counting each unordered pair once yields \(3412368\) edges and the degree spectrum given above. A disjoint-set union over these exact edges yields one component containing all \(880632\) states, proving connectivity. Every potential single slide is tested; this is a complete finite graph traversal, not a sampled exploration.

**5. Maximum-delay orbits.** Let \(\Gamma=S_3^3\rtimes S_3\) permute the three symbols independently on each coordinate and permute the coordinate axes. This group of order \(1296\) preserves all point-line incidences, hence preserves power domination and \(\tau\). The graph-data reference identifies it as the full automorphism group. With the integer encoding above, set representatives are

\[
S_A=\{0,4,11,33,43,52\},\qquad S_B=\{0,4,8,10,39,52\}.
\]

The independent `verify_slowest_orbits.py` constructs and checks each of the \(1296\) group actions on all \(81\) graph edges. It computes \(1296\) distinct translates of each representative, verifies their disjointness and time \(10\), and verifies the respective point counts \(3\) and \(4\). Since the exhaustive time table has exactly \(2592=1296+1296\) time-ten sets, these two orbits exhaust the slowest configurations.

## Verification

All three verification programs are standalone, require no input files and reconstruct the graph and tested objects. With GCC or Clang and Python 3, from the extracted directory run:

```text
g++ -O3 -std=c++17 verify_grid.cpp -o grid_check
./grid_check
g++ -O3 -std=c++17 verify_lcf.cpp -o lcf_check
./lcf_check
python3 verify_slowest_orbits.py
```

The C++ programs use compiler-supported 64-bit bit-operation intrinsics and must be built with assertions enabled (do not define `NDEBUG`). Each checks exact candidate counts, table entries, slide edges, degrees and connectivity; the Python program checks the explicit graph isomorphism and the two maximal-delay symmetry orbits. The expected final output of each program ends with `PASS`. These checks were executed on the files embedded with this result.

## Relationship to prior work

The Gray graph is a canonical cubic semisymmetric graph, with the \(27\)-point/\(27\)-line realization and its LCF encoding established in classical graph-geometry literature. The power-domination reconfiguration framework of Bjorkman et al. (first public on 5 January 2022) supplies definitions and general structural questions about changing sensor sets, but its inspected text gives no Gray-graph minimum-sensor census or token-slide result. Allie et al. (first public on 2 October 2025) study general bounds for propagation radius; these do not determine the exact point-versus-line spectrum or slide connectivity here.

The published *Efficient open domination and minimum-trade geometry of the Gray graph* studies a different constraint: each vertex has exactly one selected neighbor, producing \(252\) efficient open dominating sets of size \(18\). Its exact-cover/trade-graph theorem does not imply a classification of six-vertex power-dominating sets, the present synchronous time spectrum, or the present token-slide graph. Searches of published mathematical records, aliases and closely related graph-invariant tables did not identify the composite claim. This negative search result is not a proof of historical uniqueness.

## Limitations

The theorem concerns this one explicitly labelled \(54\)-vertex graph, rather than all semisymmetric cubic graphs or higher-dimensional point-line incidence graphs. It does not classify all inclusion-minimal nonminimum power-dominating sets, the time distribution at larger sensor counts, or the diameter of the slide graph. The exact counts and connectivity are supported by exhaustive finite enumeration and independently implemented checkers, rather than a short symbolic closed-form classification of all \(880632\) sets. A separate independent mathematical audit has not been performed. Unindexed historical equivalence remains a residual priority risk; no empirical physical power-grid claim is made.

## References

1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798, first posted 5 January 2022; https://arxiv.org/abs/2201.01798.
2. I. Allie, B. du Preez, D. Reagon and A. Roux, *Bounds on the propagation radius in power domination*, arXiv:2510.02211, first posted 2 October 2025; https://arxiv.org/abs/2510.02211.
3. I. Z. Bouwer, *An edge but not vertex transitive cubic graph*, Canadian Mathematical Bulletin 11 (1968), 533–535; https://doi.org/10.4153/CMB-1968-063-0.
4. E. W. Weisstein, *Gray Graph*, MathWorld, graph geometry and LCF representation; https://mathworld.wolfram.com/GrayGraph.html.
5. *Efficient open domination and minimum-trade geometry of the Gray graph*, publicly available mathematical result, 8 November 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-efficient-open-domination-and-minimum-trade-geometry-of-the-gray--9d6ef7a316dc.
