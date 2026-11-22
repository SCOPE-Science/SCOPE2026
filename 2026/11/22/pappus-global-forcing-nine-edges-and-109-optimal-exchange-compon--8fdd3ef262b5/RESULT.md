# Pappus global forcing: nine edges and 109 optimal exchange components

## Finding

Let \(P\) be the eighteen-vertex Pappus graph, with the affine-incidence presentation specified below. An edge subset \(S\subseteq E(P)\) is **globally perfect-matching forcing** when the restrictions \(M\cap S\), over all perfect matchings \(M\) of \(P\), are pairwise distinct. Then

\[
\operatorname{gf}(P)=9,
\qquad \#\{S:|S|=9,\ S\text{ globally forcing}\}=13\,608.
\]

For optimum sets, join \(S\) and \(T\) by a \(t\)-replacement move if \(|S\setminus T|=|T\setminus S|\) lies between one and \(t\). Their one-replacement graph \(\mathcal R_1\) has exactly \(104\,490\) edges and

\[
\mathcal R_1\cong C\;\sqcup\;108\,(K_3\square K_3),
\qquad |V(C)|=12\,636,
\]

where \(C\) is connected. The two-replacement graph \(\mathcal R_2\) is connected, so the sharp optimal-reconfiguration threshold is exactly two. More precisely, each of the 108 nine-state components has a two-replacement edge into the large component. The one-move degree distribution is

\[
(4:972,\ 13:2916,\ 15:1944,\ 16:1944,\ 17:2916,\ 19:1944,\ 21:972).
\]

A useful auxiliary exact census is that \(P\) has 603 *nice even cycles*, by length
\[
(6:18,\ 8:54,\ 10:54,\ 12:225,\ 14:108,\ 16:108,\ 18:36).
\]
Here a cycle is *nice* if deleting its vertices leaves a graph with a perfect matching.

## Assumptions and scope

Use the field \(\mathbb F_3\). The nine point vertices are \(p_{x,y}\), where \(x,y\in\mathbb F_3\), and the nine line vertices are \(\ell^x_c\), \(\ell^y_c\), \(\ell^d_c\), for \(c\in\mathbb F_3\). The incidences are \(x=c\), \(y=c\), and \(y-x=c\), respectively. This is the Pappus graph, isomorphic to the cubic eighteen-vertex LCF presentation \([5,7,-7,7,-7,-5]^3\). It has 27 edges. All edge subsets, perfect matchings, and exchange vertices are *labelled* by this fixed graph; no quotient by graph automorphisms is taken.

A perfect matching covers every vertex exactly once. Every optimum \(S\) has nine edges. A one-replacement move deletes one selected edge and adds one different unselected edge; a two-replacement move may change one or two selected edges simultaneously, always remaining among the globally forcing nine-edge subsets.

## Proof

**1. Perfect-matching and cycle reductions.** Enumerate the line vertex paired with each of the nine point vertices, requiring each line to appear exactly once. This is an exhaustive enumeration of the perfect matchings because the graph is bipartite with nine vertices per shore. It yields exactly 42 perfect matchings. With a fixed ordering of its 27 edges, encode each matching as a 27-bit integer. Two matchings \(M,N\) have different observation signatures on \(S\) precisely when

\[
S\cap(M\mathbin{\triangle}N)\ne\varnothing.
\]

Consequently \(S\) is globally forcing if and only if the above holds for all \(\binom{42}{2}=861\) distinct matching pairs. Equivalently, \(S\) must hit every nice even cycle: each component of the symmetric difference of two perfect matchings is an even alternating cycle; conversely, a nice even cycle supports two perfect matchings obtained by selecting its alternating halves and extending by a matching of its vertex complement. Computing the distinct cycle-components from the 861 matching pairs gives exactly 603 cycles and the length distribution stated above. This finite cycle collection is complete by the equivalence.

**2. Minimum and census.** The `verify_affine.cpp` program recursively generates each \(k\)-element edge subset exactly once, for every integer \(1\le k\le9\), in increasing edge-index order. For each candidate it tests all 861 symmetric differences. The exact numbers of globally forcing sets, in order \(k=1,2,\ldots,9\), are

\[
(0,0,0,0,0,0,0,0,13\,608).
\]

The empty set cannot distinguish 42 matchings. The tests therefore exclude every set of fewer than nine edges, and count *every* optimum, proving the minimum and multiplicity. The loop runs over the full \(\binom{27}{k}\) combinations for each stated cardinality; no sampling or heuristic stopping is used.

**3. Exchange graph.** The same program indexes all 13,608 optimum masks and connects two when they have exactly eight common selected edges. It visits all nine choices of a removed edge and all eighteen choices of an added edge from each optimum, giving the complete one-replacement graph, with 104,490 unordered edges. Exhaustive component traversal produces one component of order 12,636 and 108 components of order nine. Each small component is four-regular, each adjacent pair has one common neighbour and each nonadjacent pair has two, so each is strongly regular with parameters \((9,4,1,2)\); the four neighbours of a vertex split into two disjoint edges by the one-common-neighbour rule; the other four vertices meet distinct choices of one endpoint from each edge by the two-common-neighbour rule, giving the unique three-by-three rook graph \(K_3\square K_3\). The exact degree distribution is as stated.

Finally, for each of the 108 small components, the program exhaustively checks pairs of removed selected edges and pairs of added unselected edges. It finds a valid optimum in the large component at symmetric-difference distance four (a two-replacement move). Hence the whole \(\mathcal R_2\) is connected because the large component is already connected in \(\mathcal R_1\). Since \(\mathcal R_1\) has 109 components, two is sharp.

**4. Independent graph presentation and test.** `verify_lcf.cpp` reconstructs \(P\) from its Hamiltonian eighteen-cycle with repeated chord offsets \([5,7,-7,7,-7,-5]\), enumerates perfect matchings by unmatched-vertex recursion, and checks observation signatures directly, without using the incidence presentation or the symmetric-difference test implementation. It independently reproduces the optimum count, edge count, component histogram, small-component structure, and two-replacement bridges. `verify_nice_cycles.py` separately enumerates the matching permutations and cycle components. `verify_isomorphism.py` checks a completely explicit vertex bijection between the affine graph and the LCF graph on all 27 edges.

## Verification

The included source files require only a C++17 compiler and Python 3 standard library. From the directory containing the extracted files, execute:

```sh
c++ -O2 -std=c++17 verify_affine.cpp -o verify_affine
./verify_affine
c++ -O2 -std=c++17 verify_lcf.cpp -o verify_lcf
./verify_lcf
python3 verify_nice_cycles.py
python3 verify_isomorphism.py
```

Their complete expected outputs are in `AFFINE_REFERENCE.txt`, `LCF_REFERENCE.txt`, , `CYCLES_REFERENCE.txt`, and `ISO_REFERENCE.txt`. All four programs were executed on their actual delivered source bytes during preparation. Both C++ verifiers enumerate all globally forcing candidates through size nine and construct the full optimum one-replacement graph; the cycle verifier independently checks the nice-cycle histogram. The theorem is finite and exhaustive, rather than a numerical extrapolation.

## Relationship to prior work

Vukičević and Sedlar introduced total forcing of perfect matchings in 2004, and the later global-forcing terminology was used by Vukičević and Došlić in their 2007 grid-graph work. Che and Chen's 2011 survey (Section 5.1, pp. 124–127) records the general information bound and cyclomatic bound. On this graph they give \(\lceil\log_2 42\rceil=6\) and \(|E(P)|-|V(P)|+1=10\), respectively; neither determines the attained value nine or counts and connectivity of its optima.

The graph itself has a classical affine-incidence/LCF representation; prior results about forcing a *single prescribed* perfect matching (local forcing), about perfect-matching alternating-cycle flips, and about optimum matchings on different graphs concern distinct configuration spaces. They do not supply the complete edge-observation census or the one-/two-replacement geometry reported here. Published priority is qualified by the limitations below.

## Limitations

This is an exact statement about the fixed eighteen-vertex Pappus graph, not an infinite family of incidence graphs. The counts rely on exhaustive finite enumeration with an explicit complete search, independently replayed using a nonidentical graph presentation. The literature comparison does not exclude unindexed or inaccessible earlier exact computations; in particular, some original historical articles were not fully inspectable. No independent scholarly audit has been performed.

## References

1. D. Vukičević and J. Sedlar, *Total forcing number of the triangular grid*, Mathematical Communications 9 (2004), 169–179. Public source dated 2004-12-22: https://hrcak.srce.hr/en/clanak/1373
2. D. Vukičević and T. Došlić, *Global forcing number of grid graphs*, Australasian Journal of Combinatorics 38 (2007), 47–62. https://ajc.maths.uq.edu.au/pdf/38/ajc_v38_p047.pdf
3. Z. Che and Z. Chen, *Forcing on Perfect Matchings – A Survey*, MATCH Communications in Mathematical and in Computer Chemistry 66 (2011), 93–136, especially Section 5.1. https://match.pmf.kg.ac.rs/electronic_versions/Match66/n1/match66n1_93-136.pdf
4. I. J. Dejter, *Pappus-Desargues digraph confrontation*, first posted 2009-04-07. https://arxiv.org/abs/0904.1096
5. E. W. Weisstein, *Pappus Graph*, MathWorld. https://mathworld.wolfram.com/PappusGraph.html
