# Antipodal completion and the sharp two-spare mixed-resolution threshold of the icosahedron

## Finding

Let \(I\) be the ordinary twelve-vertex icosahedral graph. A *mixed resolving set* is a set \(S\subseteq V(I)\) whose distance vectors distinguish all \(42\) elements of \(V(I)\sqcup E(I)\), where the distance from vertex \(w\) to edge \(uv\) is \(\min\{d(w,u),d(w,v)\}\). The following is a complete finite classification.

1. The mixed metric dimension of \(I\) is \(6\). **Every** minimum mixed resolving set is the union of exactly three of the six antipodal vertex pairs (distance-three pairs), and every such union is valid. Hence there are exactly \(\binom63=20\) minimum sets. Conversely, each is the antipodal completion of any ordinary three-landmark metric basis using those three axes.
2. Precisely ten minimum sets induce a six-cycle \(C_6\); the other ten induce two disjoint triangles \(2K_3\). Antipodal complementation interchanges these types.
3. The complete cardinality polynomial of mixed resolving subsets is
   \[
   R_I(z)=20z^6+240z^7+405z^8+220z^9+66z^{10}+12z^{11}+z^{12}.
   \]
   The inclusion-minimal mixed resolving sets have cardinality polynomial
   \[
   M_I(z)=20z^6+120z^7.
   \]
   Thus there are \(964\) mixed resolving sets and \(140\) inclusion-minimal ones.
4. Form an addition/deletion reconfiguration graph on all mixed resolving sets with at most \(b\) selected vertices; edges toggle exactly one selected vertex. At budgets \(b=6,7,8\), the component counts are, respectively, \(20,140,1\). At budget seven there are twenty components of size seven and 120 isolated states; at budget eight all \(665\) available states are connected. Consequently **two spare landmarks are necessary and sufficient** to move between any two optimum six-landmark configurations, while maintaining mixed resolution at every intermediate stage. In fact, the same two spares connect all feasible placements of cardinality at most eight.

The minimum-set classification is equivalent to a rank-three choice of axes from the six antipodal pairs, but with both endpoints of each chosen axis present. It differs from the ordinary vertex-only resolving bases, which use one endpoint on each of three axes.

## Assumptions and scope

All graph edges are simple, unweighted and undirected. Coordinates and vertices are labelled, so antipodal choices are counted as distinct vertex subsets. The graph has vertex set \(\{0,1,\ldots,11\}\): vertex \(0\) is the north pole, vertex \(1\) the south pole, vertices \(a_i=2+i\) and \(b_i=7+i\) are two staggered five-cycles indexed modulo five. The thirty edges are precisely
\[
\{0a_i,\ 1b_i,\ a_i a_{i+1},\ b_i b_{i+1},\ a_i b_i,\ a_i b_{i-1}:i\in\mathbb Z/5\mathbb Z\}.
\]
The resulting graph is the ordinary degree-five icosahedral graph. Its six antipodal pairs (distance-three vertex pairs) in these labels are
\[
\{0,1\},\ \{2,9\},\ \{3,10\},\ \{4,11\},\ \{5,7\},\ \{6,8\}.
\]
A mixed resolving set is **inclusion-minimal** if removing any one of its landmarks destroys mixed resolution. A reconfiguration is a sequence of valid mixed resolving sets; tokens are indistinguishable, occupy distinct vertices, and the permitted elementary move is an addition or removal, not a simultaneous swap.

## Proof

**Exact finite criterion.** Let the forty-two elements be the twelve vertices followed by the thirty unordered edges. Construct the twelve-by-twelve distance matrix \(D\) by shortest-path search in the displayed thirty-edge graph, and for any graph element \(x\) set
\[
\delta_w(x)=\begin{cases}D_{wx},&x\in V(I),\\\min(D_{wu},D_{wv}),&x=uv\in E(I).\end{cases}
\]
For two distinct elements \(x,y\), define the *witness mask* \(W_{xy}=\{w:\delta_w(x)\ne\delta_w(y)\}\). Thus \(S\) is mixed resolving **if and only if** \(S\cap W_{xy}\ne\varnothing\) for each of the exactly \(\binom{42}{2}=861\) unordered element pairs. This equivalence follows immediately from the definition and is not a heuristic.

The accompanying `verify_cpp.cpp` constructs all \(861\) nonempty witness masks with integer Floyd–Warshall distances, and tests each of the \(2^{12}=4096\) subsets against **every** mask. Separately, `verify_python.py` constructs the same graph by edges and computes twelve independent breadth-first-search distance rows, then builds a complete ordered distance signature for every element and tests all \(4096\) subsets for signature uniqueness. There is no reliance on a stored data table, random search, truncated sample, or external library.

**Minimum and antipodal classification.** Both exhaustive finite criteria give no mixed resolving subsets of cardinality at most five, and exactly twenty of cardinality six. Independently of a precomputed list of minima, each checker identifies the six pairs at graph distance three and generates the \(\binom63=20\) sets obtained by taking both endpoints of any three such pairs. A direct comparison of the full six-subset enumeration with this generated family gives equality. Thus all mixed bases, and no others, have the asserted antipodal-completion form. The Python checker additionally verifies directly that each of the \(\binom63 2^3=160\) choices of one endpoint on each of three axes distinguishes all twelve vertices. The completion relationship therefore has the stated concrete meaning; it is not an assertion that arbitrary vertex-resolving sets become mixed resolving.

Every minimum set induces a 2-regular six-vertex graph, as directly checked from all thirty edges. Its induced triangle count is either zero or two: the former is a connected six-cycle, while the latter is two vertex-disjoint triangles. The counts are ten each. The complement of any minimum set is the union of its other three antipodal pairs, and the check confirms that complementation exchanges the two classes. These are exhaustive induced-subgraph statements, not classifications by graph drawings.

**Complete all-size and minimal enumerations.** Each checker computes the exact subset-cardinality histogram using the same complete \(4096\)-element universe but different resolving predicates (distance-signature injectivity versus intersection of \(861\) witness masks). Both yield, for sizes zero through twelve,
\[
(0,0,0,0,0,0,20,240,405,220,66,12,1).
\]
Since mixed resolution is monotone under addition of landmarks, a successful subset is inclusion-minimal exactly when none of its single-vertex deletions is successful. Testing this condition for every successful subset gives exactly twenty inclusion-minimal sets of size six and 120 of size seven, with none of larger cardinality. The two displayed polynomials follow coefficient by coefficient.

**Sharp addition/deletion threshold.** At budget six, the twenty minima are isolated. A seven-vertex state can contain at most one six-vertex minimum: any two different three-axis selections contain at most two common antipodal pairs, so their union contains at least eight vertices. Therefore no budget-seven path can pass between distinct optima. Enumeration further gives exactly 120 feasible seven-sets containing no six-set, which are isolated, and twenty size-seven stars attached to the minima. Hence the 140 components have sizes \(1\) (120 times) and \(7\) (twenty times).

At budget eight, all optima are mutually connected *constructively*: replacing one chosen antipodal pair with one unchosen pair can be executed as two additions followed by two deletions, passing through mixed resolving supersets of sizes seven and eight. The three-axis choices form the connected Johnson graph on the three-element subsets of six axes, so these replacements connect all twenty optima. To verify the stronger claim that **all** size-six, -seven, and -eight feasible sets join the same component, the checkers independently construct the toggle graph on all 665 valid subsets of those sizes and traverse it completely. Both find exactly one connected component of size 665. The mathematical search space and transition predicate are explicit and finite, so this is an exhaustive proof of the stronger connectivity conclusion.

## Verification

Extract the two standalone sources and run

```sh
python3 -S verify_python.py
g++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
./verify_cpp
```

Both programs contain their own construction of the full thirty-edge graph and all assertions for the size counts, minimum-family equality, induced geometries, minimal-set counts and reconfiguration transitions. Their expected terminal markers are `ICOSAHEDRAL_MIXED_VERIFY_OK` and `ICOSAHEDRAL_MIXED_WITNESS_VERIFY_OK`. The Python program uses ordered distance tuples; the C++ program uses a dual family of 861 element-pair witness bitmasks. The former constructs distances by BFS and the latter by Floyd–Warshall; the pairwise criteria provide genuinely different algorithmic paths to the same exhaustive census. There are no unresolved computational subcases.

## Relationship to prior work

Kelenc, Kuziak, Taranenko and Yero introduced mixed metric dimension and considered structural examples. Milivojević Danas and collaborators supplied general bounds and exact computations for twelve selected standard graphs, but their visible graph table (arXiv:2007.05808, Table 8) does not include the icosahedron. Sedlar and Škrekovski treated unicyclic graphs and cactus graphs; their edge-disjoint-cycle hypotheses do not apply to this multiply triangulated graph.

Prior research on the **ordinary vertex-only** metric dimension of the icosahedral graph, including the published account *Antipodal matroid bases and one-slide transport detours on the icosahedron*, determines ordinary resolving triples from distinct antipodal pairs. A vertex-only basis distinguishes twelve vertices, while a mixed basis must distinguish twelve vertices **and thirty edges**; the prior ordinary basis characterization neither states nor implies that taking antipodal completions separates the thirty edges, that those completions are the only mixed bases, or that the full mixed-resolution polynomial and two-spare threshold have these values. The separate known mixed metric basis theorem for complete prisms concerns \(K_n\square K_2\), not the icosahedron. Targeted searches under the terms mixed resolving sets, mixed metric dimension, mixed landmark basis, Platonic graphs, antipodal icosahedral generators and mixed-basis reconfiguration did not produce a covering published claim. This is not a proof that no unindexed equivalent result exists.

## Limitations

This result is a complete **finite** theorem for the ordinary twelve-vertex icosahedral graph. It makes no assertion for other Platonic solids, general Taylor graphs, or arbitrary antipodal distance-regular graphs. The thirty-edge labelled presentation and the full finite certificate are needed for the all-size count and for the 665-state connectivity claim; the small-instance checks must not be extrapolated to infinite families. The novelty comparison is best-effort and not an independent historical-priority audit. No independent scholarly validation has been performed.

## References

1. M. Milivojević Danas, J. Kratica, A. Savić, Z. Lj. Maksimović, *Some new general lower bounds for mixed metric dimension of graphs*, arXiv:2007.05808v1, first public 2020-07-11. https://arxiv.org/abs/2007.05808
2. J. Sedlar, R. Škrekovski, *Mixed metric dimension of graphs with edge disjoint cycles*, arXiv:2010.10487v1, first public 2020-10-20. https://arxiv.org/abs/2010.10487
3. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, *Mixed metric dimension of graphs*, arXiv:1611.04292v1, first public 2016-11-14. https://arxiv.org/abs/1611.04292
4. *Antipodal matroid bases and one-slide transport detours on the icosahedron*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-antipodal-matroid-bases-and-one-slide-transport-detours-on-the-i--afe70695ac53
5. *Mixed metric bases of complete prisms*, published 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mixed-metric-bases-of-complete-prisms--2c5387cbdbd0
